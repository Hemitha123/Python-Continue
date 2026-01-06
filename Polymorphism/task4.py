#festival Polymorphism

class festival():
    def cel(self):
        print("Festivals")
class Diwali(festival):
    def cel(self):
        print("Happy Diwali")
class Christmas(festival):
    def cel(self):
        print("Merry Christmas")
class Eid(festival):
    def cel(self):
        print("Eid Mubharak")

diwali=Diwali()
christmas=Christmas()
eid=Eid()
Festival=festival()
Festival.cel()
for x in (diwali,christmas,eid):
    x.cel()