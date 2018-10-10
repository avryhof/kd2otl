from setuptools import setup

setup(
    name='kd2otl',
    version='0.0.1',
    packages=['kd2otl'],
    url='https://github.com/avryhof/kd2otl',
    license='MIT',
    author='Amos Vryhof',
    author_email='amos@vryhofresearch.com',
    description='My HAM Radio Website.',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
    install_requires=[
        "django",
        "django-cms",
    ],
)
