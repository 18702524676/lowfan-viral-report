# stats.md — 可复算统计表
编制：2026-10-16 23:51 Asia/Shanghai｜窗口：近30天

## 1. YouTube 总览
- n=2181（有粉丝且>0）｜queries=45｜channels=1542
- 低粉=508（23.3%）｜低粉离群=328｜有效离群(views≥1e5)=187｜有效离群频道数=149
- ratio 中位：全样本=2.21｜低粉=26.50｜非低粉=1.05
- 发布区间：2026-09-16 12:00:35+00:00 → 2026-10-16 09:03:41+00:00
- 采集 UTC：2026-10-16T15:51:10.209195+00:00

### 1.1 频道年龄（天）
- 全样本: n=2181 median_age=1174d｜≤90d 8.5%｜≤180d 16.4%
- 低粉离群: n=328 median_age=190d｜≤90d 29.6%｜≤180d 48.8%
- 有效离群: n=187 median_age=219d｜≤90d 29.4%｜≤180d 47.1%
- 低粉非离群: n=180 median_age=386d｜≤90d 16.1%｜≤180d 32.2%
- 非低粉: n=1673 median_age=1489d｜≤90d 3.6%｜≤180d 8.3%
- 离群频道去重=247｜≤90d=76｜≤180d=115
- 有效离群频道去重=149｜≤90d=42｜≤180d=65

### 1.2 时长 lift（相对低粉离群）
- ≤60s lift=1.44 CI95=(1.33, 1.55)｜基线占比=46.6%｜离群内=67.1%
- ≤3min lift=1.18 CI95=(1.13, 1.23)
- >10min lift=0.3 CI95=(0.19, 0.43)

时长交叉表（out=True 为低粉离群）:
out     False  True   All
dur                      
≤60s      795   220  1015
1-3m      509    62   571
3-10m     104    25   129
10-30m    219    10   229
>30m      224    11   235
All      1851   328  2179

### 1.3 按种子词（按有效离群频道数降序）
            query  n  out  out_ch  out100k  ch100k  share_pct  lift  med_views  med_out_views  short_out_pct  newch_out100k
 pet dog training 50   16      14       16      14       32.0  2.13    1421911        1421911             81              6
language learning 50   19      13       16      11       38.0  2.53     244536         225866             84              5
 bike maintenance 50   11      10       11      10       22.0  1.46     258306         267449             73              2
               手工 50    9       8        9       8       18.0  1.20     234085         272833             78              4
 personal finance 50    9       9        7       7       18.0  1.20     325061         147825             33              4
         AI tools 50    8       8        7       7       16.0  1.06     178774         326180             62              5
        gardening 50    7       7        7       7       14.0  0.93    1801909        1633805             43              2
     home workout 50    9       6        9       6       18.0  1.20    1296632        1219312            100              1
       car repair 50    6       6        6       6       12.0  0.80    1067811        1221709             50              2
 skincare routine 50    7       6        7       6       14.0  0.93     634070         688830             86              2
             中国历史 50   12       8        5       5       24.0  1.60      60225          73778             25              2
            chess 49    6       5        6       5       12.2  0.81    1784715        1775899             17              3
    origami craft 49    5       5        5       5       10.2  0.68     928337         425739             60              1
      side hustle 48    7       7        4       4       14.6  0.97     154365         124457             29              2
          fishing 50    4       4        4       4        8.0  0.53    3838838        6687016            100              4
               护肤 43    4       4        4       4        9.3  0.62    1437596        2939070             75              2
               健身 50    6       4        6       4       12.0  0.80     571571         666520             67              2
     productivity 50    4       4        4       4        8.0  0.53     358037         309527             25              2
 spanish learning 43    9       4        9       4       20.9  1.39     357504         357504            100              4
  stoicism quotes 50   31       8       12       3       62.0  4.12      56448          77079            100              0
    study with me 49    6       6        3       3       12.2  0.81      89576         223332             50              2
  coding tutorial 49    5       5        3       3       10.2  0.68     105295         154623             20              0
      woodworking 50    3       3        3       3        6.0  0.40    6392841        7397923            100              1
         diy home 49    3       3        3       3        6.1  0.41    5481046        4033807            100              1
     phone repair 50    3       3        3       3        6.0  0.40     538476         427717             33              0
               训犬 48    9       8        2       2       18.8  1.25      32420          18451             67              1
