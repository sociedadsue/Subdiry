import requests

print("Subdiry by Sociedad. Tools para sitios web.")
print("")
website = input("URL del sitio web (Incluir http:// o https:// al comienzo): ")

if website.count("/") == 2:
    website = website + "/"

if website.count(" ") != 0:
    print("")
    print("URL mal puesta.")
    exit()

def subdirectories():
    file = open("subdiry", "r")
    filecontent = file.readlines()
    print("Escaneando " + website)
    for i in range(len(filecontent)):
        requested = requests.get(website + filecontent[i])
        if requested.ok:
            print(str(requested) + ": " + filecontent[i])

def ping():
    print("Mandando conexion a " + website)
    ping = requests.get(website)
    if ping.ok:
        print("Se ha podido conectar al sitio.")
    else:
        print("No se pudo mandar un paquete al sitio.")

def html():
    print("Sacando el HTML de " + website)
    print(requests.get(website).text)

def guia():
    print("¿Que quieres hacer con la URL?")
    print("1- Buscar algun subdirectorio.")
    print("2- Ver si hay conexion.")
    print("3- Sacar el HTML de un sitio.")
    print("H- Mirar esta guia de vuelta.")
    print("U- Cambiar URL seleccionada.")
    print("X- Salir.")

guia()

salir = False
while salir == False:
    respuesta = input()
    if respuesta == "1":
        subdirectories()
    if respuesta == "2":
        ping()
    if respuesta == "3":
        html()
    if respuesta == "H":
        guia()
    if respuesta == "U":
        website = input("Nueva URL: ")
        if website.count("/") == 2:
            website = website + "/"
        if website.count(" ") != 0:
            print("URL mal puesta.")
            break
        print("La URL ahora es: " + website)
    if respuesta == "X":
        salir = True
