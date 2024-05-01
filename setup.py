from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.0"
DESCRIPTION = "Create Splunk icons for App/Add-On Development"
LONG_DESCRIPTION = """
Creates icons to be used for developing Splunk apps and add-ons via resizing a provided image.\n
More information about Splunk"s required image sizes can be found here:\n
https://dev.splunk.com/enterprise/docs/developapps/createapps#Add-icons-to-your-app
"""

# Setting up
setup(
    name="splicon",
    version=VERSION,
    entry_points = {
        'console_scripts': ['splicon=splicon.splicon:create_splunk_icons'],
    },
    author="Sebastian Schimper",
    author_email="sebastianschimper@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["argparse", "pillow"],
    keywords=["python", "splunk", "icon", "development"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Splunk Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)