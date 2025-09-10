# Log Anomaly Detection

This project demonstrates how to detect anomalous user activity in authentication logs using an Isolation Forest model.

## Project overview

- Generate synthetic authentication logs for multiple users with random timestamps and success/failure indicators.
- Engineer features (e.g., failures per user per hour) and one-hot encode categorical fields.
- Train an Isolation Forest model to identify outliers representing potentially malicious behavior.
- Output the top anomalies to a CSV file for further inspection.

The code is written in Python and uses pandas and scikit-learn. Use it as a starting point for building custom detection pipelines.
