🚀 Background Task Processing System

A Django-based backend system designed to handle long-running tasks asynchronously without blocking API requests.

---

 📌 Project Overview

In traditional API design, long-running tasks (such as file processing, data aggregation, or external API calls) block the request-response cycle, leading to poor performance and bad user experience.

This project demonstrates how to design a backend mechanism that:

- Stores tasks in the database
- Processes them asynchronously
- Tracks their lifecycle states
- Allows clients to monitor task progress

---

✨ Key Features

- ✅ Asynchronous task handling
- ✅ Task lifecycle management
- ✅ Status tracking system
- ✅ Basic error logging
- ✅ REST API integration
- ✅ PostgreSQL database support

---
🔄 Task Lifecycle States

Each task moves through the following states:

- PENDING– Task created but not started
- RUNNING – Task currently executing
- SUCCESS – Task completed successfully
- FAILED – Task failed due to an error

---

🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL

---


---

⚙️ How the System Works

1. A client sends a request to create a background task.
2. The task is saved in the database with status = `PENDING`.
3. The background process updates status to `RUNNING`.
4. After execution:
   - If successful → status becomes `SUCCESS`
   - If error occurs → status becomes `FAILED`
5. The client can check the task status using the provided API endpoint.

Setup Instructions

git clone https://github.com/rishikavanamala/background_tasks_processor.git
cd background_tasks_processor


Install Dependencies:
pip install -r requirements.txt

 Run Migrations
python manage.py makemigrations
python manage.py migrate

 Run Development Server
python manage.py runserver


Server will start at:

http://127.0.0.1:8000/
