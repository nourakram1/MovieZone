import os
import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import (
    apology,
    login_required,
    search,
    trending_day,
    trending_weak,
    idsearch,
    usd,
    playing_now,
    top_rated,
    upcoming,
    popular,
    recommendations,
    genres,
    search_genre
)

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")


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
    """Show portfolio of stocks"""
    movies=trending_day()
    rand = random.choice(movies)
    return render_template(
        "index2.html",
        rand=rand,
        movies=movies,
        movies1=playing_now(),
        movies2=top_rated(),
        movies3=upcoming(),
        movies4=popular(),
        gen=genres(),
        index=False
        )


@app.route("/open", methods=["GET", "POST"])
@login_required
def open():
    """Show portfolio of stocks"""
    if request.method == "GET":
        return redirect("/")
    else:
        id = request.form.get("movie_id")
        rows = db.execute("SELECT * FROM history WHERE user_id = ? AND movie = ?", session["user_id"], id)
        if len(rows) == 0:
            db.execute("INSERT INTO history (user_id, movie) VALUES (?, ?)", session["user_id"], id)
        else:
            db.execute("DELETE FROM history WHERE user_id = ? AND movie = ?", session["user_id"], id)
            db.execute("INSERT INTO history (user_id, movie) VALUES (?, ?)", session["user_id"], id)

        movie = idsearch(id)
        actors = movie["credits"]["cast"]
        crew = movie["credits"]["crew"]
        if movie["budget"] == 0:
            movie["budget"] = "-"
        else:
            movie["budget"] = usd(int(movie["budget"]))
        if movie["revenue"] == 0:
            movie["revenue"] = "-"
        else:
            movie["revenue"] = usd(int(movie["revenue"]))
        new_fav = True
        new_watch = True
        if (
            len(
                db.execute(
                    "SELECT * FROM watch WHERE user_id = ? AND watch = ?",
                    session["user_id"],
                    id,
                )
            )
            == 1
        ):
            new_watch = False
        if (
            len(
                db.execute(
                    "SELECT * FROM favourites WHERE user_id = ? AND favourit = ?",
                    session["user_id"],
                    id,
                )
            )
            == 1
        ):
            new_fav = False

        writers = []
        director = {}
        for person in crew:
            if person["known_for_department"] == "Directing" and person["job"] == "Director":
                director = person
            elif person["known_for_department"] == "Writing":
                writers.append(person)
        if movie["images"]["backdrops"]:
            downdrop = random.choice(movie["images"]["backdrops"])

            return render_template(
                "open2.html", movie=movie, new_fav=new_fav, new_watch=new_watch, actors=actors, director=director, writers=writers, gen=genres(), relatives=recommendations(id), downdrop=downdrop, index=True
            )
        else:
            return render_template(
                "open2.html", movie=movie, new_fav=new_fav, new_watch=new_watch, actors=actors, director=director, writers=writers, gen=genres(), relatives=recommendations(id), index=True
            )



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        password1 = request.form.get("password")
        password2 = request.form.get("confirmation")
        name = request.form.get("username")
        if not name:
            return apology("Username is not typed!")
        if not password1:
            return apology("Password is not typed!")
        if not password2:
            return apology("Password is not typed!")
        if password1 != password2:
            return apology("Password doesn't match!")
        namecheck = db.execute("SELECT * from users WHERE username = ?;", name)
        if len(namecheck) != 0:
            return apology("The Username is already taken!")
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            name,
            generate_password_hash(password1),
        )
        row = db.execute("SELECT * FROM users WHERE username = ?", name)
        session["user_id"] = row[0]["id"]
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
def movie_search():
    if request.method == "GET":
        return redirect("/")
    else:
        movie_name = request.form.get("movie_name")
        movies = search(movie_name)
        return render_template("search.html", movies=movies, movie_name=movie_name, gen=genres(), index=True)


@app.route("/favourites", methods=["GET", "POST"])
def favourite():
    if request.method == "GET":
        rows = db.execute(
            "SELECT * FROM favourites WHERE user_id = ?", session["user_id"]
        )
        movies = []
        for row in rows:
            movies.insert(0, idsearch(row["favourit"]))
        user_name = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["username"]
        return render_template("favourites2.html", movies=movies, gen=genres(), index=True, user_name=user_name)
    elif request.method == "POST":
        id = request.form.get("favourite_id")
        if request.form.get("case") == "add":
            db.execute(
                "INSERT INTO favourites (user_id, favourit) VALUES (?, ?)",
                session["user_id"],
                id,
            )
        if request.form.get("case") == "delete":
            db.execute("DELETE FROM favourites WHERE favourit = ?", id)
        return redirect("/favourites")


@app.route("/want_to_watch", methods=["GET", "POST"])
def want_to_watch():
    if request.method == "GET":
        rows = db.execute("SELECT * FROM watch WHERE user_id = ?", session["user_id"])
        movies = []
        for row in rows:
            movies.insert(0, idsearch(row["watch"]))
        user_name = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["username"]
        return render_template("watch.html", movies=movies, gen=genres(), index=True, user_name=user_name)
    elif request.method == "POST":
        id = request.form.get("watch_id")
        if request.form.get("case") == "add":
            db.execute(
                "INSERT INTO watch (user_id, watch) VALUES (?, ?)",
                session["user_id"],
                id,
            )
        if request.form.get("case") == "delete":
            db.execute("DELETE FROM watch WHERE watch = ?", id)
        return redirect("/want_to_watch")


@app.route("/history", methods=["GET", "POST"])
def history():
        if request.method == "POST":
            if request.form.get("clear_history") == "yes":
                db.execute("DELETE FROM history")
                return render_template("history.html", gen=genres(), index=True)
            else:
                redirect("/history")
        else:
            rows = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
            movies = []
            for row in rows:
                movies.insert(0, {"date":row["time"], "movie":idsearch(row["movie"])})
            user_name = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]["username"]
            return render_template("history.html", movies=movies, gen=genres(), index=True, user_name=user_name)



@app.route("/genre", methods=["GET", "POST"])
def movie_genre():
    if request.method == "GET":
        return redirect("/")
    else:
        genre_id = request.form.get("genre_id")
        genre_name = request.form.get("genre_name")
        movies = search_genre(genre_id)
        return render_template("genre.html", movies=movies, genre_name=genre_name, gen=genres(), index=True)
