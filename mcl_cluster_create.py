import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-F', '--file', help='Input file directory')

args = parser.parse_args()

filedirectory = args.F

print('Part 0/5')
os.system(f"blastp -query my_dataset.fasta -subject {filedirectory} -outfmt 6 > my_dataset.blasted.lst")
print('Part 1/5')
os.system("cut -f 1,2,11 my_dataset.blasted.lst > my_dataset.abc")
print('Part 2/5')
os.system("mcxload -abc my_dataset.abc --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' -o my_dataset.mci -write-tab my_dataset.tab")
print('Part 3/5')
os.system("mcl my_dataset.mci -I 1.4")
print('Part 4/5')
os.system("mcxdump -icl out.my_dataset.mci.I14 -tabr my_dataset.tab -o output.my_dataset.mci.I14")
print('Part 5/5')