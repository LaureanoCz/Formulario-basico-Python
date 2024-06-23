import formulario
import clubes

print("     ---Bienvenido---")
print("Los clubes disponibles son:\n- Deporte\n- Ciencia\n- Lectura")

while True:
    opcion = input("Elige tu club favorito: ").lower()
    if "deporte" in opcion:
        print("-=-= Deporte =-=-")
        print(clubes.deporte)
        formulario.formu()
        break
    elif "lectura" in opcion:
        print("-=-= Lectura =-=-")
        print(clubes.lectura)
        formulario.formu()
        break
    elif "ciencia" in opcion:
        print("-=-= Ciencia =-=-")
        print(clubes.ciencia)
        formulario.formu()
        break
    else:
        print("Escoge una opción válida.")