from tipos import *
from estado import Estado
from utiles import es_administrador


def carga_parametros_validos(args: list[str]):
    return len(args) == 3 and args[2].isdigit() and int(args[2]) > 0


def carga(dni: DNI, clave: CLAVE, saldo: MONTO):
    if not es_administrador(dni, clave):
        return RESULTADO.UsuarioNoHabilitado

    estado = Estado()

    estado.saldo += saldo

    estado.guardar()

    return RESULTADO.OK
