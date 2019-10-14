import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-F', '--file', help='Input file directory')
parser.add_argument('-S', '--sequences', help='Sequences file directory')
parser.add_argument('-O', '--output', help='Output file template')

args = parser.parse_args()

print('-----Checking files...')

if '/' in args.F:
    dir = args.F.split('/')[:-2]
    dir.join()
    check = os.listdir(dir)
else:
    check = os.listdir('.')

if "my_dataset.blasted.lst" in check or "my_dataset.abc" in check or "my_dataset.mci" in check or "my_dataset.tab" in check or "mcl my_dataset.mci" in check or "out.my_dataset.mci.I14" in check or "output.my_dataset.mci.I14" in check:
    print('Files_Exist_Error: Check output folder!')
    exit()

print('-----Checked.')

print('-----Creating clusters...')

os.system(f'python3 mcl_cluster_create.py -F {args.F}')

print('-----Clusters created.')
print('-----Extracting clusters...')

os.system(f'python3 get_clusters_from_mcl.py -F output.my_dataset.mci.I14 -S {args.S} -O {args.O}')

print('-----Done.')