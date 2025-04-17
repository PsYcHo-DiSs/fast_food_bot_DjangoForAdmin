FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Делаем скрипт запуска исполняемым
RUN chmod +x entrypoint.sh

# Используем наш скрипт как точку входа
ENTRYPOINT ["./entrypoint.sh"]