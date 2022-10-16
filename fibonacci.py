print("Fibonacci\n\n")

N = int(input("Write N numbers: "))
T1 = 0
T2 = 1
T3 = 0

while T3 <= N:
    print(f"{T3} -> ", end="")
    T3 = T1 + T2
    T1 = T2
    T2 = T3

print("Fim")
