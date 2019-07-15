"""
lottery.py

動作確認環境
python : 3.7.3
numpy : 1.16.4
"""

import sys
import numpy as np

class Lottery:
    """
    くじ引きのクラス

    table : 抽選テーブル, 選択肢(key)と確率分布(value)が対応している辞書型.
    result : 抽選結果, tableのkeyと同じ型
    result_list : 複数の抽選結果, resultのnp.array
    """
    def __init__(self, table={"HIT":0.1, "MISS":0.9}):
        self.table = table
        self.result = None
        self.result_list = None

    def draw(self, times=1):
        """
        抽選を行い, 結果を返す
        1以上の回数を指定された場合は複数の結果をnp.arrayで返す

        times : 抽選回数, 整数型
        """
        if(times==1):
            self.result = np.random.choice(list(self.table.keys()), p=list(self.table.values()))
            return self.result
        else:
            self.result_list = np.random.choice(list(self.table.keys()), times, p=list(self.table.values()))
            return self.result_list


if __name__ == '__main__':

    # バージョン確認
    print(sys.version)
    print(np.__version__)

    # 動作確認
    table = {"A":0.5, "B":0.3, "C":0.2}
    lottery = Lottery(table)
    print(lottery.draw())
    print(lottery.draw(10))
