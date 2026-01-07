CREATE TABLE IF NOT EXISTS analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    cost_price REAL NOT NULL,
    last_month INTEGER NOT NULL,
    prev_month INTEGER NOT NULL,
    gst REAL NOT NULL,
    trend TEXT NOT NULL,
    recommended_quantity INTEGER NOT NULL,
    selling_price REAL NOT NULL,
    explanation TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
