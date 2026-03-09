# ==============================

# GUARDADO

# ==============================

# YEFRY BERAS = 22-MISN-2-040

def guardar_progreso(nivel):

    with open(ARCHIVO_GUARDADO, "w") as f:

        json.dump({"nivel": nivel}, f)


def cargar_progreso():

    if os.path.exists(ARCHIVO_GUARDADO):

        with open(ARCHIVO_GUARDADO, "r") as f:

            return json.load(f).get("nivel",1)

    return 1
