## step1

### 方針
全組み合わせの合計を出して、小さいものからk個取得する
heapに(sum,(val1,val2))で格納して、k個popすれば取得できそう

### 制約
num1,num2はそれぞれ最低1つ以上
num1,num2は負の値を取り得る
kは1以上　かつ　全ペア数以下の値になる

```
num1が無くなるまで以下を継続
　num1から数字を1つ取り出してください
    num2が無くなるまで以下を継続
        num1 + num2を合計して、(sum,(val1,val2))でheapに格納

k回以下を継続
・min-heapの一番小さいものを取り出す
・そこから、ペアを抜き取って答えに加える
```

```python
# step1_1
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        smallest_sums = []
        
        for x in nums1:
            for y in nums2:
                sum_val = x + y
                heapq.heappush(heap,(sum_val,(x,y)))

        for _ in range(k):
            sum_val,(x,y) = heapq.heappop(heap)
            smallest_sums.append((x,y))

        return smallest_sums

```

上記で提出したら、Memory制限超過してしまった。
足し算をそもそもk回しかしない　または　足し算の結果を保存し続けない
どちらかのアプローチが必要そう？

他の解答を確認
```
https://github.com/MA-yo-TA/leetcode/pull/11/changes#diff-63b4572b60d464a21b76eec94977ff3883a9e00b3b7fdbd9df84448eaa214af9
https://github.com/h-masder/Arai60/pull/11/changes#diff-2cf1d4231314471fb70840584eb921eb8012ef1a813c956cb2befd08d45e3242
https://github.com/kazuki-official/leetcode/pull/10/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852
```
→自分の全探索は、必要以上の走査を行っており以下に探索を減らせるかが重要
初めに、nums1[i]+nums2[0]を全部、heapに入れて置いてpopする毎に、取り出したやつの右をheapに入れてpopしていくやり方がsetも使わないので、とてもクリーンだった
要素1 + 要素2 の組み合わせで最小/最大をk個取り出す時の書き方として擦れそう

```python
# step1_2
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallest_sums = []

        for i in range(min(k,len(nums1))):
            sum_vals = nums1[i] + nums2[0]
            heapq.heappush(heap, (sum_vals, (i, 0)))

        for _ in range(k):
            sum_vals, (x, y) = heapq.heappop(heap)
            smallest_sums.append((nums1[x], nums2[y]))
            if y <= len(nums2) -2:
                heapq.heappush(heap, ((nums1[x] + nums2[y+1]), (x, y+1)))

        return smallest_sums

```
上記で一旦通せた。

## step2

・y <= len(nums2) -2:　←　y+1とした方が、意図が伝わりやすそう
・答えの追加をタプルでやってしまっている
・x,yではなくi,jの方が良いか
・popで取り出したsum_valsは使っていないので　”_”にしても良いかも

```python
# step2

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallest_pairs = []

        for i in range(min(k, len(nums1))):
            sum_vals = nums1[i] + nums2[0]
            heapq.heappush(heap, (sum_vals, (i, 0)))

        while heap and len(smallest_pairs) < k:
            _, (i, j) = heapq.heappop(heap)
            smallest_pairs.append([nums1[i], nums2[j]])
            if j+1 <= len(nums2)-1:
                sum_vals = nums1[i] + nums2[j+1]
                heapq.heappush(heap, (sum_vals, (i, j+1)))

        return smallest_pairs

```

## step3

上記をエラーなく3回通す