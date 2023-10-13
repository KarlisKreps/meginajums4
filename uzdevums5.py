
# read() nolasa datni

datne=open('info1.txt', encoding='utf-8')
print(datne.read(5))
datne.seek(0)
print(datne.read(5))
pos=datne.tell()
print(f"Kursors atordas {pos} pozicijaa")
datne.seek(0)
print(f"Kursors atrodas {datne.tell()} pozicijaa")
#nolasit divas reizes piekto simbolu

datne=open('info1.txt', 'r', encoding='utf-8')
viss=datne.readlines()
print("viss=", viss)

