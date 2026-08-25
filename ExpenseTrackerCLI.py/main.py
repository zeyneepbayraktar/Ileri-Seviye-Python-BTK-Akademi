# ============================================================
# EXPENSE TRACKER CLI UYGULAMASI
# Bu dosya harcama ekleme, görüntüleme, silme, güncelleme ve aylık özet
# hesaplama işlemlerini kullanıcıdan alınan girdilerle gerçekleştiren bir
# örnek uygulamadır. Basit bir console arayüzü üzerinden çalışır.
# ============================================================

from datetime import date as dt
class Expense:
    def __init__(self, id, description, amount, date):
        self.id= id
        self.description = description
        self.amount = amount
        self.date = date 

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add(self):
        description = input("Write the description: ")
        amount = input("Write amount: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Sayı giriniz!")
            return
        print(description, amount)
        new_id = len(self.expenses) + 1
        print(new_id)
        date = str(dt.today())
        new_expense = Expense(new_id, description, amount, date)
        self.expenses.append(new_expense)
        print(self.expenses)

    def delete(self):
        delete_id = input("Enter the ID to delete: ")
        try:
            delete_id = int(delete_id)
        except ValueError:
            print("Sayı giriniz!")
        print(delete_id)
        self.expenses = [i for i in self.expenses if i.id != delete_id]

    def update(self):
        update_id = input("Enter the ID to update: ")
        try:
            update_id =int(update_id)
        except ValueError:
            print("Sayı giriniz!")
        print(update_id)
        for i in self.expenses:
            if i.id ==update_id:
                yeni_description = input("New description: ")
                yeni_amount = input("New amount: ")
                i.description = yeni_description
                i.amount = int(yeni_amount)
            

    def view(self):
        for i in self.expenses:
            print(f"{i.id} {i.date} {i.description} {i.amount}")

    def summary(self):
        print(sum(int(i.amount) for i in self.expenses))

    def summaryOfTheMonth(self):
        month = input("Which month? (1-12): ")
        print(sum(int(i.amount) for i in self.expenses if int(i.date.split("-")[1]) == int(month)))


tracker = ExpenseTracker()
while True:
    cevap = input("What you want to do(1. Add, 2. View, 3. Delete, 4. Update, 5. Summary, 6.Summary of the Month, 7. Exit): ")
    try:
        cevap = int(cevap)
    except ValueError:
        print("Sayı giriniz!")
        continue
    if cevap == 1:
        tracker.add()
    elif cevap == 2:
        tracker.view()
    elif cevap == 3:
        tracker.delete()
    elif cevap == 4:
        tracker.update()
    elif cevap == 5:
        tracker.summary()
    elif cevap == 6:
        tracker.summaryOfTheMonth()
    elif cevap == 7:
        break  
    else:
        print("Geçersiz seçim")

