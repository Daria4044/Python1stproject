from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Temporary grocery list data
grocery_list = [
    {"item": "Apples", "quantity": "5", "category": "Fruits"},
    {"item": "Milk", "quantity": "1 Liter", "category": "Dairy"},
    {"item": "Rice", "quantity": "2 kg", "category": "Grains"},
]

# Home route (GET only)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", grocery_list=grocery_list)

# Separate POST route to handle form submission
@app.route("/add-item", methods=["POST"])
def add_item():
    item_name = request.form.get("item-name")
    quantity = request.form.get("quantity")
    category = request.form.get("category")

    if item_name and quantity and category:
        grocery_list.append({"item": item_name, "quantity": quantity, "category": category})

    return redirect(url_for('home'))

# Other routes
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

# ✅ Dynamic route
@app.route("/user/<username>")
def user_profile(username):
    return render_template("user.html", username=username)

# ✅ Test route
@app.route("/test")
def test():
    return "Test is working!"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
