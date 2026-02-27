import os

print("🔥 BRO GPT OFFLINE + MEMORIA PRO ACTIVADO 🔥")
print("Escribí 'salir' para cerrar.")
print("Comandos:")
print("/perfil → ver datos guardados\n")

archivo_memoria = "memoria.txt"

# Estructura del perfil
perfil = {
    "pc": "",
    "juego_favorito": ""
}

# Cargar memoria si existe
if os.path.exists(archivo_memoria):
    with open(archivo_memoria, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            if linea.startswith("pc:"):
                perfil["pc"] = linea.replace("pc:", "").strip()
            if linea.startswith("juego:"):
                perfil["juego_favorito"] = linea.replace("juego:", "").strip()

while True:
    pregunta = input("Vos: ").lower()

    if pregunta == "salir":
        print("BRO GPT: Nos vemos gamer 🎮")
        break

    # Guardar PC
    if pregunta.startswith("mi pc tiene"):
        perfil["pc"] = pregunta.replace("mi pc tiene", "").strip()
        with open(archivo_memoria, "w") as f:
            f.write(f"pc:{perfil['pc']}\n")
            f.write(f"juego:{perfil['juego_favorito']}\n")
        print("BRO GPT: Datos de tu PC guardados 🔥")
        continue

    # Guardar juego favorito
    if pregunta.startswith("mi juego favorito es"):
        perfil["juego_favorito"] = pregunta.replace("mi juego favorito es", "").strip()
        with open(archivo_memoria, "w") as f:
            f.write(f"pc:{perfil['pc']}\n")
            f.write(f"juego:{perfil['juego_favorito']}\n")
        print("BRO GPT: Juego favorito guardado 🎮🔥")
        continue

    # Mostrar perfil
    if pregunta == "/perfil":
        print("🔥 PERFIL GAMER 🔥")
        print("PC:", perfil["pc"] if perfil["pc"] else "No configurada")
        print("Juego favorito:", perfil["juego_favorito"] if perfil["juego_favorito"] else "No configurado")
        continue

    # Respuestas dinámicas
    if "rtx 3050" in pregunta:
        print("BRO GPT: Con esa GPU vas sólido en 1080p 😎")

    elif perfil["juego_favorito"] and perfil["juego_favorito"] in pregunta:
        print(f"BRO GPT: Uh, {perfil['juego_favorito']} es GOD TIER 🔥")

    else:
        print("BRO GPT: Interesante gamer 🤔 contame más.")
