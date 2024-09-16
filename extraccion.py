from estado import Estado
from tipos import *
from utiles import mismo_dia
from constantes import ahora


def extraccion_parametros_validos(args: list[str]):
    return len(args) == 3 and args[2].isdigit() and int(args[2]) > 0


def extraccion(dni: DNI, clave: CLAVE, monto: MONTO):
    estado = Estado()

    if dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    if monto <= 0:
        return RESULTADO.ParametrosInvalidos

    usuario = estado.usuarios[dni]

    if usuario.clave != clave:
        return RESULTADO.ClaveIncorrecta

    realizo_extracciones = (
        len(
            list(
                filter(
                    lambda m: mismo_dia(m[0])
                    and m[1] == OPERACION.EXTRACCION
                    and m[2] == dni,
                    estado.movimientos,
                )
            )
        )
        > 2
    )

    if realizo_extracciones:
        return RESULTADO.NoCumplePoliticaAdelanto

    if monto > int(usuario.sueldo / 2):
        return RESULTADO.NoCumplePoliticaExtraccionAdelanto

    if monto > estado.saldo:
        return RESULTADO.SaldoCajeroInsuficiente

    if monto > usuario.saldo:
        return RESULTADO.SaldoInsuficiente

    usuario.saldo -= monto

    estado.saldo -= monto

    estado.movimientos.append((ahora, OPERACION.EXTRACCION, dni))

    estado.guardar()

    return RESULTADO.OK
