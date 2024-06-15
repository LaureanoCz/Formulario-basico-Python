import formulario
import clubes

print("     ---Bienvenido---")
print("Los clubes disponibles son:\n- Deporte\n- Ciencia\n- Lectura")

while True:
    opciona = input("Elige tu club favorito: ").lower()
    if "deporte" in opciona:
        print("-=-=Deporte=-=-")
        print(clubes.deporte)
        formulario.formu()
        break
    elif "lectura" in opciona:
        print("-=-=Lectura=-=-")
        print(clubes.lectura)
        formulario.formu()
        break
    elif "ciencia" in opciona:
        print("-=-=Ciencia=-=-")
        print(clubes.ciencia)
        formulario.formu()
        break
    else:
        print("Escoge una opción válida.")