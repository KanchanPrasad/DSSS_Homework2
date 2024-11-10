from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    classifiers=[
        'License :: Apache License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],},
)
