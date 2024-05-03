# Vendor Management System

The Vendor Management System is a web application designed to manage vendors, track purchase orders, and evaluate vendor performance.

## Features

- **Vendor Profile Management**: Create, update, delete, and view vendor profiles.
- **Purchase Order Tracking**: Track purchase orders with details such as PO number, order date, items, quantity, and status.
- **Vendor Performance Evaluation**: Evaluate vendor performance metrics including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Setup

1. Clone the repository:

```
git clone https://github.com/Yash-Bari/vendor-management.git
cd vendor-management
```

2. Create a virtual environment and install dependencies:

```
python -m venv venv
source venv/bin/activate  # for Unix/Linux
venv\Scripts\activate      # for Windows
pip install -r requirements.txt
```

3. Connect to your database of choice in `vendor_management/settings.py`. By default, the application is configured to use SQLite.

4. Apply database migrations:

```
python manage.py migrate
```

5. Create a superuser for accessing the admin panel:

```
python manage.py createsuperuser
```

6. Run the development server:

```
python manage.py runserver
```

7. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to manage vendors, purchase orders, and historical performance data.
- **API Endpoints**: Access API endpoints for vendors and purchase orders at `http://127.0.0.1:8000/api/`.
- **All API are as given in assingment file.**
