from pathlib import Path
from time import ctime
import shutil

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
another_py_files = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)

path = path.with_suffix(".py")
print(path)

path = Path("/Users/apple/Desktop/datastructure/data.py")
print(path.stat())
print(ctime(path.stat().st_ctime))


source = Path("/Users/apple/Desktop/datastructure/data.py")
target = Path("/Users/apple/Desktop/datastructure/structure.py")

shutil.copy(source, target)
