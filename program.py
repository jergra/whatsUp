
def do(a):
    first = 0
    second = 0

    for b in range(len(a)):
        for c in range(len(a)):
            print(a[b], a[c])
            if a[b] + a[c] == 9:
                first = a[b]
                second = a[c]
                return first, second
            
myArray = [1, 3, 5, 6, 11, 12, 13]

print("result:", do(myArray))






        
    