from setuptools import setup, find_packages

setup(
    name='Singkatan',
    version='0.1.0',
    description='A simple converter for slang word in indonesian into actual word',
    url='https://github.com/khumam/Singkatan',
    author='Khoerul Umam',
    author_email='id.khoerulumam@gmail.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='slang converter word in indonesian',
)
