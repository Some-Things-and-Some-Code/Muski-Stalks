"""
Controller for the thing
"""

from EmailServices import *

es = EmailServices()


def main():

    # Testing the email sender
    es.send_email()


if __name__ == '__main__':
    main()
