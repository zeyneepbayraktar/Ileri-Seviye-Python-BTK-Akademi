# ============================================================
# KALITIM (INHERITANCE)
# Bir class'in baska bir class'in ozelliklerini ve methodlarini
# devralmasidir. Kod tekrarini onler.
# Kalip: class AltClass(UstClass):
#   - Person  -> ust class (parent / base / super class)
#   - Student -> alt class (child / derived class)
# ============================================================

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person olusturuldu")
    def intro(self):
        print(self.name, self.surname, self.age)

# pass => "govdesi bos" demek. Student icinde hicbir sey yazmasak da
# Person'daki __init__ ve intro() oldugu gibi devralinir.
class Student(Person):
    pass

class Teacher(Person):
    pass

# --- Ust class'tan nesne ---
p1 = Person("Ayse", "Turan", 30)
p1.intro()

# --- Alt class'lar kendi __init__'i olmadigi icin Person'unkini kullanir ---
s1 = Student("Fatma", "Bayrak", 19)
s1.intro()

t1 = Teacher("Nur", "Ali", 50)
t1.intro()
