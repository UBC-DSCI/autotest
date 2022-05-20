"""
http://docs.python-guide.org/en/latest/writing/structure
"""
import os
import site
import sys
from pathlib import Path
import importlib.resources as ir

curr_dir = Path(__file__).parent
root_dir = curr_dir
#~/repos/pythonlibs/diskinventory/notebooks/datadir


student_ids = data_dir /  "fakestudentnames.csv"
exchange_dir = root_dir / 'exchange'
assign_db = (root_dir / "gradebook.db").resolve()
sys.path.insert(0, root_dir)

sep = "*" * 30
print(
    (
        f"{sep}\ncontext imported. Front of path:\n"
        f"{sys.path[0]}\n{sys.path[1]}\n{sep}\n"
        f"root_dir = {root_dir}\n"
    )
)
site.removeduppaths()

