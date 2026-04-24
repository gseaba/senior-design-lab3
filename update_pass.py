import hashlib

def generate_hash():
    password = input("Enter new site password: ")
    h = hashlib.sha256(password.encode()).hexdigest()
    print(f"\nCopy this hash into STORED_HASH in app.py:\n{h}")

if __name__ == "__main__":
    generate_hash()