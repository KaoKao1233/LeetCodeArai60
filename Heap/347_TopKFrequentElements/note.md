## step1

### 方針
counterで登場する数字の頻度を確認して、頻度の上位k個を返却する

### 制約
- numsは最低1個以上
- nums[i]は負の値を取り得る
- kは必ず1以上、でnumsに登場する種類の範囲内（3種類しかないのに、4種類返せみたいなことは言われない）
- 答えは必ず一意になる

### エッジケース
- numsが1の時　→　特にcounterすることなく、その数字を返却
- numsに登場する数字が1種類の時　→　その数字を返却

```
リストに登場する数字の種類を数えて
頻度の多い順に並び替えて
頻度の多いものから、k個の数字を返却して
```

```python
# step1_1
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
```

ここまで書いてみたが、counterで取得した結果をどうやったら降順で並び替えられるのか分からない・・・\
方針確認と合わせて他解答を確認

```
https://github.com/MA-yo-TA/leetcode/pull/10
https://github.com/kazuki-official/leetcode/pull/9
https://github.com/h-masder/Arai60/pull/10
https://github.com/dorxyxki/arai60/pull/9/changes
```
- counterを頻度で並び替えはsorted(list,key)でできそう
- counterで辞書作成したら、上位抽出の方法に複数選択肢がある。
  - バケットソート
  - ヒープ

今回はヒープの例題なので、ヒープのアプローチで解いてみる\
→heapにpushする際には、(num,count)のタプルでpushしようと思うが、heapはnumとcountのどちらを基準にする？\
→これは、左のものを基準にするっぽい

```python
import heapq
from typing import Counter, List

# step1_2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        top_k_nums = []

        for num, count in num_to_count.items():
            if len(top_k_nums) < k:
                heapq.heappush(top_k_nums, (count,num))

            elif top_k_nums[0][0] < count:
                heapq.heappushpop(top_k_nums, (count,num))

        return [num for count, num in top_k_nums]

```

取り合えず、上記で通せた。\
ただ、最後にまたもう一度numを取り出すためにtop_k_numsを走査するのはちょっと気になる\
それなら、無理にheapを使うのではなく、ソートのタイミングでsort(欲しい項目,key)で並び替えと取り出しを同時に行う方が綺麗に感じる\
step2ではそれでやってみる

## step2

すぐに取り出せないメソッドがこの問題では多いと感じた
- lamda x : x * 2　←　lamdaはその場限りの関数で、引数xを取る。具体的な処理は:以降の部分でx*2を行う
- sorted(x, key=y)
  - x は並べ替える対象。
  - y は「各要素をどう見て並べるか」を決める関数で、y が返した値の大小で並び順が決まる。
  - y を省略すると x の要素そのものの値で並ぶ。

```python
# step2_1
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        top_k_elements = sorted(num_to_count, key = num_to_count.get, reverse=True)[:k]

        return top_k_elements

```

lamdaの書き方も手に馴染みがないので、練習

```python
# step2_2
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        top_k_elements = sorted(num_to_count, key=lambda key : num_to_count[key], reverse=True)[:k]

        return top_k_elements

```

## step3
上記2通りの書き方を3回連続で通す