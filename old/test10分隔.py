def x(char, times):
    """单行分隔"""
    print (char * times)


def line(char, times):
    """多行分隔线

    :param char: 分隔字符
    :param times: 分隔次数
    """
    row = 0
    while row < 5:
        x(char, times)
        row += 1

