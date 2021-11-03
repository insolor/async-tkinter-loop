from setuptools import setup, find_packages

install_requires = [
    'asyncio'
]

test_requires = [
    'pytest',
    'pytest-timeout',
    'pytest-cov',
    'flake8',
]

setup(name='async-tkinter-wrapper',
      version='0.0.1',
      description='Asynchronous wrapper for tkinter',
      url='https://github.com/insolor/async-tkinter-wrapper',
      author='insolor',
      author_email='insolor@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=install_requires,
      extras_require=dict(test=test_requires),
      zip_safe=True)
