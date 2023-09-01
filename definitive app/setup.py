from setuptools import setup

setup(
    name='CubeMatch',
    version='0.01',
    author='David Perez',
    author_email='david.perez@cubematch.com',
    packages=['cubematchfinance'],
    install_requires = ['pdfplumber','PyPDF2','PyQt5','pandas','pyxlsb','openpyxl','docx2pdf'],
    entry_points =  {
        "consoles_scripts":[
            'cubematch = cubematchfinance.__main__:main'
            ]
    }   
)
