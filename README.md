
# 📝 Feedback Collection App

A simple feedback form built using **Python Flask**, **HTML/CSS**, and **SQLite**, where users can submit feedback with a rating and view submissions in a dashboard.

---

## 🚀 Features

- 🌐 Clean, responsive frontend (HTML + CSS)
- 📦 Feedback stored locally in SQLite database
- ⭐ Star rating system (1 to 5)
- 🕒 Timestamp for every submission
- 📊 Dashboard to view all submitted feedback

---

## 📁 Folder Structure

```
feedback-app/
├── app.py
├── feedback.db (auto-created on first run)
├── static/
│   ├── style.css
│   └── dashboard.css
├── templates/
│   ├── index.html
│   └── dashboard.html
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x  
- Flask

Install Flask with:

```bash
pip install flask
```

---

## ▶️ How to Run

1. Open **Command Prompt** in the project folder  
2. Run the app:

```bash
python app.py
```

3. Open your browser and go to:

```
http://localhost:5000
```

- **Form page**: `/`
- **Dashboard**: `/dashboard`