japanese learning 45   19       3        6       2       42.2  2.81      56554          34794            100              2
               露营 50    2       2        2       2        4.0  0.27    1331344        4617124              0              2
               理财 50    8       8        1       1       16.0  1.06       2860           1021             75              0
 budget meal prep 50    8       7        1       1       16.0  1.06      16135          18250             88              0
 chinese learning 50    5       5        1       1       10.0  0.66       8655           3019             80              1
  guitar beginner 50    8       4        3       1       16.0  1.06      79440          70937            100              0
       excel tips 50    4       4        1       1        8.0  0.53      26757          70290            100              1
      travel vlog 50    1       1        1       1        2.0  0.13    2462775        2035687              0              1
               副业 48   15      11        0       0       31.2  2.08        766            205              7              0
   first aid tips 50    9       9        0       0       18.0  1.20      20567           7003             78              0
             AI工具 49    6       6        0       0       12.2  0.81      22836          11766             33              0
               考研 50    5       5        0       0       10.0  0.66       4890           5877             60              0
               汽修 50    4       4        0       0        8.0  0.53      10826           9349             50              0
               读书 50    4       4        0       0        8.0  0.53       6942          19271              0              0
             西语学习 50    5       3        0       0       10.0  0.66        325            419             60              0
             英语学习 50    2       2        0       0        4.0  0.27      55140          36170             50              0
             日语学习 49    2       2        0       0        4.1  0.27       4911           6444             50              0
             宠物训练 13    2       2        0       0       15.4  1.02        463           1290             50              0
meditation guided 50    1       1        0       0        2.0  0.13      83537          62223              0              0

### 1.4 蓝海操作化筛选（ch100k≥5 且 med_views≥1e5 或有 out100k）
            query  n  out  out_ch  out100k  ch100k  share_pct  lift  med_views  med_out_views  short_out_pct  newch_out100k
 pet dog training 50   16      14       16      14       32.0  2.13    1421911        1421911             81              6
language learning 50   19      13       16      11       38.0  2.53     244536         225866             84              5
 bike maintenance 50   11      10       11      10       22.0  1.46     258306         267449             73              2
               手工 50    9       8        9       8       18.0  1.20     234085         272833             78              4
 personal finance 50    9       9        7       7       18.0  1.20     325061         147825             33              4
         AI tools 50    8       8        7       7       16.0  1.06     178774         326180             62              5
        gardening 50    7       7        7       7       14.0  0.93    1801909        1633805             43              2
     home workout 50    9       6        9       6       18.0  1.20    1296632        1219312            100              1
       car repair 50    6       6        6       6       12.0  0.80    1067811        1221709             50              2
 skincare routine 50    7       6        7       6       14.0  0.93     634070         688830             86              2
             中国历史 50   12       8        5       5       24.0  1.60      60225          73778             25              2
            chess 49    6       5        6       5       12.2  0.81    1784715        1775899             17              3
    origami craft 49    5       5        5       5       10.2  0.68     928337         425739             60              1

### 1.5 红海候选（Top50 内零低粉离群）
（无）

