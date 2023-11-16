from cx_Freeze import setup, Executable
buildOptions = dict(packages=['PyQt5','PySide2','ifcopenshell'])

exe = [Executable('BIM수량산출.py')]

setup(
    name = 'test',
    version='0.0.1',
    author ='me',
    description='description',
    options = dict(build_exe = buildOptions),
    executables = exe
)
