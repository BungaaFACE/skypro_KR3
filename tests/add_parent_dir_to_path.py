# from pathlib import Path
import sys
import os
from pathlib import Path


PARENT_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# PARENT_FOLDER = str(Path(__file__).parent.parent)

sys.path.append(PARENT_FOLDER)
