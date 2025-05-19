# 🔐 Simple Python Login System

A basic Python script for secure user **registration** and **login**, using **SHA-256 password hashing**. User credentials are stored in a local text file (`hashedpass.txt`).

---

## 📁 Files Included

| File Name       | Description                                      |
|----------------|--------------------------------------------------|
| `encryptpwd.py` | The main Python script for handling user auth.  |
| `hashedpass.txt`| Stores usernames and their SHA-256 hashed passwords. |

---

## ⚙️ How It Works

### 📝 Registration

- Prompts the user for a **username** and **password**.
- Hashes the password using `hashlib.sha256`.
- Stores the result in `hashedpass.txt` in the format:

  ```text
  username,hashed_password

---

🧪 Example Stored Hashes

ana,24d4b96f58da6d4a8512313bbd02a28ebf0ca95dec6e4c86ef78ce7f01e788ac
freddy,51eeed7251f3f56288ee554afaa1028b7fbc3daacc4a952be4ae8d18ddaf3320
jeff,2e0b8d61fa2a6959d254b6ff5d0fb512249329097336a35568089933b49abdde
marilyn,dc5321cfe2b29a8856229f03b89cb5c597c5b19f255bed7dc888f0867b25c78d

---
🧰 Requirements
Python 3.x

pwinput module for hidden password input

Installation
To install the required library:

pip install pwinput

---

▶️ How to Run
Run the script from the terminal:

python encryptpwd.py

---

- Type `R` to register a new user.
- Type `L` to log in with an existing account.

---

## 📝 Notes

- Passwords are **never** stored in plaintext.
- SHA-256 provides **one-way secure hashing** (cannot be reversed).
- `hashedpass.txt` will be created automatically if it doesn't exist.
- This is a learning project — not meant for production use.
- For production systems, consider:
  - Password salting
  - Input validation
  - Secure file permissions
  - Encrypted databases or secure storage solutions

---

## 📄 License

This project is open-source and free to use for educational purposes.



