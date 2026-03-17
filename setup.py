import os
import glob

from setuptools import setup, find_packages


def get_version() -> str:
    """Read the version string from metaflow/version.py."""
    with open("metaflow/version.py", mode="r") as f:
        return f.read().splitlines()[0].split("=")[1].strip(" \"'")


def find_devtools_files() -> list[str]:
    """Recursively collect all files under the devtools directory."""
    return [
        path
        for path in glob.iglob("devtools/**/*", recursive=True)
        if os.path.isfile(path)
    ]


setup(
    # ------------------------------------------------------------------ #
    # Package identity                                                     #
    # ------------------------------------------------------------------ #
    name="metaflow",
    version=get_version(),
    description="Metaflow: More AI and ML, Less Engineering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Metaflow Developers",
    author_email="help@metaflow.org",
    license="Apache Software License",

    # ------------------------------------------------------------------ #
    # PyPI classifiers                                                     #
    # ------------------------------------------------------------------ #
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],

    # ------------------------------------------------------------------ #
    # Project links shown on PyPI                                          #
    # ------------------------------------------------------------------ #
    project_urls={
        "Source": "https://github.com/Netflix/metaflow",
        "Issues": "https://github.com/Netflix/metaflow/issues",
        "Documentation": "https://docs.metaflow.org",
    },

    # ------------------------------------------------------------------ #
    # Package discovery and data                                           #
    # ------------------------------------------------------------------ #
    packages=find_packages(exclude=["metaflow_test"]),
    py_modules=["metaflow"],
    include_package_data=True,
    package_data={
        "metaflow": [
            "tutorials/*/*",                          # bundled tutorial files
            "plugins/env_escape/configurations/*/*",  # env escape configs
            "py.typed",                               # PEP 561 marker
            "**/*.pyi",                               # type stub files
        ]
    },

    # Installs devtools files into share/metaflow/devtools
    data_files=[("share/metaflow/devtools", find_devtools_files())],

    # ------------------------------------------------------------------ #
    # CLI entry points                                                     #
    # ------------------------------------------------------------------ #
    entry_points={
        "console_scripts": [
            "metaflow=metaflow.cmd.main_cli:start",        # main CLI
            "metaflow-dev=metaflow.cmd.make_wrapper:main", # dev wrapper CLI
        ]
    },

    # ------------------------------------------------------------------ #
    # Dependencies                                                         #
    # ------------------------------------------------------------------ #
    install_requires=[
        "requests",  # HTTP client for API calls
        "boto3",     # AWS SDK for S3 and cloud integrations
    ],
    extras_require={
        # Install matching type stubs: pip install metaflow[stubs]
        "stubs": ["metaflow-stubs==%s" % get_version()],
    },
)
