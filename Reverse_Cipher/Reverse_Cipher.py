
# Reverse Cipher


message = 'Three can keep a secret if two of them are dead'
translated = ''

i = len(message) - 1

while i >= 0:

	translated = translated + message[i]
	i = i - 1


print('Your encrypted message is: ')
print()
print(translated)