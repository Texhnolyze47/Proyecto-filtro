
# funcion que se encarga de enviar y codificar la info al arduino

def encode_send(ard, data):
    # print(f"enviar: {data}")
    enc = f"{data}\n".encode("UTF-8")
    print(f"enviar: {data}")

    ard.write(enc)

# funcion que se encarga de descodificar la info del arduino
def decode_response(ard):
    linea = ard.readline()
    respuesta = linea.decode()
    print("Tipo de variable", linea)
    print("Tipo de variable", respuesta)
    return respuesta

