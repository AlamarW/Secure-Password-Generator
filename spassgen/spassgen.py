import random
import string
import re

class PasswordGen:
    """
    A class to represent a password Generator

    '''

    Attributes
    ----------

    pass_len : int
        a non-negative integer between 6-25 (default 6)

    enable_symbols : bool
        a T or F value on weather a symbol is included in the passstring (default True)

    seed : int
        a non-negative integer to supplement the randomization (default is 1)


    Methods
    -------
    randomize()
        Randomizes Capital letters, lowercase numbers, symbols and numbers to a length of pass_len
    """

    def __init__(self, pass_len: int=6, enable_symbols: bool=True):
        """
        Parameters
        ----------

        pass_len : int
            a non-negative integer to supplement the randomization (default is 6)

        enable_symbols : bool
            a T or F value on weather a symbol is included in the passstring (default True)
        
        seed : int
            a non-negative integer to supplement the randomization (default is 1)
        """
        
        self.pass_len = pass_len
        self.enable_symbols = enable_symbols

    def generate(self):
        """Generates a random string of Capital, lowercase, symbols, and numbers to length of pass_len.

        If a pass_len or seed isn't passed in the defaults are used.

        Parameters
        ----------
        None

        Raises
        ------
        AttributeError
            if seed is less than 1 or if pass_len is less than 6 or greater than 25

        """

        # Catching all the dumb things and this is the only way I know how to right now

        if type(self.pass_len) is not int:
            raise AttributeError("pass_len must be an integer!")
        if self.pass_len < 6 or self.pass_len > 25 or type(self.pass_len) is not int:
            raise AttributeError("pass_len cannot be less than 6 or greater than 25")

        if type(self.enable_symbols) is not bool:
            raise AttributeError("enable_symbols must be a bool!")

        # Defining 4 seperate methods, each which generate pass_len worth of things
        def random_upper(self):
            """Generates a list of random Upper Case letters to the length of pass_len"""
            upper_list = []
            for n in range(0, self.pass_len):
                random_upper = random.choice(string.ascii_uppercase)
                upper_list.append(random_upper)
            return upper_list

        def random_lower(self):
            """Generates a list of random Lower Case letters to the length of pass_len"""
            lower_list = []
            for n in range(0, self.pass_len):
                    random_lower = random.choice(string.ascii_lowercase)
                    lower_list.append(random_lower)
            return lower_list

        def random_integer(self):
            """Generates a list of random integers to the length of pass_len"""
            int_list = []
            for n in range(0, self.pass_len):
                random_int = random.randint(0,9)
                int_list.append(str(random_int))
            return int_list
            

        def random_symbol(self):
            """Generates a list of random symbols to the length of pass_len"""
            choices = ['!','@','$','%','&','*','?']
            symbol_list = []
            for n in range(0, self.pass_len):
                random_symbol = random.choice(choices)
                symbol_list.append(random_symbol)
            return symbol_list
                
        def generate_password(self):
            """Generates the actual password by combining a list and making random choices"""
            upper_chars = random_upper(self)
            lower_chars = random_lower(self)
            numbers = random_integer(self)
            if self.enable_symbols == True:
                symbols = random_symbol(self)
            else:
                symbols = None

            try:
                combined_list = upper_chars + lower_chars + numbers + symbols

            except:
                combined_list = upper_chars + lower_chars + numbers

            password =''
            for n in range(0, self.pass_len):
                choice = random.choice(combined_list)
                password += choice
            return password

        # Check if gen'd password contains at least 1 upper, 1 lower, 1 number,
        # and 1 symbol if enabled

        if self.enable_symbols == True:
            password = generate_password(self)
            if re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@$%&*?]).{6,}$", password):
                return password
            else:
                return generate_password(self)

        if self.enable_symbols == False:
            password = generate_password(self)
            if re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$", password):
                return password
            else:
                return generate_password(self)
                
