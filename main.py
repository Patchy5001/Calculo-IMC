peso = float(input("Introduza o peso (em kg): "))
altura_cm = float(input("Introduza a altura (em cm): "))

altura_m = altura_cm / 100

imc = peso / (altura_m * altura_m)

imc = round(imc, 2)

print(f"\nIMC: {imc}")

if imc < 18.5:
    print("Fora do peso normal")
elif imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")

