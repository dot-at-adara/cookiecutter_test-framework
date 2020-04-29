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
    description="'{{cookiecutter.repo_name}}' sub package using cookiecutter {{ cookiecutter.project_folder}}",
    long_description="Sample",
    long_description_content_type="text/markdown",
    include_package_data=True,
    url='https://github.com/dot-at-adara/{{cookiecutter.repo_name}}',
    packages=['cookiecutter_test_framework.{{cookiecutter.project_folder}}.{{cookiecutter.project_slug}}',
              '{{cookiecutter.test_folder}}'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}}={{ cookiecutter.project_folder}}.core.setup.command_line:main',
        ],
    },
    keywords=(
        'cookiecutter, Python, projects, project templates, Jinja2, skeleton, scaffolding, '
        'project directory, setup.py, package, packaging'
    ),
    python_requires='>=3.6',
    install_requires=requirements
)
