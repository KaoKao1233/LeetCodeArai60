# step1

# ・問題文英語なんだ、、慣れるまでは日本語翻訳機能を使いたいな
# ・Atcoderでやこれまで、型明示してこなかったから、違和感
# ・selfってなんだ？
# →おまじない的にselfを渡すみたいだけど、なんでだろ
# →javaでset/getの中でthisをつけるように関数の場合は取り合えずselfを渡すという理解でとどめる
# ・Optional[ListNode]はheadの型ヒントなんだろうけど、listであること以外何を意味してるのか分かんない
# →listnodeはあるポインタが次のポインタの場所をもっているリスト（基本情報で散々やったやつだ）
# →optionalは次のポインタ入ってるかもしれないし、noneかもしれないという意味
# most voted の書き方を参考にしたが、完走した人のコードをいくつか拝見して、好みを探す方が良いのか？
# 普段レビュー依頼を出されている方々は、5分見て分からなかったとき何を見て方向性を確認しているのだろうか。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False


# step2

# SlowとFastだけだと、何がどう早い/遅いなのか分かりにくいと思うので、動く点であることを示す
# ブロック毎に改行した方が可読性が上がると思うので、改行する
# step1では while slow.next and fast.next.next: を継続条件としていたが、 while SlowMovingPoint and FastMovingPoint.next: の方が
# slowの次があり、fastの次の次があるという言葉をコードに落とし込めている
# return trueを改行せずに書いてるから、return falseも改行しないように統一する


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        SlowMovingPoint = head
        FastMovingPoint = head

        while SlowMovingPoint and FastMovingPoint.next:
            SlowMovingPoint = SlowMovingPoint.next
            FastMovingPoint = FastMovingPoint.next.next

            if SlowMovingPoint == FastMovingPoint:
                return True
        return False