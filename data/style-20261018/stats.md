# stats（2026-10-18 生成，scripts/compute_stats.py）

## 公式
- 中位数/最高值：候选组合内所有已采作品的播放量（X 为 impression_count）。
- 播放/粉丝倍数：每条作品 播放÷该账号当前粉丝（粉丝=0 的剔除），取中位数。注意粉丝是采集日数值，老视频发布时粉丝更少，倍数偏低估。
- 低粉爆款：账号粉丝<10,000 且 播放 ≥ 10×粉丝（粉丝为0时按1算）的作品数。
- 头部前3集中度：组合内播放量最高的3个账号播放总和 ÷ 组合内全部账号播放总和。
- 点赞率：点赞÷播放 的中位数。
- 平台之间不混比。
- youtube_ontopic：仅保留标题命中原理类关键词正则（how…work/inside/made/explain/engine/machine/原理/内部/结构/怎么/机械/制造/工程/动画 等，见脚本 TOP）的作品，用于剔除频道里的无关视频；仍是近似。

## youtube

|候选|风格|题材|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉爆款(账号)|前3集中度|点赞率|
|-|-|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|日常物品/家电内部结构|10(6)|195|394|888,264|0.174|255|3(2)|0.984|0.0107|
|C02|蓝图/工程制图|机械原理/发明|10(6)|158|850|8,541,561|0.655|1,010|17(5)|0.98|0.0146|
|C03|等距信息图|供应链/从A到B工业流程|10(6)|192|1,927|2,996,987|0.248|2,184|10(4)|0.835|0.0271|
|C04|显微叙事|人体/材料微观原理|10(4)|189|1,561|7,612,986|0.108|130|1(1)|0.963|0.0049|
|C05|移轴微缩|城市基础设施如何运转(水电地铁垃圾)|10(6)|157|231|57,945|0.055|178|13(4)|0.758|0.0139|
|C06|卫星简报|超级工程/基建建设|10(6)|200|756|93,026|0.087|392|11(2)|0.615|0.0143|
|C07|白板讲解|物理/工程原理|9(5)|162|85|16,969|0.106|46|5(4)|0.869|0.0087|
|C08|数据实物化|能耗/尺度对比原理|10(6)|199|2,211|4,244,304|0.497|1,244|16(3)|0.9|0.0066|
|C09|点云测绘|建筑/古迹结构原理|10(6)|172|323|272,068|0.206|140|12(4)|0.948|0.0103|
|C10|科幻全息|前沿科技原理(芯片/核聚变/火箭)|10(6)|174|529|247,541|0.269|218|8(3)|0.936|0.0126|
|C11|50s扁平卡通(复古教育片口吻)|家电/日常用品原理|10(6)|193|372|472,348|0.806|196|15(6)|0.868|0.0129|
|C12|积木玩具|建造/机械原理(儿童向)|10(6)|164|1,166|1,049,564|0.373|763|6(4)|0.871|0.009|
|C13|低多边形等距|交通/物流系统怎么运转|10(6)|181|902|1,275,353|0.421|202|10(3)|0.909|0.0114|
|C14|移轴微缩|工厂/生产线微缩巡游|10(6)|161|198|504,784|1.0|71|26(6)|0.991|0.0066|
|C15|综艺节奏扁平|发明演化史(某物进化史)|10(6)|155|1,256|343,826|0.196|130|9(2)|0.913|0.0156|
|C16|铜版画|古代/维多利亚机械与发明原理|10(6)|171|172|169,674|0.092|23|5(1)|0.984|0.0178|
|C17|AI生产 3D原理(跨平台AI制作教程/需求)|用AI做3D原理动画|10(6)|186|1,619|161,372|0.281|952|1(1)|0.718|0.0178|

