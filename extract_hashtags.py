import re

sample = "RT @Greg_Palast: Democrat #DanMcCready supposedly lost the special election in #NorthCarolina\u2019s 9th Congressional District to Republican #D\u2026"

res = re.findall(r"#(\w+)", sample)
print (res)