import os
import pathlib

DIR = pathlib.Path(__file__).parent

path = DIR 

init_file = path / "__init__.py"

if not init_file.exists():
    init_file.touch()

# add all files in dir as imports
imports = []
for file in os.listdir(path):
    if file == "__init__.py":
        continue

    if file.endswith(".py"):
        imports.append(file[:-3])

with open(init_file, "w") as f:
    for import_ in imports:
        f.write(f"from .{import_} import *\n")