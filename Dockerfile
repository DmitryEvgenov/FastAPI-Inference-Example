# Используем официальный образ Python 3.8 как базовый
FROM python:3.8-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip3 install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY ./app /app

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