低粉爆款示例：
- C01 科普小火箭（粉1,790）播放738,181 https://youtu.be/rNq-R98Xz34 《靖康之恥究竟有多恥？皇后被迫一天接客上百人，嬪妃公主被明碼標價公開售賣！【科普小火箭】》
- C01 jane fu（粉85）播放3,622 https://youtu.be/PI6APEsZhzo 《浮动式球阀，三维动画仿真工作原理，直观易懂 标清 Segment 1》
- C01 科普小火箭（粉1,790）播放32,925 https://youtu.be/rn_82m3Om9U 《世界上最奇特的14種章魚，誰能想到，章魚的世界原來如此奇妙！【科普小火箭】》
- C02 Ian Ure（粉27）播放20,757 https://youtu.be/39XSIzLuzKg 《Rich Picture Rebooted, Rewired & Reinvented...》
- C02 Miko（粉342）播放34,353 https://youtu.be/Q41a9A_-LZ4 《Ranking Doomslayer armors》
- C02 Miko（粉342）播放30,366 https://youtu.be/-pqUXEmAJcs 《Ranking Every Demon Slayer Season & Movie》
- C03 Live īnfra（粉966）播放578,104 https://youtu.be/tGFhNQ5eY4Y 《How Cartoons were made in the 1950s | Mickey Mouse | Stop Animation | Optical Il》
- C03 Zaid A（粉7,560）播放2,996,987 https://youtu.be/rzSOiSyZIIk 《The Secret Trick Animators Hid in LEGO Batman #cg #lego》
- C03 Ben Diagi（粉160）播放3,994 https://youtu.be/Tl599PBpW7w 《Isometric animation》
- C04 Mr.Origin 🌍（粉1,180）播放31,682 https://youtu.be/qzSGjCAL9Hs 《The secret power of a Tesla coil on leaves 🔋🌿 #teslacoil #science #experiment》
- C05 MyInfra App（粉1）播放810 https://youtu.be/nku7W2DfoG8 《Infrastructure Development Animated》
- C05 Illustrated System（粉5）播放1,014 https://youtu.be/_ZNsfJoFPdo 《Why Southeast Asia's haze is so bad: in Indonesia, the ground itself is burning》
- C05 Illustrated System（粉5）播放844 https://youtu.be/xWxB2lFEZuw 《How does a record player work?》
- C06 NextGenX Megaprojects（粉459）播放93,026 https://youtu.be/rg45Ih0IZ3U 《How China Built 20,000m Mountain Tunnels That Shocked the World (Full Process)》
- C06 Caught The Moment（粉145）播放17,616 https://youtu.be/fBqY07b7Vh4 《BOLTED TO THE GROUND》
- C06 NextGenX Megaprojects（粉459）播放27,167 https://youtu.be/CFfSCHG5lVI 《How Saudi Arabia's Impossible $8.8 Trillion NEOM Collapsed》
- C07 LolliXan（粉841）播放16,969 https://youtu.be/RZS9g80-0Vs 《Roar of a T-rex (Jurassic World Dominion)》
- C07 Lammy Titus（粉19）播放362 https://youtu.be/3S8cpL4Dz34 《environment infographics》
- C07 Science-Up（粉28）播放520 https://youtu.be/Hh891T8P-lQ 《What is Science? | Whiteboard Animation Video | Science-Up》
- C08  ORIGINAL DATA（粉9,240）播放2,646,274 https://youtu.be/78Zr92ZlvY4 《Sea Monsters Size Comparison | Fish Size Comparison | 3d Animation Comparison》
- C08  ORIGINAL DATA（粉9,240）播放1,002,979 https://youtu.be/-53YFIDjW7o 《Most EXPENSIVE Car Of Famous Football Players $ 36,000,000》
- C08 Hero Manager Data Verse（粉5,030）播放542,089 https://youtu.be/rU4Ct-_nEno 《All Hulks Size Comparison | 3D Animation (All Live Action Hulks)》
- C09 DLT Solutions（粉1,270）播放229,743 https://youtu.be/F7gktaMblLY 《Laser Scanning for As-Built Drawings》
- C09 Coast 2 Coast（粉36）播放5,024 https://youtu.be/y3MZaYvvLdg 《UAV Technical Surveys》
- C09 Coast 2 Coast（粉36）播放3,829 https://youtu.be/kHNAl6QjyF0 《Steam Plant Exterior & Interior 3D Rendering》
- C10 有志科普（粉12）播放1,248 https://youtu.be/vbl_dk7ceEg 《材料科普实验室-硝酸铵 #制作过程 #实验 #趣味实验 #硝酸铵》
- C10 有志科普（粉12）播放572 https://youtu.be/1hZj_3qhefU 《芯片制造过程原理》
- C10 Made & Explained（粉3）播放133 https://youtu.be/m8sAIxnoQxs 《The History of the iPhone》
- C11 future seeir（粉224）播放141,143 https://youtu.be/ye0vTIK7Ckw 《NEWEST CARS (cars of the future cartoon)》
- C11 Friedrich Moore（粉453）播放24,859 https://youtu.be/f6vLdM1G0Bo 《Big Boy: Presented By Robert Montgomery 1954 Educational Documentary WDTVLIVE42 》
- C11 Sherry Retro（粉119）播放6,156 https://youtu.be/c6Zu3oMCMYg 《A 1950s commercial for the 1954 RCA air conditioner.》
- C12 Sewers Delight（粉636）播放396,504 https://youtu.be/zqRvljnNLFk 《How a Sewing Machine Works via animation》
- C12 Scowen On（粉1,250）播放36,141 https://youtu.be/cxHJ99wrKSw 《Introduction to LEGO® Technic Power Functions: Motors, Gears, Switches, Racks & 》
- C12 Lego Pilot（粉5,830）播放154,477 https://youtu.be/nbKyMK6Mseo 《Engines of the LEGO Technic Airplane Multi-engine Piston HK-10》
- C13 Global Airport Parking（粉110）播放322,797 https://youtu.be/iLPcwA1JDV4 《Old Global Airport Parking: How it Works》
- C13 SOUAirport（粉468）播放154,102 https://youtu.be/grdE8-Gy8CA 《Get on board... to the slopes | Southampton Airport》
- C13 Global Airport Parking（粉110）播放33,393 https://youtu.be/Sziq6mgk-nc 《Global Airport Parking: How it Works》
- C14 Tiny Assembly Line（粉0）播放555 https://youtu.be/n7g4J4YRO58 《Triumph Just Unveiled the Bonneville T40, So Our Tiny Crew Built a Bonneville》
- C14 Tiny Assembly Line（粉0）播放252 https://youtu.be/Lze4xosa1hA 《Honda Rebel 500 2027 Gets E-Clutch! Watch Robots Build It》
- C14 Ken Fung（粉1）播放182 https://youtu.be/HfE86QJeZGE 《HD Tilt-shift video #3 (Mongkok, Hong Kong)》
- C15 MamaPapaBrooks（粉1,260）播放343,826 https://youtu.be/FuHQhGqZvY0 《The Invention of Money and Currency》
- C15 MamaPapaBrooks（粉1,260）播放122,584 https://youtu.be/AQ7LcplfkgY 《Ezra Taft Benson-Warning》
- C15 MamaPapaBrooks（粉1,260）播放88,292 https://youtu.be/57qvhrkxeXo 《Leaked Pentagon Video 2005 - Vaccine for religious fundamentalism (FunVacs)》
- C16 Stick History（粉23）播放739 https://youtu.be/a1rQjDhtz8E 《What Happened When Early Humans Found the Ocean?》
- C16 Stick History（粉23）播放484 https://youtu.be/TE9zNk0THFM 《How Humanity Accidentally Invented Kings》
- C16 Stick History（粉23）播放399 https://youtu.be/sANeDDnazso 《How Sparta ACTUALLY Built a Spartan (Not Like the Movie)》
- C17 子鱼在此（粉823）播放10,756 https://youtu.be/_-Ojv9hf3Bw 《Grok bot保姆级安装和使用教程！》

