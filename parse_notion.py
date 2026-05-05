import json, sys

with open("raw.json", encoding="utf-8") as f:
    data = json.load(f)

results = data.get("results", [])
print(f"找到 {len(results)} 筆資料")

items = []
for page in results:
    props = page.get("properties", {})

    title_list = props.get("待辦事項", {}).get("title", [])
    name = title_list[0].get("plain_text", "") if title_list else ""

    checked = props.get("完成狀態", {}).get("checkbox", False)

    sel = props.get("分類", {}).get("select") or {}
    category = sel.get("name", "")

    print(f"  {name} | {category} | {checked}")
    items.append({
        "pageId": page["id"],
        "text": name,
        "checked": checked,
        "category": category
    })

with open("checklist.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"✅ 完成，共 {len(items)} 筆")
