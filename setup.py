from setuptools import setup, find_packages

setup(
    name="apihub-universal-sdk",
    version="4.6.0",
    author="VeoCore Infra Global",
    description="Universal SDK for accessing next-gen AI Video APIs (Sora, Veo 3, Claude 4.6)",
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    entry_points={
        'console_scripts': [
            'apihub-setup=apihub_sdk.main:run_setup',
        ],
    },
)
