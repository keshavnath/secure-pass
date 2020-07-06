import requests, hashlib, sys

def request_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    res=requests.get(url)
    if res.status_code != 200 :
        print(f"ERROR CODE {res.status_code}")
        raise ValueError
    else:
        print("Request Accepted [CODE:200]")
        print("Getting Response")
        return res

def sha1(raw_password):
    encrypted_pass=hashlib.sha1(raw_password.encode("utf-8")).hexdigest().upper()
    return encrypted_pass

def leak_count(hashes, tail):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if (h==tail):
            return count
    return 0

def api_check(password):
    password=sha1(password)
    first5, tail = password[:5], password[5:]
    response = request_data(first5)
    return (leak_count(response, tail))

def formalcheck(password):
    print(f"Sending Encrypted Password {sha1(password)}")
    count = api_check(password)
    print(f"This password has been part of {count} data leaks.\n\n")

def main():
    inp=0
    while(True):
        print("Enter the password you wish to check, then press Enter:-")
        inp=str(input())
        formalcheck(inp)

if __name__ == "__main__":
    print("\nWelcome to Password Security Checker, a project in Cyber Security")
    print("You are assured that your password is not stored in the system, nor is it sent to any person or website.")
    print("Aditionally, all the data sent and received is encrypted, ensuring maximum security.\n\n")
    while(True):
        try:
            sys.exit(main())
        except:
            print("An error occured.\n\n")