import csv


def load_data(filepath):
    """
    Load retail data from a CSV file.
    Returns a list of product dictionaries.
    """

    products = []

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Debug visibility (safe to keep)
        print("CSV headers:", reader.fieldnames)

        for row in reader:
            products.append({
                "product": row["product"],
                "category": row["category"],
                "cost_price": float(row["cost_price"]),
                "last_month": int(row["units_sold_last_month"]),
                "prev_month": int(row["units_sold_prev_month"]),
                "gst": float(row["gst_percent"])
            })

    return products


def analyze_product(product):
    """
    Analyze demand trend and recommend pricing strategy.
    Returns a dictionary for DB insert + UI rendering.
    """

    last = product["last_month"]
    prev = product["prev_month"]

    # Demand trend logic
    if last > prev:
        demand_trend = "rising"
        quantity_multiplier = 1.2
        margin = 0.25
        explanation = (
            "Demand is rising based on last two months sales. "
            "Pricing includes GST and a margin of 25%."
        )
    elif last == prev:
        demand_trend = "stable"
        quantity_multiplier = 1.1
        margin = 0.20
        explanation = (
            "Demand is stable based on last two months sales. "
            "Pricing includes GST and a margin of 20%."
        )
    else:
        demand_trend = "falling"
        quantity_multiplier = 0.9
        margin = 0.15
        explanation = (
            "Demand is falling compared to previous month. "
            "Lower stock and conservative pricing recommended."
        )

    recommended_quantity = int(last * quantity_multiplier)

    # Pricing logic
    base_price = product["cost_price"] * (1 + product["gst"] / 100)
    recommended_price = round(base_price * (1 + margin), 2)

    return {
        "product_name": product["product"],
        "category": product["category"],
        "demand_trend": demand_trend,
        "recommended_quantity": recommended_quantity,
        "recommended_price": recommended_price,
        "explanation": explanation
    }
