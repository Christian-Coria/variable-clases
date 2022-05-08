class Persona:
    #iniciamos la variable de clase:
    contador_persona = 0

    def __init__(self,nombre,edad):
        #incrementamos la variable
        Persona.contador_persona +=1
        #asignamos el nuevo valos a id persona
        self._id_persona = Persona.contador_persona
        self._nombre = nombre
        self._edad = edad 


    def __str__(self):
        return f" Persona: [{self._id_persona} , {self._nombre}. {self._edad}] "

persona1 = Persona("juan", 33)
print(persona1)
persona2 = Persona("julio", 55)
print(persona2)
 #verificamos el contador
print(f"EL ID ES: {Persona.contador_persona}")