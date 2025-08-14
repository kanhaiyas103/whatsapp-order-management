# streamlit_dashboard.py
import streamlit as st
import requests

API = "http://localhost:8000"  # Change to your deployed backend URL

st.set_page_config(page_title="Vendor Dashboard", page_icon="📦")
st.title("📦 WhatsApp Orders Dashboard")

# Show pending orders
orders = requests.get(f"{API}/orders/pending").json()

if not orders:
    st.success("✅ No pending orders right now!")
else:
    for order in orders:
        st.subheader(f"Order #{order['id']}")
        st.write(f"🕒 {order['created_at']}")
        st.write(f"👤 {order['customer']}")
        st.write(f"💬 {order['message']}")
        st.write(f"📦 {order['qty']} x {order['item']}")
        if st.button(f"Mark as delivered", key=order['id']):
            requests.post(f"{API}/orders/deliver", json={"order_id": order['id']})
            st.rerun()
