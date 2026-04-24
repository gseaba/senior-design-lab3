## Overview
This application serves as a professional portfolio featuring dynamic user profiles and a secure "Message Vault."

### Key Features
- **Dynamic Profiles:** User information and bios served via Flask and SQLite.
- **Secure Message Vault:** A protected area for viewing messages, gated by a SHA-256 hashed password system.
- **Session Management:** Secure user sessions to prevent unauthorized access to protected routes.
- **Responsive Design:** A custom "Black & Gold" UI theme optimized for clarity and professional aesthetics.
- **Production Deployment:** Managed by Gunicorn and Nginx on a Linux VPS with automated recovery.

## Tech Stack
- **OS:** Ubuntu 24.04 LTS (Production) / Arch Linux (Development)
- **Backend:** Python 3, Flask
- **WSGI:** Gunicorn
- **Proxy:** Nginx
- **Database:** SQLite3
- **Security:** SHA-256 Password Hashing, Flask-Session

## Project Structure
```text
senior-design-lab3/
├── app.py              # Main Flask application logic
├── init_db.py          # Database initialization script
├── update_pass.py      # Utility for generating SHA-256 password hashes
├── data/
    └── messages.db     # SQLite database file
├── requirements.txt    # Python dependency manifest
├── static/
│   └── css/
│       └── style.css   # Custom Black & Gold styling
├── templates/
│   ├── base.html       # Shared layout template
│   ├── index.html      # Portfolio homepage
│   ├── login.html      # Secure login page with error handling
│   └── protected.html  # The Message Vault
└── lab3.service        # Systemd unit file for production auto-start
```

## Installation & Deployment

### Local Development
1. **Clone the repo:** `git clone <repo-url>`
2. **Setup Venv:** `python -m venv venv && source venv/bin/activate`
3. **Install Deps:** `pip install -r requirements.txt`
4. **Init DB:** `python init_db.py`
5. **Run:** `python app.py`

### Production Deployment
This project is designed for high-availability on a Linux VPS:
1. **Systemd Integration:** Managed via `lab3.service` to ensure the app survives system reboots and crashes.
2. **Reverse Proxy:** Nginx handles incoming HTTP traffic on Port 80 and funneling it to the Gunicorn Unix socket.
3. **Permissions:** Configured with specific `chmod` settings to allow `www-data` access to the socket and database while maintaining home directory security.

## 🛡 Security Implementation
The "Message Vault" uses a one-way **SHA-256 hashing algorithm**. 
- **No Plaintext Storage:** Passwords are never stored in the database.
- **Session Logic:** Authentication is handled via server-side sessions; unauthorized attempts to access `/protected` result in an immediate redirect to the login gate.
- **Input Validation:** Error handling is implemented to provide feedback on failed login attempts without leaking system details.

---
**Developers:** Garrett Seaba, Bowen Davis, Jane Kim 
**Course:** Senior Design 1, University of Iowa  
**Date:** April 2026
