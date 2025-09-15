# Ransomware Simulator & Detection

This project provides a hands‑on look at how ransomware encrypts files and how defenders might respond.  It includes:

- `encryptor.py` – a script that traverses a target directory and encrypts all files using a symmetric key.  The key is generated on first run and saved to `key.key`.
- `decryptor.py` – a companion script that uses the stored key to restore encrypted files to their original state.
- `monitor.py` – a simple directory watcher powered by the `watchdog` library.  It prints alerts whenever files are created, modified, or deleted, which can indicate a ransomware attack in progress.
- `requirements.txt` – lists Python dependencies (`cryptography`, `watchdog`).

## Setup

1. **Install dependencies**

   ```bash
   pip install cryptography watchdog
   ```

2. **Prepare a test directory**

   Create a folder called `data` in this project directory and populate it with some test files (e.g. text files).  You can pass a different path to the scripts if you wish.

3. **Run the monitor (optional)**

   In one terminal, start monitoring the directory for changes:

   ```bash
   python monitor.py data
   ```

   This will print a message whenever files are created, modified, or deleted.  Use this to observe the effect of encryption.

4. **Encrypt files**

   In another terminal, run the encryptor against your data folder:

   ```bash
   python encryptor.py data
   ```

   The script will generate a key (if one does not already exist) and overwrite each file with its encrypted bytes.  It will skip Python files and the key itself.

5. **Decrypt files**

   After observing the changes, restore your files:

   ```bash
   python decryptor.py data
   ```

   The decryptor reads the same key and rewrites each file with the original contents.

## Notes

- This project is for educational purposes only.  Do not run the encryptor against any important data; it will overwrite files in place.  Always test in a safe environment.
- The monitor script is simplistic and intended to illustrate the concept of file integrity monitoring.  In real deployments you would integrate with a SIEM, endpoint security suite, or backup solution.
