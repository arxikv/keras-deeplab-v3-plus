from setuptools import find_packages, setup


setup(
    name="keras-deeplabv3",
    author="Emil Zakirov",
    version="1.2.0",
    python_requires=">=3.7, <4",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.3.0",
        "Pillow>=6.0.0",
        "matplotlib",
        "tqdm",
    ],
)