### 1.6 敏感性（阈值门槛）
- fol<10000 ratio>=10 views>=0: n=328 ≤60s%=67.1 top_ch={'pet dog training': np.int64(14), 'language learning': np.int64(13), '副业': np.int64(11), 'bike maintenance': np.int64(10), 'first aid tips': np.int64(9), 'personal finance': np.int64(9), '中国历史': np.int64(8), '手工': np.int64(8)}
- fol<10000 ratio>=5 views>=0: n=381 ≤60s%=66.1 top_ch={'副业': np.int64(15), 'pet dog training': np.int64(14), 'language learning': np.int64(13), '训犬': np.int64(12), 'stoicism quotes': np.int64(11), 'first aid tips': np.int64(10), 'chinese learning': np.int64(10), '理财': np.int64(10)}
- fol<10000 ratio>=50 views>=0: n=202 ≤60s%=67.3 top_ch={'pet dog training': np.int64(14), 'personal finance': np.int64(8), 'language learning': np.int64(7), 'gardening': np.int64(7), 'bike maintenance': np.int64(7), '副业': np.int64(7), '中国历史': np.int64(6), 'home workout': np.int64(6)}
- fol<10000 ratio>=10 views>=100000: n=187 ≤60s%=69.5 top_ch={'pet dog training': np.int64(14), 'language learning': np.int64(11), 'bike maintenance': np.int64(10), '手工': np.int64(8), 'AI tools': np.int64(7), 'personal finance': np.int64(7), 'gardening': np.int64(7), 'car repair': np.int64(6)}

### 1.7 系列化：有效离群频道中 ≥2 条的频道数=16｜max=10

## 2. B站
- 全量 n=1541｜published 中位=2025-04-01 04:55:31+00:00｜≥cutoff(2026-09-16) n=500
- 30天分析样本 n=500｜来源分布:
query
popular    500
- 低粉=22｜低粉离群=19｜离群UP数=19
- ratio 中位 全/低/非低: 0.50 / 95.28 / 0.44
- ≤3min lift=2.26 CI=(1.43, 3.07)｜>10min lift=0.13 CI=(0.0, 0.43)
out     False  True  All
dur                     
≤60s       34     5   39
1-3m       94     7  101
3-10m     148     6  154
10-30m    147     1  148
>30m       58     0   58
All       481    19  500

分区 lift（n≥5）:
   tname  n  out  share  lift  med_views
    音乐综合  7    1   14.3  3.76     181070
    手机游戏 28    3   10.7  2.82     336314
    单机游戏 47    5   10.6  2.80     232206
      日常 68    5    7.4  1.93     440130
    影视剪辑 19    1    5.3  1.39     810782
    动漫杂谈  6    0    0.0  0.00     121520
    乐评盘点  7    0    0.0  0.00     210447
    人文历史 24    0    0.0  0.00     354290
     小剧场 16    0    0.0  0.00     439157
   同人·手书 16    0    0.0  0.00     383176
      出行  9    0    0.0  0.00     399309
      搞笑 33    0    0.0  0.00     898362
      数码 13    0    0.0  0.00     258826
    新能源车  5    0    0.0  0.00     281059
    电子竞技  7    0    0.0  0.00     456117
    影视杂谈 23    0    0.0  0.00     376511
社科·法律·心理 11    0    0.0  0.00     210559
    科学科普  9    0    0.0  0.00     407628
    网络游戏 20    0    0.0  0.00     599878
      综合 17    0    0.0  0.00     186828
- 投币率 中位 离群 vs 其余: 0.81% vs 0.93%
- 收藏率 中位 离群 vs 其余: 2.65% vs 1.40%
- 分享率 中位 离群 vs 其余: 0.79% vs 0.23%

低粉离群样例（按播放）:
                                        url                             title         uploader  followers   views  duration_s   tname   query
