from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

from pathlib import Path
import shutil

class MyBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent

        target_dir = build_dir if not self.inplace else root_dir

        self.copy_file(Path('test') / '__init__.py', root_dir, target_dir)
        self.copy_file(Path('foo') / '__init__.py', root_dir, target_dir)
        self.copy_file(Path('test') / '__main__.py', root_dir, target_dir)
        self.copy_file(Path('foo') / '__main__.py', root_dir, target_dir)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return

        shutil.copyfile(str(source_dir / path), str(destination_dir / path))

setup(
    name="testpkg",
    ext_modules=cythonize(
        [
            Extension("test.*", ["test/*.py"]),
            Extension("foo.*", ["foo/*.py"])
        ],
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True
        )
    ),
    cmdclass=dict(
        build_ext=build_ext
    ),
    packages=["test", "foo"]
)
