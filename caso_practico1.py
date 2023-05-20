"""App header"""

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
    #I print the header of  the app on the screen
    cabecera()
    #I ask the user for a message
    mensaje = input("Introduce un mensaje: ")
    #I get the hash of the message
    hash_value = hash(mensaje)
    #I print the hash on the screen
    print(f"\nEl hash del mensaje es: {hash_value}")

def run():
    hash_calc()



if __name__ == "__main__":
    run()