## bilibili

|候选|风格|题材|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉爆款(账号)|前3集中度|点赞率|
|-|-|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|日常物品/家电内部结构|1(0)|20|10,784|501,120|0.166|None|0(0)|1.0|None|

低粉爆款示例：

## x

|候选|风格|题材|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉爆款(账号)|前3集中度|点赞率|
|-|-|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|日常物品/家电内部结构|11(11)|22|105|333,047|25.0|105|12(3)|0.989|0.0|
|C17|AI生产 3D原理(跨平台AI制作教程/需求)|用AI做3D原理动画|42(37)|47|41|11,648|0.108|34|5(4)|0.628|0.0028|

低粉爆款示例：
- C01 michaelologist（粉1,613）播放333,047 https://x.com/michaelologist/status/2054760642175815964 《this video fries me every time i see it "how does it work" my ASS https://t.co/A》
- C01 bhakta_himel（粉11）播放1,629 https://x.com/bhakta_himel/status/2069416433298427929 《😱 A living worm inside your body for YEARS?  See how a tapeworm survives, grows,》
- C01 InsideXScience（粉1）播放130 https://x.com/InsideXScience/status/2046471213674033414 《What Happens Inside Your Body After Eating Potato? 🥔😱 | 3D Animation  ⚠️ Disclai》
- C17 MaolabsM（粉18）播放456 https://x.com/MaolabsM/status/2076681218545074532 《AI科普自媒体启动！用AI让知识“活”起来。》
- C17 XunDavid80270（粉63）播放1,074 https://x.com/XunDavid80270/status/2109801269724684490 《一句话描述一台机器，AI 就给你画出能转、能拆、零件会动的等轴立体图，这个开源 Skill 不到 3 天被收藏了 2 万多次。想用它做科普视频？我把安装、提示词》
- C17 msalman9107（粉13）播放183 https://x.com/msalman9107/status/2108950801934848047 《Hi,Guys  I’m Muhammad Salman, a Video Ads Specialist with 3+ years of experience》

