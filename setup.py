import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()
with open('requirements.txt') as f:
    requirements = f.readlines()
setuptools.setup(
    name='{{cookiecutter.repo_name}}',  # Replace with your own username
    version="0.0.4",
    author="DOT",
    author_email="dot@adara.com",
    description="'{{cookiecutter.repo_name}}' sub package using cookiecutter framework",
    long_description="Sample",
    long_description_content_type="text/markdown",
    include_package_data=True,
    url='https://github.com/dot-at-adara/{{cookiecutter.repo_name}}',
    packages=setuptools.find_packages(include=['{{cookiecutter.repo_name}}', '*/{{cookiecutter.repo_name}}.*',
                                               'framework.core']),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}}=framework.core.setup.command_line:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=requirements
)
