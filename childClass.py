# ============================================================
# CHILD CLASS: super() ve METHOD OVERRIDE
# Alt class sadece devralmakla kalmaz, uzerine ekleme de yapar:
#   super().__init__(...) -> ust class'in constructor'ini calistirir,
#                            ortak attribute'lari tekrar yazmayiz
#   override              -> ust class'taki bir methodu alt class'ta
#                            ayni isimle yeniden yazmak
#   yeni method           -> sadece alt class'a ait davranis (study)
# ============================================================

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person olusturuldu")
    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        # Once ortak alanlari Person'a kurduruyoruz...
        super().__init__(name, surname, age)
        # ...sonra sadece Student'a ozel alani ekliyoruz.
        self.number = number
        print("Student olusturuldu")
    # Sadece Student'ta olan yeni method
    def study(self):
        print(f"{self.name} ders calisiyor")
    # OVERRIDE: Person.intro() yerine bu calisir (numara da yazilir)
    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher olusturuldu")
    # OVERRIDE: brans bilgisini de yazdirir
    def intro(self):
        print(self.name, self.surname, self.age, self.branch)

# --- Ust class ---
p1 = Person("Ayse", "Turan", 30)
p1.intro()

# --- Student: once "Person olusturuldu", sonra "Student olusturuldu" yazar.
#     Cunku super().__init__ ilk satirda cagriliyor. ---
s1 = Student("Fatma", "Bayrak", 19, 100)
s1.intro()   # override edilmis hali: numara da var
s1.study()   # sadece Student'ta olan method
print(s1.number)

# --- Teacher ---
t1 = Teacher("Nur", "Ali", 50, "math")
t1.intro()
print(t1.branch)
