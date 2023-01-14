import random
while True:
    kucukabc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    buyukABC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    rakam=["1","2","3","4","5","6","7","8","9"]
    hepsi=rakam+kucukabc+buyukABC
    password = "".join(random.choice(hepsi) for x in range(random.randint(7, 14)))
    print(password)
    tekrar=int(input("tekrar şifre oluşturmak istiyor musunuz 1.evet 2.hayır"))
    if tekrar==1:
        continue
    elif tekrar==2:
        break