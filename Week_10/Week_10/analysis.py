import csv

def load_data(filepath):
    """
    Load retail data from a CSV file.
    Returns a list of product dictionaries.
    """
    products = []

    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "product": row["product"],
                "cost_price": float(row["cost_price"]),
                "last_month": int(row["units_sold_last_month"]),
                "prev_month": int(row["units_sold_prev_month"]),
                "gst": float(row["gst_percent"])
            })

    return products


def analyze_product(product):
    """
    Analyze demand, recommend price and quantity.
    """
    last = product["last_month"]
    prev = product["prev_month"]

    # Demand trend
    if last > prev:
        trend = "rising"
        quantity_multiplier = 1.2
        margin = 0.25
    elif last == prev:
        trend = "stable"
        quantity_multiplier = 1.1
        margin = 0.20
    else:
        trend = "falling"
        quantity_multiplier = 0.9
        margin = 0.15

    recommended_quantity = int(last * quantity_multiplier)

    # Pricing
    base_price = product["cost_price"] * (1 + product["gst"] / 100)
    selling_price = round(base_price * (1 + margin), 2)

    explanation = (
        f"Demand trend is {trend}. "
        f"Recommended quantity adjusted accordingly. "
        f"Selling price includes GST and a {int(margin * 100)}% margin."
    )

    return {
        "product": product["product"],
        "trend": trend,
        "recommended_quantity": recommended_quantity,
        "selling_price": selling_price,
        "explanation": explanation
    }
