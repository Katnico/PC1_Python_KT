def determinarcomida(hora):

    horas, minutos = map(int, hora.split(':'))

    if 7 <= horas < 8 or (horas == 8 and minutos == 0):
        return "Es hora de desayunar."
    elif 12 <= horas < 13 or (horas == 13 and minutos == 0):
        return "Es hora de almorzar."
    elif 18 <= horas < 19 or (horas == 19 and minutos == 0):
        return "Es hora de cenar."

horausuario = input("Ingrese la hora en formato HH:MM: ")

try:
    resultado = determinarcomida(horausuario)
    if resultado:
        print(resultado)
except ValueError:
    print("Error: Ingrese una hora válida en formato HH:MM.")