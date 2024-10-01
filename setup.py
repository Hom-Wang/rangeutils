import importlib
import sys
from pathlib import Path

from setuptools import find_packages, setup


def import_module(file: str):
    file = Path(file).resolve()
    if file.parent not in sys.path:
        sys.path.append(str(file.parent))
    return importlib.import_module(file.stem)


package_path = Path(__file__).resolve().parent / r"rangeutils"
version = import_module(file=package_path / "version.py")

long_description = ""
with open("README.md") as f:
    long_description = f.read()

setup(
    name="rangeutils",
    version=version.__version__,
    packages=find_packages(),
    package_data={"rangeutils": ["*"]},
    # include_package_data=True,
    entry_points={"console_scripts": []},
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=[
        "numpy",
    ],
)
