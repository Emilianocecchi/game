import random

# Datos ficticios de las elecciones legislativas 2025 por provincia (porcentajes de votos iniciales)
datos_electorales = {
    "Buenos Aires": {"Mileismo": 40, "Peronismo": 30, "Kirchnerismo": 15, "Macrismo": 10, "Radicalismo": 5},
    "Córdoba": {"Mileismo": 45, "Macrismo": 25, "Radicalismo": 15, "Peronismo": 10, "Kirchnerismo": 5},
    "Santa Fe": {"Mileismo": 38, "Peronismo": 28, "Kirchnerismo": 20, "Radicalismo": 10, "Macrismo": 4},
    "Mendoza": {"Radicalismo": 35, "Mileismo": 30, "Peronismo": 20, "Macrismo": 10, "Kirchnerismo": 5}
}

# Lista de provincias disponibles
provincias = list(datos_electorales.keys())

# Función para simular la campaña electoral
def simular_campaña(provincia, partido_elegido):
    print(f"\nSimulando campaña en {provincia} con el partido {partido_elegido}...")
    
    # Obtener los datos base de la provincia
    votos_base = datos_electorales[provincia]
    
    # Factor aleatorio para simular el impacto de la campaña (-5% a +5%)
    impacto_campaña = random.uniform(-5, 5)
    
    # Calcular nuevos porcentajes
    resultado = {}
    for partido, porcentaje in votos_base.items():
        if partido == partido_elegido:
            nuevo_porcentaje = porcentaje + impacto_campaña
        else:
            nuevo_porcentaje = porcentaje - (impacto_campaña / (len(votos_base) - 1))
        resultado[partido] = max(0, min(100, nuevo_porcentaje))  # Asegurar que esté entre 0 y 100
    
    # Normalizar para que sume 100%
    total = sum(resultado.values())
    for partido in resultado:
        resultado[partido] = (resultado[partido] / total) * 100
    
    return resultado

# Función principal del juego
def juego_electoral():
    print("¡Bienvenido al Juego Electoral Argentina 2025!")
    print("Elige una provincia y un partido para simular tu campaña.\n")
    
    # Mostrar provincias disponibles
    print("Provincias disponibles:")
    for i, prov in enumerate(provincias, 1):
        print(f"{i}. {prov}")
    
    # Selección de provincia
    while True:
        try:
            eleccion_prov = int(input("\nIngresa el número de la provincia: "))
            if 1 <= eleccion_prov <= len(provincias):
                provincia_elegida = provincias[eleccion_prov - 1]
                break
            else:
                print("Número inválido. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Mostrar partidos disponibles en esa provincia
    partidos = list(datos_electorales[provincia_elegida].keys())
    print(f"\nPartidos disponibles en {provincia_elegida}:")
    for i, partido in enumerate(partidos, 1):
        print(f"{i}. {partido}")
    
    # Selección de partido
    while True:
        try:
            eleccion_partido = int(input("\nIngresa el número del partido: "))
            if 1 <= eleccion_partido <= len(partidos):
                partido_elegido = partidos[eleccion_partido - 1]
                break
            else:
                print("Número inválido. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Simular la campaña y mostrar resultados
    resultados = simular_campaña(provincia_elegida, partido_elegido)
    print("\nResultados de la simulación:")
    for partido, porcentaje in resultados.items():
        print(f"{partido}: {porcentaje:.2f}%")
    
    # Determinar ganador
    ganador = max(resultados, key=resultados.get)
    print(f"\n¡El ganador en {provincia_elegida} es {ganador}!")

# Iniciar el juego
if __name__ == "__main__":
    juego_electoral()