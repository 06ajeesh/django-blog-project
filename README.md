# Django Blog Application  

A **feature-rich blogging platform** built with **Django**, allowing users to **write, read, and manage** blogs efficiently. The application provides **role-based functionality** for Writers and Readers, ensuring a seamless blogging experience.

<img src="https://github.com/user-attachments/assets/19d5d55d-1b57-4363-a52a-7070c1d8949e" width="90%" />


---

## **🚀 Features**  

### **🔹 Authentication**  
- Secure **user registration & login** using Django Authentication.  
- Users choose their role (**Writer** or **Reader**) during registration (default: Reader).  
- **Account Management:** Users can update profile details or delete their accounts.

### **📝 Writer Features**  
- **Create Blogs**: Writers can add blog posts with:  
  - **Title**  
  - **Content**  
  - **Optional Image Upload**  
  - **Slug (customizable)**  
- **Manage Blogs**: Writers can view, update, or delete their past submissions from the **dashboard**.

### **📖 Reader Features**  
- **Browse Blogs**: All blog posts are displayed as **cards with images and short descriptions**.  
- **Detailed View**: Clicking on a blog shows its **full content** with comments.  
- **Commenting System**: Readers can add comments on blog posts.

### **📊 Dashboard & User Roles**  
- **📌 Writers** have a **personal dashboard** to manage blogs.  
- **📌 Readers** have an **interactive feed** with blog previews.  
- **🔒 Account Section**: Users can update or delete their accounts anytime.

---

## **🛠️ Technologies Used**  
- **Django** - Backend framework  
- **Django Authentication** - User management  
- **Bootstrap** - Responsive UI  
- **SQLite** - Default database (can be changed to PostgreSQL/MySQL)  

---

## Screenshots

Here are some screenshots from the application:

- **Welcome Page**  
  <img src="https://github.com/user-attachments/assets/19d5d55d-1b57-4363-a52a-7070c1d8949e" width="75%" />

- **Login Page**  
  <img src="https://github.com/user-attachments/assets/8caa90dc-5d82-4cd0-bb6c-79a51400ad02" width="75%" />

- **Register Page**  
  <img src="https://github.com/user-attachments/assets/6a75f4fb-187b-46e4-9afd-8635655481d6" width="75%" />

- **Reader Home Page**  
  <img src="https://github.com/user-attachments/assets/7c0d11aa-2960-415b-9ff7-1fc837119c54" width="75%" />

- **Blog Detailed Page**  
  <img src="https://github.com/user-attachments/assets/0f2d411d-e1b1-4642-ba6f-d66bcebd6082" width="75%" />

- **Writer Home Page**  
  <img src="https://github.com/user-attachments/assets/7a2a953e-e884-49df-b934-55cabdbc97b7" width="75%" />

- **Blog Update Page**  
  <img src="https://github.com/user-attachments/assets/3c90a048-e2f5-479b-905f-d726785ce2bb" width="75%" />

- **User Account Page**  
  <img src="https://github.com/user-attachments/assets/3385b122-8343-4fa6-ba3c-558981cab886" width="75%" />

  
---


## Installation

To set up the project locally, follow these steps:


### 1. Open Project Folder  
**Open a free folder for the project in command-line**

### 2. Clone the Repository  
Run the following command in your terminal:  
  ```bash
  git clone https://github.com/06ajeesh/django-blog-project.git
  ```  



### 3. Create and Activate a Virtual Environment  
**For Windows:**  
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```

**For macOS/Linux:**  
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```


### 4. Change Directory
```bash
cd django-blog-project
```

### 5. Apply Database Migrations  
```bash
python manage.py migrate
```

### 6. Run the Development Server  
```bash
python manage.py runserver
```

### 8. Open the Application in Your Browser  
```
http://127.0.0.1:8000/
```

Now, your **Django Blog Application Project** web application is up and running! 🚀
