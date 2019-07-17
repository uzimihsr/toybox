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
    くじ引きのクラス.

    Parameters
    ----------
    table : 選択肢(key)と確率分布(value)が対応している辞書型
        抽選テーブル
    """
    def __init__(self, table={"HIT":0.1, "MISS":0.9}):
        # 抽選テーブル
        self.table = table

    def draw(self, times=1):
        """
        抽選を行い, 結果を返す.
        1以上の回数を指定された場合は複数の結果をnp.arrayで返す.

        Parameters
        ----------
        times : 整数
            抽選回数

        Returns
        -------
        result : 文字列またはnp.array(文字列)
            抽選結果(単独または複数回)
        """
        if(times==1):
            result = np.random.choice(list(self.table.keys()), p=list(self.table.values()))
            return result
        else:
            result_list = np.random.choice(list(self.table.keys()), times, p=list(self.table.values()))
            return result_list


if __name__ == '__main__':

    # バージョン確認
    print(sys.version)
    print(np.__version__)

    # 動作確認
    table = {"A":0.5, "B":0.3, "C":0.2}
    lottery = Lottery(table)
    print(lottery.draw())
    print(lottery.draw(10))
