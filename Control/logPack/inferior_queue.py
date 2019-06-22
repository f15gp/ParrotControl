'''
キュー でも標準でQueueパッケージ(排他付き)があるので、これは没にする
Queue, but Python has Queue module which is useful in thread.
So, this class doesn't use.

Author: Bunya Masayuki, f15gp@outlook.jp
'''

class InferiorQueue():
    """キュー Queue"""

    def __init__(self):
        self.__queue_list = []

    def push(self, value):
        self.__queue_list.append(value)

    def pop(self):
        try:
            value = self.__queue_list.pop(0)
        except IndexError:
            value = None

        return value

if __name__ == "__main__":
    queue = InferiorQueue()

    queue.push("a")
    queue.push("b")
    queue.push(2)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
