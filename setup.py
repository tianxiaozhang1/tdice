import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'tdice',        
  packages = ['tdice'],  
  version = '1.0',      
  license='MIT',        
  description = 'TDICE is a dice strategy game based on KDice, which itself is similar to Risk.',  
  author = 'Tianxiao Zhang',                   
  author_email = 'tianxiaozhang@gmail.com',     
  url = 'https://github.com/tianxiaozhang1/tdice',   
  download_url = 'https://github.com/tianxiaozhang1/tdice/archive/refs/tags/v_01.tar.gz',    
  keywords = ['game', 'python', 'dice'],   
  install_requires=[            
          'pygame',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)