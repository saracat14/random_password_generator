import random
import time

caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
print("Hola usuario")
while True:
    longitud = int(input("Dicte la longitud de la contraseña:"))
    for i in range(longitud):
        password += random.choice(caract)
    print (password)
    choice = input("¿Quieres crear otra contraseña?(si/no)")
    if choice == "no":
        break
    time.sleep(2)