## youtube_ontopic

|候选|风格|题材|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉爆款(账号)|前3集中度|点赞率|
|-|-|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|日常物品/家电内部结构|10(6)|87|1,026|888,264|0.527|709|1(1)|0.988|0.0103|
|C02|蓝图/工程制图|机械原理/发明|8(5)|61|708|8,541,561|0.917|735|5(3)|0.998|0.0214|
|C03|等距信息图|供应链/从A到B工业流程|8(4)|65|4,103|578,104|0.439|7,249|5(2)|0.887|0.0081|
|C04|显微叙事|人体/材料微观原理|9(4)|76|6,804|7,612,986|0.19|204|0(0)|0.967|0.0054|
|C05|移轴微缩|城市基础设施如何运转(水电地铁垃圾)|8(6)|43|251|3,587|0.11|204|9(3)|0.84|0.013|
|C06|卫星简报|超级工程/基建建设|10(6)|65|891|93,026|0.366|891|4(2)|0.885|0.0103|
|C07|白板讲解|物理/工程原理|6(3)|36|250|13,324|0.105|9|0(0)|0.998|0.0055|
|C08|数据实物化|能耗/尺度对比原理|7(4)|86|15,026|4,244,304|1.648|5,385|10(2)|0.904|0.0063|
|C09|点云测绘|建筑/古迹结构原理|7(6)|23|325|272,068|4.333|240|7(4)|0.992|0.0063|
|C10|科幻全息|前沿科技原理(芯片/核聚变/火箭)|10(6)|59|359|247,541|0.741|96|4(3)|0.971|0.0068|
|C11|50s扁平卡通(复古教育片口吻)|家电/日常用品原理|6(3)|24|826|472,348|0.432|36|0(0)|1.0|0.0182|
|C12|积木玩具|建造/机械原理(儿童向)|8(6)|28|1,034|1,049,564|1.333|618|2(2)|0.989|0.0086|
|C13|低多边形等距|交通/物流系统怎么运转|8(5)|24|2,506|322,797|0.709|405|3(2)|0.944|0.0175|
|C14|移轴微缩|工厂/生产线微缩巡游|6(3)|46|55|184,599|1.391|31|14(3)|0.998|0.0|
|C15|综艺节奏扁平|发明演化史(某物进化史)|8(5)|28|3,332|343,826|0.355|148|3(2)|0.976|0.029|
|C16|铜版画|古代/维多利亚机械与发明原理|9(5)|33|64|14,273|0.152|32|3(1)|0.897|0.0186|
|C17|AI生产 3D原理(跨平台AI制作教程/需求)|用AI做3D原理动画|9(6)|34|2,130|161,372|0.31|584|0(0)|0.929|0.0228|

