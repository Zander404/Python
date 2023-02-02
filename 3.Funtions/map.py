# Map function aplicate a same function for a list of objects

store = [("shrirt", 20.00),
         ("pants", 25.00),
         ("jackets",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = list(map(to_euros,store))

for i in store_euros:
    print(i)