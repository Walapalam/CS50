import validators

if validators.email(input("Whats your email address? ")) == True:
    print("Valid")
else:
    print("Invalid")