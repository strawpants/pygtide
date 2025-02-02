import os.path
import re

from numpy.distutils.core import setup, Extension

def find_version(*paths):
    fname = os.path.join(os.path.dirname(__file__), *paths)
    with open(fname) as fp:
        code = fp.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", code, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = find_version('pygtide', '__init__.py')

with open('README.md', 'r') as f:
    long_description = f.read()

ext = [Extension(name='pygtide.etpred',
                 sources=['src/etpred.f90'])]

setup(
    name='pygtide',
    version=VERSION,
    packages=['pygtide'],
    package_data={'pygtide': ['commdat/*']},
    ext_modules=ext,
    install_requires=['numpy', 'pandas','requests'],
    author='Gabriel C. Rau, Tom Eulenfeld',
    author_email='gabriel@hydrogeo.science',
    url='http://doi.org/10.5281/zenodo.1346664',
    description=('A Python module and wrapper for ETERNA PREDICT to compute '
                 'gravitational tides on Earth'),
    long_description=long_description,
    long_description_content_type='text/markdown'
    )
