from pathlib import Path

from IPython.testing.tools import full_path

file_path = Path('Scripts')
full_path = full_path(file_path)
print(file_path.name)
print(file_path.stem)
print(file_path.parent)
print(file_path.parent)