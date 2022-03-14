
def Email_Slicer():
    Email = input("what is your email ?\n").strip()
    Email_username,Email_domain = email_process(Email)
    print_email(Email_username,Email_domain)

def print_email(Email_username,Email_domain):
    print("username:{} -- domain:{}".format(Email_username,Email_domain))

def email_process(email):
    Email_username = email[0:email.index("@")]
    Email_domain = email[email.index("@")+1:]
    return [Email_username,Email_domain]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Email_Slicer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
