import logging, os, glob

# Take directory of modules
modules_dir = os.path.dirname(__file__)

# Take .py files
files = os.path.join(modules_dir, "*.py")
modules = glob.glob(files)

# PLoad all modules
# (__all__ is a list of all modules,
# "from src.módulos import *" loads all modules from __all__)
__all__ = [os.path.basename(module)[:-3]
             for module in modules
               if os.path.isfile(module) and not module.endswith('__init__.py')]
