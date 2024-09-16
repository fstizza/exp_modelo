from tipos import *
from estado import Estado
from constantes import ahora
from utiles import mismo_mes


def cambio_clave_parametros_validos(args: list[str]):
    return len(args) == 3


def cambio_clave(dni: DNI, clave: CLAVE, nueva_clave: CLAVE):

    estado = Estado()

    if dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    if estado.usuarios[dni].clave != clave:
        return RESULTADO.ClaveIncorrecta

    if len(nueva_clave) < 8:
        return RESULTADO.NoCumpleRequisitosClave1

    contiene_letra_numero = (
        len(list(filter(lambda d: d.isdigit(), nueva_clave))) > 0
        and len(list(filter(lambda d: d.isalpha(), nueva_clave))) > 0
    )

    if not contiene_letra_numero:
        return RESULTADO.NoCumpleRequisitosClave2

    realizo_cambios_de_clave = (
        len(
            list(
                filter(
                    lambda m: mismo_mes(m[0])
                    and m[1] == OPERACION.CLAVE
                    and m[2] == dni,
                    estado.movimientos,
                )
            )
        )
        > 0
    )

    if realizo_cambios_de_clave:
        return RESULTADO.CambioDeClaveBloqueado

    estado.usuarios[dni].clave = nueva_clave

    estado.movimientos.append((ahora, OPERACION.CLAVE, dni))

    estado.guardar()

    return RESULTADO.OK
