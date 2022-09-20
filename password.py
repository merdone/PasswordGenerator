import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = " "
passwords = []


def limits(x):
    if x > 100:
        print("Слишком большое число")
        x = 100
    if x < 8:
        print("Пароль не может быть таким маленьким, ставлю минимальное значение 8")
        x = 8


pcount = int(input("Сколько паролей генерировать: "))
plen = int(input("Сколько символов в пароле: "))
limits(plen)
isnumbers = str(input("Использовать цифры: "))
if isnumbers == "Да" or isnumbers == "Yes" or isnumbers == "Y":
    chars += digits
else:
    print("Напишите верный ответ")
isUPletters = str(input("Использовать большие буквы: "))
if isUPletters == "Да" or isUPletters == "Yes" or isUPletters == "Y":
    chars += uppercase_letters
else:
    print("Напишите верный ответ")
isLOWletters = str(input("Использовать маленькие буквы: "))
if isLOWletters == "Да" or isLOWletters == "Yes" or isLOWletters == "Y":
    chars += lowercase_letters
else:
    print("Напишите верный ответ")
isStupid = str(input("Использовать специальные символы: "))
if isStupid == "Да" or isStupid == "Yes" or isStupid == "Y":
    chars += punctuation
else:
    print("Напишите верный ответ")
delSumbols = str(input("Удалить символы [il1Lo0O]: "))


def generate_password(length, chars):
    password = ""
    if delSumbols == "Да" or delSumbols == "Yes" or delSumbols == "Y":
        chars.replace("i", "")
        chars.replace("l", "")
        chars.replace("1", "")
        chars.replace("L", "")
        chars.replace("o", "")
        chars.replace("0", "")
        chars.replace("O", "")
    else:
        pass
    for i in range(1, length + 1):
        password += str(random.choice(chars))
        passwords.append(password)
    print(f"Your password is: {password}")


def limits(plen):
    if plen > 100:
        print("Слишком большое число")
        plen = 100
    if plen < 8:
        print("Пароль не может быть таким маленьким")
        plen = 8


for _ in range(1, pcount + 1):
    generate_password(plen, chars)