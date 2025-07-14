
# ------------------------ Caesar Cipher


MAX_KEY_SIZE = 26


def getMode():

	while True:

		mode = input('Do you wish to encrypt or decrypt a message? (e/d): ').lower()

		if mode in 'encrypt e decrypt d'.split():

			return mode

		else:

			print('Please enter "encrypt" or "e" or "decrypt" or "d" ')


def getMessage():

	message = input('Please enter your message: ')
	return message

def getKey():

	key = 0

	while True:

		key = int(input('Enter the key number (1-%s): ' % (MAX_KEY_SIZE)))

		if key >= 1 and key <= MAX_KEY_SIZE:

			return key



def getTranslatedMessage(mode, message, key):

	if mode[0] == 'd':

		key = -key

	translated = ''

	for symbol in message:

		if symbol.isalpha():

			num = ord(symbol)
			num = num + key

			if symbol.isupper():

				if num > ord('Z'):

					num = num - 26

				elif num < ord('A'):

					num = num + 26

			elif symbol.islower():

				if num > ord('z'):

					num = num - 26

				elif num < ord('a'):

					num = num + 26

			translated = translated + chr(num)

		else:

			translated = translated + symbol


	return translated


mode = getMode()
message = getMessage()
key = getKey()


print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))


