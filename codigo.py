
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
        email = input("Email: ")
        if '@' not in email:
            print("El email debe contener el símbolo '@'.")
        else:
            break
    

    print("Gracias por completar el formulario.")
    print("Tu solicitud será revisada pronto.")

deporte = "Horarios: 16:00 hs - 18:00 hs\nLugar: Sum deportivo\nDescripcion: Se hará hará  vistazo a distintas disciplinas físicas  en deportes variados"
lectura = "Horarios: 17:00 hs - 19:00 hs\nLugar: Biblioteca\nDescripcion: Exploraremos varias obras literarias de géneros variados (fantasia, ciencia ficcion, realismo, etc.)"
ciencia = "Horarios: 11:00 hs - 12:30 hs\nLugar: Laboratorio\nDescripcion: Experimentaremos y haremos fenómenos químicos."

print("---Bienvenido al formulario para inscribirte a los clubs---")
print(f"Los clubes disponibles son:\n- deporte\n- lectura\n- ciencia")
opciona = input("Elige tu club favorito: ").lower()
if opciona == "deporte":
    print("-=-=Deporte=-=-")
    print(deporte)
    formu()
elif opciona == "lectura":
    print("-=-=Lectura=-=-")
    print(lectura)
    formu()
elif opciona == "ciencia":
    print("-=-=Ciencia=-=-")
    print(ciencia)
    formu()