dict = {}
print(dict)
dict["Prueba"] = []
print(dict)
dict["Prueba"].append([1,2])
dict["Prueba"].append([3,4])
print(dict["Prueba"][0][1])
print(dict["Prueba"][1])
arreglo = [2,3,4,5]
del arreglo[0]
print(arreglo)

#metodo de la burbuja
arr = [4,3,5,55,9,1]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            aux = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = aux

print(arr)

arr2 = [["son", 2, "father"]]
arr2.extend([["son", 2, "father"]])
a = "son"
print(arr2)

if a in arr2:
    print("si funciona pai")
    arr2.remove(a)
    print(arr2)