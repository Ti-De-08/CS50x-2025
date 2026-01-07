from Week_10.retaillens.analysis import load_data, analyze_product

data = load_data("sample_data.csv")

for product in data:
    result = analyze_product(product)
    print("-----")
    print(f"Product: {result['product']}")
    print(f"Trend: {result['trend']}")
    print(f"Recommended Quantity: {result['recommended_quantity']}")
    print(f"Selling Price: ₹{result['selling_price']}")
    print(f"Explanation: {result['explanation']}")
