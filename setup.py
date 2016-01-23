import setuptools

setuptools.setup(
    name="pcr-marker-design",
    version="0.1.0",
    url="https://github.com/PlantandFoodResearch/pcr-marker-design",

    author="John McCallum",
    author_email="john.mccallum@plantandfood.co.nz",

    description="Tools for PCR assay design from NGS variant data",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)