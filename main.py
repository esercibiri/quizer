import random

from sözlük import words
soru=[]
cevap=[]
x=0
rand_kel=""
rand_cev= ""
class User:
    def __init__(self,id,name):
        self.kod=id
        self.ad=name

for i in range(len(words)):
    a = words[i]["word"]
    b = words[i]["mean"]
    m = User(b,a)
    soru.append(m.ad)
    cevap.append(m.kod)

len_soru = len(soru)

while x < len_soru:
    x += 1
    rand_num=random.randint(0, len(soru)-1)
    answer=input(f"{soru[rand_num]} \n")
    if answer == cevap[rand_num]:
        print("doğru bildin geç")
        rand_kel=soru[rand_num]
        rand_cev=cevap[rand_num]
        soru.remove(rand_kel)
        cevap.remove(rand_cev)

    else:
        print("az çalışda gel")
        print(f"Doğru cevap:{cevap[rand_num]}")
        x -= 1