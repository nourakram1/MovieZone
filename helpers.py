import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid
import json

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def search(moviename):
    """Look up quote for symbol."""


    url = (f"https://api.themoviedb.org/3/search/movie?query={urllib.parse.quote_plus(moviename)}&append_to_response=videos,images")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    ids = []

    for movie in response.json()["results"]:
        ids.append(movie["id"])

    # Query API
    try:
        results = []
        for id in ids:
            url1 = (f"https://api.themoviedb.org/3/movie/{urllib.parse.quote_plus(str(id))}?api_key=874996f4786dc54c86215bab9abd3b35")
            response = requests.get(url1, headers=headers)
            results.append(response.json())
        return results

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None

def trending_day():

    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)
    return response.json()["results"]

def trending_weak():
    url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)
    return response.json()["results"]

def idsearch(id):

    url = (f"https://api.themoviedb.org/3/movie/{urllib.parse.quote_plus(str(id))}?api_key=874996f4786dc54c86215bab9abd3b35&append_to_response=videos,images,credits")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def playing_now():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]


def top_rated():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]


def upcoming():
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]


def popular():
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]


def recommendations(id):

    url = (f"https://api.themoviedb.org/3/movie/{urllib.parse.quote_plus(str(id))}/recommendations?language=en-US&page=1")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)
    results = []
    for result in response.json()["results"]:
        results.append({"id": result["id"], "poster_path": result["poster_path"], "title": result["title"], "original_title": result["original_title"]})
    return results


def genres():

    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["genres"]


def search_genre(id):

    url = (f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=en-US&page=1&sort_by=popularity.desc&with_genres={urllib.parse.quote_plus(str(id))}")

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzQ5OTZmNDc4NmRjNTRjODYyMTViYWI5YWJkM2IzNSIsInN1YiI6IjY0ZWNmZjc1NDU4MTk5MDBlMzU0MDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.20zn6icOSlTA558vb07LDe-sMg_IzyL33zyNzwuUCjE"
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]



