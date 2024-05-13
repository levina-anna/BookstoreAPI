# Используем образ Python
FROM python:3.11.5

# Обновляем пакеты, устанавливаем nano
RUN pip install --upgrade pip
RUN apt update && apt install nano

# Устанавливаем переменную окружения для Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /Bookstore_API

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /Bookstore_API

# Запускаем приложение на Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
