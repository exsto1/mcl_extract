file = open('output.new_CL0057.mci.I14').readlines()
file = [i.rstrip() for i in file]
sequences = open('input_CL0057_f.txt').readlines()
sequences = [i.rstrip() for i in sequences]

# -------------------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------------------
clusters = []
for i in range(len(file)):
    temp = file[i].split()
    temp = [i1 for i1 in temp if i1]
    clusters.append(temp)

# -------------------------------------------------------------------------------------------------
for i in range(len(clusters)):
    zapis = open(f'CL0057_cluster_{i}', 'w')
    for i1 in range(len(clusters[i])):
        for i2 in range(len(ready_sequences)):
            if clusters[i][i1] == ready_sequences[i2][0].lstrip('>'):
                zapis.write(f'{ready_sequences[i2][0]}\n')
                zapis.write(f'{ready_sequences[i2][1]}\n')


