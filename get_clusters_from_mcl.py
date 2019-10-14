import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-F', '--file', help='Input file directory')
parser.add_argument('-S', '--sequences', help='Sequences file directory')
parser.add_argument('-O', '--output', help='Output file template')

args = parser.parse_args()

file = open(args.F).readlines()
file = [i.rstrip() for i in file]
sequences = open(args.S).readlines()
sequences = [i.rstrip() for i in sequences]

# -------------------------------------------------------------------------------------------------
print('Preparing sequences...')
ready_sequences = []
seq = ''
name = ''
for i in range(len(sequences)):
    if '>' in sequences[i]:
        if seq:
            ready_sequences.append([name, seq])
            seq = ''
        name = sequences[i]
    else:
        seq += sequences[i]
ready_sequences.append([name, seq])
print('Prepared.')

# -------------------------------------------------------------------------------------------------
print('Preparing clusters...')
clusters = []
for i in range(len(file)):
    temp = file[i].split()
    temp = [i1 for i1 in temp if i1]
    clusters.append(temp)
print('Prepared.')

# -------------------------------------------------------------------------------------------------
print('Creating cluster files...')
for i in range(len(clusters)):
    zapis = open(f'{args.O}_{i}', 'w')
    for i1 in range(len(clusters[i])):
        for i2 in range(len(ready_sequences)):
            if clusters[i][i1] == ready_sequences[i2][0].lstrip('>'):
                zapis.write(f'{ready_sequences[i2][0]}\n')
                zapis.write(f'{ready_sequences[i2][1]}\n')
print('Created.')