https://www.bilibili.com/video/BV1gEps62E1e             《啦嗒铛》1.0正式发售宣传片 | GSE            香港GSE       5371 1974008         159    单机游戏 popular
https://www.bilibili.com/video/BV12Qp56VEBT                          何为Phira？           少哲-三角洲       7519 1271155         113      日常 popular
https://www.bilibili.com/video/BV1YhpY66E3p                 礼花炸响那一刻 又有个家庭蒸蒸日上            木白0v0       7133 1114347         142      日常 popular
https://www.bilibili.com/video/BV1Qope6rEH5                       豆包指导穿搭，笑死我了           七七酱就是我        662 1060793         438      日常 popular
https://www.bilibili.com/video/BV1Uqpg6TEQT                      当女朋友游戏技术比我好时             霄海Yo        175 1056591          10    单机游戏 popular
https://www.bilibili.com/video/BV1x9pt6JEkh     我让两个AI互相问了1000个问题，它们进化出了自己的语言          在公司楼下捡钱       7975  838423         246    单机游戏 popular
https://www.bilibili.com/video/BV1yxpC69Eds                 爱慕杰的海棠花开【AI全民制作人】          rairery       4131  459920         205      日常 popular
https://www.bilibili.com/video/BV152pC6gEPP                    锐评万花筒写轮眼从夯到拉排名            我老高了_       7174  415032         520 MAD·AMV popular
https://www.bilibili.com/video/BV1Pupy6sEVh                             Bad翻跳              顾霖炎       1124  374893          41    明星舞蹈 popular
https://www.bilibili.com/video/BV1pVJU64Ey6                             这鹦鹉魔了            茜熙嘻嘻吖       1093  339835          20      日常 popular
https://www.bilibili.com/video/BV152pC6gEqN       国产恐怖游戏《叫魂》电影式预告片公开 | 执念化作心魔 子时熄灯12AMBLACKOUT       1536  332035         112    单机游戏 popular
https://www.bilibili.com/video/BV1GGpR6AETH                 我在5:20睡觉，13:14准时起          我不叫流星yu       5556  325117          41     GMV popular
https://www.bilibili.com/video/BV1ktJ16JECb                第一集：“当你出生就自带豪气之咒!”         白了个白AIGC       3030  284060         101    手机游戏 popular
https://www.bilibili.com/video/BV1PtJ16nEcn 放弃大脑！祀狼2技4连青春爆炸队！真正的轮椅【明日方舟终末地洛茜】            毛巾欧尼酱       8699  210711         119    手机游戏 popular
https://www.bilibili.com/video/BV1SGJ168E1c         [性转马尔福] “哈利，你敢发誓你从未爱过我吗？”        沙拉shaula2       2047  198170          38    手机游戏 popular

## 3. X
- n=138 cols=['query_topic', 'id', 'url', 'username', 'followers', 'impressions', 'likes', 'replies', 'reposts', 'bookmarks', 'ratio_impr_followers', 'lowfan', 'outlier_ratio10', 'effective_10k_impr', 'created_at', 'text', 'collected_at']
- 低粉=126｜离群(ratio≥10)=11｜低粉且 impressions≥10k=1
- impressions 中位=96.0｜低粉子集中位=78.0
                    n  low  out  eff  med_impr
query_topic                                   
craft_skincare     23   18    2    1     421.0
ai_tools           25   22    0    0      37.0
dog_training       22   21    1    0      27.5
finance_hustle     22   19    1    0      29.0
illustration_game  21   21    6    0     142.0
language           25   25    1    0     240.0

## 4. 抖音（浏览器人工搜索，定性）
- 文件：`data/douyin.csv`｜采集：**2026-10-17 00:10–00:18** Asia/Shanghai
- n=**26**｜`qualified=是` **8**｜其中 `published_approx` 落在 2026-09/10 的达标 **4**（其余达标行发布时间更早或标注模糊，仅作案例）
- 口径说明：无公开播放；达标标记为采集脚本字段，**不可与 YouTube 播放/粉丝比直接比较**。点赞≠播放。

| keyword | n | qualified=是 | 粉丝<1万 | 点赞中位 | 粉丝中位 |
|---|---:|---:|---:|---:|---:|
| 家常菜 | 5 | 2 | 2 | 4760 | 119000 |
| 看房避坑 | 4 | 2 | 2 | 2686 | 9849 |
| 自行车保养 | 4 | 1 | 1 | 1668 | 63500 |
| 汽修 | 3 | 1 | 1 | 1245 | 47000 |
| AI工具 | 2 | 1 | 1 | 1626 | 1492501 |
| 折纸 | 2 | 1 | 1 | 3974 | 240230 |
| 日语入门 | 3 | 0 | 0 | 1892 | 38000 |
| 训犬 | 2 | 0 | 0 | 3780 | 850500 |
| 面试经验 | 1 | 0 | 0 | 5455 | 21000 |

