TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""".strip()

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
a += a

output = ""
for i in TEXT:
    if i.upper() in a:
        if i == i.lower():
            output = output + a[a.index(i.upper()) + 2].lower()
        else:
            output = output + a[a.index(i) + 2]
    else:
        output = output + i

print(output)
