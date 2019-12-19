# Secure-Password-Generator
A simple module for generating passwords

To run:

from PasswordGen import PasswordGen

password_var = PasswordGen(pass_len=6, enable_symbols=True)
print(password_var.generate())
