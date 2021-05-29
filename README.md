# cip

## 介绍
cip: C/C++ Install Package.cip是C/C++的包管理器.

cip会自动从需求文件中拉取github或者gitee等仓库中的包，也可以自动更新包。

## 安装
```text
pip install cip
```

cip依赖gitpython包,也需要安装:
```text
pip install gitpython
```

## 开源
- [github上的项目地址](https://github.com/jdhxyy/cip)
- [gitee上的项目地址](https://gitee.com/jdhxyy/cip)

## API
```python
def set_lib_path(path=None):
    """设置库目录.默认是命令行当前目录下的clib目录"""

def set_requirements(path=None):
    """设置需求文件.默认是库目录同级的requirements.txt文件"""

def update(path=None):
    """更新仓库.如果不指定远程仓库路径,则根据需求文件全部更新"""
```

## 使用方法
在工程目录下新建需求文件requirements.txt,输入python,打开python命令行,然后根据需求文件自动拉取或者更新包.

```python
import cip
cip.update()
```