达标样例（qualified=是，按 keyword）：
- [AI工具] Ai 工具评测｜粉 3003｜赞 1461｜藏 1688｜分享 126｜2026-05-26 16:53｜https://www.douyin.com/video/7644120893395832070
- [家常菜] 保持微笑！｜粉 373｜赞 4760｜藏 572｜分享 84｜约5月前｜https://www.douyin.com/video/7629855401353849061
- [家常菜] 流浪者｜粉 1｜赞 1084｜藏 145｜分享 93｜2026-10-05 03:11:19｜https://www.douyin.com/video/7692892349111153081
- [折纸] 锦程科学实验站｜粉 2460｜赞 5814｜藏 7958｜分享 1373｜2026-03-26 17:20｜https://www.douyin.com/video/7621491665975598543
- [汽修] 重庆渝车惠汽修｜粉 2957｜赞 1118｜藏 3045｜分享 342｜2026-10-15 17:42｜https://www.douyin.com/video/7696827783884883899
- [看房避坑] 婷婷在威海｜粉 754｜赞 3876｜藏 5060｜分享 4960｜2026-10-15 19:43｜https://www.douyin.com/video/7696858918483818225
- [看房避坑] 武汉库感说房｜粉 4698｜赞 1113｜藏 401｜分享 702｜2026-10-12 17:30｜https://www.douyin.com/video/7695325024391154998
- [自行车保养] 御驰单车｜粉 8641｜赞 1025｜藏 586｜分享 143｜2026-05-27 11:31｜https://www.douyin.com/video/7644409208046062757

## 5. 小红书（浏览器人工搜索，定性）
- 文件：`data/xiaohongshu.csv`｜采集：**2026-10-17 00:24–00:35** Asia/Shanghai
- n=**27**｜`qualified=是` **16**｜其中发布近似落在近30天（≥09-17）的达标 **2**
- **口径注意**：部分赞/藏为页面「x万」估整（如 1.1万→11000、10万→100000）；粉丝为主页精确值。无阅读量；**不可与 YouTube 播放或抖音点赞直接比绝对值**。

| keyword | n | qualified=是 | 粉丝<1万 | 点赞中位 | 粉丝中位 |
|---|---:|---:|---:|---:|---:|
| AI工具 | 4 | 3 | 3 | 6675 | 5633 |
| 护肤步骤 | 4 | 2 | 2 | 9164 | 95627 |
| 训犬 | 3 | 2 | 2 | 2059 | 900 |
| 副业 | 2 | 2 | 2 | 9560 | 1495 |
| 看房避坑 | 2 | 2 | 2 | 9604 | 304 |
| 日语入门 | 4 | 1 | 1 | 7639 | 29147 |
| 手工 | 2 | 1 | 1 | 31582 | 69989 |
| 折纸 | 2 | 1 | 1 | 62500 | 46784 |
| 自行车保养 | 2 | 1 | 1 | 2495 | 55720 |
| 面试经验 | 2 | 1 | 1 | 21538 | 46558 |

