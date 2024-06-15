import pwinput
import hashlib


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def read_hashedpass():
    """Reads login credentials from 'hashedpass.txt'."""
    with open("hashedpass.txt", "r") as my_file:
        data = my_file.readlines()
            
        new_data = []
            
        for line in data:
            fields = line.split(',')
            fields[1] = fields[1].rstrip()
            new_data.append(fields)
        return new_data
    

def store_login(username, hashed_password):
    """Stores a new login entry (username, hashed_password) in 'hashedpass.txt'."""
    with open("hashedpass.txt", "a") as my_file:
        my_file.write(f"{username},{hashed_password}" + "\n")
    print(f"New login '{username}' stored successfully.")

def register():
    """Handles user registration."""
    username = str(input("Enter username: "))
    password = pwinput.pwinput(prompt="Enter password: ", mask="*")
    
    # Hash the password before storing
    hashed_password = hash_password(password)
    
    # Store username and hashed password in 'hashedpass.txt'
    store_login(username, hashed_password)

def login():
    """Handles the login process."""
    
    
    username = str(input("Enter username: "))
    password = pwinput.pwinput(prompt="Enter password: ", mask="*")
    
    logged_in = False
    hashedpass = read_hashedpass()
    for line in hashedpass:
        if line[0] == username:
            # Hashing the input password to compare with the stored hashed password
            input_hashed_password = hash_password(password)
            if line[1] == input_hashed_password:
                logged_in = True
                break
    
    if logged_in:
        print("Login successful")
        main()
    else:
        print("Login unsuccessful")
        exit()

def main():
    print("Welcome to the Main menu")

if __name__ == "__main__":
    register_or_login = input("Register (R) or Login (L)? ").strip().lower()
    if register_or_login == 'r':
        register()
    elif register_or_login == 'l':
        login()
    else:
        print("Invalid choice. Exiting.")
        exit()