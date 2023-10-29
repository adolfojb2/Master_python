


class Acciones:
    def registro(self):
        print("\nOk!!! Vamos a registrarte en el sistema... ")

        username = input("¿Cual es tu nombre de usuario?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        #crear el objeto "usuario" con el modelo
        #llamar el método usuario.registrar()