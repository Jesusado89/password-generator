import random


def generator_password(longitud):
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!¡¿?'*+,.-#$%&/()=_^{}[]|"
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    return password


longitud = int(input("Enter the password length: "))
password = generator_password(longitud)
print("The end password is:", password)
