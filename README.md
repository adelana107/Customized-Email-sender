# 📧 Customized Email Sender (Django)

A Django-based web application that allows users to send **customized, template-based emails** with dynamic content.  
It supports HTML emails, context variables (like name, course, and date), and automatically falls back to a default template if the selected one doesn’t exist.

---

## 🚀 Features

- ✉️ Send rich HTML emails using Django’s built-in email system.  
- 🧾 Choose different email templates based on selected courses or categories.  
- 🔁 Automatically uses a fallback template if a specific one is missing.  
- 📅 Includes dynamic timestamps and context variables in every email.  
- ✅ Simple, responsive UI built with Django forms.

---

## 🛠️ Built With

- **Django** – Web framework for Python  
- **HTML/CSS** – For templates and frontend styling  
- **SMTP** – Email sending (via Django’s `EmailMultiAlternatives`)  
- **Python 3** – Core programming language

---

## 📂 Project Structure

Customized-Email-sender/
│
├── main_app/
│ ├── views.py # Main email sending logic
│ ├── forms.py # Django form for email input
│ ├── templates/
│ │ ├── home.html # Main form page
│ │ ├── Success.html # Success confirmation page
│ │ └── emails/
│ │ ├── default.html # Fallback HTML email template
│ │ ├── course1.html # Optional course-specific templates
│ │ └── course2.html
│ └── ...
│
├── manage.py
└── requirements.txt

yaml

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/adelana107/Customized-Email-sender.git
cd Customized-Email-sender
2️⃣ Create and activate a virtual environment
bash

python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux
3️⃣ Install dependencies
bash

pip install -r requirements.txt
4️⃣ Configure email settings
In your settings.py, add your email backend configuration:

python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
▶️ Run the App
bash

python manage.py runserver
Then open your browser and go to:
👉 http://127.0.0.1:8000/

🧠 How It Works
User fills out the form (name, email, subject, message, and course).

The app builds an email context including the current date/time.

Django tries to load a course-specific HTML email template.

If that template doesn’t exist, it automatically falls back to emails/default.html.

The app sends both plain-text and HTML versions via EmailMultiAlternatives.

After sending, the user is redirected to the Success page.

🪄 Example Template Context
python

{
    'name': 'Adelana',
    'email': 'adelana@example.com',
    'subject': 'Welcome to Python 101!',
    'course': 'Python 101',
    'message': 'Glad to have you in the course!',
    'date': 'October 4, 2025'
}
🏁 Future Improvements
Add support for file attachments

Enable bulk email sending (CSV import)

Add email preview before sending

Use Celery for background task scheduling

🧑‍💻 Author
Adelana Oluwafunmibi Cornelius
📧 adelana787898@gmail.com
🌐 GitHub Profile

