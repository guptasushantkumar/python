from setuptools import setup

def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='structure_demo',
      version='0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      url='https://github.com/guptasushantkumar/python',
      author='Flying Circus',
      author_email='example@example.com',
      license='NONE',
      packages=['aviva_edh_cyclops'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)
