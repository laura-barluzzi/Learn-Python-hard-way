try: 
    from setuptools import setup

except ImportError:
    from distutils.core import setup
    
config = {"description": "Exercise 47",
          "author": "Laura Barluzzi",
          "url": "URL to get it at.",
          "download_url": "Where to download it.",
          "author_email": "laura.barluzzi@gmail.com",
          "version": "0.0.1",
          "install_requires": ["nose"], 
          "packages": ["ex47"],
          "scripts": [],
          "name": "exercise47"}
           
           
setup(**config)
