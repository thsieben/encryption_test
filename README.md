# Steps to pyminify, cythonize, and pyinstall a project

## Pyminifier
For an individual file, you can perform the following operations.
- Call `pyminifier file_name.py` to perform basic obfuscation. This will
  strip comments from your file and print them to the console.
- Save the results to a file with `pyminifier file_name.py > results.py`
- Make the file very hard to read by substituting function names, classes,
  variables, etc. with the `--nonlatin` flag.

**Noted issues**
- When using nonlatin substitution across multiple files, e.g. with helper
  classes called by a main function, can get errors with not calling the correct
  obfuscated file, or other errors with substitution messing with the program
  executing at all.



## Cythonize
Within a project directory, create a `setup.py` file which will contain the
necessary setup to cythonize your python files.
- At a minimum, the setup file should have
  `setup(name="name", ext_modules=cythonize('python files'))`
- names and ext_modules
- You can also extend the build_ext class to have other functionality to create
  extensions for multiple directories and file extensions.
- To create the cythonized version, run `python setup.py build_ext --inplace`.
- Note if you are using python3 to run the above command with `python3`.


## PyInstaller
Once you have the necessary cythonized and pyminified versions of your files, you can bundle them with PyInstaller to make an executable.
- Run `pyinstaller --onefile "file_name.py"`.

**Noted issues**
- Currently having an issue where after running pyinstaller on a version of cythonize, there is a recursion limit reached.
