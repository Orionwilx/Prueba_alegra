# Calculadora de Huella de Carbono
# 
# Este script calcula la huella de carbono de una persona en base al número de kilómetros recorridos
# semanalmente en coche, autobús y bicicleta. Usa las siguientes tasas de emisión:
# - Coche: 0.21 kg de CO2 por kilómetro
# - Autobús: 0.1 kg de CO2 por kilómetro
# - Bicicleta: 0 kg de CO2 por kilómetro
#
# Para ejecutar este script, simplemente sigue las instrucciones y proporciona el número de kilómetros
# que recorres en coche, autobús y bicicleta cada semana.
#
# Al final, el script mostrará la huella total de carbono en kilogramos de CO2.

def calcular_huella_carbono():
    # Tasa de emisión de CO2 en kg por kilómetro
    tasa_coche = 0.21  # kg CO2/km
    tasa_autobus = 0.1  # kg CO2/km
    tasa_bicicleta = 0.0  # kg CO2/km

    # Solicitar los kilómetros recorridos al usuario
    km_coche = float(input("Introduce el número de kilómetros que recorres semanalmente en coche: "))
    km_autobus = float(input("Introduce el número de kilómetros que recorres semanalmente en autobús: "))
    km_bicicleta = float(input("Introduce el número de kilómetros que recorres semanalmente en bicicleta: "))

    # Calcular la huella de carbono para cada medio de transporte
    huella_coche = km_coche * tasa_coche
    huella_autobus = km_autobus * tasa_autobus
    huella_bicicleta = km_bicicleta * tasa_bicicleta

    # Calcular la huella total de carbono
    huella_total = huella_coche + huella_autobus + huella_bicicleta

    # Mostrar el resultado al usuario
    print(f"\nTu huella total de carbono semanal es: {huella_total:.2f} kg de CO2")

# Ejecutar la función para calcular la huella de carbono
if __name__ == "__main__":
    calcular_huella_carbono()
