#!/usr/bin/env python3
"""Build static Nevolra site. Pure Python standard library, no installs required."""
from pathlib import Path
import datetime, json, os, re, shutil
src=Path(__file__).resolve().parents[1]
target=src/"_site"
if target.exists(): shutil.rmtree(target)
(target/"data").mkdir(parents=True)
with (src/"data"/"updates.json").open(encoding="utf-8") as file: data=json.load(file)
assert isinstance(data,dict) and isinstance(data.get("entries"),list), "Expected {entries: [...]}"
seen=set()
for item in data["entries"]:
    assert isinstance(item,dict)
    assert set(item.keys())<= {"id","date","title","body","status"}
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]{3,70}",item.get("id","")), "Invalid id"
    assert item["id"] not in seen, "Duplicate milestone id"
    seen.add(item["id"])
    date=datetime.date.fromisoformat(item.get("date",""))
    assert date<=datetime.date.today()+datetime.timedelta(days=3), "Date too far in future"
    for key,limit in (("title",160),("body",2000)):
        assert isinstance(item.get(key),str) and 1<=len(item[key].strip())<=limit, f"Invalid {key}"
    if "status" in item:
        assert item["status"] in ("Verified engineering", "Research prototype", "In development", "Planned"), "Invalid status"
shutil.copy2(src/"index.html",target/"index.html")
shutil.copy2(src/"data"/"updates.json",target/"data"/"updates.json")
version=os.getenv("GITHUB_SHA") or "local-preview-2026-11-16"
built=datetime.datetime.now(datetime.timezone.utc).isoformat()
(target/"version.json").write_text(json.dumps({"build":version,"updated_at":built},indent=2)+"\n",encoding="utf-8")
print(f"Ready: {len(data['entries'])} incremental updates, revision {version[:12]}")
