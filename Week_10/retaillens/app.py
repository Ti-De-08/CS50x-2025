import os
import sqlite3
from flask import Flask, render_template, request
from analysis import load_data, analyze_product

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DB_NAME = "retaillens.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None

    if request.method == "POST":
        file = request.files.get("datafile")

        # Validation
        if not file or file.filename == "":
            error = "No file uploaded"
            return render_template("index.html", results=[], error=error)

        if not file.filename.lower().endswith(".csv"):
            error = "Only CSV files are allowed"
            return render_template("index.html", results=[], error=error)

        # Save file
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Load and analyze
        products = load_data(filepath)

        conn = get_db_connection()
        cursor = conn.cursor()

        for product in products:
            analysis = analyze_product(product)
            results.append(analysis)

            cursor.execute(
                """
                INSERT INTO analyses
                (product_name, category, demand_trend,
                 recommended_quantity, recommended_price, explanation)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    analysis["product_name"],
                    analysis["category"],
                    analysis["demand_trend"],
                    analysis["recommended_quantity"],
                    analysis["recommended_price"],
                    analysis["explanation"],
                ),
            )

        conn.commit()
        conn.close()

    return render_template("index.html", results=results, error=error)


@app.route("/history")
def history():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            product_name,
            category,
            demand_trend,
            recommended_quantity,
            recommended_price,
            created_at
        FROM analyses
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return render_template("history.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
