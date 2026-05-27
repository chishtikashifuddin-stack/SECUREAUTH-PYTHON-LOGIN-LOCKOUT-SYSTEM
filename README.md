# 🔐 Login and Signup System (Python Project)

A simple command-line based Login and Signup System built using Python.

This project allows users to:
- Create a new account (Sign Up)
- Login using User ID and Password
- Block users after 3 wrong password attempts

The project stores user credentials in a text file and uses basic Python concepts for learning purposes.

---

# 📌 Features

✅ User Signup System  
✅ User Login Authentication  
✅ Password Verification  
✅ User Blocking After 3 Failed Attempts  
✅ Stores Data in Text File  
✅ Beginner Friendly Project  
✅ Menu Driven Program  

---

# 🛠️ Technologies Used

- Python 3
- OS Module
- File Handling

---

# 📂 Project Structure

```bash
Login-Signup-System/
│
├── main.py
├── example.txt
└── README.md
```

---

# ▶️ How To Run The Project

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

---

## Step 2: Download Project

Clone project using Git:

```bash
git clone https://github.com/your-username/login-signup-system.git
```

OR download ZIP manually.

---

## Step 3: Open Terminal

Move to project folder:

```bash
cd Login-Signup-System
```

---

## Step 4: Run Program

```bash
python main.py
```

---

# 📄 About example.txt

The `example.txt` file stores user data.

Format:

```txt
username,password
```

Example:

```txt
admin,1234
john,password123
```

---

# 📋 Program Flow

## Main Menu

```txt
A → Sign Up
B → Login
```

---

# 🔑 Signup Process

1. User enters new ID
2. User enters password
3. Data is saved into `example.txt`

Example:

```txt
rahul,rahul123
```

---

# 🔐 Login Process

1. User enters User ID
2. Program checks availability
3. User enters password
4. Login successful if password matches

---

# 🚫 Security Feature

If user enters wrong password 3 times:

- User gets blocked
- User cannot login again during runtime

---

# 💡 Python Concepts Used

- Functions
- Lists
- Loops
- Conditional Statements
- File Handling
- OS Commands
- User Input
- Global Variables

---

# ⚠️ Limitations

- Passwords are stored in plain text
- No database used
- Blocking resets after program restart
- No encryption/security hashing
- Works only on local machine

---

# 🚀 Future Improvements

- Add Password Encryption
- Use Database (MySQL/SQLite)
- Add Forgot Password Feature
- Add Email Verification
- Improve User Interface
- Create GUI Version

---

# 👨‍💻 Author

Developed by Kashifuddin chishti

---

# 📜 License

This project is free to use for educational purposes.
