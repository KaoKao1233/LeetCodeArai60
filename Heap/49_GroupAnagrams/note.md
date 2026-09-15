## step1

暫く考えるも、文字列を並び替えて比較する方法しか思い浮かばず他PRを確認

```
https://github.com/MA-yo-TA/leetcode/blob/16a25f84b0d09ccfef91e31c8078e9d518e3a2ef/49-Group-Anagrams/note.md?plain=1
https://github.com/h-masder/Arai60/blob/7a89fc0e5984f5ee3db06aceb028f259a27739c2/49_Group_Anagrams/memo.md
https://github.com/kazuki-official/leetcode/blob/d91bf362c120df6b611d9565b73a54f09701d0e7/memo.md
```
上記を確認
→sortして比較という発想が素晴らしいと感動
→sortした単語を1つずつ辞書にチェックに行く、あったらvalueに追加みたいことできるんだろうか
→できそう

```
strsが無くなるまで下記継続
・strsから取り出したものをソートして辞書を確認して
・キーに存在したら、valueにその文字列を追加
・キーに無い場合は、そのキーのvalueを[]で作成して

最後、辞書のvaluesを教えて
```

```python
# step1
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_word_to_strs = defaultdict(list)

        for s in strs:
            s.sort()
            sorted_word_to_strs[s].append(s)
        return sorted_word_to_strs.values()

```
s.sort()
・文字列に対して、ソートは無理
・文字列をソートしたい場合は、引数をソートして、リスト化して返すsorted(s)を使う
※リストはunhashbleなので、最後はまた結合させる必要あり

色々な解答を見ていると、キーの仕方が複数あって面白い
a = ["a","b","cd"]の時に両者の返り値を比較すると、strの方は2文字以上の区切りにも対応するが、joinでは区別ができない
・str(sorted(s))　→　["a","b","cd"] ※ただ、記号が多く含まれる都合上、長大化するとメモリを圧迫する可能性あり
・"".join(sorted(s))　→　abcd

```python
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_word_to_strs = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_word_to_strs[sorted_s].append(s)

        return list(sorted_word_to_strs.values())

```

メモリ使用量
0~100の文字列が1~10^4個あり、それら全てをアナグラム毎に分類するので、
10^4 * 141byte (a = "a" で getsizeof(a)で確認)
= 約1.4MB
制約は見つけられなかったが、間違いなくパスしてそう

## step2

・str(sorted(s))の方でも書いてみる
・名前を工夫しようとして、sとしていたところをstrにしたら、予約語を奪ってしまいクラッシュ・・・、wordに変更

```python
# step2

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_word_to_word = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            sorted_word_to_word[sorted_word].append(word)

        return list(sorted_word_to_word.values())


# import sys


# a = str("'a',"*100)

# print(sys.getsizeof(a))

```

# step3

連続で3回通す
