import random


def choose_even_or_not():
    choice=input("alege daca numarul e par (p) sau impar(i)")
    while choice  not in ["p","i"]:
        print("Scuze, ai introdus o alegere invalida")
        choice=input("alege te rog din nou p sau i")
    return choice
def choose_user_number():
    num=float(input("alege un numar intre  0 si 10"))
    while int(num)!=num or num not in range(0,11):
        print("Scuze, ai introdus un numar gresit")
        num=float(input("alege un numar intre  0 si 10"))
    return int(num)
def wanna_play_choice():
    choice=input("mai vrei sa te joci? Y/N")
    while choice.upper() not in ["Y","N"]:
        choice=input("Scuze, nu am inteles...mai vrei sa te joci? Y/N")
    if choice.upper()=="Y":
        return True
    else:
        return False



user_wins=0
computer_wins=0
consecutive_wins=0
wanna_play=True
while wanna_play:
    choose=choose_even_or_not()
    user_choice=choose_user_number()
    computer_choice=random.randint(0,10)
    sum=user_choice+computer_choice
    if sum%2==0:
        print("suma este para")
        if choose=="p":
            print("felicitari ai castigat")
            user_wins+=1
            consecutive_wins+=1
        else:
            print("uf ai pierdut")
            computer_wins+=1
            consecutive_wins=0


    else:
        print("suma este impara")
        if choose=="i":
            print("felicitari ai castigat")
            user_wins += 1
            consecutive_wins+=1
        else:
            print("uf ai pierdut")
            computer_wins += 1
            consecutive_wins=0
    if consecutive_wins>1:
        print("oh wow ai castigat de "+str(consecutive_wins)+" ori consecutiv")
    wanna_play=wanna_play_choice()
print("Scorul e "+str(user_wins)+" pentru tine si "+str(computer_wins)+" pentru mine ")
