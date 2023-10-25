import datetime

seychas = datetime.datetime.now()

print(f'\n\n сейчас время {seychas}\n' )

delta =  datetime.timedelta(seconds=5)
delta2 =  datetime.timedelta(minutes=12) 
delta3 =  datetime.timedelta(hours=12) 
print(f"delta in second = {delta}\n")
print(f"delta2 in minute = {delta2}\n")
print(f"delta3 in hour = {delta3}\n")
howhours =datetime.timedelta(hours=3)
kak_dolgo = int(input("на сколько часов замутировать?"))
cherez_Tree_chasa = datetime.datetime.now()+datetime.timedelta(hours=kak_dolgo)
print(f"USER замутирован до: {cherez_Tree_chasa}")