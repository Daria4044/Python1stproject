from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from my_web_server.models import db, GroceryItem

app = Flask(__name__)

# 🔧 Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keepfresh.db'
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
        # 🛠️ Match field name in your model: item_name
        new_item = GroceryItem(item=item_name, quantity=quantity, category=category)
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for("home"))

# ✅ Other routes
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

# 🚀 Run the app
if __name__ == "__main__":
    app.run(debug=True)
