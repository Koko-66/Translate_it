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
import yagmail
import yagmail_creds


# code taken from https://mailtrap.io/blog/yagmail-tutorial/
def send_email_confimation(order_number, customer, message):
    """Send confirmation email."""
    try:
        # initializing the server connection
        yag = yagmail.SMTP(yagmail_creds.user, yagmail_creds.password)
        # yag = yagmail.SMTP(yagmail_creds.user,
        # oauth2_file="~/oauth2_creds.json")
        yag.send(to=customer,
                 subject=f"Order {order_number} - confirmation",
                 contents=message)
        print("\nEmail sent successfully.")
    except EOFError:
        print("Error, e-mail was not sent. Please bear with us while investigate \
the issue.")
