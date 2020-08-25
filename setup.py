import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='drn',
    version='0.1',
    author='raven38',
    author_email='current.address@unknown.invalid',
    description=('Package for calculating segmentation accuracy (mAP and Pixel accuracy) '
                 'using PyTorch'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raven38/drn',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'drn = segment:main',
        ],
    },
    install_requires=[
        'numpy',
        'pillow',
        'torch',
        'torchvision'
    ]
)
