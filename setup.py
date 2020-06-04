from setuptools import setup

setup(
    name="pydd",
    version="1.0",
    description="mv (using dd followed by rm) with a progressbar",
    url="https://github.com/avivajpeyi/pydd",
    author="Avi Vajpeyi",
    author_email="avi.vajpeyi@gmail.com",
    license="MIT",
    packages=["pydd"],
    zip_safe=False,
    install_requires=["tqdm>=4.32.1"],
    entry_points={"console_scripts": ["pydd=pydd.pydd:main"]},
)
