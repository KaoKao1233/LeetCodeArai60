step1

(4)8,5,4,2
(4)8,5,4,3,2 # add 3
(5)8,5,5,4,3,2 # add 5
(5)10,8,5,5,4,3,2 # add 10
(8)10,9,8,5,5,4,3,2 # add 9
(8)10,9,8,5,5,4,4,3,2 # add 4

initは普段書かない部分なので、一旦解き方の方針だけ考えて他回答などから確認する

◆方針
得点を降順に並べて、リストのn番目を常に握っておく。
n番目の得点を基準に下記で判断して返却値を決める
1.n番目より高い　→　n番目の位置をリストの左に1つずらす
2.n番目より低い　→　n番目の位置は変わらない
3.n番目と同じ　→　n番目の位置は変わらない

→1の挿入をリストで行うと先頭から値を確認して挿入することになるのでO(N)になってしまいTLEしそう。

下記を確認する。
https://github.com/kazuki-official/leetcode/pull/8
https://github.com/h-masder/Arai60/pull/9
https://github.com/MA-yo-TA/leetcode/pull/9

◆学んだこと
・min-heapでn番目を更新する方法で実装している
・クラス名をメソッドのように呼び出したタイミングで空のインスタンスを作成。その後、initにより初期化が行われる。
・selfを使って、インスタンスに値を格納することでメソッド跨ぎでもクラス内で値を使いまわせる。

<自然言語>
◆init
1.受け取ったリストを降順にしてください
・先頭からK番目までをスライスして、ヒープ化してください

（2.受け取ったリストを昇順にしてください
・リストをポップして、ヒープサイズがKになるまでpushしてください）

※1と2だとどちらが優れた選択になるのだろう
※判定基準としては、バグの混入リスクと処理速度で、1はサイズのみの評価で速そう
2は値を1つずつ評価できるから、バグの混入は少なそう
感覚的に1の方が絶対早いが、安全性の2を選択したくなる。どちらを優先するべきかはこれが使用される状況に依存するので、どちらでも実装できることが大事そう

◆add
heapの最小値と比較してください
最小値より小さい場合：
　最小値を返却してください
最小値より大きい場合：
　heapの最小値をpopして受け取った数字をheapにpushして最小値を返却してください。

</自然言語>

◆step1_1
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = []
        nums.sort(reverse=True)

        for x in nums:
            heapq.heappush(self.top_k,x)
            if len(self.top_k) == k:
                break

    def add(self, val: int) -> int:
        if val <= self.top_k[0]: # addする前の状態はtop_k[0]が無いのに、参照してしまった
            return self.top_k[0]
        heapq.heappushpop(self.top_k,val)
        return self.top_k[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


◆step1_2
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = []
        nums.sort(reverse=True)

        for x in nums:
            heapq.heappush(self.top_k,x)
            if len(self.top_k) == k:
                break

    def add(self, val: int) -> int:
        if len(self.top_k) == 0:
            heapq.heappush(self.top_k,val)

        else:
            if val <= self.top_k[0]:
                return self.top_k[0]
            heapq.heappushpop(self.top_k,val)

        return self.top_k[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


addする際にheapサイズが0の時に対して気を配ってみたが、acceptされない・・・
暫く時間が立ったので、改めて先ほど見た他の解答を確認
→initでtop_kが必ず、k個で構成されると思い込んでしまっていた。
ただしくは、numsの数+1まで取り得た


step1_3

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k = []
        nums.sort(reverse=True)

        for x in nums:
            heapq.heappush(self.top_k,x)
            if len(self.top_k) == k:
                break

    def add(self, val: int) -> int:
        if len(self.top_k) < self.k:
            heapq.heappush(self.top_k,val)

        else:
            if val <= self.top_k[0]:
                return self.top_k[0]
            heapq.heappushpop(self.top_k,val)

        return self.top_k[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


それなりにコードを書き始める前に流れを考えたが、エッジケースへの配慮が全然足りなかった
次回以降、問題を解く際にエッジケースでは制約の端の数字の場合を必ず検討して対策する


step2

step1を終えて気になるところ
・top_kがあんまりしっくりこない
・他にクリーンな書き方があるか

改めて下記を見て、改善点を探る
https://github.com/kazuki-official/leetcode/pull/8
https://github.com/h-masder/Arai60/pull/9
https://github.com/MA-yo-TA/leetcode/pull/9

・addの際に、一旦何でもheapに加えて基本的にはheap[0]を返す（ただし、heapサイズがkを超える場合はpopする）という書き方が自分にはとても無駄が無いように感じた。
・elementsという書き方がとても上位の要素の集まりというニュアンスが汲めていて良いと思った。

step3

step2にて記述したものをエラーなく3回連続で通す
