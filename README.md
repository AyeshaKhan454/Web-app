# **My To-Do List**  
#### **Video Demo:**
< https://youtu.be/sauKuotFL6c?si=xA-JF8hmCEhA1ihq > 
---

### **Description**  

### Why I Chose This Project Idea  
I chose this project because it is a straightforward yet practical web application that allows me to apply and enhance my newly acquired knowledge of web development. It serves as a great way to integrate front-end and back-end skills while creating something functional and user-friendly.  

### The Primary Use Case(s) of the Application  
This web application is designed to effectively help users keep track of their daily tasks, ensuring better organization and productivity in their routines.  

### The Target Audience or Users  
The *My To-Do List* web app is suitable for users of all ages and professions, whether they are students, teachers, employees, or anyone looking to manage their tasks more efficiently.  

### Technologies, Tools, or Frameworks Used  
The web app uses **HTML/Jinja**, **CSS**, and **JavaScript** for front-end development to create an interactive and visually appealing interface. For back-end development, I utilized the **Flask** framework to handle server-side functionality and connected it to a database to store users' task information securely.  

---

### **Features**

#### **Key Functionalities**  
- The primary functionality of this application is to allow users to easily manage their tasks.  
- Users can add their pending tasks, which will immediately appear on the page.  
- Tasks can be deleted with just one click, providing a seamless and efficient user experience.  

#### **Innovative Aspects**  
- To enhance user interaction, the app provides real-time feedback with Flask messages.  
- Messages like *"Task added successfully"* or *"Task deleted successfully"* confirm to users that their changes have been applied correctly.  

#### **Areas Where It Stands Out Compared to Similar Projects**  
- The *My To-Do List* app stands out because of its scalability and user-centric design.  
- Multiple users can register, log in, and log out, ensuring a personalized experience.  
- Each user's tasks and updates are securely stored in a database, keeping data organized and distinct for every individual.  

---

### **File Structure Descriptions**

#### **Main Files**

1. **`static`**  
   - This folder contains all the static resources such as images and CSS files that enhance the app's appearance and user interface.  
   - **`images`**  
     - **`background.jpg`**: This is the visually appealing background image applied to the app, giving it a professional and polished look while maintaining readability.  
     - **`icon.png`**: A favicon for the browser tab, providing a unique identity to the app through a recognizable icon.  
   - **`styles.css`**  
     - This file holds the custom CSS rules for styling the application. It ensures the user interface is intuitive, consistent, and responsive. Features like button hover effects and adaptive layout adjustments are managed here.  

2. **`templates`**  
   - This directory houses all the Jinja2 HTML templates used in the Flask application, enabling the dynamic generation of content based on the backend logic.  
   - **`apology.html`**: A special template to display error messages or custom alerts to users, ensuring clarity in case of issues or invalid input.  
   - **`index.html`**: The main interface for the to-do list, where users can add, view, and delete tasks in an organized table layout.  
   - **`layout.html`**: Acts as a parent template for other HTML files. Common elements like navigation bars and footers are defined here for consistency.  
   - **`login.html`**: Allows users to log into their accounts securely. Includes form elements for username and password input.  
   - **`register.html`**: A registration page for new users to sign up. Features fields for username, password, and password confirmation.  

#### **Root Files**

3. **`app.py`**  
   - The core of the application, this Python script is the main entry point for the Flask app. It handles routing, user authentication, database interactions, and session management. Routes like `/index`, `/add`, `/delete`, `/login`,`/logout`, and `/register` define the app's behavior.  

4. **`helpers.py`**  
   - **`apology(message, code=400):`** Renders an apology page with a custom error message.
   - **`login_required(f):`** Ensures a user is logged in before accessing certain routes. Redirects to the login page if not authenticated

5. **`project.db`**  
   **users:** Stores user data with id, username, and hash (hashed password).
   **list:** Stores tasks with id, user_id (foreign key), date, task, and status  

#### **Other Files**

6. **`README.md`**  
   - A markdown file that provides an overview of the project. It explains its purpose, features, installation steps, and any additional information for contributors or users.  

