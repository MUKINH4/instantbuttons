from timeit import repeat
from playsound import playsound

print("-_" * 10)
print("Instant Buttons")
print("-_" * 10)

url = "https://www.myinstants.com/media/sounds/"

sons = [url + 'tmpd9mca4be.mp3', url + 'tmpoqn0rct4.mp3',
    url + 'y2mate_rLgMJTu.mp3', url + 'tomi.mp3', url + 'uepa-mp3cut.mp3', url + 'vinheta-xaropinho-rapaz_dx3f4Be.mp3'
    ]

print("[0] - Ele gosta \n[1] - UUUI\n[2] - Dança gatinho, dança\n[3] - Tomi\n[4] - UEPA\n[5] - RAPAZ Xaropinho\n")
escolha = int(input("Escolha qual som tocar! "))

def tocar():
    if escolha == 0:
        playsound(sons[escolha])
    elif escolha == 1:
        playsound(sons[escolha])
    elif escolha == 2:
        playsound(sons[escolha])
    elif escolha == 3:
        playsound(sons[escolha])
    elif escolha == 4:
        playsound(sons[escolha])
    elif escolha == 5:
        playsound(sons[escolha])

tocar()