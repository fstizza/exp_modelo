from estado import Estado
from operaciones.extraccion.parametros_extraccion import ParametrosExtraccion
from tipos import RESULTADO, OPERACION
from utiles import mismo_dia
from constantes import CANTIDAD_EXTRACCIONES_MAXIMA_DIA, ahora


def extraccion(solicitud: ParametrosExtraccion):
    estado = Estado()

    if solicitud.dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    if solicitud.monto <= 0:
        return RESULTADO.ParametrosInvalidos

    usuario = estado.usuarios[solicitud.dni]

    if usuario.clave != solicitud.clave:
        return RESULTADO.ClaveIncorrecta

    realizo_extracciones = (
        len(
            list(
                filter(
                    lambda m: mismo_dia(m[0])
                    and m[1] == OPERACION.EXTRACCION
                    and m[2] == solicitud.dni,
                    estado.movimientos,
                )
            )
        )
        > CANTIDAD_EXTRACCIONES_MAXIMA_DIA
    )

    if realizo_extracciones:
        return RESULTADO.NoCumplePoliticaAdelanto

    if solicitud.monto > int(usuario.sueldo / 2):
        return RESULTADO.NoCumplePoliticaExtraccionAdelanto

    if solicitud.monto > estado.saldo:
        return RESULTADO.SaldoCajeroInsuficiente

    if solicitud.monto > usuario.saldo:
        return RESULTADO.SaldoInsuficiente

    usuario.saldo -= solicitud.monto

    estado.saldo -= solicitud.monto

    estado.movimientos.append((ahora, OPERACION.EXTRACCION, solicitud.dni))

    estado.guardar()

    return RESULTADO.OK
