# E-Stock and Customer Tracker

A Django-based client, service, and inventory management system built for **Systems Inc.**, designed to streamline internal operations and improve organizational efficiency.

## 🚀 Project Overview

The **E-Stock and Customer Tracker** centralizes customer information, product details, ongoing/ completed services, and inventory updates into one intuitive platform.
It replaces manual record-keeping with a structured, searchable, and automated workflow—enhancing accuracy, reducing time spent on repetitive tasks, and improving accountability.

## ✨ Key Features

* **Client Management:** Add, edit, and track customer details, contact information, and service history.
* **Inventory Tracking:** Maintain product details, part information, categories, and descriptions.
* **Service Monitoring:** Track job IDs, due dates, priority levels, and repair/service status.
* **Billing & Maintenance Efficiency:** Simplified workflow for generating and managing job-related billing and maintenance records.
* **Search & Filters:** View ongoing and completed services easily.
* **Responsive UI:** Clean, modern interface built for both desktop and laptop use.
* **Background Video UI Enhancement:** Professionally styled UI with background video overlays for the dashboard and service pages.

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Database:** SQLite (default Django database)
* **Other Tools:** Django Template Engine, Font Awesome

## 📂 Project Structure

```
project/
├── clients/           # Client-related models & views
├── products/          # Product & inventory management
├── services/          # Service/job tracking
├── templates/         # HTML templates
├── static/            # CSS, JS, images, videos
└── manage.py
```

## 📝 Learning Outcomes

* Developed a full-stack Django application from scratch.
* Strengthened understanding of MVC architecture, database modeling & form handling.
* Improved UI/UX design skills through custom templates and responsive layouts.

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   ```
2. Navigate into the project folder:

   ```bash
   cd project
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Start the server:

   ```bash
   python manage.py runserver
   ```

## 📌 Future Enhancements

* Automated invoice generation
* Email/SMS notifications for job status
* Role-based user authentication
* Analytics dashboard for service trends

---

Feel free to modify this README to match your repo.
Let me know if you want badges, screenshots, or a better description! 😄
