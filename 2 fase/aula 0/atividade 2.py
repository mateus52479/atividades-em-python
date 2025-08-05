C = float(input("digite a temperatura em grauls celcius: "))

temp = int(input("digite a temperatura para a converção: 1-fahrenheit, 2-kelvin, 3-reaumur: "))

match temp:
    case 1: 
        F = C * 1.8 +32
        print(f"temperatura em fahrenheit: {F}")
    case 2:
        K = C + 273.15
        print(f"temperatura em kelvin: {K}")
    case 3:
        RE = C * 0.8
        print(f"temperatura em reaumur: {RE}")