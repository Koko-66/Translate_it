"""
Email customer the order details
"""
import yagmail
import yagmail_creds


# code taken from https://mailtrap.io/blog/yagmail-tutorial/
def send_email_confimation(order_number, customer, message):
    """
    Send confirmation email.
    """
    try:
        # initializing the server connection
        yag = yagmail.SMTP(yagmail_creds.user,
                           yagmail_creds.password)
        # sending the email
        yag.send(to=customer,
                 subject=f"Order {order_number} - confirmation",
                 contents=message)
        print("Email sent successfully")
    except EOFError:
        print("Error, email was not sent")
