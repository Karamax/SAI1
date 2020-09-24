import random
import string
import re


GENRANGE = string.ascii_uppercase + string.ascii_lowercase + string.digits


def saveStringReversedFile(string):
    with open(input("Enter file name: "), 'w') as file:
        file.write(string[::-1])

genString = "".join(random.choice(GENRANGE) for x in range(20))
numString = ''.join(re.findall('[0-9]', genString))

saveStringReversedFile(numString)
