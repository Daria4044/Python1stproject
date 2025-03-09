from flask import Flask, request, render_template

app = Flask(__name__)

# Home route with search form
@app.route("/", methods=["GET", "POST"])
def home():
    query = request.args.get("q", "").strip()  # Get search term from URL query string

    if request.method == "POST":
        query = request.form.get("search", "").strip()  # Get search term from form submission

    # If query is empty, show error message
    if not query:
        return render_template("index.html", message="Please enter a search term", query=query)

    return render_template("index.html", query=query)

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)