from tipos import *
from constantes import FORMATO_FECHA
from utiles import es_administrador
from estado import Estado


def consulta_movimientos_parametros_validos(args: list[str]):
    if len(args) != 5:
        return False

    try:
        f1 = datetime.strptime(args[3], FORMATO_FECHA)
        f2 = datetime.strptime(args[4], FORMATO_FECHA)
        return True
    except:
        return False


def consulta_movimientos(
    dni: DNI, clave: CLAVE, dni_consulta: DNI, desde: FECHAHORA, hasta: FECHAHORA
):
    if not es_administrador(dni, clave):
        return RESULTADO.UsuarioNoHabilitado

    estado = Estado()

    if dni_consulta not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    movimientos = filter(
        lambda m: m[0] >= desde and m[0] <= hasta and m[2] == dni_consulta,
        estado.movimientos,
    )

    print(f"Movimientos del usuario DNI {dni_consulta}")
    for movimiento in movimientos:
        fecha = movimiento[0].strftime("%Y-%m-%d-%H:%M")
        operacion = movimiento[1]
        print(f"* {fecha} | {operacion}")

    return RESULTADO.OK
