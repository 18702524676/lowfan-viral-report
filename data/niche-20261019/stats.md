# 细分领域统计（2026-10-19，不含B站）

## 口径
- 打标：niche/tag_and_stats.py 的 RULES，按作品标题（X 为正文）正则匹配，自上而下首个命中；未命中=未归类。规则粗糙，可在 niche/tagged.csv 逐条复核。
- 样本不足：某平台某领域账号数<3 或作品数<15。
- 指标：YouTube/TikTok/Instagram=播放；X=曝光（impression，非视频播放）；抖音/小红书=互动量（赞+评+藏+转，缺失记0）。
- 低粉爆款：粉丝<1万 且 播放≥10×粉丝（抖音/小红书：互动≥1×粉丝）；粉丝0按1。
- 前3集中度：该领域该平台最高3个账号指标之和÷总和。
- 去重：同平台同作品只计一次（YouTube 合并 style 切题样本与 track 科普视频样本）。
- 未纳入：track-research 的 douyin_profiles/xiaohongshu_profiles/tiktok_profiles/instagram_profiles 无标题列，无法按题材打标。

## youtube

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|127(70)|567|953|255|21,439,081 [Zack D. Films](https://youtu.be/bZoR8A2znpo)|33|0.98|足|
|人体/医学|24(14)|95|4,249|168|13,402,223 [Zack D. Films](https://youtu.be/FaZGpRV4RPY)|4|0.983|足|
|尺度与数据对比|6(3)|78|16,892|5,785|4,244,304 [Best of World 3D](https://youtu.be/qx849WxoKsQ)|10|0.904|足|
|建筑/基建工程|34(22)|64|821|668|1,049,564 [RJMBricksToo](https://youtu.be/sEmqB9PZ3rg)|10|0.755|足|
|机械原理|28(17)|59|1,096|1,039|8,541,561 [kekemorning](https://youtu.be/g85IMgI82IQ)|2|0.976|足|
|材料与制造工艺|21(9)|58|2,300|2,074|227,901 [How It's Made Archive](https://youtu.be/taU2ZRwdiHU)|6|0.81|足|
|动植物/生物|17(13)|50|130|93|12,955,677 [Zack D. Films](https://youtu.be/phV94hbwFo8)|3|1.0|足|
|汽车/发动机|22(18)|47|185|155|26,097 [kekemorning](https://youtu.be/LQskK7UL21I)|11|0.78|足|
|天文|18(12)|45|963|135|28,389,881 [Beyond the Observable Universe](https://youtu.be/ycgEOES7GRI)|0|1.0|足|
|物理/数学原理(考试向)|20(13)|42|558|301|11,313,909 [Zack D. Films](https://youtu.be/mIHafmS6fYc)|5|0.985|足|
|家电与日常物品|22(11)|40|834|238|4,310,319 [Zack D. Films](https://youtu.be/nnyHzQZOfaQ)|2|0.952|足|
|电力/电子/芯片|21(16)|37|830|707|888,264 [Redknot-乔红](https://youtu.be/yF2BY8kQfyo)|8|0.99|足|
|发明史|19(15)|35|28|17|10,046,567 [Zack D. Films](https://youtu.be/XFY7-td3LA8)|4|0.998|足|
|航空航天/火箭|17(14)|31|514|405|322,797 [Global Airport Parking](https://youtu.be/iLPcwA1JDV4)|6|0.905|足|
|地理/地球/气候|14(11)|31|319|188|7,529,041 [Beyond the Observable Universe](https://youtu.be/rG_MpsZ8hYc)|5|0.999|足|
|微观世界|2(1)|2|5,017|318|9,716 [子疯实验室](https://youtu.be/G2oq2xm2R_0)|0|1.0|样本不足|

低粉爆款代表：
- 机械原理：jane fu（粉85）3,622 https://youtu.be/PI6APEsZhzo 《浮动式球阀，三维动画仿真工作原理，直观易懂 标清 Segment 1》 2018-12-09
- 机械原理：QubitMind（粉82）2,670 https://youtu.be/MAHh23mVty4 《Pascal’s Law Explained in 10 Seconds ⚡ | Hydraulic Lift | Ph》 2026-09-09
- 航空航天/火箭：Global Airport Parking（粉110）322,797 https://youtu.be/iLPcwA1JDV4 《Old Global Airport Parking: How it Works》 2013-10-24
- 航空航天/火箭：Lego Pilot（粉5,830）154,477 https://youtu.be/nbKyMK6Mseo 《Engines of the LEGO Technic Airplane Multi-engine Piston HK-》 2026-05-05
- 未归类：Unreal in 5 Minutes!（粉4,240）49,068 https://youtu.be/I3uiXmGTJMw 《Set up ANIMATIONS for Beginners in Unreal Engine 5!》 2025-07-12
- 未归类：Mr. Integral（粉591）8,412 https://youtu.be/mmC_ozQmWQc 《How Do Electrons Walk Through a Wall?》 2026-10-09
- 发明史：MamaPapaBrooks（粉1,260）343,826 https://youtu.be/FuHQhGqZvY0 《The Invention of Money and Currency》 2011-03-30
- 发明史：Ian Ure（粉27）20,757 https://youtu.be/39XSIzLuzKg 《Rich Picture Rebooted, Rewired & Reinvented...》 2014-01-06
- 物理/数学原理(考试向)：Live īnfra（粉966）578,104 https://youtu.be/tGFhNQ5eY4Y 《How Cartoons were made in the 1950s | Mickey Mouse | Stop An》 2022-06-09
- 物理/数学原理(考试向)：QubitMind（粉82）25,794 https://youtu.be/nzFdqRnPxek 《AC Generator Explained ⚡ | Electromagnetic Induction & Worki》 2026-09-16
- 家电与日常物品：Sewers Delight（粉636）396,504 https://youtu.be/zqRvljnNLFk 《How a Sewing Machine Works via animation》 2016-11-25
- 家电与日常物品：Curious Fox（粉23）944 https://youtu.be/wlBsLr8uEQM 《Why a Pen Can’t Tap Your Phone but a Finger Can #shorts  #sc》 2026-10-13
- 动植物/生物：Bright Anatomy（粉289）5,971 https://youtu.be/OGUq9xCbaDU 《Hammerhead Shark Life Cycle: From Embryo to Adult | 3D Anato》 2026-08-28
- 动植物/生物：Fibrox3d（粉4）76 https://youtu.be/lVOKG1KpWss 《Plant As-Built Modeling from 3D Laser Scanning & Point Cloud》 2026-05-02
- 电力/电子/芯片：QubitMind（粉82）3,348 https://youtu.be/n2roFhA8kUw 《How Does a Wind Turbine Generate Electricity? 🌬️⚡ | Wind Ene》 2026-09-17
- 电力/电子/芯片：Angelus（粉196）2,641 https://youtu.be/b-Xkw_u373M 《How Does a Battery Actually Work? (Animated Science)》 2026-08-29
- 汽车/发动机：Mr. Integral（粉591）18,711 https://youtu.be/BVuTvJvgdgw 《How Does Tesla's Roadster Fly Over Cars?》 2026-10-17
- 汽车/发动机：Caught The Moment（粉145）2,128 https://youtu.be/ZWyv4Lq1k2Y 《This Saturn V Test Stand Blasted Engine Fire Sideways in Ala》 2026-10-16
- 建筑/基建工程：How It's Made Archive（粉9,660）235,514 https://youtu.be/YrJas4_L4Wo 《How It's Made - Construction Wood》 2016-08-15
- 建筑/基建工程：DLT Solutions（粉1,270）229,743 https://youtu.be/F7gktaMblLY 《Laser Scanning for As-Built Drawings》 2016-10-07
- 人体/医学：Why Though?（粉18）1,302 https://youtu.be/4a3TtBZoSns 《Why Do We Dream? The Weird Science Explained!》 2026-09-14
- 人体/医学：Adam Explained（粉2）448 https://youtu.be/2TWZUkDPE7A 《appendicitis, appendix surgery, appendectomy, human anatomy,》 2026-09-17
- 材料与制造工艺：How It's Made Archive（粉9,660）227,901 https://youtu.be/taU2ZRwdiHU 《How It's Made - Chipboard Office Furniture》 2016-08-13
- 材料与制造工艺：How It's Made Archive（粉9,660）136,475 https://youtu.be/CS5svagJGs0 《How It's Made - Gold Rings》 2016-08-23
- 地理/地球/气候：CRACK EXAM WITH FUN（粉249）2,908 https://youtu.be/fxgPh4TJGdc 《How Natural Levees Form: River Flood Dynamics ExplainedNatur》 2026-10-01
- 地理/地球/气候：Curious Fox（粉23）1,032 https://youtu.be/JV4198yzKw8 《Why does a tilted ship roll back upright? 🚢 #howitworks #sci》 2026-10-13
- 尺度与数据对比： ORIGINAL DATA（粉9,240）2,646,274 https://youtu.be/78Zr92ZlvY4 《Sea Monsters Size Comparison | Fish Size Comparison | 3d Ani》 2023-08-12
- 尺度与数据对比：Hero Manager Data Verse（粉5,030）542,089 https://youtu.be/rU4Ct-_nEno 《All Hulks Size Comparison | 3D Animation (All Live Action Hu》 2026-08-02

## tiktok

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|7(4)|65|7,879|1,752|27,500,000 [howitliterallyworks(头部)](https://www.tiktok.com/@howitliterallyworks/video/7287245860465806623)|7|0.998|足|
|汽车/发动机|3(2)|13|3,098|2,458|1,700,000 [engineeringexplained3](https://www.tiktok.com/@engineeringexplained3/video/7346633503590665473)|3|1.0|样本不足|
|电力/电子/芯片|1(1)|2|14,341|14,341|25,100 [team.engineering.explain](https://www.tiktok.com/@team.engineering.explain/video/7627135273759034638)|0|1.0|样本不足|
|动植物/生物|2(2)|2|5,939|5,939|10,300 [team.engineering.explain](https://www.tiktok.com/@team.engineering.explain/video/7627867029403389197)|0|1.0|样本不足|
|人体/医学|1(0)|1|12,100,000|—|12,100,000 [howitliterallyworks(头部)](https://www.tiktok.com/@howitliterallyworks/video/7289198906519457054)|0|1.0|样本不足|
|发明史|1(1)|1|17,700|17,700|17,700 [team.engineering.explain](https://www.tiktok.com/@team.engineering.explain/video/7625650020963880222)|0|1.0|样本不足|

低粉爆款代表：
- 未归类：howitworks767（粉209）33,100 https://www.tiktok.com/@howitworks767/video/7353457606780046638 《This is how Pharrel Williams produced Finna》 
- 未归类：howitworks767（粉209）28,100 https://www.tiktok.com/@howitworks767/video/7350740058560793902 《How does a gas turbine work?》 2024-3-27
- 汽车/发动机：engineeringexplained3（粉1,359）1,700,000 https://www.tiktok.com/@engineeringexplained3/video/7346633503590665473 《What Is Double Clutching- Don't Granny Shift!》 2024-3-16
- 汽车/发动机：team.engineering.explain（粉3,153）277,700 https://www.tiktok.com/@team.engineering.explain/video/7626755474066607391 《How Audi Eliminated Turbo Lag Electric Supercharger!》 4-9(2026)

## instagram

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|7(1)|71|5,652|1,682|1,600,000 [sscientific.girl](https://www.instagram.com/sscientific.girl/reel/DejwUjQORIs/)|9|0.982|足|
|汽车/发动机|2(0)|2|764,500|—|1,400,000 [engineeringexplained(头部)](https://www.instagram.com/engineeringexplained/reel/DbdbcYuhQGU/)|0|1.0|样本不足|
|机械原理|1(1)|1|3,402|3,402|3,402 [madetoworkhq](https://www.instagram.com/madetoworkhq/reel/DemXPLZP2Yd/)|1|1.0|样本不足|

低粉爆款代表：
- 机械原理：madetoworkhq（粉6）3,402 https://www.instagram.com/madetoworkhq/reel/DemXPLZP2Yd/ 《Hydraulic ram: the pump with no motor》 2026-10-17
- 未归类：madetoworkhq（粉6）3,132 https://www.instagram.com/madetoworkhq/reel/Demd3ywtq7o/ 《What's inside the box on a wind turbine?》 2026-10-17
- 未归类：madetoworkhq（粉6）2,457 https://www.instagram.com/madetoworkhq/reel/DenSLYTvDs4/ 《》 

## douyin

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|7(3)|30|1,622|28|32,000 [珂姬与科技(头部)](https://www.douyin.com/video/7617382133341965587)|0|0.955|足|
|微观世界|2(2)|21|106|106|17,527 [显微镜下(QSNM1111)](https://www.douyin.com/video/7482013230827703610)|1|1.0|样本不足|
|机械原理|5(2)|20|60|22|774,663 [机械视界(头部)](https://www.douyin.com/video/7656268481386465203)|1|1.0|足|
|建筑/基建工程|4(2)|9|68|36|371,000 [机械视界(头部)](https://www.douyin.com/video/7621436532246826250)|0|1.0|样本不足|
|家电与日常物品|4(2)|8|666|994|90,000 [珂姬与科技(头部)](https://www.douyin.com/video/7448572123020315919)|0|0.995|样本不足|
|材料与制造工艺|2(1)|4|9,480|176,573|176,573 [机械原理动画分享](https://www.douyin.com/video/7622115054129200070)|1|1.0|样本不足|
|汽车/发动机|3(1)|3|666|187|1,249 [机械视界(头部)](https://www.douyin.com/video/7694945627188235556)|0|1.0|样本不足|
|电力/电子/芯片|3(0)|3|6,344|—|15,442 [机械科普君](https://www.douyin.com/video/7681297690235243827)|0|1.0|样本不足|
|动植物/生物|2(2)|2|638|638|1,208 [显微镜下(QSNM1111)](https://www.douyin.com/video/7640274962930261690)|0|1.0|样本不足|
|航空航天/火箭|1(1)|1|84|84|84 [机械原理动画演示](https://www.douyin.com/video/7560938235728383286)|0|1.0|样本不足|
|人体/医学|1(0)|1|723|—|723 [机械视界(头部)](https://www.douyin.com/video/7696068615874809124)|0|1.0|样本不足|

低粉爆款代表：
- 机械原理：机械原理动画分享（粉3,674）140,597 https://www.douyin.com/video/7616138812720222570 《[置顶]交替往复#直线运动机构 #机械原理动图》 2026-03-12 07:08
- 材料与制造工艺：机械原理动画分享（粉3,674）176,573 https://www.douyin.com/video/7622115054129200070 《[置顶]#圆管扩口机 #机械原理动图 #还有这种操作》 2026-03-28 09:39
- 微观世界：显微镜下(QSNM1111)（粉6,600）17,527 https://www.douyin.com/video/7482013230827703610 《[置顶]槟榔放大500倍后给好奇的老铁们看看？》 2025-03-15 20:32

## xiaohongshu

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|8(3)|37|148|100|981 [原理搞不懂](https://www.xiaohongshu.com/explore/6a9b8be90000000029013e6c)|0|0.492|足|
|发明史|2(1)|13|3,280|428|109,721 [解码视界](https://www.xiaohongshu.com/explore/69e2054f000000001a032566)|1|1.0|样本不足|
|微观世界|2(1)|11|470|208|55,000 [微观之眼(头部)](https://www.xiaohongshu.com/explore/6a9bc88e000000000b00199e)|0|1.0|样本不足|
|机械原理|3(1)|9|142|32|1,002 [泵阀之家](https://www.xiaohongshu.com/explore/69a17b28000000001d011ac6)|0|1.0|样本不足|
|家电与日常物品|4(1)|6|320|4,485|4,485 [科普先生五月](https://www.xiaohongshu.com/explore/6ac3a0ce00000000150007cd)|1|0.954|样本不足|
|汽车/发动机|3(1)|4|509|262|2,240 [解码视界](https://www.xiaohongshu.com/explore/6a28dcdc000000001603c00f)|0|1.0|样本不足|
|航空航天/火箭|2(0)|2|365|—|392 [科普君乔木](https://www.xiaohongshu.com/explore/6ad3454d0000000014039c52)|0|1.0|样本不足|
|人体/医学|1(1)|1|74|74|74 [微观小尘](https://www.xiaohongshu.com/explore/6a953d0e000000000a00b770)|0|1.0|样本不足|
|电力/电子/芯片|1(0)|1|4,015|—|4,015 [微观之眼(头部)](https://www.xiaohongshu.com/explore/6aaa047f000000002601c94d)|0|1.0|样本不足|
|动植物/生物|1(0)|1|232|—|232 [微观之眼(头部)](https://www.xiaohongshu.com/explore/6a79c08c000000003301ca78)|0|1.0|样本不足|

低粉爆款代表：
- 家电与日常物品：科普先生五月（粉2,882）4,485 https://www.xiaohongshu.com/explore/6ac3a0ce00000000150007cd 《一口气讲完过山车的工作原理》 2026-10-05
- 发明史：原理搞不懂（粉3,406）8,041 https://www.xiaohongshu.com/explore/6a9a849c000000001203404e 《恭喜你，成功发明了涡扇发动机》 2026-09-04(页面显示09-04)

## x

|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|
|-|-|-|-|-|-|-|-|-|
|未归类|35(30)|82|64|48|333,047 [michaelologist](https://x.com/michaelologist/status/2054760642175815964)|7|0.945|足|
|人体/医学|9(8)|22|32|32|5,710 [kaiaRowena](https://x.com/kaiaRowena/status/2107003418099470577)|10|0.928|足|
|汽车/发动机|15(15)|15|0|0|36 [InsideXScience](https://x.com/InsideXScience/status/2047911209035596027)|1|0.975|足|
|机械原理|4(4)|13|65|65|6,215 [guanmo_ai](https://x.com/guanmo_ai/status/2110937526315655282)|0|0.992|样本不足|
|材料与制造工艺|3(3)|7|44|44|130 [xingor_dev](https://x.com/xingor_dev/status/2107674342238867888)|0|1.0|样本不足|
|动植物/生物|4(3)|5|50|40|50,379 [xingor_dev](https://x.com/xingor_dev/status/2104170801205567960)|1|1.0|样本不足|
|家电与日常物品|4(4)|4|112|112|5,609 [v_serbulenko](https://x.com/v_serbulenko/status/2097274455483371764)|1|1.0|样本不足|
|物理/数学原理(考试向)|3(3)|4|8|8|16 [hpjqm93191651](https://x.com/hpjqm93191651/status/2104783475962216564)|0|1.0|样本不足|
|地理/地球/气候|3(3)|4|51|51|107 [xingor_dev](https://x.com/xingor_dev/status/2107348746065658247)|0|1.0|样本不足|
|微观世界|1(1)|2|56|56|81 [xingor_dev](https://x.com/xingor_dev/status/2107674344604541112)|0|1.0|样本不足|
|航空航天/火箭|2(2)|2|84|84|114 [xingor_dev](https://x.com/xingor_dev/status/2106312108908671294)|0|1.0|样本不足|
|天文|1(1)|1|2,498|2,498|2,498 [xingor_dev](https://x.com/xingor_dev/status/2103087892524359903)|0|1.0|样本不足|

低粉爆款代表：
- 人体/医学：bhakta_himel（粉11）1,629 https://x.com/bhakta_himel/status/2069416433298427929 《😱 A living worm inside your body for YEARS?  See how a tapew》 2026-06-23
- 人体/医学：InsideXScience（粉1）130 https://x.com/InsideXScience/status/2046471213674033414 《What Happens Inside Your Body After Eating Potato? 🥔😱 | 3D A》 2026-04-21
- 未归类：michaelologist（粉1,613）333,047 https://x.com/michaelologist/status/2054760642175815964 《this video fries me every time i see it "how does it work" m》 2026-05-14
- 未归类：xingor_dev（粉548）17,750 https://x.com/xingor_dev/status/2104852135326453990 《我最近在试一个可以减少 AI 视频生成抽卡的工作流：  Blender Previs + Seedance 2.5  o》 2026-09-29
- 动植物/生物：xingor_dev（粉548）50,379 https://x.com/xingor_dev/status/2104170801205567960 《a realistic underwater fish simulation with Opus 5.5 + @thre》 2026-09-27
- 家电与日常物品：RehmanAhmed0（粉6）64 https://x.com/RehmanAhmed0/status/2082396970606608717 《Bring your ideas to life with AI-powered cartoon animations 》 2026-07-29
- 汽车/发动机：InsideXScience（粉1）36 https://x.com/InsideXScience/status/2047911209035596027 《Nimesulide: How It Works Inside Your Body 💊🔥 | Full Pharmaco》 2026-04-25
