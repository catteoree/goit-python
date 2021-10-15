from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Sorting files and unpacking archives to directories: '
                  'images, audio, video, documents, others and archives.',
      url='https://github.com/catteoree/goit-python/tree/main/lesson07/clean_folder',
      author='Perederko Iryna',
      author_email='catteoree@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean']}
      )
