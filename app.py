import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
        to_do = db.execute("SELECT id, task, date FROM list WHERE user_id = :user_id", user_id=session["user_id"])
        return render_template("index.html", to_do=to_do)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    new_task = request.form.get("add_task")
    if new_task:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        default_status = "Pending"
        tasked = db.execute("INSERT INTO list (task, date, user_id, status) VALUES (:task, :date, :user_id, :status)",
                   task=new_task, date=current_date, user_id=session["user_id"], status=default_status)
        if tasked:
            flash("Task added successfully.", "success")
    return redirect("/")


@app.route("/delete", methods=["POST"])
@login_required
def delete_button():
    if request.form.get('delete_button') == 'delete':
        task_id = int(request.form.get('id'))
        user_id = int(session["user_id"])
        result = db.execute("DELETE FROM list WHERE id = :id AND user_id = :user_id", id=task_id, user_id=user_id)
        if result:
            flash("Task deleted successfully.", "success")
        else:
            flash("Error: Task could not be deleted.", "error")
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":
        # username check
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # password check
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # confirmation check
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords must match", 400)

        username = request.form.get("username")
        result = db.execute("SELECT id FROM users WHERE username = ?", username)

        if result:
            return apology("Username already taken", 400)

        hashed_password = generate_password_hash(request.form.get("password"))

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed_password)

        new_user = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = new_user[0]["id"]
        return redirect("/login")

    else:
        return render_template("register.html")
