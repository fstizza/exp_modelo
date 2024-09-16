from tipos import *
from constantes import *
from json import dump, load


class Usuario:
    saldo: MONTO
    sueldo: MONTO
    clave: CLAVE
    nombre: NOMBRE
    dni: DNI

    def __init__(self, json=None):
        if json != None:
            self.saldo = int(json["saldo"])
            self.sueldo = int(json["sueldo"])
            self.clave = json["clave"]
            self.nombre = json["nombre"]
            self.dni = json["dni"]

    def aJson(self):
        return {
            "saldo": self.saldo,
            "sueldo": self.sueldo,
            "clave": self.clave,
            "nombre": self.nombre,
            "dni": self.dni,
        }


class Estado:
    usuarios: dict[DNI, Usuario]
    saldo: int
    movimientos: list[MOVIMIENTO]

    def __init__(self):
        self.__leer()

    def __leer(self):
        try:
            with open("estado.json", "r") as estado_archivo:
                estado_json = load(estado_archivo)

                self.movimientos = list(
                    map(
                        lambda m: (
                            datetime.strptime(m["fecha"], FORMATO_FECHA),
                            OPERACION(m["op"]),
                            m["dni"],
                        ),
                        estado_json["movimientos"],
                    )
                )

                usuarios = list(
                    map(lambda u: (u["dni"], Usuario(u)), estado_json["usuarios"])
                )

                self.usuarios = {}
                self.usuarios.update(usuarios)

                self.saldo = int(estado_json["saldo"])
        except:
            self.__inicial()
            self.guardar()

    def __inicial(self):
        usuario_administrador = Usuario()
        usuario_administrador.clave = clave_administrador
        usuario_administrador.nombre = nombre_administrador
        usuario_administrador.saldo = 0
        usuario_administrador.sueldo = 0
        usuario_administrador.dni = dni_administrador

        self.usuarios = {dni_administrador: usuario_administrador}
        self.saldo = 0
        self.movimientos = []

    def guardar(self):
        with open("estado.json", "w") as estado_archivo:
            dump(
                {
                    "usuarios": list(map(lambda u: u.aJson(), self.usuarios.values())),
                    "movimientos": list(
                        map(
                            lambda m: {
                                "fecha": m[0].strftime(FORMATO_FECHA),
                                "op": int(m[1]),
                                "dni": m[2],
                            },
                            self.movimientos,
                        )
                    ),
                    "saldo": self.saldo,
                },
                estado_archivo,
            )
