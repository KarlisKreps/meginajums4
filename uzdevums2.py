
def nolasitDatni():
    datne=open('info.txt', encoding='utf-8')
    dati=datne.readline()
    rinda=dati.split(" ")
    print(rinda)

nolasitDatni()