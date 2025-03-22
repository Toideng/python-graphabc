import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
VERSION = (HERE / "version.py").read_text().split()[-1].strip("\"'")

setup(
	name="graphabc",
	version=VERSION,

	description='PascalABC GraphABC module in Python',
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/Toideng/python-graphabc",
	author="Toideng",
	author_email="<toideng@toideng.com>",
	license="LGPLv3+",

	keywords=['pascal', 'pascalabc', 'pascalabc.net', 'graphics', 'education'],
	classifiers=[
		"License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
		"Topic :: Education",
		"Topic :: Multimedia :: Graphics",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Education",
		"Programming Language :: Pascal",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Operating System :: POSIX :: Linux",
		"Operating System :: Microsoft :: Windows",
		"Typing :: Typed",
	],

	packages=find_packages(),
	include_package_data=True,

	setup_requires=["raylib>=5.5.0.2"],
	install_requires=["raylib>=5.5.0.2"],
	python_requires='>=3.8.1',   # Python 3.8 not tested, but hopefully can work
)

