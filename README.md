# 🥦 KeepFresh – Grocery Management Web App

**KeepFresh** is a full-stack web app built with Flask. It helps users manage grocery items, track expiry dates, and get recipe ideas based on what's in the fridge. It also includes client-side JavaScript and server-side routing, plus a working database with CRUD features.

---

## 🚀 Features

- 🛒 **Organized Shopping** – Add, view, edit, and delete grocery items.
- 📅 **Expiry Reminders** – Stay notified before food items go bad.
- 🍽️ **Smart Recipes** – Explore recipes based on your groceries.
- 🧾 **Form Handling** – Add new items using HTML forms.
- 🔁 **Dynamic Routing** – User profile pages via `/user/<username>`.
- 💻 **Client-Side Interaction** – JavaScript interaction and media elements.
- 🖼️ **Static Media** – Custom CSS, images, audio, and video integration.
- 🧠 **Custom 404 Page** – Better UX for invalid routes.

---

## 🔒 Security & Best Practices

- ✅ Input validation for all form fields.
- ✅ Secure data models using SQLAlchemy.
- ✅ `.env` file for keeping sensitive config private.
- ✅ `.gitignore` set up to exclude secrets and compiled files.
- ✅ Custom error page (`404.html`) to handle unknown routes securely.

---

## 🏗️ Project Structure

```plaintext
my-web-server/
├── static/                  # Static files (CSS, JS, media)
│   ├── styles.css           # Main styles
│   ├── script.js            # JavaScript interactivity
│   ├── video.mp4            # Embedded video
│   ├── audio.mp3            # Background audio
│   └── images/
│       └── about-image.jpg  # Image used on the About page
├── templates/               # HTML templates rendered by Flask
│   ├── index.html
│   ├── products.html
│   ├── profile.html
│   ├── recipes.html
│   ├── notifications.html
│   ├── about.html
│   ├── user.html
│   └── 404.html             # Custom error page
├── my_web_server/           # Backend logic
│   ├── app.py               # Main Flask app
│   ├── models.py            # SQLAlchemy DB models
│   └── __init__.py          # Package initializer
├── instance/
│   └── keepfresh.db         # SQLite database
├── .env                     # Environment variables (not tracked by Git)
├── .gitignore               # Ignore rules for version control
├── requirements.txt         # Python package dependencies
└── README.md                # Project documentation

---

## ✅ Technologies Used

- Python + Flask
- HTML / CSS
- JavaScript (client-side logic)
- SQLite + SQLAlchemy (ORM)
- Jinja2 templating
- Git & GitHub for version control

---

## 💡 Notes

- This app was created as part of the SE_19 module.
- It follows the best practices in structure, routing, and deployment.
- Tasks completed include form handling, dynamic pages, client-side scripts, and full CRUD with a database.

---

