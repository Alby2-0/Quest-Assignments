
import logging

logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class InvalidLoginError(Exception):
    pass


username = "employee"
password = "12345"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == "" or entered_password == "":
            raise InvalidLoginError("Username or password cannot be empty")

        if entered_username != username or entered_password != password:
            raise InvalidLoginError("Invalid username or password")

    except InvalidLoginError as e:
        attempts += 1
        print("Login failed:", e)
        logging.warning("Failed login attempt %d", attempts)

        if attempts == max_attempts:
            print("Maximum login attempts exceeded.")
            logging.error("Maximum login attempts exceeded")
        else:
            print("Attempts remaining:", max_attempts - attempts)

    else:
        print("Login successful! Welcome, employee.")
        logging.info("Successful login by employee")
        break

    finally:
        print("Login process completed for this attempt.")

if attempts == max_attempts:
    print("Access denied.")
