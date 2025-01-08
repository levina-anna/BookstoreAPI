import os
import time
from fastapi import FastAPI, Query
from sqlalchemy import create_engine, text
import logging
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bookstore API",
    description="This is a simple API for accessing bookstore product and category data",
    version="1.0.0"
)

DATABASE_URL = os.getenv('DATABASE_URL', "mysql+mysqldb://user:123@localhost:3307/bookstore")

engine = None
for _ in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("Connection to database successful")
        break
    except Exception as e:
        print(f"Database not ready, retrying... Error: {str(e)}")
        time.sleep(1)
else:
    print("Failed to connect to the database after 10 retries")

@app.get("/products_and_categories")
def get_products_and_categories(
        category_id: int = Query(None, description="Filter by category ID")
):
    global engine
    if engine is None:
        return JSONResponse(content={"error": "Database connection is not initialized"}, status_code=500)

    sql_query = """
        SELECT 
            p.id AS product_id,
            p.title AS product_title,
            p.price AS product_price,
            p.old_price AS product_old_price,
            c.category_id,
            c.category_name
        FROM 
            product p
        JOIN 
            product_category pc ON p.id = pc.product_id
        JOIN 
            category c ON pc.category_id = c.category_id
    """

    if category_id is not None:
        sql_query += " WHERE c.category_id = :category_id"

    with engine.connect() as connection:
        try:
            result = connection.execute(
                text(sql_query),
                {'category_id': category_id} if category_id is not None else {}
            )

            products_and_categories = [
                {
                    "product_id": row[0],
                    "product_title": row[1],
                    "product_price": row[2],
                    "product_old_price": row[3],
                    "category_id": row[4],
                    "category_name": row[5]
                }
                for row in result
            ]
            logger.info(f"API request: endpoint='/products_and_categories'")
            logger.info(f"API response: {products_and_categories}")
            return products_and_categories
        except Exception as e:
            logger.error(f"Error in API request: {str(e)}")
            return JSONResponse(content={"error": str(e)}, status_code=500)
