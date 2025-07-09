# Planner
#### Video Demo: https://youtu.be/DOOkEjItAQA
#### Description:
Planner is a task management web application made with Flask, SQL and HTML/CSS/JS. It allows users to add tasks they wish to accomplish. Tasks can be added with the following features:
- A title, or name of the task
- A description. This could be any subtasks or resources, and explanations linked to the task
- A category dropdown, allowing you to choose between categories such as Learning, Work, Health, Personal, etc.
- A Priority selection, allowing users to set the priority level of their task
- Tasks are added and shown in the Active Tasks section. A number on the nav bar, and next to Active Tasks shows the number of tasks pending
- Tasks can be marked as completed.
- Completed tasks show at the bottom, and a number is also shown
- Tasks can be deleted from the database
- Tasks can be edited, in case the user needs to change any informationn about them
- The color theme of the site can be changed between Light and Dark colors.
- Completed tasks can be undo, in order to mark them as pending again.
- A quick count of pending and done task is shown at the top.
- Tasks are sorted by priority level

## Tech Stack:
I used Python with Flask for the back-end of this application. Flask was chosen because of its easy to understand routes and functions. For database, I used SQLite since it is good for small and medium sized projects. I used SQLAlchemy as an ORM, so I can use my database table as a class in Python. The HTML and CSS front-end was chosen for a light-weight, responsive, single-page design. JavaScript was also integrated for functionality and DOM manipulation.

## Working of App:
The `app.py` file defines the Flask Application. It configures the SQLite database using SQLAlchemy. and contains all the route logic for the web interface. The `Task` model is defined here, representing each task with fields for title, description, category, priority, completion status, and timestamps for creation and completion. The model also includes helper methods for marking tasks as completed or uncompleted, as well as properties for displaying human-readable priority labels and emojis. The routes in `app.py` handle all CRUD operations: creating, editing, deleting, and updating the status of tasks. The main page displays all tasks, separated into active and completed sections. Additional routes allow filtering by category or priority, and an AJAX endpoint provides task data for editing. The application ensures the database and its directory exist before starting, and all database operations are performed using SQLAlchemy’s ORM for safety and maintainability.

`layout.html` provides a base structure for the application’s pages, including the necessary CSS and JavaScript imports. It defines blocks for the page title, head content, main content, and scripts, allowing for easy extension and customization. This separation of layout and content promotes maintainability and reusability across the project.

The `index.html` file has the main HTML template for the application. It is responsible for rendering the user interface, including the task lists, forms for adding and editing tasks, and the controls for switching between dark and light modes. The template uses Jinja2 syntax to dynamically display tasks and their properties, and it includes modern UI elements such as large buttons, icons, and glassmorphism cards. The design is mobile-first, ensuring usability on all devices, and the layout adapts gracefully to different screen sizes.

`style.css` contains all the CSS for the application, implementing the modern, Apple-inspired design. It defines color variables for both light and dark themes, uses CSS Grid and Flexbox for responsive layouts, and applies glassmorphism effects with backdrop filters and semi-transparent backgrounds. The CSS also styles all UI elements, including forms, buttons, cards, and modals, to ensure a cohesive and visually appealing experience. Special attention is given to accessibility, with focus-visible outlines and large touch targets for mobile users. I used vanilla CSS instead if any framework so I could learn better responsive UI skills.

## Conclusion
Plan is a thoughtfully designed, modern task management application that balances functionality, aesthetics, and maintainability. Every file in the project serves a clear purpose, from the robust backend logic in `app.py` to the polished user interface in the templates and CSS. The use of SQLAlchemy ensures that the app is ready for future growth, while the mobile-first design guarantees accessibility for all users. Whether you are looking to manage your daily tasks or seeking inspiration for your own Flask projects, Plan provides a solid foundation and a delightful user experience.
