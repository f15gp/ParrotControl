'''
呼び出し可能なメソッドの一覧を表示させる

Author: Bunya Masayuki, f15gp@outlook.jp
'''

import queue

# アトリビュート一覧のうち
# callable なオブジェクトのみを表示する
for attr in dir(queue):
    if callable(getattr(queue, str(attr))):
        print(attr)

