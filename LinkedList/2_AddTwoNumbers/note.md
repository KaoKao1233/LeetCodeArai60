step1

２つのリストを同時に走行（同じ長さではないので片方だけになるタイミングも出てくる）
一の位から順に足していき、繰り上がった場合は次回の計算で余剰分として上乗せする

<自然言語>
AさんBさんどちらも、valueが無くなるまで続けてください
AさんBさんvalueを先頭から1つずつください
前回の計算の余剰 + (A+B)の和一の位をノードのvalueに格納、余剰が生まれれば、それは別で保管（0 or 1）
次のノードへ移動

headの返却
<自然言語>

下記で書ききってみたが、アクセプトされなかったため、方針があっているかどうか確認
https://github.com/kazuki-official/leetcode/pull/5/changes
https://github.com/MA-yo-TA/leetcode/pull/6/changes
https://github.com/ryosuketc/leetcode_arai60/pull/5/changes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_a = l1
        list_b = l2
        sum_list = ListNode(val = 0)
        head = sum_list
        sum_list_runner = head
        is_carrying = False

        while not (list_a.next is None and list_b.next is None):
            if list_a is not None and list_b is not None:
                sum_value = list_a.val + list_b.val
            elif list_a is not None and list_b is None:
                sum_value = list_a.val
            else:
                sum_value = list_b.val
            
            if is_carrying:
                sum_value += 1
            if sum_value > 9:
                is_carrying = True
                sum_value = 0
            else:
                is_carrying = False
            
            sum_list_runner.val = sum_value
            sum_list_runner.next = ListNode()
            sum_list_runner = sum_list_runner.next
        
        sum_list_runner.next = None
        
        return head


他の解答を見て学んだ点
・divmod(a, b)でaをbで割った商と余りが返却される
・自分の記述の場合、l1とl2の片方がnoneの場合で複数場合分けが必要だったが、noneの場合をval = 0と考えて三項演算子を用いると記述量を減らせる
・l1とl2のnextがない場合、処理終了としていたが最後の最後に繰り上がった場合のことを考慮できていなかった
・こちらの問題でもdummy_headを使っている　→　連結リストの問題では多くの場合、番兵が有効のため最初のノードを特別扱いする必要がある場合には番兵の使用を検討することでバグの発生率を下げられる


step2

下記を今度は整形するため参照
https://github.com/kazuki-official/leetcode/pull/5/changes#diff-0ec46bd78c96c48cbfa4269694a8b6a78a051cd4e9d07f3a46d355337c9122ecR8
https://github.com/MA-yo-TA/leetcode/pull/6/changes

・最初私もl1とl2を別の変数で受け取っていたが、ただ引数のノードを進むだけで先頭の返却やval/nextの変更はないので、記述量削減のため今回は割愛
・listnode(val = digit)の方が、実務では好まれそう　※今回は引数自体が少ないので省略しても問題は無さそう
・val1,val2はvalue_l1とvalue_l2の方が可読負荷は少なそう


step3

step2での記述を3回連続ミスなく記述