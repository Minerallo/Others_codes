import cx_Freeze

executables = [cx_Freeze.Executable("supermanGame.py")]

cx_Freeze.setup(
    name="supermanGame",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["character_game.png",
                                             "background.png"]}},
    executables=executables
)
# then cd folder directory
# and python setup.py build for 32bit
# or python setup.py bdist to create install.exe
