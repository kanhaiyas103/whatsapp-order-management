# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3
from datetime import datetime
import re

app = FastAPI()

# --- Database helper ---
def get_db():
    conn = sqlite3.connect("orders.db")
    return conn

# --- Create table on startup ---
@app.on_event("startup")
def startup():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS orders
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         created_at TEXT,
                         customer TEXT,
                         message TEXT,
                         item TEXT,
                         qty INTEGER,
                         delivered INTEGER DEFAULT 0)''')

class DeliverRequest(BaseModel):
    order_id: int

# --- Twilio WhatsApp Webhook ---
@app.post("/webhook/whatsapp")
async def handle_whatsapp(request: Request):
    form = await request.form()
    msg = form.get('Body', '').strip()
    customer = form.get('From', '')

    # Parse message like "I need 2 breads"
    match = re.match(r".*?(\d+)\s+([a-zA-Z]+)", msg)
    qty = int(match.group(1)) if match else 1
    item = match.group(2) if match else msg

    with get_db() as conn:
        conn.execute(
            "INSERT INTO orders (created_at, customer, message, item, qty) VALUES (?, ?, ?, ?, ?)",
            (datetime.utcnow().isoformat(), customer, msg, item, qty)
        )
    return {"status": "received"}

# --- Get pending orders ---
@app.get("/orders/pending")
def get_pending_orders():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, created_at, customer, message, item, qty FROM orders WHERE delivered=0"
        ).fetchall()
        return [
            {"id": r[0], "created_at": r[1], "customer": r[2], "message": r[3], "item": r[4], "qty": r[5]}
            for r in rows
        ]

# --- Mark as delivered ---
@app.post("/orders/deliver")
def deliver_order(req: DeliverRequest):
    with get_db() as conn:
        conn.execute("UPDATE orders SET delivered=1 WHERE id=?", (req.order_id,))
    return {"status": "delivered"}
