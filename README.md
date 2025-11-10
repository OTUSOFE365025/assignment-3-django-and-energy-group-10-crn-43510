Assignment 3 — Django Frameworks & Energy Efficiency
Course: Software Architecture (SOFE 3650U)
Group 10 — CRN 43510
Author: Kenneth Nnah
Overview
This project demonstrates how to use the Django ORM framework to implement a Cash Register Application that:
1. Populates a database with product UPC codes, names, and prices.
2. Allows users to scan or enter a UPC via a web interface (and console) to display the product name and price.
The app also includes Django’s admin panel for product management and uses SQLite as its backend database.

Features
•	• Django ORM Integration — Use Django’s models and migrations without a full web server setup.
•	• Cash Register UI — Input UPC and instantly get product info.
•	• Fixture Loading — Populate the database from a simple products.json file.
•	• Admin Panel Access — View and edit products in a graphical interface.
•	• Web & Console Versions — Run from the terminal or via a local web browser.
Project Structure

assignment-3-django-and-energy-group-10-crn-43510/
├── db/
│   ├── models.py            # Product model (UPC, name, price)
│   ├── forms.py             # ScanForm for UPC input
│   ├── views.py             # scan_view (renders scan.html)
│   └── fixtures/products.json
├── templates/scan.html
├── main.py
├── manage.py
├── settings.py
├── urls.py
└── README.md

How to Run (Windows Instructions)
1.	Clone the repository: git clone https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-10-crn-43510.git
2.	Create and activate a virtual environment: python -m venv venv && venv\Scripts\activate
3.	Install Django: pip install django
4.	Apply migrations: python manage.py makemigrations && python manage.py migrate
5.	Load product fixtures: python manage.py loaddata products
Running the Application
Option A — Console Version: Run python main.py and scan UPCs directly in the terminal.
Option B — Web Version: Run python manage.py runserver and visit http://127.0.0.1:8000/ in a browser.
Energy Efficiency Scenario (Q2)

System: Smartphone health-monitoring app
Stimulus: The app collects sensor data efficiently without draining the battery.
Response: Adjusts sampling and processing frequency dynamically based on user activity.
Response Measure: Battery consumption reduced by 25% compared to constant sampling mode.

•	Architectural Tactics:
•	1. Adaptive Sampling — Adjust data collection based on user context (e.g., slower sampling when idle).
•	2. Batching Work — Combine multiple updates and process together to reduce frequent CPU/network usage.
Technologies Used
•	Python 3.13.7
•	Django 5.2.8
•	SQLite3 Database
•	HTML/CSS for UI
License
Based on Dan Caron’s Django ORM Template (MIT License). Modified for educational purposes at Ontario Tech University, 2025.