达标样例（qualified=是）：
- [AI工具] Alpha AI｜粉 9915｜赞 8547｜藏 11000｜藏/赞 1.29｜08-12｜更早｜https://www.xiaohongshu.com/explore/6a7c549c00000000250110f8
- [AI工具] 乐学的AI笔记｜粉 168｜赞 6798｜藏 5643｜藏/赞 0.83｜编辑于 08-22｜更早｜https://www.xiaohongshu.com/explore/6a89a86d0000000033008dae
- [AI工具] AI时倾｜粉 1351｜赞 6552｜藏 11000｜藏/赞 1.68｜09-22 广东｜近30天｜https://www.xiaohongshu.com/explore/6ab1a88f000000003303186b
- [副业] 法野.AI｜粉 2866｜赞 18000｜藏 22000｜藏/赞 1.22｜10-06 福建｜近30天｜https://www.xiaohongshu.com/explore/6ac4e5ae000000001203bf11
- [副业] 莎迪｜粉 125｜赞 1121｜藏 932｜藏/赞 0.83｜09-08｜更早｜https://www.xiaohongshu.com/explore/6a9fc943000000002503496f
- [手工] 嘻嘻哈哈｜粉 8320｜赞 1164｜藏 1043｜藏/赞 0.90｜05-25｜更早｜https://www.xiaohongshu.com/explore/6a13f575000000000702e500
- [折纸] 纸小晴｜粉 4422｜赞 25000｜藏 18000｜藏/赞 0.72｜07-05｜更早｜https://www.xiaohongshu.com/explore/6a4a29cd000000001100584d
- [护肤步骤] 是潘潘呐｜粉 255｜赞 1329｜藏 1090｜藏/赞 0.82｜06-26｜更早｜https://www.xiaohongshu.com/explore/6a3dfbb0000000001602782b
- [护肤步骤] 护肤日记｜粉 38｜赞 1116｜藏 1353｜藏/赞 1.21｜01-05｜更早｜https://www.xiaohongshu.com/explore/695b996e00000000220331ff
- [日语入门] Momo｜粉 98｜赞 1095｜藏 1141｜藏/赞 1.04｜05-05｜更早｜https://www.xiaohongshu.com/explore/69f9a60e0000000035031ea0
- [看房避坑] 避雷姐成长计划｜粉 468｜赞 18000｜藏 26000｜藏/赞 1.44｜编辑于 03-18｜更早｜https://www.xiaohongshu.com/explore/69b954ed000000001e00dabf
- [看房避坑] 遇安｜粉 141｜赞 1208｜藏 1114｜藏/赞 0.92｜06-17｜更早｜https://www.xiaohongshu.com/explore/6a326d91000000001003ec13
- [自行车保养] 公路车图鉴｜粉 6067｜赞 1799｜藏 2181｜藏/赞 1.21｜编辑于 05-25｜更早｜https://www.xiaohongshu.com/explore/6a0d0a3a00000000070221e4
- [训犬] 阿拉灵不灵（尴尬期中）｜粉 900｜赞 2059｜藏 1532｜藏/赞 0.74｜07-15｜更早｜https://www.xiaohongshu.com/explore/6a575d0d000000001603cec1
- [训犬] 得力爪鲜食🐾🐾｜粉 838｜赞 1210｜藏 1132｜藏/赞 0.94｜08-03｜更早｜https://www.xiaohongshu.com/explore/6a7088ca0000000011021c85
- [面试经验] 么凹猫｜粉 1472｜赞 2076｜藏 2163｜藏/赞 1.04｜08-04｜更早｜https://www.xiaohongshu.com/explore/6a71ae22000000002403f756

## 6. TikTok（浏览器人工搜索，定性）
- 文件：`data/tiktok.csv`｜采集：**2026-10-17 00:46–01:37** Asia/Shanghai（raw UTC 2026-10-16T16:46–17:37Z）
- n=**32**｜`qualified=是` **23**｜其中发布 ≥2026-09-16 的达标 **15**
- 有公开 **views**；保存率=saves/views。views 缺失 2 行。**不可与 YouTube 播放做跨平台绝对值比较**（分发池与抽样不同）。

| keyword | n | qualified=是 | 粉丝<1万 | 播放中位 | 粉丝中位 |
|---|---:|---:|---:|---:|---:|
| side hustle | 5 | 5 | 5 | 98100 | 3292 |
| interview tips | 4 | 4 | 4 | 130500 | 3165 |
| AI tools | 5 | 3 | 3 | 34600 | 4865 |
| apartment hunting | 3 | 3 | 3 | 12800 | 2040 |
| diy craft | 3 | 3 | 3 | 642300 | 7369 |
| bike maintenance | 2 | 2 | 2 | 610950 | 3262 |
| dog training | 3 | 1 | 1 | 98300 | 27800 |
| skincare | 3 | 1 | 1 | 425250 | 86700 |
| japanese lesson | 2 | 1 | 1 | 69950 | 17074 |
| origami | 2 | 0 | 0 | 153800 | 36300 |

