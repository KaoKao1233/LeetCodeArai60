142_LinkedListCycleII


step1

前回は初見で問題文の理解に苦労したが、アルゴリズム毎に解くことで前回問題の英語知識をそのまま使えるので問題文が抵抗感なく読める
headをfor文で1つずつ取り出し、Hashsetでnodeとindexを管理すれば、上手くいきそう
→headをfor文で1つずつ取ろうとしてもheadはイテラブル（中身の要素を最初から1つずつ取り出せる）ではないから、取り出せない
→head（次のnodeへの場所が書いてあるだけの紙）、list（すべての要素の場所が書いてある紙）
hashsetでの解法に移行
前回の141_LinkedListCycle(https://leetcode.com/problems/linked-list-cycle/)をなぞる形で記述し、Acceptされた


step2

【参考PR】
https://github.com/MiuNagato/LeetCode_arai60/pull/3/changes
https://github.com/MA-yo-TA/leetcode/pull/3/changes
https://github.com/tamagoyaki-chiu/LeetCode-Practice/pull/5/changes
https://github.com/hiro111208/leetcode/pull/2/changes
https://github.com/denyaho/Leetcode_repository/pull/2/changes

【常識系】
https://discord.com/channels/1084280443945353267/1262761766887358557/1316060484239228978
https://github.com/tayzarnw/LeetCode/pull/4#issuecomment-2038618765
https://discord.com/channels/1084280443945353267/1262761766887358557/1316089240680923257


処理を書く際に、心がけとして早期離脱を意識していたが、自分の中でしっくりくる記述指針が無かった。しかし自然言語に直した際に文として違和感が無いかという見方をすれば良いのかと指針ができた。
それを踏まえると自分の判定条件は、自然言語に直すと違和感があるため、step2で修正が必要と思った。
具体的にstep1では、whileの中で、今のnodeに訪れたことがなければ～～～～、訪れたことがあれば～～～という書き方になっている。
ただ、betterは訪れたことがあれば、すぐreturn。そして訪れたことがなければ～～～が自然だと思った。


step3

floydのアプローチを考えたときにどうやってループを証明するのか、分からなかったのでfloydのアプローチをstep3では試みたい。
step2でチラ見した感じ、相変わらずslowとfastを用意するっぽい
ただ、slowとfastが重なる箇所がループの戻り箇所とは限らないので、どうやってそこを示せばよい？
headから1つずつ進むやつと、meeting_pointから1つずつ進むやつが最初に出会うところがサイクルの起点になる理由が分からない
下記で納得した

地点A：スタート地点
地点B：ループの入り口
地点C：ウサギと亀が出会う場所

X：ABの距離
Y：BCの距離
Z：Cから残りのループを走ってBに行くまでの距離

下記が成立する
2(X+Y) = X+Y+Z+Y
→X = Z
→よって、スタート地点から1個ずつ進ませた駒と衝突点から1個ずつ進ませた駒の合流地点がループの起点となる

一応、floydのアプローチでacceptできたが、圧倒的にsetの解き方の方が腹落ちするし、ループ証明との結びつきも自然な解法だと思った。ただ、floydの方はwhileの中にwhileがあり、setのアプローチよりも記述が増えるので改善ポイントが多いという点では良いと思った。
https://github.com/tayzarnw/LeetCode/pull/4#discussion_r1546155136
上記を見て、2重whileを避けた方が見通しが良いと指摘があり、試してみたがwhileを外だしするとなると、なんで1つ目のwhileを抜けたのかチェックするところに漏れが生じて、エラーを重ねてしまった。
何となく、他の人の解答を見て、分かった気になっていただけで完全に自分の思考をコードに落とし込めているのではなかったと気づいた。
if文を増やすのはバグの温床に繋がりやすい気がするが、それよりも可読性を優先することが実務には沿っているのだろう。