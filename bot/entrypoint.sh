#!/bin/sh

# Ждём, пока база поднимется
echo "🕒 Ждём базу данных..."
sleep 5

echo "===> Прогоняем скрипт на создание таблиц и автонаполнение..."
python database/models.py

echo "===> Запускаем бота..."
python main.py