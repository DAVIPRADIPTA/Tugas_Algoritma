import random
def suit () :
    user = str(input("masukan pilihanmu (gajah,orang,atau semut) :"))
    pilihan = ["gajah", "orang", "semut"]
    komputer = random.choice(pilihan)
    print(f"kamu memilih : {user}")
    print(f"komputer memilih : {komputer}")
    if user == komputer :
        print("seri")
    elif user == "gajah" and komputer == "semut" or \
         user == "semut" and komputer == "orang" or \
         user == "orang" and komputer == "gajah":
        print("Kamu kalah")
    else :
        print("kamu menang")
    lagi = input("ingin bermain lagi? (y/n) :")
    suit() if lagi == "y" else print ("permainan selesai")
suit()

