from tipos import *
from estado import Estado


def consulta_saldo_parametros_validos(args: list[str]):
    return isinstance(args[0], str) and isinstance(args[1], str)


def consulta_saldo(dni, clave):
    estado = Estado()

    if dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    if estado.usuarios[dni].clave != clave:
        return RESULTADO.ClaveIncorrecta

    saldo = estado.usuarios[dni].saldo

    print(f"El saldo del usuario DNI {dni} es: {saldo}")

    return RESULTADO.OK
