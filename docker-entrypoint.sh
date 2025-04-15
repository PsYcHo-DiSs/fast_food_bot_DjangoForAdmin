#!/bin/bash

# Важно: если база ещё не создана — models.py создаст её и таблицы
echo "⚙️  Инициализация базы..."
python3 ./database/models.py

echo "🚀 Запуск основного приложения..."
exec python3 main.py