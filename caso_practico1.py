"""Cabecera de la aplicación"""

def cabecera():
    a = """
    ██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗ █████╗ ██╗      ██████╗
    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔════╝
    ███████║███████║███████╗███████║██║     ███████║██║     ██║     
    ██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██║██║     ██║     
    ██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║███████╗╚██████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
                                      <VIJUDAN> 
    """

    print(a)



def hash_calc():
    #Impirmo por pantalla la cabecera de la apicación
    cabecera()
    #Solicito al usiario el mensaje
    mensaje = input("Introduce un mensaje: ")
    #Obtengo el hash del mensaje
    hash_value = hash(mensaje)
    #Saco por pantalla el hash
    print(f"\nEl hash del mensaje es: {hash_value}")

def run():
    hash_calc()



if __name__ == "__main__":
    run()

