from pathlib import Path

path = Path("/Users/apple/Desktop/datastructure/data.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_suffix(".py")
print(path)
