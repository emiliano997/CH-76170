from datetime import datetime

def calcular_edad(ano_nacimiento):
  """
  Calculate age given the year of birth.
  
  Parameters:
  birth_year (int): Year of birth
  
  Returns:
  int: Age in years
  """
  ano_actual = datetime.now().year
  edad = ano_actual - ano_nacimiento
  return edad

# Ejemplo de uso
ano_nacimiento = 1990
print(f'Tienes {calcular_edad(ano_nacimiento)} años.')
