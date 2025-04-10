def validar_correo(correo: str):
    import re
    return re.match(r'^[a-z0-9]+[\.]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$', correo)