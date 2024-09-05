# Secure-Password-Generator
A simple module for generating passwords


# To Install
```python
pip install spassgen
```

# To Use
```python
from spassgen import PasswordGen

password_var = PasswordGen(pass_len=6, enable_symbols=True)

print(password_var.generate())
```

# Things to note
The class PasswordGen currently requires both pass_len (that defaults to 6 characters) and enable_symbols (which defaults to true). I recommend keeping the symbols intact, but some sites don't take symbols for their passwords.

You have to use the generate method to return an actual password. Refer to 'To Use' to check that out

# Things to Come
I plan on making a generate_many function that generates a user specified amount of passwords and stores them in a list.

Password storage?
Make a local storage so that PasswordGen doesn't generate the same password twice, of course there're problems with this, so we'll see.
