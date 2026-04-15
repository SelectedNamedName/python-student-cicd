# 1. Используем легкий образ Python
FROM python:3.11-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл зависимостей
COPY requirements.txt .

# 4. Устанавливаем зависимости (если они есть)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем все файлы проекта (.py файлы) в контейнер
COPY . .

# 6. Запускаем программу
CMD ["python", "main.py"]