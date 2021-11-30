import statistics

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

n = {n1,n2,n3}

media = statistics.mean(n)
mediana = statistics.median(n)
varianza = statistics.variance(n)

print("La media es: ",media)
print("La mediana es: ",mediana)
print("La varianza es: ",varianza)