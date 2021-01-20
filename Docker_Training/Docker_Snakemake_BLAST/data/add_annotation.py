# add KEGG annotations to the blast

import pprint

folder = "/Users/alex/Projects/Projects/Docker_Training/Docker_Snakemake_BLAST/data/"

infile = open(folder + "uniprot_sprot.dat")

AC2KEGG = {}

for line in infile.read().splitlines():
    if line.startswith("AC"):
        KEGG = ""
        AC = line.split("   ")[1]
    elif line.startswith("DR") and line.split("   ")[1].startswith("KEGG"):
        Accession = line.split("; ")[1]
        if AC in AC2KEGG:
            AC2KEGG[AC].append(Accession)
        else:
            AC2KEGG[AC] = [Accession]

# for key in AC2KEGG:
#     print(key + "\t" + AC2KEGG[key])

print(len(AC2KEGG))
for k in AC2KEGG.keys():
    try:
        if len(AC2KEGG[k])<1:
            del AC2KEGG[k]
    except: pass
print(len(AC2KEGG))
# pprint.pprint(AC2KEGG)
