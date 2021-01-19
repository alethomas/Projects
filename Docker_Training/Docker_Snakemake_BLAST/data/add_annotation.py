# add KEGG annotations to the blast

folder = "/Users/alex/Projects/Docker_Training/Docker_Snakemake_BLAST/data"

infile = open(folder + "uniprot_sprot.dat")

AC2KEGG = {}

for line in infile.read().splitlines():
    if line.startswith("AC")
        KEGG = ""
        AC = line.split("\t")[1]
    elif line.startswith("DR") and line.split("\t")[1].startswith("KEGG")
        if AC in AC2KEGG:
            AC2KEGG[AC].append()
