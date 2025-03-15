

from setuptools import setup, find_packages

setup(
    name="pad",
    version="0.0.1",
    author="Lina Marcela Roldan Pulgarin",
    author_email="lina.roldan@est.iudigital.edu.co",
    description="",
    py_modules=["actividad_1", "actividad_2"],
    install_requires=[
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "requests",
        "numpy",
        "openpyxl",
    ]
    
    
)
