"""
juggler.py

動作確認環境
python : 3.7.3
numpy : 1.16.4
"""

import sys
import numpy as np

from lottery import Lottery

class Juggler(Lottery):
    """
    ジャグラー(スロット)のクラス

    Parameters
    ----------
    name : 文字列
        機種名
    table : 選択肢(key)と確率分布(value)が対応している辞書型
        抽選テーブル
    """
    def __init__(self,
                 name="名無しのジャグラー",
                 table={"BIG":0.1, "REG":0.1, "CHERRY_BIG":0.1, "CHERRY_REG":0.1, "CHERRY":0.1,
                        "GRAPE":0.1, "REPLAY":0.1, "PIERROT":0.1, "BELL":0.1, "MISS":0.1}):
        self.name = name
        self.functions = {"BIG":self.big, "REG":self.reg, "CHERRY_BIG":self.cherry_big,
                          "CHERRY_REG":self.cherry_reg, "CHERRY":self.cherry, "GRAPE":self.grape,
                          "REPLAY":self.replay, "PIERROT":self.pierrot, "BELL":self.bell, "MISS":self.miss}
        super().__init__(table=table)

    def draw(self):
        """
        1回転させて結果に応じたメソッドを呼び出す.
        """
        draw_result = super().draw(1)
        self.functions[draw_result]()

    def simulate(self, times=100):
        """
        複数回回転させて結果をnp.arrayで返す.

        Parameters
        ----------
        times : 整数
            抽選回数
        """
        draw_result_list = super().draw(times)
        return draw_result_list

    def count_results(self, result_list):
        """
        抽選結果リストから各出目の出現回数を算出する

        Parameters
        ----------
        result_list : np.array(文字列)
            抽選結果のリスト

        Returns
        -------
        counter : 出目(key)と出現回数(value)が対応した辞書型
            各出目の出現回数
        """
        counter = {}
        for key in self.table.keys():
            counter.setdefault(key, np.count_nonzero(result_list==key))
        return counter

    def count_medals_in(self, result_list):
        """
        抽選結果リストから現在までに投入されたメダル数を計算する

        Parameters
        ----------
        result_list : np.array(文字列)
            抽選結果のリスト

        Returns
        -------
        medals_in : 整数
            抽選結果から計算した現在までに投入されたメダル数
        """
        counter = self.count_results(result_list)
        medals_in = len(result_list) * (3) + counter["REPLAY"] * (-3)
        return medals_in

    def count_medals_out(self, result_list):
        """
        抽選結果リストから現在までに払い出されたメダル数を計算する

        Parameters
        ----------
        result_list : np.array(文字列)
            抽選結果のリスト

        Returns
        -------
        medals_out : 整数
            抽選結果から計算した現在までに払い出されたメダル数
        """
        counter = self.count_results(result_list)
        medals_out = counter["BIG"] * (309) + \
                     counter["REG"] * (101) + \
                     counter["CHERRY_BIG"] * (309) + \
                     counter["CHERRY_REG"] * (101) + \
                     counter["CHERRY"] * (1) + \
                     counter["GRAPE"] * (7) + \
                     counter["PIERROT"] * (10) + \
                     counter["BELL"] * (15)
        return medals_out

    def count_medals(self, result_list):
        """
        抽選結果リストから現在のメダル数を計算する

        Parameters
        ----------
        result_list : np.array(文字列)
            抽選結果のリスト

        Returns
        -------
        medals : 整数
            抽選結果から計算した現在のメダル数
        """
        # counter = self.count_results(result_list)
        # medals = len(result_list) * (-3) + \
        #          counter["BIG"] * (312) + \
        #          counter["REG"] * (104) + \
        #          counter["CHERRY_BIG"] * (312) + \
        #          counter["CHERRY_REG"] * (104) + \
        #          counter["CHERRY"] * (1) + \
        #          counter["GRAPE"] * (7) + \
        #          counter["REPLAY"] * (3) + \
        #          counter["PIERROT"] * (10) + \
        #          counter["BELL"] * (15)
        medals = self.count_medals_out(result_list) - self.count_medals_in(result_list)
        return medals

    def big(self):
        """
        BIGが出た場合の処理.
        """
        print("ペカッ!")

    def reg(self):
        """
        REGが出た場合の処理.
        """
        print("ペカッ!")

    def cherry_big(self):
        """
        CHERRY_BIGが出た場合の処理.
        """
        print("チェリー(ペカッ!)")

    def cherry_reg(self):
        """
        CHERRY_REGが出た場合の処理.
        """
        print("チェリー(ペカッ!)")

    def cherry(self):
        """
        CHERRYが出た場合の処理.
        """
        print("チェリー")

    def grape(self):
        """
        GRAPEが出た場合の処理.
        """
        print("ブドウ")

    def replay(self):
        """
        REPLAYが出た場合の処理.
        """
        print("リプレイ")

    def pierrot(self):
        """
        PIERROTが出た場合の処理.
        """
        print("ピエロ")

    def bell(self):
        """
        BELLが出た場合の処理.
        """
        print("ベル")

    def miss(self):
        """
        MISSが出た場合の処理.
        """
        print("ハズレ")


if __name__ == '__main__':

    # バージョン確認
    print(sys.version)
    print(np.__version__)

    juggler = Juggler()
    juggler.draw()
    result_list = juggler.simulate(19)
    print(result_list)
    print(juggler.count_results(result_list))
    print(juggler.count_medals(result_list))
