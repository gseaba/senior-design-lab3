## Overview
This application serves as a professional portfolio featuring dynamic user profiles and a secure "Message Vault." It adheres to the **KISS (Keep It Simple, Stupid)** engineering philosophy—prioritizing minimalist, transparent configurations over complex automated tools.

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
├── lab3.db             # SQLite database file
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
