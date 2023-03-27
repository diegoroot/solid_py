class User:
    def __init__(self, code, nombre):
        self.__nombre = nombre
        self.__code = code
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    

    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, nuevo_code):
        self.__code = nuevo_code


class UserDB:
    user = User(None, None)

    def __init__(self, user):
        self.user = user

    def save(self):
        #attributes = list(bobby.__dict__.keys())
        print("guardamos el usuario. " + self.user.nombre)


class UserSend:
    user = User(None, None)

    def __init__(self, user):
        self.user = user

    def send(self):
        print("enviamos el usuario. "  + self.user.nombre)


diego_user = User(1, 'Diego')
import pdb; pdb.set_trace()
print("Nombre: " + diego_user.nombre)
print("Código: " + str(diego_user.code))

diego_user_db = UserDB(diego_user)
diego_user_db.save()
diego_user_send = UserSend(diego_user)
diego_user_send.send()