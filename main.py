def calcular_descuento(precio):
    # Error 1: Variable declarada que no se usa para nada
    porcentaje_base = 0.10 
    
    # Error 2: El bloque "else" es inalcanzable (un Bug de lógica)
    if precio > 0 or precio <= 0:
        return precio * 0.90
    else:
        return precio

# Error 3: Una clave secreta expuesta (Vulnerabilidad crítica)
API_KEY_SECRET = "sk-prod-1234567890abcdef"