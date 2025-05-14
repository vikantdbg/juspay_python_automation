Here is a **complete and professional `README.md` file** for your **Juspay Python Automation** project:

---

```markdown
# 💳 Juspay Payment Flow Automation (Python Version)

This project automates a sample payment flow on the [Guru99 Payment Gateway](https://demo.guru99.com/payment-gateway/index.php) using **Playwright (Python)** and **Pytest**.

It includes test cases for:
- ✅ Successful payments (with valid card)
- ❌ Failed payments (with invalid card)

The script automatically generates:
- 🎥 Screen recordings
- 📸 Screenshots
- 🧪 HTML reports (via `pytest-html`)

---

## 📁 Folder Structure

```

juspay\_python\_automation/
│
├── tests/
│   ├── test\_payment\_success.py     # Valid card test
│   └── test\_payment\_failure.py     # Invalid card test
│
├── .env                            # Environment config (card numbers, CVV, etc.)
├── requirements.txt                # Dependencies
├── pytest.ini                      # Pytest settings
└── README.md                       # This file

````

---

## ⚙️ Tech Stack

| Tool            | Purpose                                          |
|-----------------|--------------------------------------------------|
| `Playwright`    | Browser automation (form filling, clicking)     |
| `Pytest`        | Test runner framework                           |
| `pytest-html`   | Generate HTML test reports                      |
| `python-dotenv` | Manage secrets & environment variables          |

---

## 📦 Setup Instructions

> ⚠️ Assumes Python 3.10+ is installed on your machine

### 1. Clone / Download the Repository

```bash
git clone https://github.com/your-username/juspay_python_automation.git
cd juspay_python_automation
````

Or download and unzip manually.

---

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
python -m playwright install
```

> If `playwright==1.42.1` fails, just run:

```bash
pip install playwright
```

---

### 4. Update Environment Variables

Edit the `.env` file with the correct test values:

```env
TARGET_URL=https://demo.guru99.com/payment-gateway/index.php
VALID_CARD=4111111111111111
INVALID_CARD=1234567890123456
CVV=123
EXP_MONTH=12
EXP_YEAR=2026
```

---

## 🚀 Run Tests

### Generate HTML report with video and screenshots:

```bash
python -m pytest tests/ --html=report.html --self-contained-html
```

HTML report will be saved as `report.html`.

---

## 📂 Output Artifacts

| Folder                | Content                         |
| --------------------- | ------------------------------- |
| `output/videos/`      | Video recording of each session |
| `output/screenshots/` | Screenshots of final state      |
| `report.html`         | Summary HTML test report        |

---

## 🛠️ Author

**Vikrant Singh**


---

## 📌 Notes

* The site always returns "Payment successful" even for invalid cards — handled via logic check.
* Tests are isolated and portable. Just change `.env` for reusability.

```

---

```
