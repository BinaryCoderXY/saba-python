import os
import re
import sys
import platform
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

# 这个类让 setup.py 调用 CMake
class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        cwd = os.path.abspath(os.getcwd())
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # 输出目录 = Python 包目录
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE=Release",
        ]

        build_args = ["--config", "Release"]
        os.makedirs(self.build_temp, exist_ok=True)
        cpu_count = os.cpu_count() or 4
        jobs = f"-j{cpu_count}"
        # CMake 配置
        subprocess.check_call(["cmake", cwd] + cmake_args, cwd=self.build_temp)
        # CMake 编译
        subprocess.check_call(["cmake", "--build", ".",jobs] + build_args, cwd=self.build_temp)

# 安装
setup(
    name="saba-python",
    version="0.1.0",
    author="BinaryCoderXY",
    description="Python binding for Saba MMD renderer",
    ext_modules=[CMakeExtension("saba")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
)