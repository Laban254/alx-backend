#!/usr/bin/env python3
"""Basic Flask app """

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Function documentation: Renders the index.html template."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