达标样例（qualified=是）：
- [AI tools] @matt.elior｜粉 4865｜播 477400｜赞 27900｜藏 18176｜保存率 3.81%｜2026-10-12｜近30天｜https://www.tiktok.com/@matt.elior/video/7695584552596622599
- [AI tools] @olena.carter｜粉 3062｜播 24600｜赞 190｜藏 148｜保存率 0.60%｜2026-07-23｜更早｜https://www.tiktok.com/@olena.carter/video/7665599937417153805
- [AI tools] @evanbuild｜粉 4618｜播 24400｜赞 452｜藏 1｜保存率 0.00%｜2026-10-16｜近30天｜https://www.tiktok.com/@evanbuild/video/7697217076112510238
- [apartment hunting] @home.nest.living｜粉 470｜播 68600｜赞 2228｜藏 618｜保存率 0.90%｜2026-10-11｜近30天｜https://www.tiktok.com/@home.nest.living/video/7695467540063030558
- [apartment hunting] @kamyiah.withkeys｜粉 2040｜播 12800｜赞 677｜藏 246｜保存率 1.92%｜2026-09-22｜近30天｜https://www.tiktok.com/@kamyiah.withkeys/video/7688171237134126367
- [apartment hunting] @camila.tunoni｜粉 2842｜播 11100｜赞 444｜藏 91｜保存率 0.82%｜2026-09-02｜更早｜https://www.tiktok.com/@camila.tunoni/video/7680958331212582152
- [bike maintenance] @ddzxclzevbg｜粉 951｜播 768500｜赞 4401｜藏 905｜保存率 0.12%｜2026-10-08｜近30天｜https://www.tiktok.com/@ddzxclzevbg/video/7694119296183602446
- [bike maintenance] @gugoiss_ebikes｜粉 5573｜播 453400｜赞 3518｜藏 1575｜保存率 0.35%｜2026-09-10｜更早｜https://www.tiktok.com/@gugoiss_ebikes/video/7683483399062916383
- [diy craft] @tahminascraft_35｜粉 7369｜播 1900000｜赞 60600｜藏 23920｜保存率 1.26%｜2026-10-09｜近30天｜https://www.tiktok.com/@tahminascraft_35/video/7694695519758650656
- [diy craft] @hazelmake｜粉 1276｜播 642300｜赞 95000｜藏 9328｜保存率 1.45%｜2026-10-05｜近30天｜https://www.tiktok.com/@hazelmake/video/7693329349755292942
- [diy craft] @craftyhome04｜粉 7692｜播 25900｜赞 12400｜藏 6135｜保存率 23.69%｜2026-09-02｜更早｜https://www.tiktok.com/@craftyhome04/video/7680857502728146198
- [dog training] @pomtoro｜粉 7501｜播 45000｜赞 4762｜藏 836｜保存率 1.86%｜2026-09-23｜近30天｜https://www.tiktok.com/@pomtoro/video/7688853532287585566
- [interview tips] @softlifecfo｜粉 4565｜播 291900｜赞 41400｜藏 23763｜保存率 8.14%｜2026-10-01｜近30天｜https://www.tiktok.com/@softlifecfo/video/7691484528925232414
- [interview tips] @ayarosemc｜粉 1304｜播 198600｜赞 21700｜藏 11069｜保存率 5.57%｜2026-09-21｜近30天｜https://www.tiktok.com/@ayarosemc/video/7687792578137214222
- [interview tips] @aubreyyydevries｜粉 1766｜播 62400｜赞 7167｜藏 4078｜保存率 6.54%｜2026-09-18｜近30天｜https://www.tiktok.com/@aubreyyydevries/video/7686682613565623583
- [interview tips] @tytherecruiterguy｜粉 7231｜播 47500｜赞 3080｜藏 2603｜保存率 5.48%｜2026-09-02｜更早｜https://www.tiktok.com/@tytherecruiterguy/video/7680758979223375118
- [japanese lesson] @k_lyn.__｜粉 9448｜播 44500｜赞 5102｜藏 2532｜保存率 5.69%｜2026-06-08｜更早｜https://www.tiktok.com/@k_lyn.__/video/7648792941808422162
- [side hustle] @gigissidehustle｜粉 3610｜播 1300000｜赞 49600｜藏 53889｜保存率 4.15%｜2026-10-10｜近30天｜https://www.tiktok.com/@gigissidehustle/video/7694901672782384397
- [side hustle] @zachhh.mp4｜粉 3292｜播 462100｜赞 20500｜藏 17554｜保存率 3.80%｜2026-09-18｜近30天｜https://www.tiktok.com/@zachhh.mp4/video/7686904096200117512
- [side hustle] @gracesidehustle8｜粉 3070｜播 98100｜赞 5137｜藏 3626｜保存率 3.70%｜2026-07-14｜更早｜https://www.tiktok.com/@gracesidehustle8/video/7662183098909510925
- [side hustle] @side.hustle.sam｜粉 1497｜播 38500｜赞 1805｜藏 1698｜保存率 4.41%｜2026-10-10｜近30天｜https://www.tiktok.com/@side.hustle.sam/video/7695188908610489613
- [side hustle] @creating.kj｜粉 6409｜播 32600｜赞 1632｜藏 2076｜保存率 6.37%｜2026-09-21｜近30天｜https://www.tiktok.com/@creating.kj/video/7687804994321386785
- [skincare] @blemishdermlab｜粉 868｜播 411800｜赞 1089｜藏 181｜保存率 0.04%｜2026-09-11｜更早｜https://www.tiktok.com/@blemishdermlab/video/7684088913643752717

