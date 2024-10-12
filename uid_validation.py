import re


def valid_uid(uid):
    """Function checks Conditions for Valid UID"""

    # Check if the UID has exactly 10 characters
    if len(uid) != 10:
        return False

    # Check if all characters are alphanumeric
    if not uid.isalnum():
        return False

    # Check if there are at least 2 uppercase characters
    if len(re.findall(r"[A-Z]", uid)) < 2:
        return False

    # Check if there are at least 3 digits
    if len(re.findall(r"[0-9]", uid)) < 3:
        return False

    # Check if all characters are unique
    if len(set(uid)) != len(uid):
        return False

    return True


# Input processing
def main():
    T = int(input())  # Number of test cases

    for _ in range(T):
        uid = input().strip()  # Reading UID
        if valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
