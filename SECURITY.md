## 🔐 8.1 – Common Security Risks (Explained Like I’m 5)

When we put our web app on the internet, bad people might try to break it or steal data. Here's how they can do it – and how we protect our app:

### 🧨 1. SQL Injection
**What it is:** A hacker types sneaky code instead of normal data (like item name) to break the database.

**How we protect:** We use SQLAlchemy ORM with models – this keeps the database safe by escaping dangerous input.

---

### 🧼 2. XSS (Cross-Site Scripting)
**What it is:** Someone enters dangerous scripts (JavaScript) in a form to mess up your page or steal data.

**How we protect:** Flask auto-escapes user input in templates. We also don’t allow raw HTML in form inputs.

---

### 🛂 3. Sensitive Info Exposure
**What it is:** Accidentally showing secret info (like database passwords) to others.

**How we protect:** We moved secrets (like the DB URI) to a `.env` file and excluded it in `.gitignore`.

---

### 🚫 4. Broken Routes & Error Pages
**What it is:** If a user types a wrong URL, they might see a boring or insecure error.

**How we protect:** We added a **custom `404.html` page** so users don’t see Flask's default error page.

---

### ✅ What we already did right:
- Used `.env` to hide sensitive config.
- Sanitized user input using Flask forms and model validation.
- Validated data before saving to the DB.
- Used a custom 404 page.
