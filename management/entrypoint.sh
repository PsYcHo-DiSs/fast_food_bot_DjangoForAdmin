#!/bin/sh

# Ждём, пока база поднимется
echo "🕒 Ждём базу данных..."
sleep 5

echo "🚀 Применяем миграции..."
python manage.py migrate

# Создаем суперпользователя, если его нет (можешь изменить под себя)
echo "🔐 Создаём суперпользователя..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '1')
EOF

echo "✅ Запускаем Django-сервер..."
exec python manage.py runserver 0.0.0.0:8000