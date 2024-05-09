def verificar_ponto_retangulo(x, y, retangulo):
    if  -800<= x <=22 and -20<= y <=35:
        return True
    else:
        return False

def main():
    x = float(input())
    y = float(input())
    retangulo = (-800, -20, 22, 35)
    if verificar_ponto_retangulo(x, y, retangulo):
        print("SIM")
    else:
        print("NAO")
main()