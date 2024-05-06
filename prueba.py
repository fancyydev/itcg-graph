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

arr2 = [["son", 1, "father"]]
arr2.extend([["son2", 2, "father2"], ["son3", 3, "father3"]])
a = "son"
print(arr2)

for i in arr2:
    print(i[0])

if a in arr2:
    print("si funciona pai")
    arr2.remove(a)
    print(arr2)
    
dict = {
    "first":[1,2],
    "second":[2,3]
}
print(len(dict))

open_state = [[1,2],[2,3],[3,4]]
open_state[0] = [1,3]
print("Accesando a: " + str(open_state[0][1]))

def funcion():
    return ["prueba", "pa"]
a = funcion()
print(a)