# ============================================================
# ITERABLE VE ITERATOR
# Iterable, üzerinde iter() ile dolaşılabilen nesnedir.
# Iterator ise sıradaki elemana geçmemizi sağlayan nesnedir.
# Burada liste iterable, iter(liste) ile iterator elde edilir.
# ============================================================

sayilar = [1, 2, 3, 4, 5]
# print(dir(sayilar)) 
iterator = iter(sayilar)

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break

