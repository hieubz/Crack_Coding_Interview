"""
Modules are simply Python files, nothing more.
The single file in our small program is a module.
Two Python files are two modules. If we have two files in the
same folder, we can load a class from one module for use in the
other module.

Note: done use import * cuz this syntax can bring unexpected objects into
our local namespace and it takes longer to find where that class/method is located

"""
from .database import Database as DB

db = DB()
