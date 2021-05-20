from setuptools import setup


setup(
    name="design-history-template",
    version="0.1.0",
    description="Base templates for design history prototypes",
    url="https://github.com/test-and-trace/design-history-template",
    author="Adam Shimali",
    license="MIT",
    packages=["design_history_template"],
    package_data={"design_history_template": ["templates/**/*.html"]},
    install_requires=["jinja2"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
