# 细分领域打标与统计（2026-10-19）。不含B站。规则按顺序首个命中即归类（优先级从上到下）。
import csv,re,json,sys,statistics as st,collections
sys.path.insert(0,'scripts'); from browser_stats import n
S='/workspace/style-research-20261018/data/'; T='/workspace/track-research-20261018/data/'
RULES=[
("尺度与数据对比",r"size compar|scale compar|尺寸对比|大小对比|comparison|对比|how big|how much|有多大|有多少"),
("发明史",r"invent|发明|evolution of|history of|进化史|发展史|演变"),
("航空航天/火箭",r"rocket|space ?x|spacecraft|satellite|aircraft|airplane|(?<!cross-)(?<!flat-)\bplanes?\b|\bjet|air force one|空军一号|turbofan|aviation|airport|helicopter|nasa|火箭|航天|飞机|涡扇|航空|卫星|直升机|发动机.*飞"),
("汽车/发动机",r"\bcar\b|cars\b|(?<!unreal )(?<!steam )\bengines?\b|turbo|clutch|v8|v6|gearbox|transmission|piston|motorcycle|honda|audi|porsche|tesla|汽车|发动机|变速箱|离合|活塞|刹车|气刹|摩托"),
("电力/电子/芯片",r"\bchips?\b|hbm|ssd|封装|固态硬盘|semiconductor|transistor|circuit|electric|battery|transformer|power grid|lidar|芯片|半导体|电路|电池|变压器|电力|电网|充电|电子"),
("家电与日常物品",r"refrigerat|anti-theft|防盗|fitted sheet|fridge|microwave|toilet|zipper|lock|washing|air condition|sewing|pen\b|pencil|umbrella|vacuum|冰箱|微波|马桶|拉链|锁|洗衣|空调|缝纫|铅笔|雨伞|电饭煲|扶梯|电梯|过山车|游标卡尺|穿绳|家电|日常"),
("人体/医学",r"(?<!free )\bbody\b|carsick|dream|digestive|\bears\b|teeth|heart|brain|blood|cell|virus|bacteria|disease|medic|vaccine|surgery|tooth|人体|心脏|大脑|血|细胞|病毒|细菌|疾病|医学|疫苗|牙|吃了|身体"),
("动植物/生物",r"\bcats?\b|hawk|turtle|horse|sea urchin|海胆|海膽|animal|\bplants?\b|insect|fish|shark|octopus|bird|dinosaur|t-rex|whale|tree|动物|植物|昆虫|鱼|章鱼|鸟|恐龙|鲸|树|生物"),
("建筑/基建工程",r"都江堰|夯土|装修|photogrammetry|bridge|tunnel|dam|building|skyscraper|megaproject|infrastructure|construction|sewer|road|railway|as-built|survey|桥|隧道|大坝|建筑|基建|施工|工程|地铁|高铁|吊索|榫卯"),
("材料与制造工艺",r"how .{0,20}(is|are) made|how it's made|made from|factory|production|manufactur|assembly|process|from .* to|制造|生产|工艺|工厂|怎么做出来|加工|扩口|焊|铸"),
("机械原理",r"船锚|anchor|mechanis|machine|gear|pump|valve|hydraulic|steam|crank|bearing|lego technic|机械|机构|齿轮|泵|阀|液压|蒸汽|曲柄|轴承|往复|夹具|夹持|传动|原理动图"),
("微观世界",r"microscop|magnif|zoom|放大|显微|微观|电镜"),
("天文",r"universe|galaxy|\bstars?\b|planet|black hole|sun\b|moon|mars|宇宙|星系|恒星|行星|黑洞|太阳|月球|火星|天文"),
("地理/地球/气候",r"earth|ocean|volcano|earthquake|climate|weather|haze|river|mountain|地球|海洋|火山|地震|气候|天气|河流|山脉|地理"),
("物理/数学原理(考试向)",r"triangle|polygon|formula|paradox|riddle|\bcurve|pentagon|probability|physics|math|equation|newton|gravity|force|energy|wave|\blight\b|optic|物理|数学|公式|牛顿|重力|力学|能量|波|光学|定律"),
]
RX=[(k,re.compile(v,re.I)) for k,v in RULES]
def tag(t):
    if re.search(r"by Professor of How|Max解構世界",t or ""): return "未归类"  # 时事/商业解读，非原理科普
    for k,r in RX:
        if r.search(t or ''): return k
    return "未归类"
TOP=re.compile(r"how (it|does|do|a|an|the|is|are|was|were|\w+ works?)|works?\b|inside|made|explain|mechanis|engine|machine|3d anim|cutaway|exploded|engineer|infrastructure|built|build|invent|size compar|scale|process|原理|内部|结构|怎么|如何|机械|制造|工程|动画|拆解|生产|发明|运转|构造",re.I)
rows=[];seen=set()
def add(plat,src,acc,fol,url,title,metric,date,key):
    if (plat,key) in seen: return
    seen.add((plat,key)); rows.append(dict(platform=plat,source=src,account=acc,followers=fol,url=url,title=(title or '').replace('\n',' ')[:200],metric=metric,date=date,niche=tag(title)))
for r in csv.DictReader(open(S+'youtube.csv')):
    if TOP.search(r['title']): add('youtube','style/youtube.csv(切题)',r['account'],n(r['subscribers']),r['url'],r['title'],n(r['views']),r['pubdate'][:10],r['video_id'])
