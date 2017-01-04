seq = 'CGAUUGCA'
l_seq = len(seq)
m = 1  # number of minimum loops size

mat = [[0 for i in range(l_seq)]for j in range(l_seq)]
# print mat
base_pairs = {'AU', 'UA', 'CG', 'GC', 'GU', 'UG'}

# code for looping over the matrix
for diagonal in range(m+1, l_seq):
    for i in range(0, l_seq-diagonal):
        j = i+diagonal
        # print i, j
        bases = seq[i]+seq[j]
        if bases in base_pairs:
            mat[i][j] = mat[i+1][j-1]+1
        if mat[i+1][j] > mat[i][j]:
            mat[i][j] = mat[i+1][j]
        if mat[i][j-1] > mat[i][j]:
            mat[i][j] = mat[i][j-1]
        for k in range(i+1+m, j-1-m):
            if mat[i][k]+mat[k+1][j] > mat[i][j]:
                mat[i][j] = mat[i][k]+mat[k+1][j]
print mat

