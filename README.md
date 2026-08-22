<div align="center">

#  TalentFlow AI
### Enterprise HR & Employee Lifecycle Management Platform

A modern Human Resource Management System (HRMS) built with **Django**, **Django REST Framework**, **MySQL**, and **JWT Authentication**, designed to streamline the complete employee lifecycle for organizations.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-blue?style=for-the-badge&logo=mysql)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)

</div>

---

# 📖 Overview

TalentFlow AI is a scalable Enterprise HR platform developed using Django and Django REST Framework. The system enables organizations to efficiently manage employees, attendance, departments, leave requests, performance reviews, and secure authentication through JWT-based APIs.

The project follows a modular architecture and industry-standard backend practices suitable for enterprise applications.

---

# ✨ Features

✅ JWT Authentication

✅ Role-Based Access Control (Admin, HR, Manager, Employee)

✅ Employee Management

✅ Department Management

✅ Attendance Tracking

✅ Leave Management

✅ Performance Reviews

✅ REST APIs

✅ Secure Login System

✅ Responsive Dashboard

✅ Modular Django Apps

---

# 🏗️ Architecture

```
                Client (Web / Mobile)
                        │
                        ▼
             Django REST Framework APIs
                        │
        JWT Authentication & Authorization
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Employees       Attendance       Performance
        ▼               ▼               ▼
          Department Management
                        │
                        ▼
                     MySQL Database
```

---

# 🛠️ Tech Stack

## Backend

- Python
- Django
- Django REST Framework

## Database

- MySQL

## Authentication

- JWT Authentication

## Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

## Tools

- Git
- GitHub
- Postman
- VS Code

---

# 📂 Project Structure

```
TalentFlow_AI
│
├── apps
│   ├── accounts
│   ├── employees
│   ├── attendance
│   ├── organizations
│   ├── performance
│   └── notifications
│
├── config
├── templates
├── static
├── requirements
├── manage.py
└── README.md
```

---

# 🔐 Authentication

The application uses **JWT (JSON Web Token)** Authentication.

After successful login:

- Access Token
- Refresh Token

are generated.

Protected APIs require:

```
Authorization: Bearer <Access Token>
```

---

# 🚀 Installation

```bash
git clone https://github.com/harshgiri3531/Telentflow_AI.git
```

```bash
cd Telentflow_AI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Start Server

```bash
python manage.py runserver
```

---

# 📡 API Testing

All REST APIs were tested using **Postman**.

Examples:

- Login API
- Employee CRUD APIs
- Attendance APIs
- Leave APIs
- Performance APIs

---

# 🔒 Security

- JWT Authentication
- Password Hashing
- Role-Based Access Control
- Protected API Endpoints
- Authentication Middleware

---

# 🚀 Future Enhancements

- AI Resume Screening
- Payroll Management
- Recruitment Module
- AI Employee Performance Prediction
- Face Recognition Attendance
- Email Notifications
- HR Analytics Dashboard
- AI Chatbot (RAG + LangChain)

---

# 👨‍💻 Author

**Harsh Giri**

B.Tech Computer Science & Engineering (Artificial Intelligence)

Meerut Institute of Engineering & Technology

GitHub

https://github.com/harshgiri3531

LinkedIn


---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

🤝 Contributions are welcome.