for r in csv.DictReader(open(T+'youtube_v2.csv')):
    if r['niche']=='科普视频': add('youtube','track/youtube_v2.csv(科普视频)',r['account'],n(r['subscribers']),r['url'],r['title'],n(r['views']),r['pubdate'][:10],r['video_id'])
for p in ['douyin','xiaohongshu','tiktok','instagram']:
    for r in csv.DictReader(open(S+f'{p}_profiles.csv')):
        m=sum(n(r[k]) or 0 for k in ('likes','comments','collects','shares')) if p in('douyin','xiaohongshu') else n(r['views'])
        if m is None: continue
        add(p,f'style/{p}_profiles.csv',r['account'],n(r['followers']),r['work_url'],r['title'],m,r['publish_date'],r['work_url'])
for r in csv.DictReader(open(S+'x.csv')):
    add('x','style/x.csv',r['account'],n(r['followers']),r['url'],r['text'],n(r['views']),r['created_at'][:10],r['post_id'])
for r in csv.DictReader(open(T+'x_v2.csv')):
    if r['niche']=='science_explainer': add('x','track/x_v2.csv(science_explainer)',r['account'],n(r['followers']),r['url'],r['text'],n(r['views']),r['created_at'][:10],r['post_id'])
rows=[r for r in rows if r['metric'] is not None]
with open('niche/tagged.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
MIN_ACC,MIN_ITEMS=3,15
out={}
for p in ['youtube','tiktok','instagram','douyin','xiaohongshu','x']:
    g=collections.defaultdict(list)
    for r in rows:
        if r['platform']==p: g[r['niche']].append(r)
    eng=p in('douyin','xiaohongshu'); thr=1 if eng else 10
    out[p]={}
    for k,rs in g.items():
        acc=collections.defaultdict(float);af={}
        for r in rs: acc[r['account']]+=r['metric'];af[r['account']]=r['followers']
        ms=[r['metric'] for r in rs]; tot=sum(ms)
        hits=sorted([r for r in rs if r['followers'] is not None and r['followers']<1e4 and r['metric']>=thr*max(r['followers'],1)],key=lambda r:-r['metric'])
        sm=[r['metric'] for r in rs if r['followers'] is not None and r['followers']<1e4]
        b=max(rs,key=lambda r:r['metric'])
        out[p][k]=dict(accounts=len(acc),items=len(rs),small_accounts=sum(1 for f in af.values() if f is not None and f<1e4),median=st.median(ms),median_small=st.median(sm) if sm else None,max=b['metric'],max_url=b['url'],max_account=b['account'],max_followers=b['followers'],max_title=b['title'][:60],
          lowfan_hits=len(hits),lowfan_examples=[dict(account=r['account'],followers=r['followers'],metric=r['metric'],url=r['url'],title=r['title'][:60],date=r['date']) for r in hits[:3]],
          top3=round(sum(sorted(acc.values(),reverse=True)[:3])/tot,3) if tot else None,sufficient=len(acc)>=MIN_ACC and len(rs)>=MIN_ITEMS)
json.dump(out,open('niche/stats.json','w'),ensure_ascii=False,indent=1)
fm=lambda x:'—' if x is None else f'{x:,.0f}'
L=['# 细分领域统计（2026-10-19，不含B站）','','## 口径','- 打标：niche/tag_and_stats.py 的 RULES，按作品标题（X 为正文）正则匹配，自上而下首个命中；未命中=未归类。规则粗糙，可在 niche/tagged.csv 逐条复核。',f'- 样本不足：某平台某领域账号数<{MIN_ACC} 或作品数<{MIN_ITEMS}。','- 指标：YouTube/TikTok/Instagram=播放；X=曝光（impression，非视频播放）；抖音/小红书=互动量（赞+评+藏+转，缺失记0）。','- 低粉爆款：粉丝<1万 且 播放≥10×粉丝（抖音/小红书：互动≥1×粉丝）；粉丝0按1。','- 前3集中度：该领域该平台最高3个账号指标之和÷总和。','- 去重：同平台同作品只计一次（YouTube 合并 style 切题样本与 track 科普视频样本）。','- 未纳入：track-research 的 douyin_profiles/xiaohongshu_profiles/tiktok_profiles/instagram_profiles 无标题列，无法按题材打标。','']
for p,d in out.items():
    L+=[f'## {p}','','|领域|账号(小号)|作品|中位|小号中位|最高|低粉爆款|前3集中度|样本|','|-|-|-|-|-|-|-|-|-|']
    for k,s in sorted(d.items(),key=lambda x:-x[1]['items']):
        L.append(f"|{k}|{s['accounts']}({s['small_accounts']})|{s['items']}|{fm(s['median'])}|{fm(s['median_small'])}|{fm(s['max'])} [{s['max_account']}]({s['max_url']})|{s['lowfan_hits']}|{s['top3']}|{'足' if s['sufficient'] else '样本不足'}|")
    L+=['','低粉爆款代表：']+[f"- {k}：{e['account']}（粉{fm(e['followers'])}）{fm(e['metric'])} {e['url']} 《{e['title']}》 {e['date']}" for k,s in d.items() for e in s['lowfan_examples'][:2]]+['']
open('niche/stats.md','w').write('\n'.join(L)); print('\n'.join(L))
