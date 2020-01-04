from pathlib import Path

path = Path("/Users/apple/Desktop/datastructure")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(paths)
print(py_files)

path = path.with_suffix(".py")
print(path)
