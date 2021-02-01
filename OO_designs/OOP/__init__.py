"""
the __init__.py files are required to make Python treat directories containing the file as packages - loadable module
=> if you import without __init__.py, Python does not know where the source code for stuff is and unable to recognize
 it as a package
=> or you need to amend the system path by:
import sys
sys.path.insert(0, 'path/to/file.py')

This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later
on the module search path
This is the first file to be loaded in a module, so you can use it to execute code that you want to run each time
a module is loaded,
"""

