from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'instance', 'tasks.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Ensure instance directory exists
instance_dir = os.path.join(basedir, 'instance')
os.makedirs(instance_dir, exist_ok=True)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Task model
class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    priority = db.Column(db.Integer, nullable=False)  # 1=high, 2=medium, 3=low
    completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Task {self.title}>'
    
    def to_dict(self):
        """Convert task to dictionary for JSON responses."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
    
    @property
    def priority_label(self):
        """Get human-readable priority label."""
        priority_map = {1: 'High', 2: 'Medium', 3: 'Low'}
        return priority_map.get(self.priority, 'Unknown')
    
    @property
    def priority_emoji(self):
        """Get emoji representation of priority."""
        priority_map = {1: '🔴', 2: '🟡', 3: '🟢'}
        return priority_map.get(self.priority, '⚪')
    
    def mark_completed(self):
        """Mark task as completed."""
        self.completed = True
        self.completed_at = datetime.utcnow()
    
    def mark_uncompleted(self):
        """Mark task as not completed."""
        self.completed = False
        self.completed_at = None

@app.route('/')
def index():
    """Main page showing all tasks."""
    # Get active tasks ordered by priority (1=high, 2=medium, 3=low)
    active_tasks = Task.query.filter_by(completed=False).order_by(Task.priority.asc(), Task.created_at.desc()).all()
    
    # Get completed tasks
    completed_tasks = Task.query.filter_by(completed=True).order_by(Task.completed_at.desc()).all()
    
    # Get task counts
    active_count = len(active_tasks)
    completed_count = len(completed_tasks)
    total_tasks = active_count + completed_count
    
    return render_template('index.html', 
                         active_tasks=active_tasks,
                         completed_tasks=completed_tasks,
                         active_count=active_count,
                         completed_count=completed_count,
                         total_tasks=total_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task."""
    try:
        title = request.form['title'].strip()
        description = request.form.get('description', '').strip()
        category = request.form['category']
        priority = int(request.form['priority'])
        
        # Validation
        if not title or not category:
            return redirect(url_for('index'))
        
        if priority not in [1, 2, 3]:
            return redirect(url_for('index'))
        
        # Create new task
        new_task = Task(
            title=title,
            description=description,
            category=category,
            priority=priority
        )
        
        db.session.add(new_task)
        db.session.commit()
        
    except (ValueError, KeyError):
        # Handle invalid form data
        pass
    
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    """Edit an existing task."""
    try:
        title = request.form['title'].strip()
        description = request.form.get('description', '').strip()
        category = request.form['category']
        priority = int(request.form['priority'])
        
        # Validation
        if not title or not category:
            return redirect(url_for('index'))
        
        if priority not in [1, 2, 3]:
            return redirect(url_for('index'))
        
        # Find and update the task
        task = Task.query.get_or_404(task_id)
        task.title = title
        task.description = description
        task.category = category
        task.priority = priority
        
        db.session.commit()
        
    except (ValueError, KeyError):
        # Handle invalid form data
        pass
    
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    """Mark a task as completed."""
    task = Task.query.get_or_404(task_id)
    task.mark_completed()
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/uncomplete_task/<int:task_id>')
def uncomplete_task(task_id):
    """Mark a task as not completed."""
    task = Task.query.get_or_404(task_id)
    task.mark_uncompleted()
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Delete a task."""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/get_task/<int:task_id>')
def get_task(task_id):
    """Get task data for editing (AJAX endpoint)."""
    task = Task.query.get(task_id)
    
    if task:
        return jsonify(task.to_dict())
    
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/category/<category>')
def tasks_by_category(category):
    """Get tasks by category."""
    active_tasks = Task.query.filter_by(completed=False, category=category).order_by(Task.priority.asc(), Task.created_at.desc()).all()
    completed_tasks = Task.query.filter_by(completed=True, category=category).order_by(Task.completed_at.desc()).all()
    
    active_count = len(active_tasks)
    completed_count = len(completed_tasks)
    total_tasks = active_count + completed_count
    
    return render_template('index.html', 
                         active_tasks=active_tasks,
                         completed_tasks=completed_tasks,
                         active_count=active_count,
                         completed_count=completed_count,
                         total_tasks=total_tasks,
                         filter_category=category)

@app.route('/tasks/priority/<int:priority>')
def tasks_by_priority(priority):
    """Get tasks by priority."""
    active_tasks = Task.query.filter_by(completed=False, priority=priority).order_by(Task.created_at.desc()).all()
    completed_tasks = Task.query.filter_by(completed=True, priority=priority).order_by(Task.completed_at.desc()).all()
    
    active_count = len(active_tasks)
    completed_count = len(completed_tasks)
    total_tasks = active_count + completed_count
    
    return render_template('index.html', 
                         active_tasks=active_tasks,
                         completed_tasks=completed_tasks,
                         active_count=active_count,
                         completed_count=completed_count,
                         total_tasks=total_tasks,
                         filter_priority=priority)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)