from setuptools import setup, find_packages

setup(
    name="pygame_music_materials",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "pygame_music_materials": ["musics/*.wav"],
    },
    install_requires=[
        "pygame>=2.5.2",
    ],
)
