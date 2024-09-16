from datetime import datetime
from os import sys
from constantes import FORMATO_FECHA
from extraccion import extraccion, extraccion_parametros_validos
from alta_usuario import alta_usuario, alta_usuario_parametros_validos
from cambio_clave import cambio_clave, cambio_clave_parametros_validos
from carga import carga, carga_parametros_validos
from consulta_saldo import consulta_saldo, consulta_saldo_parametros_validos
from consulta_movimientos import (
    consulta_movimientos,
    consulta_movimientos_parametros_validos,
)
from tipos import RESULTADO


def main(args: list):
    if len(args) == 0:
        print("Sin argumentos.")
        exit(1)

    resultado = RESULTADO.Error
    if args[0] == "extraccion":
        if extraccion_parametros_validos(args[1:]):
            resultado = extraccion(args[1], args[2], int(args[3]))
        else:
            print("Parametros inválidos")
    elif args[0] == "clave":
        if cambio_clave_parametros_validos(args[1:]):
            resultado = cambio_clave(args[1], args[2], args[3])
        else:
            print("Parametros inválidos")
    elif args[0] == "saldo":
        if consulta_saldo_parametros_validos(args[1:]):
            resultado = consulta_saldo(args[1], args[2])
        else:
            print("Parametros inválidos")

    elif args[0] == "alta":
        if alta_usuario_parametros_validos(args[1:]):
            resultado = alta_usuario(
                args[1], args[2], args[3], args[4], args[5], int(args[6])
            )
        else:
            print("Parametros inválidos")

    elif args[0] == "carga":
        if carga_parametros_validos(args[1:]):
            resultado = carga(args[1], args[2], int(args[3]))
        else:
            print("Parametros inválidos")
        pass
    elif args[0] == "movimientos":
        if consulta_movimientos_parametros_validos(args[1:]):
            resultado = consulta_movimientos(
                args[1],
                args[2],
                args[3],
                datetime.strptime(args[4], FORMATO_FECHA),
                datetime.strptime(args[5], FORMATO_FECHA),
            )
        else:
            print("Parametros inválidos")
    else:
        print("Operación inválida.")

    print(f"Resultado: {resultado.value}")


if __name__ == "__main__":
    main(sys.argv[1:])
