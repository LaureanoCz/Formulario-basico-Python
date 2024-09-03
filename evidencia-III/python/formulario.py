#Archivo que contiene el codigo del formulario que se completa al momento de elegir el club seleccionado

def formu():
    nombre = input("Escribe tu nombre y apellido: ")
    
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("La edad debe ser un número entero positivo.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número entero válido para la edad.")

    while True:
        fecha = input("Fecha de nacimiento (día/mes/año): ")
        try:
            dia, mes, anio = map(int, fecha.split('/'))
            
            import datetime
            datetime.datetime(anio, mes, dia)
            break
        except ValueError:
            print("La fecha debe tener el formato día/mes/año. Por ejemplo: 01/01/2000.")

    while True:
        email = input("Correo electrónico: ")
        if '@' not in email:
            print("El correo electrónico debe contener el símbolo '@'.")
        else:
            break
    
    print("Gracias por completar el formulario.")
    print("Tu solicitud será revisada pronto.")