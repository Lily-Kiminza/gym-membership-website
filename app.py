"""
IronRow Gym - Membership Website
A beginner-friendly Flask project.

WHAT THIS FILE DOES:
- Starts a small web server on your computer
- Sends different HTML pages depending on which URL is visited
- Handles the contact form when someone submits it
"""

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-to-any-random-text"  # needed for flash messages

# ---------------------------------------------------------
# DATA (in a real app this would come from a database.
# For a beginner project, plain Python lists/dictionaries
# are perfect and easy to understand.)
# ---------------------------------------------------------

MEMBERSHIP_PLANS = [
    {
        "name": "Drop-In",
        "price": "$15",
        "period": "per visit",
        "features": ["Full gym floor access", "Locker room access", "No commitment"],
        "highlight": False,
    },
    {
        "name": "Monthly",
        "price": "$49",
        "period": "per month",
        "features": [
            "Unlimited gym floor access",
            "All group classes included",
            "Free fitness assessment",
            "Cancel anytime",
        ],
        "highlight": True,
    },
    {
        "name": "Annual",
        "price": "$39",
        "period": "per month, billed yearly",
        "features": [
            "Everything in Monthly",
            "2 personal training sessions/month",
            "Guest passes (4/year)",
            "Priority class booking",
        ],
        "highlight": False,
    },
]

CLASSES = [
    {"day": "Monday", "time": "6:00 AM", "name": "Strength Foundations", "coach": "Marcus"},
    {"day": "Monday", "time": "6:00 PM", "name": "HIIT Circuit", "coach": "Dana"},
    {"day": "Tuesday", "time": "7:00 AM", "name": "Mobility & Recovery", "coach": "Priya"},
    {"day": "Wednesday", "time": "6:00 PM", "name": "Olympic Lifting", "coach": "Marcus"},
    {"day": "Thursday", "time": "6:00 AM", "name": "HIIT Circuit", "coach": "Dana"},
    {"day": "Friday", "time": "5:30 PM", "name": "Strength Foundations", "coach": "Priya"},
    {"day": "Saturday", "time": "9:00 AM", "name": "Community WOD", "coach": "All Coaches"},
]

# ---------------------------------------------------------
# ROUTES (each function below controls one page/URL)
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html", active_page="home")


@app.route("/membership")
def membership():
    return render_template("membership.html", plans=MEMBERSHIP_PLANS, active_page="membership")


@app.route("/classes")
def classes():
    return render_template("classes.html", classes=CLASSES, active_page="classes")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in every field before sending.", "error")
        else:
            # In a real app you'd email this or save it to a database.
            # For now we just print it to the terminal so you can see it worked.
            print(f"New inquiry from {name} <{email}>: {message}")
            flash("Thanks! Your message has been sent. We'll get back to you soon.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html", active_page="contact")


if __name__ == "__main__":
    app.run(debug=True)
