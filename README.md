# Moviezone

**Moviezone** is a dynamic web application built using Flask, integrated with TMDB's API to provide detailed and real-time movie data. Users can explore, search, and interact with a wide variety of movie details such as posters, trailers, cast, reviews, and more. The app also features user accounts to manage movie favourites, watchlists, and viewing history.

### Video Demo:
[Watch Demo on YouTube](https://www.youtube.com/watch?v=9cbuHkfgziE)

---

## Table of Contents:
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Movie Page Details](#movie-page-details)
6. [History Page Details](#history-page-details)
7. [Installation Instructions](#installation-instructions)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

---

## Project Overview

**Moviezone** is a user-friendly, interactive web application developed with Flask that pulls real-time movie data from TMDB (The Movie Database) API. It allows users to:
- Search for movies,
- View detailed movie information,
- Save favourite movies,
- Add movies to their watchlist, and
- Track movies they’ve recently watched.

The app’s primary goal is to provide a seamless experience for movie enthusiasts to explore and interact with movie information. Additionally, this project offers the opportunity to learn how to work with APIs, handle user accounts, and build dynamic web applications using Flask.

---

## Features:
- **User Accounts**:
  - Users can create accounts and log in to manage their personal movie lists (favourites, watchlist, history).
  - Each user has a secure login and session management for personalized experience.

- **Movie Search**:
  - Search movies by title or genre.
  - Display comprehensive movie data such as descriptions, ratings, release dates, trailers, and more.

- **Trending and Popular Movies**:
  - The homepage showcases the current trending, top-rated, and popular movies.
  - Users can explore these lists to find interesting films.

- **Movie Details Page**:
  - Detailed information about each movie: cast, crew, budget, revenue, genres, production companies, runtime, and more.
  - Interactive carousel for movie backdrops and embedded trailers.
  - Movie recommendations based on the selected movie.

- **Favourites List**:
  - Add and remove movies to/from the favourites list for quick access to movies of interest.

- **Watchlist**:
  - Users can add movies they wish to watch in the future to a watchlist and mark them as watched when finished.

- **History Tracking**:
  - Keep track of all movies a user has viewed with timestamps.
  - Clear history feature to reset the list.

- **Responsive Design**:
  - The application is designed to be fully responsive and provides a consistent experience across various devices (desktop, tablet, mobile).

- **API Integration**:
  - Integrated with TMDB's API to fetch real-time data about movies, trailers, cast, ratings, etc.
  
---

## Technologies Used:
- **Flask** (Python): Framework used for building the server-side application, routing, and templating.
- **TMDB API**: External API used to fetch movie data (posters, descriptions, trailers, ratings, etc.).
- **SQLite**: A lightweight database used to store user data (favourites, watchlists, and movie history).
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: Used for dynamic interactions, such as movie search and loading additional content (like trailers or cast details).
- **Jinja2**: Templating engine used by Flask for dynamic HTML rendering.
- **Bootstrap**: A framework for responsive design, ensuring the site looks good on all devices.

---


### Main Pages:
- **Home Page**: Displays trending, top-rated, upcoming, and popular movies.
- **Movie Page**: A detailed page for each individual movie with information like cast, release date, overview, etc.
- **Favourites Page**: Displays a list of movies that the user has marked as favourites.
- **Watchlist Page**: A list of movies that the user plans to watch in the future.
- **History Page**: Displays a record of recently viewed movies with the option to clear history.
- **Search Pages**: Users can search for movies by title or by genre.

---

## Movie Page Details:
On the movie details page, users will see the following information:
- **Movie Poster**: The main image representing the movie.
- **Tagline**: A brief, catchy phrase or quote related to the movie.
- **Overview (Storyline)**: A synopsis or brief description of the movie plot.
- **Genres**: The movie’s genre(s) (e.g., Drama, Comedy, Action).
- **Release Date**: The date the movie was released in theaters.
- **Budget & Revenue**: Financial details, including production cost and total earnings.
- **Language**: Languages in which the movie was produced.
- **Production Companies & Countries**: Information about the companies that produced the movie and the countries where it was filmed.
- **Director & Writers**: Key individuals involved in the creative process.
- **Runtime**: The total duration of the movie.
- **Cast**: The top-billed actors and their profiles.
- **Backdrops**: A carousel of promotional images and scenes from the movie.
- **Trailers**: Embedded YouTube trailers for previewing the movie.
- **Recommendations**: A list of similar movies recommended for the user.

---

## History Page Details:
- **Movie Titles**: The title of movies the user has viewed.
- **Timestamps**: The date and time when each movie was viewed.
- **Clear History**: A button that allows users to clear their entire movie history.

---


