FROM python:3.11.5

RUN pip install --upgrade pip
RUN apt update && apt install nano

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Bookstore_API

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /Bookstore_API

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
