# Bookstore API

API for accessing product and category data in an online store's database

## Features

- Retrieve a list of all products and their respective categories
- Filter products by category

## API Usage

- GET /products_and_categories
- GET /products_and_categories?category_id=1

## Installation and Launch

1. Clone the repository:
```bash
git clone git@github.com:levina-anna/BookstoreAPI.git
cd BookstoreAPI
```
2. Launch the application using Docker:
```
docker-compose up --build
```
3. Open the application in your browser: http://localhost:8002/docs

## Technologies Used

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.79.0-yellow)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.39-pink)
