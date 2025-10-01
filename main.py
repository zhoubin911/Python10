from tamrin.asus import Asus
from tamrin.furniture import Furniture
from tamrin.iphone import Iphone
from tamrin.lenovo import Lenovo
from tamrin.samsung import Samsung


iphone = Iphone("iphone 17", "800", "5", "6.3", "Apple", "IP964")
print(iphone)

samsung = Samsung("Galaxy S25", "800", "5", "6.2", "Samsung", "S-527")
print(samsung)

furniture = Furniture("chair", "2500" , "15","5")
print(furniture)

lenovo = Lenovo("Lenovo Legion", "1500", "19", "i5", "8GB", "LEN-002")
print(lenovo)

asus = Asus("Asus Rog", "2000", "19", "i7", "16GB", "Asus-001")
print(asus)