---

### **Design Decisions**  
Important design choices I made while building this project:  
### **Why Certain Technologies, Libraries, or Frameworks Were Chosen**  

1. **`os`**  
   The `os` module is used to interact with the operating system and manage environment variables. It ensures flexibility and security by enabling environment-specific configurations, such as database URLs or secret keys, without hardcoding sensitive information.  

2. **`cs50.SQL`**  
   The `SQL` library from the CS50 package simplifies interactions with the SQLite database. It provides a Pythonic interface for executing SQL commands, making it easier to manage tasks like querying and updating data, without the need for verbose or complex SQL code.  

3. **`Flask` Framework**  
   Flask is a lightweight web framework that is flexible and simple to use, making it ideal for building this web application. Flask allows easy integration of back-end logic with front-end templates. The specific components of Flask used in this project are:  
   - **`flash`**: To display feedback messages to the user, such as *"Task added successfully"* or *"Task deleted successfully"*, helping improve user interaction.  
   - **`redirect`**: To redirect users to different pages after completing certain actions, like logging in or submitting a form.  
   - **`render_template`**: To dynamically render HTML templates and pass data (like user tasks) to them for display.  
   - **`request`**: To handle HTTP requests, such as retrieving form data or processing task input from users.  
   - **`session`**: To maintain user sessions, allowing users to remain logged in and retain their task data across requests.  

4. **`flask_session.Session`**  
   This library is used for server-side session management. It securely stores session data, such as user authentication, making sure that user data is persisted across page reloads without relying on client-side cookies.  

5. **`werkzeug.security`**  
   - **`generate_password_hash`**: This function is used to hash passwords before storing them in the database, ensuring user credentials are stored securely.  
   - **`check_password_hash`**: It helps verify a user’s password during login by comparing the stored hash with the provided password. This adds an extra layer of security to the login process.  

6. **`datetime`**  
   The `datetime` module is used to track and display timestamps, such as when a task was added. This gives users context for their tasks, improving the overall user experience.  

7. **`helpers.py`**  
   - The **`apology`** function is used to display custom error messages in a consistent format, improving the user interface when errors occur.  
   - The **`login_required`** decorator ensures that certain routes are only accessible to authenticated users, preventing unauthorized access and enhancing security.    

---

### **How to Run the Project**  
Step-by-step instructions for running my project:  

1. Clone the repository (https://github.com/code50/171432729.git).
2. Write (cd project) in the terminal. 
3. Then type (flask run). 
4. Follow the given link to access the web app.

---

### **Usage Instructions**  
Users can interact with the project as follows:  

1. **Login/Register**  
   - Upon opening the app, a **Login Page** will appear.  
   - If you already have an account, enter your **username** and **password** to log in.  
   - If you do not have an account, click the **Register** option located on the right side of the navbar to create one.  

2. **Main Page**  
   - After logging in or registering, you will be redirected to the **Main Page**.  
   - The navbar displays the app's name on the left and a **Logout** button on the right, which you can use to log out at any time.  

3. **Adding Tasks**  
   - To add a task, type the task in the **Add Task Bar** and click the **Add** button.  
   - The newly added task will appear on the page, along with the **date and time** of entry.  
   - Each task will also have an individual **Delete** button.  
   - A flash message saying **"Task added successfully"** will confirm the addition.  

4. **Deleting Tasks**  
   - To delete a task, click the corresponding **Delete** button next to it.  
   - The task will be removed from the list, and a flash message saying **"Task deleted successfully"** will confirm the action.  

5. **Task List**  
   - All tasks will be displayed in a table, organized in the order they were added.  

---

### **Future Enhancements**  
Features and improvements I plan to add in the future:  

**Task Editing:** 
- Allow users to edit tasks after they have been added, including the ability to change task details or dates.
**User Profiles:** 
- Enable users to personalize their profiles by adding names, profile pictures, and customizing their app interface.
**Mobile App:**
- Develop a mobile version of the app for easier task management on the go.

---

**Thank you for exploring this project! I hope you find it useful and enjoyable to use.**

---
