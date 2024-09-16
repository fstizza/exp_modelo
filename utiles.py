from tipos import *
from constantes import ahora, clave_administrador, dni_administrador


def mismo_mes(fecha: FECHAHORA):
    return ahora.month == fecha.month and ahora.year == fecha.year


def mismo_dia(fecha: FECHAHORA):
    return (
        ahora.day == fecha.day
        and ahora.month == fecha.month
        and ahora.year == fecha.year
    )


def es_administrador(dni: DNI, clave: CLAVE) -> bool:
    return dni == dni_administrador and clave == clave_administrador


def contiene_letras_numeros(clave: CLAVE) -> bool:
    contiene_letra = any(c.isalpha() for c in clave)
    contiene_numero = any(c.isdigit() for c in clave)

    return contiene_letra and contiene_numero
