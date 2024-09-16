from estado import Estado, Usuario
from tipos import RESULTADO


def alta_usuario_parametros_validos(args: list[str]):
    return len(args) == 6 and args[5].isdigit() and int(args[5]) > 0


def alta_usuario(dni, clave, dni_usuario, clave_usuario, nombre, sueldo):
    estado = Estado()

    if dni not in estado.usuarios.keys():
        return RESULTADO.UsuarioInexistente

    usuario = estado.usuarios[dni]

    if usuario.clave != clave:
        return RESULTADO.ClaveIncorrecta

    if dni_usuario in estado.usuarios.keys():
        return RESULTADO.UsuarioYaExistente

    if len(estado.usuarios) >= 300:
        return RESULTADO.LimiteUsuariosAlcanzado

    nuevo_usuario = Usuario()
    nuevo_usuario.dni = dni_usuario
    nuevo_usuario.clave = clave_usuario
    nuevo_usuario.nombre = nombre
    nuevo_usuario.saldo = sueldo
    nuevo_usuario.sueldo = sueldo

    estado.usuarios[dni_usuario] = nuevo_usuario

    estado.guardar()

    return RESULTADO.OK