## 7. Instagram（浏览器关键词搜索，反证为主）
- 文件：`data/instagram.csv`｜采集：**2026-10-17 01:46–01:54** Asia/Shanghai（raw UTC 2026-10-16T17:46–17:54Z）
- n=**36**｜`qualified=是` **3**（skincare / dogtraining / sidehustle 各 1）｜近30天达标 **2**
- 粉丝中位 **160000**｜≥1万粉占比 **86.1%**
- **方法注记**：标签热门页 GraphQL 失败，改用关键词搜索；样本仍严重偏向大号 → 主要作**反证**（新号难进热门观感），强度 **D/C**。无播放字段；**不可与 YT/TikTok 播放比绝对赞**。

| keyword | n | qualified=是 | 粉丝<1万 | 点赞中位 | 粉丝中位 |
|---|---:|---:|---:|---:|---:|
| #dogtraining | 4 | 1 | 1 | 410150 | 176500 |
| #sidehustle | 4 | 1 | 1 | 24100 | 24650 |
| #skincare | 4 | 1 | 1 | 14100 | 100100 |
| #bikemaintenance | 4 | 0 | 0 | 130600 | 227000 |
| #learnjapanese | 4 | 0 | 0 | 44050 | 56250 |
| #origami | 4 | 0 | 0 | 72300 | 186000 |
| #aitools | 3 | 0 | 0 | 53700 | 171000 |
| #apartmenthunting | 3 | 0 | 2 | 216 | 2187 |
| #diy | 3 | 0 | 0 | 1100000 | 637000 |
| #interviewtips | 3 | 0 | 0 | 54100 | 385000 |

达标样例（仅 3 条）：
- [#skincare] @that.gurllisa_｜粉 1991｜赞 18500｜2026-09-12｜更早或更旧｜https://www.instagram.com/p/Dc-ek_wSQrX/
- [#dogtraining] @malwhodoesigp｜粉 2130｜赞 104600｜2026-09-16｜近30天｜https://www.instagram.com/p/DdW30ySJgeV/
- [#sidehustle] @gwen3edit｜粉 5744｜赞 21300｜2026-09-23｜近30天｜https://www.instagram.com/p/DdohszoxQqh/

