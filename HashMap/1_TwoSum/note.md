## step1

### 方針

全ての組み合わせを検討して、targetになる値の番号を返す方法しか思い浮かばない・・・
以下で方針確認

```
https://github.com/MA-yo-TA/leetcode/blob/65937d2ba9555797d5927eab96a67e1e16f9db64/1-Two-Sum/note.md?plain=1
https://github.com/h-masder/Arai60/blob/28e2c6dadf72382c1128b961ea141202a89a2b6c/1_Two_Sum/memo.md?plain=1
https://github.com/kazuki-official/leetcode/blob/465bbb9bf73dcc7f48ab05ae12aeb2ad6518b2ce/memo.md?plain=1
https://github.com/dorxyxki/arai60/pull/11/changes
```
hashで補完数を辞書で探す解法が多そうだった
2ポインタで両端から、和が目標より小さいならば、左を右へ、目標より大きいならば左へとずらして目標値になる場所を探す方法はとても面白いと思った
ただ、今回のジャンルがhashなのでhashを用いて、解く方を優先して解いてみる
今回は2つの数字の組み合わせで必ず解が見つかるから、hashでも良いが3つとかになるとポインタの方が良さそう

```
以下を解が見つかるまで続けてください
・貰った値をターゲットから引いた値がこれまでに出たかhashで確認して
・なければ、貰った値をhashに入れて次の値を確認して

ペアを教えて
```

```python
# step1
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target -num
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            num_to_index[num] = i

```

## step2

2ポインタでも書いてみる

```
左端と右端にポインタを置いてください

下記を目標値になるまで継続
・両ポインタに位置する数字の和が目標よりも小さい→左のポイントを右にずらす
・両ポインタに位置する数字の和が目標よりも大きい→右のポイントを左にずらす

目標値になった時のindexを報告
```

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0
        j = len(nums)-1
        sum_val = 0

        while sum_val != target:
            sum_val = nums[i] + nums[j]
            if sum_val < target:
                i += 1
            elif sum_val > target:
                j -= 1

        return [i, j]

```

上記で書いたが、sortしたために、元の項番を失ってしまった。
→項番と数字をタプルで持つ必要あり

```python
# step2
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((num, i) for i, num in enumerate(nums)) 
        i = 0
        j = len(sorted_nums) - 1
        sum_val = 0

        while i < j:
            sum_val = sorted_nums[i][0] + sorted_nums[j][0]

            if sum_val == target:
                return [sorted_nums[i][1], sorted_nums[j][1]]
            elif sum_val < target:
                i += 1
            elif sum_val > target:
                j -= 1

```

## step3

hashのやり方で3回連続で通す
