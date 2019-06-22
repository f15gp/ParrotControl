'''
ログ書き込み(ファイルに対して)
write logs to file.

Author: Bunya Masayuki, f15gp@outlook.jp
'''

import queue
import threading
import time
import datetime

from .file_write import FileWrite

class FileLog():
    """
    機能: 渡された文字列をファイルに書き込む。自動的に渡された文字列の先頭へ時刻を付与する。
          This class writes string to file.
          Moreover, this one inserts time before string automatically when it queues.
    """

    def put(self, value):
        log = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}" + " " + value + "\n"
        self.__queue.put(log)
        self.__queue.join()

    def worker(self):
        while True:
            log = self.__queue.get()
            if log is not None:
                with FileWrite(name=self.__file_name) as file:
                    for elem in log:
                        file.write(elem)

                self.__queue.task_done()

            time.sleep(1)

    def __init__(self, fname="log.txt"):
        self.__queue = queue.Queue()

        self.__file_name = fname

        self.__thread = threading.Thread(target=self.worker)
        self.__thread.setDaemon(True)
        self.__thread.start()

if __name__ == "__main__":
    log = FileLog()

    log.put("abc1")
    log.put("abc2")
    time.sleep(1)
    log.put("abc3")
    log.put("abc4")
    time.sleep(1)
    log.put("abc5")
    log.put("abc6")

    time.sleep(3)
