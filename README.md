A simple Python programme that lets you generate randomly generated secure passwords.

Setup:

1) Clone the Repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo

Usage:

1) Set Character Preferences: Choose whether to include uppercase letters,
    lowercase letters, and digits in the passwords. By default, all character sets are enabled.

   upper, lower, digits = True, True, True  # Set to True or False as desired

2) Specify Password Length and Quantity:

length: The desired length of each password (default is 16).
amount: The number of passwords to generate (default is 50).

Run the Script: Execute the script by running:

python password_generator.py

Parameters
upper: Boolean, whether to include uppercase letters (A-Z).
lower: Boolean, whether to include lowercase letters (a-z).
digits: Boolean, whether to include digits (0-9).
length: Integer, defines the length of each password.
amount: Integer, defines the number of passwords to generate.

Example Output:

A1b2C3d4E5F6g7H
i8J9K0l1M2N3o4P
Q5r6S7t8U9v0W1x

