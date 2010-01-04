#stupid.py contains stupid helper functions that are specific to this project, maybe one day they might get promoted to utils.py

import os
def splitjoin(path):
    """
    takes path presumed to be formatted in path/to/file.ext and returns os.path.join version
    """
    return reduce(os.path.join,path.split("/"))