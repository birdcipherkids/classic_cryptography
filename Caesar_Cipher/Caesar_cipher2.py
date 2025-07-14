
# Caesar Cipher


import pyperclip

message = input('Please enter your message: ')
key = int(input('Please enter your key: '))
mode = input('Do you want to encrypt or decrypt a message (e/d): ')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()

for symbol in message:
	if symbol in LETTERS:

		num = LETTERS.find(symbol)

		if mode == 'encrypt' or mode == 'e':

			num = num + key

		elif mode == 'decrypt' or mode == 'd':

			num = num - key

		if num >= len(LETTERS):

			num = num - len(LETTERS)

		elif num < 0:

			num = num + len(LETTERS)

		translated = translated + LETTERS[num]

	else:

		translated = translated + symbol



print('Your encrypted message is: ')
print()
print(translated)

pyperclip.copy(translated)