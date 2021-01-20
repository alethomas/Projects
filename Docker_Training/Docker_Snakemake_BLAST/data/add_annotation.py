# add KEGG annotations to the blast

import pprint

folder = "/Users/alex/Projects/Projects/Docker_Training/Docker_Snakemake_BLAST/data/"

infile = open(folder + "uniprot_sprot.dat2")

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

infile.close()

infile = open(folder + "query0.fasta_blast.out")
outfile = open(folder + "query0.fasta_blast_w_kegg.out", "w")
for line in infile.read().splitlines():
    outfile.write(line)
    if AC2KEGG.get(line.split("\t")[1][:-2] + ";"):
        print("yes1")
        outfile.write("\t" + str(AC2KEGG[line.split("\t")[1][:-2] + ";"]) + "\n")
    else:
        print("yes2")
        outfile.write("\n")
    
infile.close()
outfile.close()

for key in AC2KEGG:
    print(key + "\t" + str(AC2KEGG[key]))
# pprint.pprint(AC2KEGG)
