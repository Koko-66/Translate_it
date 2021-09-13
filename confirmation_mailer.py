"""
Set up e-mail connection and send e-mail.

Funtions:
~~~~~~~~
    send_e-mail_confirmation(int, obj, str) -> None

Variables:
~~~~~~~~~
    order_number (generated in run.py)
    customer (instance of Customer class)
    message (created in run.py by create_order_confrimation_message() function
            from order_generator module)
"""
# from boto.s3.connection import S3Connection
import os
import yagmail
# import yagmail_creds


account = os.environ['ACCOUNT']
password = os.environ['PASSWORD']


# code taken from https://mailtrap.io/blog/yagmail-tutorial/
def send_email_confimation(order_number, customer, message):
    """Send confirmation email."""
    try:
        # initializing the server connection
        yag = yagmail.SMTP(account, password)
        yag.send(to=customer,
                 subject=f"Order {order_number} - confirmation",
                 contents=message)
        print("\nEmail sent successfully.\n")
    except EOFError:
        print("Error, e-mail was not sent. Please bear with us while investigate \
the issue.")