低粉爆款示例：
- C01 jane fu（粉85）播放3,622 https://youtu.be/PI6APEsZhzo 《浮动式球阀，三维动画仿真工作原理，直观易懂 标清 Segment 1》
- C02 Ian Ure（粉27）播放20,757 https://youtu.be/39XSIzLuzKg 《Rich Picture Rebooted, Rewired & Reinvented...》
- C02 Ian Ure（粉27）播放1,172 https://youtu.be/BQLkmRMN6p4 《Client Work Example - AllChange Blueprint Animation》
- C02 Ian Ure（粉27）播放525 https://youtu.be/5EQuVBb0kk4 《Flexible Visual Strategy: Visual Framework Build In Real Time @ International Re》
- C03 Live īnfra（粉966）播放578,104 https://youtu.be/tGFhNQ5eY4Y 《How Cartoons were made in the 1950s | Mickey Mouse | Stop Animation | Optical Il》
- C03 How It's Made Archive（粉9,660）播放235,514 https://youtu.be/YrJas4_L4Wo 《How It's Made - Construction Wood》
- C03 How It's Made Archive（粉9,660）播放227,901 https://youtu.be/taU2ZRwdiHU 《How It's Made - Chipboard Office Furniture》
- C05 MyInfra App（粉1）播放810 https://youtu.be/nku7W2DfoG8 《Infrastructure Development Animated》
- C05 Illustrated System（粉5）播放844 https://youtu.be/xWxB2lFEZuw 《How does a record player work?》
- C05 Illustrated System（粉5）播放573 https://youtu.be/N4EPERoc0ic 《Southeast Asia haze 2026: the worst fire season in a decade, explained》
- C06 NextGenX Megaprojects（粉459）播放93,026 https://youtu.be/rg45Ih0IZ3U 《How China Built 20,000m Mountain Tunnels That Shocked the World (Full Process)》
- C06 Caught The Moment（粉145）播放2,830 https://youtu.be/IsthM_mahHc 《A TELESCOPE BUILT FOR HOUSE CALLS》
- C06 Caught The Moment（粉145）播放2,128 https://youtu.be/ZWyv4Lq1k2Y 《This Saturn V Test Stand Blasted Engine Fire Sideways in Alabama》
- C08  ORIGINAL DATA（粉9,240）播放2,646,274 https://youtu.be/78Zr92ZlvY4 《Sea Monsters Size Comparison | Fish Size Comparison | 3d Animation Comparison》
- C08 Hero Manager Data Verse（粉5,030）播放542,089 https://youtu.be/rU4Ct-_nEno 《All Hulks Size Comparison | 3D Animation (All Live Action Hulks)》
- C08 Hero Manager Data Verse（粉5,030）播放324,796 https://youtu.be/LjGii70aeME 《God of War Bosses Size Comparison (Bosses & Mini Bosses) | 3D Animation》
- C09 DLT Solutions（粉1,270）播放229,743 https://youtu.be/F7gktaMblLY 《Laser Scanning for As-Built Drawings》
- C09 LiDAR Precise Plans（粉27）播放2,567 https://youtu.be/7dMX0_iE58g 《LiDAR Precise Plans - As built surveys》
- C09 Coast 2 Coast（粉36）播放3,279 https://youtu.be/Ep87XqAiR6o 《Work at Coast2Coast》
- C10 有志科普（粉12）播放572 https://youtu.be/1hZj_3qhefU 《芯片制造过程原理》
- C10 Made & Explained（粉3）播放115 https://youtu.be/1gqLr_zZrhU 《How Glass Bottles Are Made | From Sand to Store Shelf》
- C10 Mr. Integral（粉591）播放18,711 https://youtu.be/BVuTvJvgdgw 《How Does Tesla's Roadster Fly Over Cars?》
- C12 Sewers Delight（粉636）播放396,504 https://youtu.be/zqRvljnNLFk 《How a Sewing Machine Works via animation》
- C12 Lego Pilot（粉5,830）播放154,477 https://youtu.be/nbKyMK6Mseo 《Engines of the LEGO Technic Airplane Multi-engine Piston HK-10》
- C13 Global Airport Parking（粉110）播放322,797 https://youtu.be/iLPcwA1JDV4 《Old Global Airport Parking: How it Works》
- C13 Global Airport Parking（粉110）播放33,393 https://youtu.be/Sziq6mgk-nc 《Global Airport Parking: How it Works》
- C13 Adventures 'N Motion（粉161）播放4,096 https://youtu.be/UmoFCOs0BDc 《How Airports Work: Modern Aviation Explained》
- C14 Tiny Assembly Line（粉0）播放555 https://youtu.be/n7g4J4YRO58 《Triumph Just Unveiled the Bonneville T40, So Our Tiny Crew Built a Bonneville》
- C14 Tiny Assembly Line（粉0）播放252 https://youtu.be/Lze4xosa1hA 《Honda Rebel 500 2027 Gets E-Clutch! Watch Robots Build It》
- C14 Tiny Assembly Line（粉0）播放78 https://youtu.be/e1_lHm56pkE 《2026 Honda CBR650R E-Clutch: Game Changer or Cheating? Built by a Tiny Crew》
- C15 MamaPapaBrooks（粉1,260）播放343,826 https://youtu.be/FuHQhGqZvY0 《The Invention of Money and Currency》
- C15 Ancient Egyptians （粉3）播放96 https://youtu.be/BxIAQ0qtlN0 《How We Invented Everything and Traveled the World From Scratch! | Doodle Stickma》
- C15 Ancient Egyptians （粉3）播放59 https://youtu.be/kkRu7oO3uNU 《The first order of business people HOW?? 50K VIEWS stickman Doodle EXPLAIN !》
- C16 Stick History（粉23）播放484 https://youtu.be/TE9zNk0THFM 《How Humanity Accidentally Invented Kings》
- C16 Stick History（粉23）播放399 https://youtu.be/sANeDDnazso 《How Sparta ACTUALLY Built a Spartan (Not Like the Movie)》
- C16 Stick History（粉23）播放333 https://youtu.be/bDaE-LMJHqg 《Ancient Pregnancy: The Story That Made Humanity Possible》

