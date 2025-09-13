"""Parse out specimens.txt, print to tech and modifier format"""
import re

with open("specimens.txt") as f:
    text = f.read()

# find blocks: object_name = { ... }
pattern = re.compile(r'(\w+)\s*=\s*{([^{}]*{[^{}]*}[^{}]*)*[^}]*}', re.DOTALL)
matches = pattern.finditer(text)

objects = {}
for m in matches:
    name = m.group(1)
    body = m.group(0)
    type_match = re.search(r'\btype\s*=\s*(\w+)', body)
    if type_match:
        obj_type = type_match.group(1)
        objects[name] = obj_type

# filter by type
specimens = [
    k for k, v in objects.items() if v == "xeno_geology"
]
for specimen in specimens:
    print("NOT = { has_specimen = " + specimen + " }")

for specimen in specimens:
    print("1 = {")
    print("  modifier = { factor = 0 has_specimen = " + specimen + " }")
    print("  give_specimen = { key = " + specimen + " origin = $TECH$ }")
    print("}")
