# 🥦 KeepFresh – Grocery Management Web App

**KeepFresh** is a dynamic web application that helps users manage groceries, track expiry dates, and find recipes based on available ingredients.

---

## 🚀 Features

- 🛒 **Organized Shopping:** Keep track of your grocery items in one place.
- 📅 **Expiry Reminders:** Get notified before your food goes bad.
- 🍽️ **Smart Recipes:** Discover recipes based on what's in your fridge.
- 📂 **Multiple Pages:** Includes Profile, Notifications, Products, Recipes, and About pages.
- 🧾 **Form Handling:** Add grocery items dynamically using forms.
- 🔁 **Dynamic Routing:** Includes routes like `/user/<username>` for dynamic pages.
- 🖥️ **Client-Side JavaScript:** Adds interactive behavior to the app (like a welcome message).
---

## 🏗️ Project Structure

my-web-server/
│── static/                  # Static files (CSS, images, videos)
│   ├── styles.css           # Stylesheet for the web app
│   ├── images/              # Images used in the app
│   ├── video.mp4            # Video file
│   ├── audio.mp3            # Audio file
│
│── templates/               # HTML templates
│   ├── index.html           # Home page
│   ├── products.html        # Products page
│   ├── profile.html         # Profile page
│   ├── recipes.html         # Recipes page
│   ├── notifications.html   # Notifications page
│   ├── about.html           # About page
│
│── app.py                   # Flask application
│── server.py                 # Server configuration
│── get-pip.py               # Python package installer
│── README.md                # This documentation

✅ This project uses dynamic routing and form handling with Flask.
