from cx_Freeze import setup, Executable


# On appelle la fonction setup

setup(

    name = "MacGyver",

    version = "0.1",

    description = "Save MacGyver !",

    build_exe_options = {"packages": ["os","pygame",],   
                        "include_files":["classes","constantes","level","images"]},

    executables = [Executable("labyrinthe.py")],

)