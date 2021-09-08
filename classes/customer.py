"""Create Customer class."""


class Customer:
    """
    A class to represent customer.

    Attributes:
    ~~~~~~~~~~
    name: str (user's name)
    e-mail: str (user's email address)
    """

    def __init__(self, name, email):
        """Constructs the customer object."""

        self.name = name
        self.email = email
