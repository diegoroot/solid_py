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
    
    def save(self):
        print("guardamos el usuario. " + self.nombre)
    
    def send(self):
        print("enviamos el usuario. " + self.nombre)

diego_user = User(1, 'Diego')
print("Nombre: " + diego_user.nombre)
print("Código: " + str(diego_user.code))
diego_user.save()
diego_user.send()