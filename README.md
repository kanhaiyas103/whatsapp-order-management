WhatsApp Multi‑Shop Order Management System (Full Stack)
A full‑stack web platform for managing customer orders across multiple registered shops through a single Twilio WhatsApp Business number.
Built with a FastAPI backend and a custom HTML/CSS/JavaScript frontend for a smooth experience for both customers and vendors.

📌 Features
Single WhatsApp Number for all shops

Multi‑Shop Registration — shopkeepers can register their store with a unique name or code

Public Shop Directory — customers can browse registered shops before ordering

WhatsApp Order Routing — backend parses messages to identify the correct shop

Secure Vendor Dashboard — shopkeepers log in to see only their orders

Order Management — vendors can mark orders as delivered

Real‑time Updates via API polling or WebSockets

Responsive Frontend with HTML5, CSS3, and JavaScript

🛠 Tech Stack
Backend: FastAPI (Python)

Frontend: HTML, CSS, JavaScript (optionally Bootstrap/Tailwind)

Database: SQLite (dev) / PostgreSQL or MySQL (prod)

Messaging API: Twilio WhatsApp Business / Sandbox

Deployment: Backend on Heroku/AWS/DigitalOcean, Frontend on Netlify/Vercel or served from backend

⚙️ Installation
1️⃣ Clone Repository
bash
git clone https://github.com/yourusername/whatsapp-multi-shop.git
cd whatsapp-multi-shop
2️⃣ Backend Setup
bash
cd backend
pip install -r requirements.txt
3️⃣ Configure Environment
Create .env file inside backend/:

text
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+1234567890
4️⃣ Run Backend
bash
uvicorn main:app --reload --port 8000
📲 Twilio WhatsApp Setup
Create a Twilio account

Activate WhatsApp Sandbox or apply for a Business number

Set the webhook URL in Twilio:

text
https://<your-domain>/webhook/whatsapp
Instruct customers to prefix messages with the shop name:

text
StoreA: I need 2 breads
🌐 Frontend Setup
Inside frontend/ folder, edit API URLs to point to your backend

Serve files via Netlify, Vercel, or directly from FastAPI’s static routes

🛒 Workflow
Shopkeeper Registration — admin adds shops to the DB.

Customer Browsing — customer sees shop list on public site.

WhatsApp Order — customer sends an order including shop name.

Order Routing — backend links the order to the correct shop.

Vendor Dashboard — shopkeeper manages their orders.
