from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        user_name = request.form.get("name")
        return render_template("greet.html", name=user_name)
    return render_template("greet_form.html")

if __name__ == "__main__":
    app.run(debug=True)