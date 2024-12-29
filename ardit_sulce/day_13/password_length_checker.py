def check_password(password):
    if len(password) < 8:
        return False
    else:
        return True

print(check_password('mylongpassword'))