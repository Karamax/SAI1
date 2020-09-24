import random, string, re

def saveStringReversedFile(string):
    with open(input("Enter file name: "), 'w') as file:
        file.write(string[::-1]) 
    
saveStringReversedFile("".join(re.findall('[0-9]', "".join(random.choice(string.ascii_uppercase + \
                                                                         string.ascii_lowercase + string.digits) for x in range(20)))))
