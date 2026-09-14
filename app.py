from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="world")

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is a simple Flask app I'm building.</p>"

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        user_name = request.form.get("name")
        return render_template("greet.html", name=user_name)
    return render_template("greet_form.html")

if __name__ == "__main__":
    app.run(debug=True)