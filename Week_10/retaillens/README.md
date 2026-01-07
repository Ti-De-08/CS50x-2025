# RetailLens

## Video Demo
<PUT YOUR UNLISTED YOUTUBE VIDEO LINK HERE>

## Description
RetailLens is a web-based data analysis application designed to help small retail shop owners make better stocking and pricing decisions. Users upload monthly sales data in CSV format, and the application analyzes demand trends to recommend optimal quantities and selling prices for each product.

The system uses rule-based analytical logic that considers recent sales performance, cost price, GST percentage, and profit margins. All analysis results are stored persistently in a SQLite database, allowing users to view historical recommendations over time.

This project was built as the final project for CS50x and demonstrates the use of Python, Flask, SQL, HTML, and data processing techniques.

---

## Features
- Upload retail sales data in CSV format
- Analyze demand trends (rising, stable, falling)
- Recommend stocking quantities
- Recommend selling prices including GST and margins
- Persist analysis results using SQLite
- View full analysis history in a browser

---

## Technologies Used
- Python 3
- Flask
- SQLite
- HTML/CSS
- CSV data processing

---

## File Structure
```
retaillens/
│
├── app.py                 # Flask application and routes
├── analysis.py            # Core analysis and business logic
├── schema.sql             # Database schema
├── retaillens.db          # SQLite database (generated at runtime)
├── sample_data.csv        # Example input dataset
├── test_analysis.py       # Basic testing for analysis logic
│
├── templates/
│   ├── index.html         # Upload and analysis results page
│   └── history.html       # Analysis history page
│
├── static/                # Static assets (optional)
├── uploads/               # Uploaded CSV files
└── README.md
```

---

## How to Run the Project

1. Navigate to the project directory:
```bash
cd retaillens
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
sqlite3 retaillens.db < schema.sql
```

4. Run the Flask server:
```bash
flask run
```

5. Open the provided URL in your browser.

---

## CSV Input Format

The uploaded CSV file must contain the following columns:
- product
- category
- cost_price
- units_sold_last_month
- units_sold_prev_month
- gst_percent

### Example
```csv
product,category,cost_price,units_sold_last_month,units_sold_prev_month,gst_percent
Wireless Mouse,Electronics,100,120,100,18
```

---

## Analysis Logic Overview

For each product, RetailLens compares sales from the last two months:
- If sales increased, demand is classified as rising
- If sales remained the same, demand is classified as stable
- If sales decreased, demand is classified as falling

Based on the demand trend:
- Stock quantity is adjusted using predefined multipliers
- Selling price is calculated using cost price, GST, and a profit margin

---

## Limitations
- The analysis logic is rule-based and not machine learning–based
- The system assumes accurate CSV input data
- User authentication and multi-user support are not implemented

---

## Future Improvements
- User accounts and authentication
- AI/ML-based demand forecasting
- Interactive data visualization dashboards
- Multi-store portfolio management
- Exportable analysis reports

---

## Author
Tirtha Debnath

Built as part of Harvard University’s CS50x.
