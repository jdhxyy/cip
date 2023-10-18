from setuptools import setup, find_packages
filepath = 'README.md'
setup(
        name="cip",
        version="1.7",
        description="c/c++ install package",
        long_description=open(filepath, encoding='utf-8').read(),
        long_description_content_type="text/markdown",
        author="jdh99",
        author_email="jdh821@163.com",
        url="https://github.com/jdhxyy/cip",
        packages=find_packages(),
        data_files=[filepath],
        # 依赖模块
        install_requires=[
        'gitpython',
        ]
    )
