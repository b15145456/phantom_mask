from flask import Flask, render_template
from flask import render_template # Remove: import Flask
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)