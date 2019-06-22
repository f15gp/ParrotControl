'''
Parrotを制御する
Control to fly a Parrot drone.

Author: Bunya Masayuki, f15gp@outlook.jp
'''

import time

from logPack import file_log

def main():
    log = file_log.FileLog()

    log.put("abc1")
    log.put("abc2")
    time.sleep(1)
    log.put("abc3")
    log.put("abc4")
    time.sleep(1)
    log.put("abc5")
    log.put("abc6")

    time.sleep(3)

if __name__ == "__main__":
    main()
