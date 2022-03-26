def garis():
    print("===================================")

def ascending(mylist):
    mylist = sorted(mylist)
    return(mylist)

def descending(mylist):
    mylist = sorted(mylist, reverse = True)
    return(mylist)


print("Masukkan tiga buah nilai")

nilaiA = int(input("Masukkan nilai A : "))
nilaiB = int(input("Masukkan nilai B : "))
nilaiC = int(input("Masukkan nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]
garis()

def rata_rata(angka):
    return sum(angka)/len(angka)

print("Urutan hasil ascending : """
      ,(ascending(angka)))

print("""Urutan hasil descending : """
      ,(descending(angka)))

print("Angka Terbesar : ",max(angka))

print("Angka Terkecil : ",min(angka))

print("Rata-rata nilai : ",rata_rata(angka))
