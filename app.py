from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = request.args.get("q", "").strip()  # Get search term from URL query (GET)
    
    if request.method == "POST":
        query = request.form.get("search", "").strip()  # Get search term from form submission
    
    # Show a message if the query is empty
    message = None
    if not query:
        message = "Please enter a search term."

    return render_template("index.html", query=query, message=message)

if __name__ == "__main__":
    app.run(debug=True)
