# HoneyTrap Honeypot

HoneyTrap is a lightweight, educational honeypot implemented in Python using Flask. It simulates a login portal to attract unauthorized login attempts and logs details about each connection for analysis.

## Features

- **Fake login page** that accepts any credentials and logs timestamp, IP address, user agent, and username/password.
- **Log viewer** at `/logs` that displays captured events in JSON format (restricted to local network by default).
- **Dockerized deployment** for quick setup in isolated environments.

## Running Locally

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the app:

   ```bash
   python app.py
   ```

3. Visit `http://127.0.0.1:5000/` to see the login page. After submitting credentials, navigate to `/logs` to view the recorded attempts.

## Using Docker

You can also run the honeypot in a container:

```bash
docker build -t honeytrap .
docker run -p 5000:5000 honeytrap
```

## Disclaimer

This project is for educational and testing purposes **only**. Do not deploy it on production networks or expose it to the public internet without proper safeguards. Unauthorized monitoring or entrapment may be illegal in your jurisdiction.

---

This honeypot illustrates my ability to build and containerize simple web services, capture network data, and visualize attack patterns.
