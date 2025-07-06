# fast_food_bot_DjangoForAdmin

Telegram-бот для оформления заказов фастфуда + админка на Django для управления контентом. Использует PostgreSQL и Docker Compose.


```
fast_food_bot_DjangoForAdmin/
├── bot/                      <-- Aiogram-бот
│   ├── database/
│   ├── keyboards/
│   ├── utils/
│   ├── main.py
│   ├── .env.example          <-- переменные для bot
│   ├── Dockerfile
│   └── entrypoint.sh
├── management/               <-- Django-админка
│   ├── conf/
│   ├── web_admin/
│   ├── manage.py
│   ├── .env.example          <-- переменные для management
│   ├── Dockerfile
│   └── entrypoint.sh
├── media/                    <-- общая папка для изображений
├── db.env.example            <-- переменные для PostgreSQL
└── docker-compose.yml
```

## 🚀 Бысткий старт (Docker Compose)

### 1. 📥 Клонируйте репозиторий

```bash
git clone https://github.com/PsYcHo-DiSs/fast_food_bot_DjangoForAdmin.git
cd fast_food_bot_DjangoForAdmin
```

### 2. 📝 Создайте `.env` файлы

Создайте `.env` файлы на основе примерных:

```bash
cp bot/.env.example bot/.env
cp management/.env.example management/.env
cp db.env.example db.env
```

Отредактируйте поля `TOKEN`, `CLICK_PAYMENT_TOKEN`, `SECRET_KEY` и т.д., подставив свои значения.

### 3. 📦 Запустите проект

```bash
docker-compose up --build
```

Это поднимет три контейнера:

- `fast_food_bot` — телеграм-бот
- `fast_food_admin` — админка на Django (http://localhost:8000)
- `fast_food_db` — PostgreSQL база данных

### 4. 🖼 Загрузка изображений

Все изображения загружаются через админку в `media/`, которая автоматически синхронизируется между ботом и Django.

---

## 🌍 Project Structure

```
Docker Bridge Network (fast_food-network)
 ┌──────────────┬───────────────┬────────────────────┐
 │     bot      │  management   │        db          │
 │  (Aiogram)   │   (Django)    │   (PostgreSQL 15)  │
 │  .env        │   .env        │     db.env         │
 │  /app/media  │  /app/media   │                    │
 └────┬─────────┴────┬──────────┴────────────┬───────┘
      │              │                      │
      │              ▼                      │
     ./media (на хосте, общая папка для изображений)
```

---

## 🇬🇧 English

### 🚀 Quick Start (Docker Compose)

1. **Clone the repository**

```bash
git clone https://github.com/your_username/fast_food_bot_DjangoForAdmin.git
cd fast_food_bot_DjangoForAdmin
```

2. **Create `.env` files from examples**

```bash
cp bot/.env.example bot/.env
cp management/.env.example management/.env
cp db.env.example db.env
```

3. **Edit your `.env` files**

Fill in your own:

- Telegram bot token
- Django secret key
- Payment token (optional)
- Group ID for manager notifications

4. **Launch the whole system**

```bash
docker-compose up --build
```

Visit the Django admin panel at: http://localhost:8000

Images uploaded in the admin panel will be available to the bot via the shared `/media/` directory.

---

### ✅ Requirements

- Docker
- Docker Compose
- Telegram Bot Token (get via @BotFather)

---

## ✅ ToDo / Coming soon

- Webhook deployment support
- Admin panel translation
- QR-code based order tracking

---

### 🔥 Enjoy & contribute!



## Лицензия

Этот проект распространяется под лицензией MIT.  
Любое использование требует сохранения авторства.

> Проект создан в учебных целях.  
> Коммерческое использование — только с согласия автора.
