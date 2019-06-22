'''
ファイルに文字列を書き込む
This writes string to file.

Author: Bunya Masayuki, f15gp@outlook.jp
'''

import os

class FileWrite():
    """
    機能: 渡された文字列をファイルに書き込む。Withでのみ使用することを想定
          This class writes string to file.
          However, we assume this is used for only 'With' syntax.
    """

    def write(self, value):
        """
        文字列を書き込む。
        This writes string to file.

        引数:
        value -- 書き込む文字列。 整形は一切行わない。
                 Writing string.　This function doesn't format anything for 'value'.
        """
        self.__file.write(value)

    def __init__(self, name, path=os.path.dirname(os.path.abspath(__file__))):
        """
        初期化
        initialize

        引数:
        name -- ファイル名
                file name
        path -- ファイルパス
                file path
        """
        self.__name = name
        self.__path = path

    def __enter__(self):
        self.__file = open(os.path.join(self.__path, self.__name), "a")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__file.close()
        return False

if __name__ == "__main__":
    str = [ "test1\n", "test2\n", "test3\n" ]

    with FileWrite(name="test1.log") as file:
        for elem in str:
            file.write(elem)

    write_path = os.path.dirname(os.path.abspath(__file__))
    with FileWrite(name="test2.log", path=write_path) as file:
        for elem in str:
            file.write(elem)

