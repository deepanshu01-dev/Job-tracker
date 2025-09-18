# 🧾 Job Application Tracker

A web-based platform built with Django and PostgreSQL that allows job seekers to track the status of their job applications in one centralized place.

## 🚀 Overview

This Job Application Tracker helps job applicants manage their job search by enabling them to:

- Save job postings
- Track the status of each application (e.g., Bookmarked, Applying, Applied, etc.)
- Update or delete job entries
- View job stats based on their status

It's designed for simplicity and ease of use, offering a clean UI with Bootstrap and Django templates — no external frontend frameworks.

---

## ✨ Features

- 📝 **User Registration & Login**
- ➕ **Add New Job Applications**
- 🗃️ **Job List Table View**
- 🔍 **Job Detail Page**
- 🛠️ **Edit & Delete Job Entries**
- 📌 **Track Status of Each Job (Bookmarked, Applying, Applied, etc.)**
- 📊 **Status Summary on Job List Page**

---

## 🧑‍💻 Tech Stack

- **Backend:** Python, Django 
- **Database:** PostgreSQL
- **Frontend:** Django Templates + Bootstrap
- **Environment:** Python Virtual Environment (`venv`)

---

## 📁 Project Structure

```bash
job-application-tracker/
├── accounts/           # User authentication (signup, login, logout)
├── jobs/               # Job-related functionality (add, update, delete, list, detail)
├── templates/          # HTML templates (Bootstrap-based)
├── static/             # Static files (CSS, JS, etc.)
├── manage.py
├── requirements.txt
└── README.md

git clone https://github.com/deepanshu01-dev/Job-tracker.git
cd job_tracker

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install -r requirements.txt



