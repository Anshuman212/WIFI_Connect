from setuptools import setup, find_packages

setup(
    name='wifi_connect',
    version='1.5',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'wifi_connect=WIFI_CONNECT.main:darth_query_network',
        ],
    },
    author='Anshuman Rai',
    author_email='raianshuman171@gmail.com',
    description='A real-time problem solver.A Python Project that connects to the best availalbe known networks which is a mannual task in Windows.',
    url='https://github.com/Anshuman212/WIFI_Connect',
)
