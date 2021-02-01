"""
Modules are simply Python files, nothing more.
The single file in our small program is a module.
Two Python files are two modules. If we have two files in the
same folder, we can load a class from one module for use in the
other module.

Note: done use import * cuz this syntax can bring unexpected objects into
our local namespace and it takes longer to find where that class/method is located

__init__.py file that defines a directory as a package
This file can contain any variable or class declarations we like and
they will be available as part of the package.

__init__.py file for the new package can still be the main point of contact
for other modules talking to it. But not putting much code in it.



"""

# from .ecommerce.database import database

print("hello world")

