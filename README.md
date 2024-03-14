# -algorithm-to-predict-each-team-s-qualified-probabilty-for-2024-cs2-copenhagen-major
 algorithm to predict each team's qualified probabilty for 2024 cs2 copenhagen major

This is a simple algorithm to predict the qualified probabilities for teams in cs2 2024 copenhagen major. All the codes are in main.py
You can change various parts of the code(the "power value" and the "random float") to make it more probable from your judgement to each team.
Here is the mechanism of the code:



Since the major schedule has came out, The first round is unchangeable. 
For the second round, the highest seed will always facing the lowest seed.
Start from the third round, the match will switch to swiss round same as valve notified.

The judging of win or lose in a round is depending on the “power value” of the team, and the power value has a random float as maximum 20%. ( if someone so toxic or someone so sick)
The power value of each team in my code is mostly the data (score） from hltv. And partially adjust it, such as i add more points to Ence because major is in Denmark, glave's hometown.

You can change the power value and the random float as you wish.

team_1  #C9
team_2 EF
team_3  #ENCE
team_4   #APEKS
team_5  #HEROIC
team_6 #9PAND
team_7  #SAW
team_8   #FUR
team_9  #ECST
team_10   #MGLZ
team_11  #IMP
team_12   #PAIN
team_13   #LVG
team_14   #AMK
team_15  #KOI
team_16  #LEG




预测哥本哈根major的简易算法，所有东西都在main.py里面
你可以调整里面的各项参数直到你觉得合理为止.
原理：
第一轮同赛程表不可改变
第二轮相同战绩队伍高种子顺位优先打最低种子顺位
第三轮开始采用瑞士轮，原理和v社公布的一致

判断胜负的办法为赋予每一个队伍“战力值”，以及最大20%的随机浮动（有个不当人或者有个责任神）
战力值由Hltv的沟槽野榜数据换算，并被小幅主观改动过，例如我给ence加了额外的一些分数，因为glave是主场作战有很大优势
你可以自由更改每个队伍的战力值，就在代码的最顶部.
BILIBILI 小扬羊
