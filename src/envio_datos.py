def encode_send(ard, data):
    # print(f"enviar: {data}")
    enc = f"{data}\n".encode("UTF-8")
    print(f"enviar: {data}")

    ard.write(enc)


def decode_response(ard):
    linea = ard.readline()
    respuesta = linea.decode()
    print("Tipo de variable", linea)
    print("Tipo de variable", respuesta)
    return respuesta

