from setuptools import find_packages, setup

package_name = "vision_rpi_bot"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="bert",
    maintainer_email="bert@berrevoets.net",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "publisher = vision_rpi_bot.publisher:main",
            "subscriber = vision_rpi_bot.subscriber:main",
        ],
    },
)
