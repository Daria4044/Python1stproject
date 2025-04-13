# 🥦 KeepFresh – Grocery Management Web App

**KeepFresh** is a full-stack web application built with **Python and Flask**. It helps users manage their grocery items, track expiry dates, and get recipe ideas based on what's already in the fridge. The app supports full **CRUD functionality**, uses a real **PostgreSQL database**, and includes both **client-side** and **server-side** features.

---

## 🌟 Key Features

- 🛒 **Add, view, edit, and delete grocery items** in your inventory
- 📅 **Track expiry dates** and get reminded before food goes bad
- 🍽️ **See recipes** based on your available groceries
- 🧾 **Forms for data entry** with input validation
- 👤 **User profile pages** at `/user/<username>`
- 🔁 **Dynamic routing** using Flask
- 🎨 **Custom styles, audio, and video**
- 📄 **404 error page** for invalid URLs

---

## 💻 Live Demo

🌐 [Live app on Render](https://keepfresh-lm77.onrender.com)  
⏳ *Note: May take a few seconds to load on free hosting.*

---

## 🔒 Security & Best Practices

- ✅ Environment variables are used via `.env` (e.g. `DATABASE_URL`)
- ✅ `.gitignore` hides secrets and compiled files
- ✅ SQLAlchemy models protect the database layer
- ✅ Forms include **basic validation** to prevent invalid input
- ✅ Custom 404 page for unknown routes
- ✅ Uses **gunicorn** for production server

---

## 🏗️ Project Structure

```plaintext
my-web-server/
├── app/                     # Main backend application
│   ├── __init__.py          # Package initializer
│   ├── main.py              # Flask app (routes, config)
│   ├── models.py            # SQLAlchemy DB models
│   ├── templates/           # HTML templates (Jinja2)
│   │   ├── index.html
│   │   ├── edit_item.html
│   │   ├── products.html
│   │   ├── recipes.html
│   │   ├── profile.html
│   │   ├── about.html
│   │   ├── notifications.html
│   │   ├── user.html
│   │   └── 404.html
│   └── static/              # CSS, JS, audio, video, images
│       ├── styles.css
│       ├── script.js
│       ├── audio.mp3
│       ├── video.mp4
│       └── images/
├── instance/
│   └── keepfresh.db         # SQLite DB for local dev
├── tests/
│   └── test_routes.py       # Pytest unit tests
├── .env                     # Environment variables (hidden)
├── .gitignore               # Files to exclude from Git
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deploy config
├── SECURITY.md              # Security summary
├── pytest.ini               # Pytest config
└── README.md                # You're here!
