# Sample Django Catalog

This project provides a simple catalog with products, attributes and contact form pages. Administrators can manage all content through the Django admin interface with a double confirmation prompt on deletion.

## Setup

1. Ensure Python 3.11+ is installed.
2. Install requirements:
   ```bash
   pip install django
   ```
3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Visit `/admin/` to log in and manage products, attributes, and form pages. Deleting items requires confirming twice.

The front page lists products and allows filtering by attributes. Contact form pages show a simple drag-and-drop form builder using SortableJS.
