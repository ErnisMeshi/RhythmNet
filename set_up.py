import setuptools


def setup():
    with open('requirements.txt') as text_file:
        requirements = text_file.read().splitlines()

    setuptools.setup(
        packages=['Rythmnet_HR_estimation'],
        author_email='ernis.meshi@student.uni-pr.edu',
        url='https://github.com/ErnisMeshi/RhythmNet.git',
        license='unlicense',
        include_package_data=True,
        install_requires=requirements,
        python_requires='>=3.10.0',
        author='Ernis Meshi',
        version='0.0.1',
        name='Rythmnet_HR_estimation',
        zip_safe=False
    )


if __name__ == '__main__':
    setup()
