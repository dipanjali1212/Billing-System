# Billing & Inventory Management System

A full-stack billing and inventory application built with Django. It provides customer management, product stock tracking, invoice creation, payment recording, dashboard analytics, and downloadable PDF invoices.

## Features

- Dashboard with revenue, invoices, customers, payments, and stock alerts
- Customer CRUD and customer account history
- Product CRUD with inventory quantities and low-stock visibility
- Invoice creation with tax and discount calculations
- Server-side price and stock validation
- Automatic stock deduction when an invoice is created
- Payment recording for cash, card, UPI, and bank transfer
- Invoice PDF downloads
- Responsive Bootstrap-based interface
- SQLite database for simple local setup

## Technology

- Python 3.10 or newer
- Django 5.2
- SQLite
- Bootstrap 5, HTML, CSS, and JavaScript
- `xhtml2pdf` for PDF invoice generation

## Requirements

Install Python 3.10 or newer and Git before starting:

- Python: <https://www.python.org/downloads/>
- Git: <https://git-scm.com/downloads>

Check that they are available:

```bash
python --version
git --version
```

On some Windows installations, use `py` instead of `python`.

## Installation

### 1. Clone the project

```bash
git clone https://github.com/dipanjali1212/Billing-System.git
cd Billing-System
```

Make sure the terminal is inside the folder that contains `manage.py` before running Django commands.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If PowerShell blocks activation, run this once as your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

When active, the terminal prompt normally starts with `(.venv)`.

### 3. Install Python packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Always install packages after activating the virtual environment so Django is available to the same Python that runs the project.

### 4. Prepare the database

This project uses SQLite, so no MySQL or PostgreSQL server is required.

```bash
python manage.py migrate
```

Use these commands only after changing models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin user

This is optional for the main billing screens, but enables the Django admin panel at `/admin/`.

```bash
python manage.py createsuperuser
```

### 6. Run the application

From the project directory, with the virtual environment active:

```bash
python manage.py runserver
```

Open:

- Application: <http://127.0.0.1:8000/>
- Admin panel: <http://127.0.0.1:8000/admin/>

Keep the terminal running while using the application. Stop the server with `Ctrl+C`.

To make it available to other devices on the same network during development:

```bash
python manage.py runserver 0.0.0.0:8000
```

Do not use Django's development server for production hosting.

## Run checks and tests

```bash
python manage.py check
python manage.py test
python manage.py migrate --check
```

The tests cover invoice calculations, database pricing, discount validation, and inventory changes.

## Common troubleshooting

### `python` is not recognized

Install Python and enable **Add Python to PATH** during installation. Restart the terminal afterward. On Windows, try:

```powershell
py --version
py -m venv .venv
```

### `No module named django` or `No module named xhtml2pdf`

Activate the virtual environment and install requirements again:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Confirm which Python is running:

```bash
python -c "import sys; print(sys.executable)"
```

### `can't open file 'manage.py'`

Change into the cloned project directory first:

```bash
cd Billing-System
python manage.py runserver
```

The correct directory contains `manage.py`, `core/`, `billing_software/`, and `templates/`.

### `127.0.0.1 refused to connect`

The development server is not running, or it was stopped. Start it again from the project directory:

```bash
python manage.py runserver 127.0.0.1:8000
```

If port `8000` is busy, use another port:

```bash
python manage.py runserver 8001
```

Then open <http://127.0.0.1:8001/>.

## Project structure

```text
Billing-System/
├── billing_software/       # Django project settings and URLs
├── core/                    # Models, forms, views, URLs, utilities, and tests
├── templates/core/          # HTML templates
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django command-line entry point
├── requirements.txt        # Python dependencies
└── README.md               # This guide
```

## Main URLs

| Area | URL |
| --- | --- |
| Dashboard | `/` |
| Customers | `/customers/` |
| Products | `/products/` |
| Invoices | `/invoices/` |
| Admin | `/admin/` |

## Development notes

- The default settings are for local development and use `DEBUG = True`.
- The included SQLite database is convenient for local use; back it up before replacing it.
- Before production deployment, move the secret key into environment variables, configure `ALLOWED_HOSTS`, disable debug mode, configure static files, and use a production WSGI/ASGI server.
- Do not commit passwords, secret keys, virtual environments, or production database files.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
