import cip


def main():
    case2()


def case1():
    cip.set_lib_path()
    cip.set_requirements()


def case2():
    cip.set_lib_path('d:\\package\\lib')
    cip.set_requirements('F:\\common_project\\cip\\requirements.txt')
    cip.update()


def case3():
    cip.update('https://github.com/jdhxyy/lagan-micropython.git')


def case4():
    cip.update()


if __name__ == '__main__':
    main()
