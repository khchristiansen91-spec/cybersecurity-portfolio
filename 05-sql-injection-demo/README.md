# SQL Injection Attack Demo

This project demonstrates how an improperly written SQL query can be exploited to bypass authentication.  It includes a deliberately vulnerable Flask application and a small exploit script.

## Overview

SQL injection is a class of web vulnerabilities in which untrusted user input is concatenated directly into a database query.  Without proper sanitization, attackers can manipulate the query to alter its logic — for example, by injecting a payload that always evaluates to true.  This repository contains:

- `app.py` – a Flask web application backed by SQLite.  The login form builds its query using Python f‑strings and unsanitised input, making it vulnerable by design.
- `exploit.py` – a script that submits a crafted username payload (`' OR 1=1 --`) to bypass authentication and demonstrate the impact of SQL injection.
- `requirements.txt` – a list of Python dependencies (`Flask`, `requests`).

## Setup

1. **Install dependencies**

   ```bash
   pip install Flask requests
   ```

2. **Run the vulnerable application**

   ```bash
   python app.py
   ```

   The app will start listening on `http://localhost:5000/` and automatically create a `users.db` file with a default `admin:secret` account.

3. **Run the exploit script** (in another terminal):

   ```bash
   python exploit.py
   ```

   The exploit will send the injection payload and should print a welcome message despite not supplying valid credentials.

## Lessons

This demo illustrates why you should **never** build SQL queries using raw string concatenation.  To mitigate SQL injection:

- Use parameterized queries (prepared statements) or an ORM (e.g. SQLAlchemy) that safely binds parameters.
- Validate and sanitize all user input, including form fields and URL parameters.
- Employ security controls like Web Application Firewalls (WAF) and regular code reviews.

Run this project only in a controlled lab environment.  Do not deploy the vulnerable application to a production network.