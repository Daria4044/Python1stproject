from flask import Flask, request, render_template

app = Flask(__name__)

# Temporary storage for grocery items
grocery_list = [
    {"item": "Apples", "quantity": "5", "category": "Fruits"},
    {"item": "Milk", "quantity": "1 Liter", "category": "Dairy"},
    {"item": "Rice", "quantity": "2 kg", "category": "Grains"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        item_name = request.form.get("item-name")
        quantity = request.form.get("quantity")
        category = request.form.get("category")
        
        if item_name and quantity and category:
            grocery_list.append({"item": item_name, "quantity": quantity, "category": category})

    return render_template("index.html", grocery_list=grocery_list)

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

if __name__ == "__main__":
    app.run(debug=True)
