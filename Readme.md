# 🥗 Calories Tracker

**Track your daily meals and calorie intake with ease!**  
A full-stack Django web application that allows users to log meals, monitor caloric goals, and filter results with flexible date range controls.

---

## 🚀 Features

- 🔐 User registration and authentication
- 🥘 Manual meal entry with calories, date, and time
- 📅 Dashboard view with filter by date range
- 🎯 User profile to set daily calorie expectations
- 📊 Real-time display of total vs expected intake
- ✏️ Edit and delete meals directly from dashboard

---

## 🧱 Tech Stack

| Layer       | Tools                         |
|-------------|-------------------------------|
| Backend     | Django                        |
| Frontend    | Django Templates, Bootstrap   |
| Auth        | Django Auth                   |
| Forms       | Django Forms (`ModelForm`)    |

---

## 📁 Project Structure

calorietracker/ 
├── users/ # Registration and profile 
├── meals/ # Meal CRUD and dashboard 
├── templates/ # HTML templates 
├── static/ # CSS, JS, assets 
├── calorietracker/ # Project config 
└── manage.py


---

## ⚙️ Installation

> **Recommended:** Use virtualenv or Poetry for isolated environments.

```bash
# Clone the repo
git clone https://github.com/your-username/calorie-tracker.git
cd calorie-tracker

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
