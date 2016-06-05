import os
from distutils.core import setup, Extension

lib_dir = '/usr/local/lib'#os.environ['LIB_DIR']

pypolychord_module = Extension(
        name= '_PyPolyChord',
        include_dirs = ['/usr/local/include'],
        library_dirs = [lib_dir],
        libraries = ['chord','gfortran'],
        sources=['_PyPolyChord.c']
        )

setup(
    name = 'PyPolyChord',
    version = '1.0',
    description = 'Run PolyChord with Python',
    ext_modules=[pypolychord_module]
)
