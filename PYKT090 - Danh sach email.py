file = open("CONTACT.in", "r")
ls = []

for s in file:
    mail = s.strip().lower()
    if mail not in ls:
        ls.append(mail)

ls.sort() 

for data in ls:
    print(data)
