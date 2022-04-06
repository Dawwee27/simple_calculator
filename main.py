print("Kalkulacka")

prve = int(input("Zadajte prve cislo"))
druhe = int(input("Zadajte druhe cislo"))
funkcie = ["sucet", "rozdiel", "delenie", "nasobenie"]
def sucet():
    x = prve + druhe
    print("sucet tychto cisiel je: ", x)

def rozdiel():
    x = prve - druhe
    print("rozdiel tychto cisiel je: ", x)

def delenie():
    x = prve / druhe
    print("podiel tychto cisiel je: ", x)

def nasobenie():
    x = prve * druhe
    print("nasobok tychto cisiel je: ", x)
for i in range(1,10):
 print("Vyberte si potrebnu funkciu: ")

 print("sucet")
 print("rozdiel")
 print("delenie")
 print("nasobenie")
 print("zmena cisiel")
 vyber_funkcie = input("Zadajte vyber:")

 if vyber_funkcie == "sucet":
    sucet()
 elif vyber_funkcie == "nasobenie":
    nasobenie()
 elif vyber_funkcie == "delenie":
    delenie()
 elif vyber_funkcie == "rozdiel":
    rozdiel()
 else:
     prve = int(input("Zadajte prve cislo"))
     druhe = int(input("Zadajte druhe cislo"))


