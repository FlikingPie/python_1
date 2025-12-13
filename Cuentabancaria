print('---------------------------------------'.center(50))
print("Bienvenido a Interbank!!".center(50))
print("---------------------------------------".center(50))

resp = "si"
dinero = 0


def ingresar_dinero():
    global dinero
    dinero = float(input("Ingrese la cantidad de dinero S/ = "))
    print(f'Su dinero en el banco es S/ {dinero}')


def menu():
    global dinero, resp

    print("\nIngrese una opción al sistema")
    print("1.- Depositar dinero")
    print("2.- Retirar dinero")
    print("3.- Salir")

    opcion = int(input("Ingrese una opción = "))

    match opcion:
        case 1:
            deposito = float(input("Ingrese cuanto dinero desee depositar S/ = "))
            dinero = dinero + deposito
            print(f'Su dinero actual es : S/ {dinero}')

        case 2:
            retiro = float(input("Ingrese cuanto dinero desee retirar S/ = "))
            if retiro > dinero:
                print("No puede retirar una cantidad mayor al dinero ingresado!!")
            else:
                dinero = dinero - retiro
                print(f'Su dinero actual es : S/ {dinero}')

        case 3:
            print("Saliendo del sistema...")
            exit()

    resp = input("¿Desea continuar? (si/no) = ").lower()


ingresar_dinero()

while resp == "si":
    menu()

print("Saliendo...")

