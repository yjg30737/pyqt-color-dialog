from setuptools import setup, find_packages

setup(
    name='pyqt-color-dialog',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Color Dialog',
    url='https://github.com/yjg30737/pyqt-color-dialog.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)