# Bookstore API

API for accessing product and category data in an online store's database

## Features

- Retrieve a list of all products and their respective categories
- Filter products by category

## API Usage

- GET /products_and_categories
- GET /products_and_categories?category_id=1

## Installation and Launch

```bash
git clone git@github.com:levina-anna/BookstoreAPI.git
cd BookstoreAPI
# Install dependencies
pip install -r requirements.txt
# Run the application
uvicorn main:app --reload
```

## Technologies Used

- Python 3.11
- FastAPI
- SQLAlchemy