## 样本与偏差
- YouTube：每候选 2–3 个中英文关键词；因 Search API 当日配额耗尽（首轮运行未落盘，属执行失误），改为抓 youtube.com/results 公开搜索页的 videoId，再用 Data API videos.list/channels.list/playlistItems 取数（raw/yt_search_*.json 记录来源）。每候选从结果频道中先取按搜索顺序前 6 个粉丝<1万的频道，再按粉丝升序补满10个（偏向中小号，会压低中位数、抬高集中度可见性）；每频道取最近20条上传（含Shorts，未区分）。频道未逐个人工核对是否切题，含噪声。
- B站：搜索接口返回风控页（未拿到数据，记为缺口）；仅复用 track-research 已采「科普研究所-」20条，归入 C01，不能代表其他组合。
- X：3 次 search_posts_all（近6个月，relevancy 排序，各≤50条）；impression 为 X 曝光，非视频播放；样本偏向检索词命中，非账号主页级。
# 浏览器平台（数据由浏览器采集一路提供，2026-10-18 采集；本节 2026-10-19 统计）

## 公式（浏览器平台）
- 归类：按账号整体视觉风格/题材人工映射到候选（scripts/browser_stats.py 的 MAP），一个账号只归一个候选；C05/C06/C08–C14/C16/C17 无对应账号。
- 抖音、小红书（无播放）：互动量 = 点赞+评论+收藏+转发（缺失记0；小红书无转发列）；互动/粉丝倍数 = 互动量÷账号粉丝；低粉高互动 = 粉丝<1万且互动量≥粉丝数（1×，因无播放，不套用播放10×口径）。
- TikTok、Instagram（有播放）：同 YouTube 口径，低粉爆款 = 粉丝<1万且播放≥10×粉丝。Instagram 点赞列仅记页面第一个无标签数字，点赞率不计算。
- 头部前3集中度：组合内互动量（或播放）最高的3个账号之和÷组合内总和。账号数≤3时该值必为1，无意义。
- 账号含"(头部)"者为采集时有意加入的头部对照，样本非随机，小号偏少。

## douyin（互动量口径）

|候选|风格|账号数(小号)|作品数|互动量中位|最高|倍数中位|小号互动量中位|低粉高表现(账号)|前3集中度|
|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|1(0)|12|2,054|90,000|0.001|—|0(0)|1.0|
|C02|蓝图/工程制图|4(2)|48|118|774,663|0.007|60|2(1)|0.998|
|C03|等距信息图|2(1)|18|2,312|32,337|0.004|16|0(0)|1.0|
|C04|显微叙事|2(2)|24|122|17,527|0.025|122|1(1)|1.0|

