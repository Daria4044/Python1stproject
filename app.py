from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home(): 
    return "Welcome to my Flask server!"

# About page
@app.route('/about')
def about():
    return "This is the about page."

# Dynamic route with a variable
@app.route('/user/<string:name>')
def greet_user(name):
    return jsonify({"message": f"Hello, {name}!"})

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)