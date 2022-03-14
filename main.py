import pandas as pd
from email_slicer import email_process,print_email

def read_file():
    email_list = pd.read_csv('emails.csv',index_col=0)
    main(email_list)


def main(emails_list):
    for email in emails_list.index:
        Email_username,Email_domain = email_process(email)
        print_email(Email_username,Email_domain)

if __name__ == '__main__':
    read_file()