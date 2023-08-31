ladoA = float(input("lado A: "))
ladoB = float(input("lado B: "))
ladoC = float(input("lado C: "))

if ladoA == ladoB and ladoB == ladoC and ladoA == ladoC:
    print("O triângulo é equilátero")
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print("O triângulo é isócele")
else:
    print("O triângulo é escaleno")
