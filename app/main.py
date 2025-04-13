import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import db, GroceryItem

# 🔧 Load environment variables
load_dotenv()

app = Flask(__name__)
@app.route("/health")
def health():
    return "ok", 200

# 🔧 Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔌 Initialize DB
db.init_app(app)

# 🔨 Create DB tables
with app.app_context():
    db.create_all()

# ✅ GET route to show all grocery items
@app.route("/", methods=["GET"])
def home():
    grocery_list = GroceryItem.query.all()
    return render_template("index.html", grocery_list=grocery_list)

# ✅ POST route to add new item
@app.route("/add-item", methods=["POST"])
def add_item():
    item_name = request.form.get("item-name")
    quantity = request.form.get("quantity")
    category = request.form.get("category")

    if item_name and quantity and category:
        new_item = GroceryItem(item=item_name, quantity=quantity, category=category)
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for("home"))

# ✅ Edit item route
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = GroceryItem.query.get_or_404(item_id)

    if request.method == "POST":
        item.item = request.form.get("item-name")
        item.quantity = request.form.get("quantity")
        item.category = request.form.get("category")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_item.html", item=item)

# ✅ Delete item route
@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    item = GroceryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))

# ✅ Other static page routes
@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/user/<username>")
def user_profile(username):
    return render_template("user.html", username=username)

# ✅ Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# 🚀 Run the app (development mode)
if __name__ == "__main__":
    app.run(debug=True)
    