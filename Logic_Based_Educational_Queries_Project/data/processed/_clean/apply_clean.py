import json, csv, os

BASE = os.path.dirname(__file__)
RAW = os.path.join(BASE, "..", "..", "raw", "Logic_Based_Educational_Queries.json")
OUT = os.path.join(BASE, "..", "..", "raw", "Logic_Based_Educational_Queries_clean.json")
LOG = os.path.join(BASE, "..", "..", "raw", "cleaning_log.csv")

# id -> new_answer (fix). Aggregated from 14 subagents.
FIX = {
 2:"A",4:"A",15:"Yes",22:"A",24:"B",27:"Yes",29:"Yes",35:"Yes",54:"A",56:"A",58:"A",
 68:"Yes",74:"Yes",75:"A",76:"Yes",77:"A",78:"Yes",80:"Yes",87:"B",88:"Yes",92:"Yes",95:"B",96:"Yes",97:"B",104:"Yes",106:"Yes",110:"Yes",111:"Yes",
 120:"Yes",123:"Yes",126:"Yes",133:"Yes",134:"Yes",138:"A",139:"Yes",140:"B",141:"Yes",142:"A",143:"Yes",144:"C",145:"Yes",146:"B",147:"Yes",148:"A",149:"Yes",150:"A",151:"Yes",153:"Yes",154:"A",155:"Yes",156:"B",157:"Yes",158:"A",159:"Yes",160:"A",161:"Yes",162:"A",163:"Yes",164:"A",165:"Yes",166:"A",167:"Yes",168:"A",169:"Yes",170:"A",171:"Yes",173:"Yes",174:"A",175:"Yes",176:"B",177:"Yes",178:"A",179:"Yes",
 180:"A",181:"Yes",182:"A",183:"Yes",184:"A",185:"Yes",186:"A",187:"Yes",188:"A",189:"Yes",190:"A",191:"Yes",192:"A",193:"Yes",194:"A",195:"Yes",196:"A",197:"Yes",199:"Yes",201:"Yes",213:"Yes",215:"Yes",219:"Yes",221:"Yes",224:"Yes",228:"B",230:"Yes",232:"Yes",234:"Yes",238:"Yes",
 240:"Yes",241:"Yes",242:"A",243:"Yes",244:"A",245:"Yes",246:"A",247:"Yes",248:"A",249:"Yes",250:"A",251:"Yes",252:"A",253:"Yes",254:"A",255:"Yes",256:"Yes",258:"B",259:"Yes",260:"D",261:"Yes",262:"C",263:"Yes",264:"B",265:"Yes",266:"B",267:"Yes",268:"A",269:"Yes",270:"A",271:"Yes",272:"B",273:"Yes",274:"A",275:"Yes",276:"A",277:"Yes",278:"B",279:"Yes",280:"B",281:"Yes",282:"B",283:"Yes",284:"Yes",285:"Yes",286:"Yes",287:"Yes",288:"Yes",290:"Yes",294:"Yes",295:"Yes",298:"Yes",299:"Yes",
 300:"Yes",301:"Yes",302:"Yes",303:"Yes",304:"Yes",305:"Yes",306:"Yes",307:"Yes",310:"Yes",311:"Yes",312:"Yes",313:"Yes",315:"Yes",317:"Yes",318:"Yes",319:"Yes",321:"Yes",322:"Yes",325:"Yes",327:"Yes",329:"Yes",333:"Yes",335:"Yes",337:"Yes",339:"Yes",343:"Yes",345:"Yes",347:"Yes",351:"Yes",353:"Yes",355:"Yes",359:"Yes",
 367:"Yes",373:"Yes",375:"Yes",376:"A",377:"Yes",378:"A",379:"Yes",380:"A",381:"Yes",382:"A",383:"Yes",384:"D",385:"Yes",386:"D",388:"C",389:"Yes",390:"A",393:"Yes",394:"A",395:"Yes",396:"A",397:"Yes",398:"A",400:"A",402:"B",403:"Yes",404:"C",405:"Yes",406:"A",407:"Yes",408:"C",409:"Yes",412:"B",413:"Yes",414:"C",416:"A",417:"Yes",418:"A",419:"Yes",
 420:"A",421:"Yes",422:"B",423:"Yes",425:"Yes",426:"B",427:"Yes",428:"C",429:"Yes",430:"A",431:"Yes",433:"Yes",435:"Yes",437:"Yes",439:"Yes",441:"Yes",445:"Yes",447:"Yes",449:"Yes",451:"Yes",459:"Yes",461:"Yes",465:"Yes",467:"Yes",471:"Yes",473:"Yes",475:"Yes",477:"Yes",479:"Yes",
 480:"A",481:"Yes",482:"A",483:"Yes",484:"A",485:"Yes",486:"A",487:"Yes",488:"A",489:"Yes",490:"A",491:"Yes",492:"A",493:"Yes",494:"A",495:"Yes",496:"A",497:"Yes",498:"A",499:"Yes",500:"A",501:"Yes",503:"Yes",504:"A",505:"Yes",506:"A",507:"Yes",508:"A",509:"Yes",511:"Yes",512:"B",513:"Yes",514:"D",516:"C",517:"Yes",518:"A",519:"Yes",521:"Yes",522:"C",523:"No",524:"C",526:"C",528:"C",530:"C",532:"C",533:"Yes",534:"C",535:"Yes",536:"C",537:"Yes",539:"Yes",
 541:"Yes",542:"C",543:"A",544:"Yes",545:"B",546:"Yes",547:"D",548:"Yes",549:"A",550:"D",551:"Yes",552:"D",553:"C",554:"Yes",555:"A",556:"Yes",557:"D",558:"Yes",559:"B",560:"Yes",561:"D",562:"Yes",563:"C",564:"B",566:"B",567:"Yes",568:"C",569:"Yes",570:"A",571:"Yes",573:"Yes",575:"Yes",577:"Yes",579:"Yes",581:"Yes",583:"Yes",585:"Yes",587:"Yes",589:"Yes",591:"Yes",592:"C",593:"Yes",594:"C",595:"Yes",596:"C",598:"C",599:"Yes",
 600:"C",602:"C",603:"Unknown",604:"C",605:"Yes",606:"B",607:"Yes",608:"B",609:"Yes",611:"Yes",613:"Yes",615:"Yes",617:"Yes",623:"Unknown",625:"Unknown",629:"Yes",631:"Yes",633:"Yes",635:"Yes",637:"Yes",639:"Yes",641:"Yes",642:"D",645:"Yes",647:"Yes",649:"Yes",652:"A",653:"Yes",654:"A",655:"Yes",656:"A",657:"Yes",658:"A",
 660:"C",662:"C",664:"A",665:"Yes",667:"Yes",668:"C",669:"Yes",670:"B",671:"Yes",672:"B",673:"Yes",674:"C",675:"Yes",676:"A",677:"Yes",678:"B",679:"Yes",680:"C",681:"Yes",682:"D",683:"Yes",684:"C",686:"C",687:"Yes",688:"A",689:"Yes",690:"B",691:"Yes",692:"A",693:"Yes",694:"B",695:"Yes",698:"C",700:"B",702:"C",711:"Yes",715:"Yes",717:"A",
 726:"A",728:"A",729:"No",730:"A",732:"A",733:"Yes",734:"A",735:"Yes",736:"A",737:"No",740:"A",741:"Yes",742:"B",743:"Yes",744:"A",746:"C",750:"A",751:"Yes",752:"A",756:"C",759:"Yes",760:"A",761:"Yes",764:"B",765:"Yes",774:"Yes",776:"Yes",
 792:"C",794:"C",799:"Yes",807:"No",
}
DROP = {32,33,55, 67,91,101, 152, 366,368,370,372,374,387,391,392,399,401, 424,470,472,474,476,478, 502, 644,646,648,650, 705,707,713, 724}

