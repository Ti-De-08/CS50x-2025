import os
from flask import Flask, render_template, request
from analysis import load_data, analyze_product

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        file = request.files.get("datafile")

        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            products = load_data(filepath)
            for product in products:
                results.append(analyze_product(product))

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
