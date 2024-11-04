## Job 1
for nombre in range(21):
    print(nombre)



## job 2

nombre <= 20

for nombre in range(0, 21, 2):
    print(nombre)


## job 3

for nombre in range(1, 21):
    print(f"{nombre}^2 = {nombre**2}")


## job 4


N = int(input("Veuillez entrer un entier supérieur à zéro : "))


if N > 0:
    
    for i in range(1, N + 1):
        print(f"Table de multiplication de {i} :")
        
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  
else:
    print("Veuillez entrer un entier supérieur à zéro.")


## job 5

while N < 13:
    print(N)


## job 6

N= int(input("Entrez un numero:"))
while N <=10:
    print(N)


