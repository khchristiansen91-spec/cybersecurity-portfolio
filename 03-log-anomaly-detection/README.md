# Log Anomaly Detection

This project demonstrates how to detect anomalous patterns in authentication logs using synthetic data and an Isolation Forest model.

## Overview

In many organizations, large volumes of login activity make it difficult to spot suspicious behavior. This project simulates a realistic environment and builds a detection pipeline:

- **Synthetic log generation:** `generate_logs.py` produces a CSV of authentication attempts for multiple users with random timestamps, IP addresses and success/failure indicators.
- **Feature engineering:** convert timestamps to features such as hour-of-day and day-of-week; compute aggregated statistics like failures per user per hour; one-hot encode categorical fields.
- **Isolation Forest modeling:** train an Isolation Forest classifier from scikit ‑learn to identify outliers representing potentially malicious login behavior.
- **Anomaly reporting:** save the top anomalies to a CSV file for further inspection and visualization.

## Running the project

1. Install dependencies (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

2. Generate a dataset of authentication logs:

   ```bash
   python generate_logs.py
   ```

   This writes `auth_logs.csv` in the current directory.

3. Train the model and output the anomalies:

   ```bash
   python train_isoforest.py
   ```

   The script reads `auth_logs.csv`, trains the Isolation Forest, and writes the most suspicious records to `anomalies.csv`.

## Customizing

Feel free to modify the parameters in `generate_logs.py` (number of users, number of records, success/failure probability) and tweak the model hyperparameters in `train_isoforest.py` to experiment with different datasets. You can also extend the feature engineering logic to include new metrics (e.g. geolocation differences, average session lengths) to improve detection accuracy.

---

*This project is for educational and portfolio purposes only. Do not run anomaly detection on real user data without appropriate authorization and privacy considerations.*
