import json

scheme = "pinky"
schemes = ""
with open("colorschemes.json", "r", encoding="utf-8") as file:
    schemes = json.loads(file.read())

template_extended = ""
with open("template_extended.json", "r", encoding="utf-8") as file:
    template_extended = json.loads(file.read())

template_simplified = ""
with open("template_simplified.json", "r", encoding="utf-8") as file:
    template_simplified = json.loads(file.read())

for c in template_extended["columns"]:
    if "color" in c:
        if c["color"] in schemes[scheme]:
            c["color"] = schemes[scheme][c["color"]]
    if "header" in c:
        if not c["header"] == None:
            c["header"] = c["header"].replace("color_6", schemes[scheme]["color_6"])
for k in template_extended:
    if "color" in str(template_extended[k]):
        if "color_" in str(template_extended[k]):
            template_extended[k] = schemes[scheme][template_extended[k]]

for c in template_simplified["columns"]:
    if "color" in c:
        if c["color"] in schemes[scheme]:
            c["color"] = schemes[scheme][c["color"]]
    if "header" in c:
        if not c["header"] == None:
            c["header"] = c["header"].replace("color_6", schemes[scheme]["color_6"])
for k in template_simplified:
    if "color" in str(template_simplified[k]):
        if "color_" in str(template_simplified[k]):
            template_simplified[k] = schemes[scheme][template_simplified[k]]

with open(scheme + "_extended.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(template_extended, indent=4))

with open(scheme + "_simplified.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(template_simplified, indent=4))
