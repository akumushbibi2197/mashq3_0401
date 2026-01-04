#1-misol
raqam = input("Karta raqamini kiriting: ")
raqamlar = [int(x) for x in raqam]

yigindi = 0
teskari = raqamlar[::-1]

for i in range(len(teskari)):
    if i % 2 == 1:
        x = teskari[i] * 2
        if x > 9:
            x -= 9
        yigindi += x
    else:
        yigindi += teskari[i]

if yigindi % 10 == 0:
    print("Karta raqami to‘g‘ri")
else:
    print("Karta raqami noto‘g‘ri")

#2-misol
n = int(input("Balandlik: "))
m = int(input("Kenglik: "))

for i in range(n):
    print("*" * m)

#3-misol
sonlar = {
    "nol":0, "bir":1, "ikki":2, "uch":3, "to‘rt":4,
    "besh":5, "olti":6, "yetti":7, "sakkiz":8, "to‘qqiz":9
}
amallar = {
    "qo‘shish":"+",
    "ayirish":"-",
    "ko‘paytirish":"*",
    "bo‘lish":"/"
}

matn = input("Ifodani kiriting: ").split()
ifoda = ""

for soz in matn:
    if soz in sonlar:
        ifoda += str(sonlar[soz])
    elif soz in amallar:
        ifoda += amallar[soz]

print("Natija:", eval(ifoda))

#4-misol
import json

fayl = "talabalar.json"

def yuklash():
    try:
        with open(fayl, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def saqlash(data):
    with open(fayl, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def qoshish(ism, yosh):
    data = yuklash()
    data.append({"ism": ism, "yosh": yosh})
    saqlash(data)

def qidirish(ism):
    for t in yuklash():
        if t["ism"] == ism:
            print(t)

def ochirish(ism):
    data = [t for t in yuklash() if t["ism"] != ism]
    saqlash(data)

#5-misol
from datetime import datetime

s1 = input("1-sana (YYYY-MM-DD HH:MM): ")
s2 = input("2-sana (YYYY-MM-DD HH:MM): ")

t1 = datetime.strptime(s1, "%Y-%m-%d %H:%M")
t2 = datetime.strptime(s2, "%Y-%m-%d %H:%M")

farq = abs(t2 - t1)

kun = farq.days
soat = farq.seconds // 3600
daq = (farq.seconds % 3600) // 60

print("Farq:", kun, "kun", soat, "soat", daq, "daq")