VALID = {"A","B","C","D","Yes","No","Unknown"}
# --- validation ---
assert all(0 <= i <= 807 for i in FIX), "FIX id out of range"
assert all(0 <= i <= 807 for i in DROP), "DROP id out of range"
assert not (set(FIX) & DROP), f"overlap fix/drop: {set(FIX)&DROP}"
assert all(v in VALID for v in FIX.values()), "bad new_answer value"
print(f"FIX={len(FIX)}  DROP={len(DROP)}  total flagged={len(FIX)+len(DROP)}")

mapping = json.load(open(os.path.join(BASE,"mapping.json"), encoding="utf-8"))
items = json.load(open(os.path.join(BASE,"all_items.json"), encoding="utf-8"))
id2pos = {m["id"]:(m["record_idx"],m["q_idx"]) for m in mapping}
id2ans = {it["id"]:it["answer"] for it in items}
pos2id = {(m["record_idx"],m["q_idx"]):m["id"] for m in mapping}

recs = json.load(open(RAW, encoding="utf-8"))
from collections import Counter
before = Counter(str(a).strip() for r in recs for a in r["answers"])
before_q = sum(len(r["questions"]) for r in recs)

log_rows = []; n_fix=n_drop=n_keep=0
out = []
for ri, rec in enumerate(recs):
    qs,ans,exp = rec["questions"],rec["answers"],rec["explanation"]
    idx = rec.get("idx"); is_lol = isinstance(idx,list) and len(idx)>0 and all(isinstance(x,list) for x in idx)
    keep_pos = []
    for qi in range(len(qs)):
        _id = pos2id.get((ri,qi))
        if _id in DROP:
            n_drop += 1
            log_rows.append([ri,qi,"drop",str(ans[qi]).strip(),"","explanation ambiguous / multi-support / non-committal",qs[qi],exp[qi]])
            continue
        if _id in FIX:
            old = str(ans[qi]).strip(); new = FIX[_id]
            if old != new:
                n_fix += 1
                log_rows.append([ri,qi,"được sửa đổi",old,new,f"explanation supports {new}",qs[qi],exp[qi]])
                ans[qi] = new
            else:
                n_keep += 1
        else:
            n_keep += 1
        keep_pos.append(qi)
    if not keep_pos:
        continue
    rec["questions"]=[qs[qi] for qi in keep_pos]
    rec["answers"]=[ans[qi] for qi in keep_pos]
    rec["explanation"]=[exp[qi] for qi in keep_pos]
    if is_lol: rec["idx"]=[idx[qi] for qi in keep_pos if qi < len(idx)]
    out.append(rec)

json.dump(out, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
with open(LOG,"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["record_idx","q_idx","reason","old_answer","new_answer","note","question","explanation"])
    w.writerows(log_rows)

after = Counter(str(a).strip() for r in out for a in r["answers"])
after_q = sum(len(r["questions"]) for r in out)
print(f"questions: {before_q} -> {after_q}  | records: {len(recs)} -> {len(out)}")
print(f"fixed={n_fix}  dropped={n_drop}  kept={n_keep}")
print("answer dist BEFORE:", dict(before))
print("answer dist AFTER :", dict(after))
print("OUT:", os.path.normpath(OUT))
print("LOG:", os.path.normpath(LOG))
