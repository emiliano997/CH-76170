def celsius_to_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    
    Parámetros:
        celsius (float): La temperatura en grados Celsius.
    
    Retorna:
        float: La temperatura en grados Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Ejemplo de uso
temperatura_celsius = 25
temperatura_fahrenheit = celsius_to_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C son {temperatura_fahrenheit}°F")
