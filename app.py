from flask import Flask, request, render_template

app = Flask(__name__)

# Home route with search form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("search")
        return f"You searched for: {query}"
    return render_template("index.html")

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