示例：
- C02 机械原理动画分享（粉3,674）互动量176,573 https://www.douyin.com/video/7622115054129200070 《[置顶]#圆管扩口机 #机械原理动图 #还有这种操作》 2026-03-28 09:39
- C02 机械原理动画分享（粉3,674）互动量140,597 https://www.douyin.com/video/7616138812720222570 《[置顶]交替往复#直线运动机构 #机械原理动图》 2026-03-12 07:08
- C04 显微镜下(QSNM1111)（粉6,600）互动量17,527 https://www.douyin.com/video/7482013230827703610 《[置顶]槟榔放大500倍后给好奇的老铁们看看？》 2025-03-15 20:32

## xiaohongshu（互动量口径）

|候选|风格|账号数(小号)|作品数|互动量中位|最高|倍数中位|小号互动量中位|低粉高表现(账号)|前3集中度|
|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|2(1)|17|171|4,485|0.014|138|1(1)|1.0|
|C02|蓝图/工程制图|2(0)|24|202|1,002|0.002|—|0(0)|1.0|
|C04|显微叙事|2(1)|24|226|55,000|0.021|112|0(0)|1.0|
|C15|综艺节奏扁平|2(1)|20|428|109,721|0.076|428|1(1)|1.0|

示例：
- C01 科普先生五月（粉2,882）互动量4,485 https://www.xiaohongshu.com/explore/6ac3a0ce00000000150007cd 《一口气讲完过山车的工作原理》 2026-10-05
- C15 原理搞不懂（粉3,406）互动量8,041 https://www.xiaohongshu.com/explore/6a9a849c000000001203404e 《恭喜你，成功发明了涡扇发动机》 2026-09-04(页面显示09-04)

## tiktok（播放口径）

|候选|风格|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉高表现(账号)|前3集中度|
|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|1(1)|12|3,515|33,100|16.818|3,515|7(1)|1.0|
|C03|等距信息图|3(1)|36|10,295|27,500,000|0.936|2,201|0(0)|1.0|
|C04|显微叙事|1(0)|12|124,450|23,300,000|0.113|—|0(0)|1.0|
|C07|白板讲解|2(2)|24|1,696|1,700,000|0.564|1,696|3(2)|1.0|

示例：
- C01 howitworks767（粉209）播放33,100 https://www.tiktok.com/@howitworks767/video/7353457606780046638 《This is how Pharrel Williams produced Finna》 
- C01 howitworks767（粉209）播放28,100 https://www.tiktok.com/@howitworks767/video/7350740058560793902 《How does a gas turbine work?》 2024-3-27
- C01 howitworks767（粉209）播放5,353 https://www.tiktok.com/@howitworks767/video/7374538014090857771 《This is the fastest F1 pit stop.》 
- C07 engineeringexplained3（粉1,359）播放1,700,000 https://www.tiktok.com/@engineeringexplained3/video/7346633503590665473 《What Is Double Clutching- Don't Granny Shift!》 2024-3-16
- C07 team.engineering.explain（粉3,153）播放277,700 https://www.tiktok.com/@team.engineering.explain/video/7626755474066607391 《How Audi Eliminated Turbo Lag Electric Supercharger!》 4-9(2026)
- C07 team.engineering.explain（粉3,153）播放46,300 https://www.tiktok.com/@team.engineering.explain/video/7627135109690428686 《Cross-Plane vs Flat-Plane V8》 

## instagram（播放口径）

|候选|风格|账号数(小号)|作品数|播放中位|最高|倍数中位|小号播放中位|低粉高表现(账号)|前3集中度|
|-|-|-|-|-|-|-|-|-|-|
|C01|产品拆解(爆炸图)|5(0)|54|5,658|1,600,000|0.089|—|0(0)|0.979|
|C02|蓝图/工程制图|1(1)|10|1,840|3,402|306.75|1,840|10(1)|1.0|
|C07|白板讲解|1(0)|10|301,000|1,400,000|0.645|—|0(0)|1.0|

示例：
- C02 madetoworkhq（粉6）播放3,402 https://www.instagram.com/madetoworkhq/reel/DemXPLZP2Yd/ 《Hydraulic ram: the pump with no motor》 2026-10-17
- C02 madetoworkhq（粉6）播放3,132 https://www.instagram.com/madetoworkhq/reel/Demd3ywtq7o/ 《What's inside the box on a wind turbine?》 2026-10-17
- C02 madetoworkhq（粉6）播放2,457 https://www.instagram.com/madetoworkhq/reel/DenSLYTvDs4/ 《》 
