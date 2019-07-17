"""
gogo_juggler.py

動作確認環境
python : 3.7.3
numpy : 1.16.4
"""

import sys
import numpy as np

from juggler import Juggler

class GoGoJuggler(Juggler):
    """
    ゴーゴージャグラーのクラス

    Parameters
    ----------
    setting : 整数(1~6)
        設定レベル
    """
    def __init__(self, setting=6):
        self.name = "ゴーゴージャグラー"
        self.setting = setting
        self.table = self.create_table(self.setting)
        super().__init__(name=self.name, table=self.table)

    def create_table(self, setting):
        """
        設定を用いて抽選テーブルを作る.

        Parameters
        ----------
        setting : 整数
            設定レベル

        Returns
        -------
        table : 選択肢(key)と確率分布(value)が対応している辞書型
            抽選テーブル
        """
        # 各出目の出現率(x/65536のx)
        BIG = [182, 183, 184, 187, 191, 200]
        REG = [135, 145, 151, 171, 192, 200]
        CHERRY_BIG = [61, 61, 62, 65, 66, 70]
        CHERRY_REG = [45, 50, 55, 60, 65, 70]
        CHERRY = [1840, 1840, 1840, 1840, 1840, 1840]
        GRAPE = [9610, 9690, 9770, 9850, 9930, 10020]
        REPLAY = [8978, 8978, 8978, 8978, 8978, 8978]
        PIERROT = [60, 60, 60, 60, 60, 60]
        BELL = [60, 60, 60, 60, 60, 60]

        table = {}
        table.setdefault("BIG", BIG[setting-1]/65536.)
        table.setdefault("REG", REG[setting-1]/65536.)
        table.setdefault("CHERRY_BIG", CHERRY_BIG[setting-1]/65536.)
        table.setdefault("CHERRY_REG", CHERRY_REG[setting-1]/65536.)
        table.setdefault("CHERRY", CHERRY[setting-1]/65536.)
        table.setdefault("GRAPE", GRAPE[setting-1]/65536.)
        table.setdefault("REPLAY", REPLAY[setting-1]/65536.)
        table.setdefault("PIERROT", PIERROT[setting-1]/65536.)
        table.setdefault("BELL", BELL[setting-1]/65536.)
        table.setdefault("MISS", 1.0-sum(table.values()))
        return table



if __name__ == '__main__':
    # バージョン確認
    print(sys.version)
    print(np.__version__)

    # 動作確認
    for i in range(1, 7):
        kikaiwari = []
        for j in range(100):
            gogo = GoGoJuggler(i)
            result_list = gogo.simulate(8000)
            kikaiwari.append(100.*gogo.count_medals_out(result_list)/gogo.count_medals_in(result_list))
        print("設定:%d, 機械割(8000回転x100回平均):%.1f%%"%(i, np.mean(kikaiwari)))
