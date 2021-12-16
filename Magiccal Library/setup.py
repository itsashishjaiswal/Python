from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Unix :: Linux :: MacOS :: MacOS X :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Magiccal',
  version='0.0.1',
  description='A very basic calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author="Ashish Jaiswal",
  author_email="a.j250897@gmail.com",
  license='MIT', 
  classifiers=classifiers,
  keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'], 
  packages=find_packages(),
  install_requires=[''] 
)