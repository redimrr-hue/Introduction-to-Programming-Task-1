correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Please enter you password:")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts

        if remaining_attempts > 0:
            print(f"Incorrect, please try again. You have {remaining_attempts} attempt(s) remaining")
        else:
            print("No attempts remain, the authorities have been called.")
            break