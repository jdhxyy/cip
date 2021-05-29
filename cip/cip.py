"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
cip: C/C++ Install Package.C/C++下的包管理工具
Authors: jdh99 <jdh821@163.com>
"""

import git
import os
import re


_path = os.getcwd() + '\\clib'
_requirements = os.getcwd() + '\\requirements.txt'


def set_lib_path(path=None):
    """设置库目录.默认是命令行当前目录下的lib目录"""
    global _path
    if path is None:
        _path = os.getcwd() + '\\clib'
    else:
        _path = path
    if not os.path.exists(_path):
        os.mkdir(_path)
    print('set lib path:', _path)


def set_requirements(path=None):
    """设置需求文件.默认是库目录同级的requirements.txt文件"""
    global _requirements
    if path is None:
        _requirements = os.path.dirname(_path) + '\\requirements.txt'
    else:
        _requirements = path
    print('set requirements:', _requirements)


def update(path=None):
    """更新仓库.如果不指定远程仓库路径,则根据需求文件全部更新"""
    global _path, _requirements

    if not os.path.exists(_path):
        set_lib_path(_path)

    if path is not None:
        _update_git(path)
        return

    if not os.path.exists(_requirements):
        print('Error:requirements file is not exist:', _requirements)
        return

    with open(_requirements, 'r') as f:
        for line in f.readlines():
            if line.isspace():
                continue
            line = line.replace(' ', '').replace('\\n', '').replace('\\t', '').replace('\\r', '').strip()
            _update_git(line)


def _update_git(path):
    dir_name = _parse_dir_from_git_path(path)
    if dir_name is None:
        print('git path is wrong format:', path)
        return

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        # 新建仓库拉取代码
        git.Repo.clone_from(path, dir_name)  # 拉取远程代码
        print(path, 'clone success')
        return

    repo = git.Git(dir_name)
    repo.execute('git clean -df')
    repo.execute('git checkout -- .')
    repo.execute('git pull origin master')
    print(path, ' is up-to-date')


def _parse_dir_from_git_path(path: str):
    if not path.endswith('.git'):
        return None
    data = path.split('.')
    data = re.split(r'[/\\]', data[-2])
    return _path + '\\' + data[-1]
