from setuptools import setup

setup(name='useful',
      version='1',
      description='Very useful code',
      url='https://github.com/catteoree/goit-python/tree/main/lesson07/useful',
      author='Perederko Iryna',
      author_email='catteoree@gmail.com',
      license='MIT',
      packages=['useful'],
      install_requires=['markdown'],
      entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
      )
