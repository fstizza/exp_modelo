from operaciones.clave.parametros_cambio_clave import ParametrosCambioClave
from tipos import RESULTADO, OPERACION
from estado import Estado
from constantes import CANTIDAD_CAMBIOS_CLAVE_MES, ahora
from utiles import contiene_letras_numeros, mismo_mes


def cambio_clave(solicitud: ParametrosCambioClave):

    estado = Estado()

    if solicitud.dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    if estado.usuarios[solicitud.dni].clave != solicitud.clave:
        return RESULTADO.ClaveIncorrecta

    if len(solicitud.nueva_clave) < 8:
        return RESULTADO.NoCumpleRequisitosClave1

    if not contiene_letras_numeros(solicitud.nueva_clave):
        return RESULTADO.NoCumpleRequisitosClave2

    realizo_cambios_de_clave = (
        len(
            list(
                filter(
                    lambda m: mismo_mes(m[0])
                    and m[1] == OPERACION.CLAVE
                    and m[2] == solicitud.dni,
                    estado.movimientos,
                )
            )
        )
        > CANTIDAD_CAMBIOS_CLAVE_MES
    )

    if realizo_cambios_de_clave:
        return RESULTADO.CambioDeClaveBloqueado

    estado.usuarios[solicitud.dni].clave = solicitud.nueva_clave

    estado.movimientos.append((ahora, OPERACION.CLAVE, solicitud.dni))

    estado.guardar()

    return RESULTADO.OK
