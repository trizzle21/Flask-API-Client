from setuptools import setup, find_packages

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)


version = get_version('github_api_client')



setup(
    name='githubapi_client',
    author='Tyler Ross',
    author_email='tdross21@gmail.com'
    version=version,
    packages=find_packages(),
    url = "",
    description='Client to access Github API.',
    author='Tyler Ross',
    install_requires=['flask==1.0.2', 'requests'],
)
