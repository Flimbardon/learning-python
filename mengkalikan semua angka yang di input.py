def multiply (a) :
    total = 1
    for x in a :
        total *= x
    return total
n = int(input("Ketikkan berapa angka yang anda inginkan dalam list :"))

a = list(map(int,input("\nKetikkan angka : ").strip().split()))[:n]

print(multiply(a))