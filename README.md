# Plan: A Modern Flask Task Manager

## Project Overview

Plan is a modern, mobile-first task management web application built with Flask and SQLAlchemy. The project is designed to provide a beautiful, intuitive, and highly functional experience for users who want to organize their tasks by category and priority, track their progress, and enjoy a visually appealing interface. The application is inspired by Apple’s design language, featuring large, readable text, glassmorphism effects, and a dark/light mode toggle for optimal usability in any environment. The front end is crafted with HTML and CSS, focusing on accessibility, responsiveness, and a clean, modern aesthetic.

The core functionality of Plan allows users to create tasks, assign them a category and a priority level, and manage their status as active or completed. Tasks are displayed in order of priority, and users can easily edit, delete, or mark them as finished. Completed tasks are visually separated and grayed out, providing a clear distinction from active tasks. The application also displays counters for both active and completed tasks, giving users a quick overview of their productivity.

## File-by-File Breakdown

### app.py
This is the main application file and the heart of the project. It defines the Flask app, configures the SQLite database using SQLAlchemy, and contains all the route logic for the web interface. The `Task` model is defined here, representing each task with fields for title, description, category, priority, completion status, and timestamps for creation and completion. The model also includes helper methods for marking tasks as completed or uncompleted, as well as properties for displaying human-readable priority labels and emojis.

The routes in `app.py` handle all CRUD operations: creating, editing, deleting, and updating the status of tasks. The main page displays all tasks, separated into active and completed sections. Additional routes allow filtering by category or priority, and an AJAX endpoint provides task data for editing. The application ensures the database and its directory exist before starting, and all database operations are performed using SQLAlchemy’s ORM for safety and maintainability.

### templates/index.html
This file contains the main HTML template for the application. It is responsible for rendering the user interface, including the task lists, forms for adding and editing tasks, and the controls for switching between dark and light modes. The template uses Jinja2 syntax to dynamically display tasks and their properties, and it includes modern UI elements such as large buttons, icons, and glassmorphism cards. The design is mobile-first, ensuring usability on all devices, and the layout adapts gracefully to different screen sizes.

### templates/layout.html
The layout template provides a base structure for the application’s pages, including the necessary CSS and JavaScript imports. It defines blocks for the page title, head content, main content, and scripts, allowing for easy extension and customization. This separation of layout and content promotes maintainability and reusability across the project.

### static/style.css
This file contains all the CSS for the application, implementing the modern, Apple-inspired design. It defines color variables for both light and dark themes, uses CSS Grid and Flexbox for responsive layouts, and applies glassmorphism effects with backdrop filters and semi-transparent backgrounds. The CSS also styles all UI elements, including forms, buttons, cards, and modals, to ensure a cohesive and visually appealing experience. Special attention is given to accessibility, with focus-visible outlines and large touch targets for mobile users.

### requirements.txt
This file lists the Python dependencies required to run the project, specifically Flask and Flask-SQLAlchemy. By specifying exact versions, it ensures that the application can be reliably installed and run in any environment.

### create_sample_data.py
This optional script is provided to help users populate the database with sample tasks for testing and demonstration purposes. It creates a set of example tasks, including both active and completed items, to showcase the application’s features and layout. This script is especially useful for new users who want to see the app in action without manually entering data.

### run.py
A simple script to start the Flask application. It ensures that the database tables are created before launching the server and provides clear instructions for accessing the app in a web browser. This script abstracts away the need to remember Flask command-line options, making it easier for users to get started.

## Design Choices and Rationale

One of the key design decisions in this project was to use SQLAlchemy as the ORM for database management. While Flask’s built-in support for SQLite is sufficient for simple projects, SQLAlchemy provides a much more robust and flexible foundation. It allows for type-safe queries, easy schema migrations, and better security against SQL injection. Using an ORM also makes the code more maintainable and easier to extend in the future, for example, if you want to add user authentication or relationships between tasks and users.

Another important choice was to focus on a mobile-first, modern UI. Many task management apps are cluttered or difficult to use on small screens. By prioritizing responsive design and large, touch-friendly elements, Plan ensures a smooth experience on both phones and desktops. The use of glassmorphism and Apple-inspired design cues was intentional, aiming to create an interface that feels both familiar and cutting-edge.

The separation of active and completed tasks, along with visual cues like graying out finished items, helps users quickly understand their progress. The inclusion of counters for both active and completed tasks provides instant feedback and motivation. The dark/light mode toggle is implemented with CSS variables and localStorage, allowing users to choose the theme that best suits their environment.

Throughout the project, maintainability and extensibility were prioritized. The code is organized into logical sections, with clear separation between the backend logic, templates, and static assets. Helper methods and properties in the Task model encapsulate common functionality, reducing duplication and making the code easier to read and modify.

## Conclusion

Plan is a thoughtfully designed, modern task management application that balances functionality, aesthetics, and maintainability. Every file in the project serves a clear purpose, from the robust backend logic in `app.py` to the polished user interface in the templates and CSS. The use of SQLAlchemy ensures that the app is ready for future growth, while the mobile-first design guarantees accessibility for all users. Whether you are looking to manage your daily tasks or seeking inspiration for your own Flask projects, Plan provides a solid foundation and a delightful user experience.
