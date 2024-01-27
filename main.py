from fastapi import FastAPI, Query
from sqlalchemy import create_engine, text
import logging
from fastapi.responses import JSONResponse

# Создаем логгер
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bookstore API",
    description="This is a simple API for accessing bookstore product and category data",
    version="1.0.0"
)

# Параметры подключения к базе данных
DATABASE_URL = "mysql://user:123@192.168.183.128:3307/bookstore"

# Проверка подключения к базе данных
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    connection.close()
    print("Подключение к базе данных успешно")
except Exception as e:
    print(f"Ошибка при подключении к базе данных: {str(e)}")


@app.get("/products_and_categories")
def get_products_and_categories(
        category_id: int = Query(None, description="Filter by category ID")
):
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

    # Если предоставлен параметр category_id, добавляем условие в SQL запрос
    if category_id is not None:
        sql_query += " WHERE c.category_id = :category_id"

    with engine.connect() as connection:
        try:
            # Если предоставлен параметр category_id, передаем его в запрос
            result = connection.execute(text(sql_query),
                                        {'category_id': category_id} if category_id is not None else {})
            # Структурируем данные
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
            # Добавляем логирование
            logger.info(f"API request: endpoint='/products_and_categories'")
            logger.info(f"API response: {products_and_categories}")
            return products_and_categories
        except Exception as e:
            # Логируем ошибку, если что-то пошло не так
            logger.error(f"Error in API request: {str(e)}")
            # Используйте JSONResponse для возврата ошибки в формате JSON
            return JSONResponse(content={"error": str(e)}, status_code=500)
