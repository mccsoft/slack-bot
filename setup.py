from distutils.core import setup

setup(
    name='slack-bot',
    version='0.3.3',
    packages=['actors', 'teamcity'],
    url='',
    license='',
    author='anp',
    author_email='',
    description='', requires=['slacker', 'pykka', 'bs4', 'slackclient', 'pyteamcity', 'requests']
)
