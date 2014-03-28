from setuptools import find_packages
from setuptools import setup
import os

version = '1.0.dev0'
shortdesc = 'Convinience for sphinx based addon documentation'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()

setup(
    name='mr.gutenberg',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    keywords='',
    author='Jens Klein, Sven Strack',
    author_email='jens@bluedynamics.com',
    license='GPLv2',
    url='https://pypi.python.org/pypi/mr.gutenberg',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['mr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zc.buildout',
        'zc.recipe.egg',
        'Sphinx',
        # theme later
        # maybe some sphinx addons
    ],
    entry_points="""\
       [zc.buildout]
       default = mr.gutenberg.recipe:Recipe
    """
)
