# Calculadora de Huella de Carbono
# Propósito: El script calcula la huella de carbono semanal de una persona basándose en los kilómetros recorridos en coche, autobús y bicicleta.

# Cómo ejecutarlo:

# Cuando se ejecuta el script, el usuario debe ingresar los kilómetros que recorre semanalmente en cada tipo de transporte.
# El script usa tasas de emisión predeterminadas para calcular la huella de carbono en kilogramos de CO2.
# Finalmente, muestra el resultado al usuario en la consola.

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
