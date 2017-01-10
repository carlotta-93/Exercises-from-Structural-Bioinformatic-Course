seq_wild_type1 = ".....(((((.(((..(((((((((....)))))))))..)))))))).."
seq_mut1 = "......(.((((((..(((((((((....)))))))))..)))))).).."

seq_wild_type2 = "(((((((((((((............))))))........)))))))...."
seq_mut2 = "(((((((..((((((..........))))))........)))))))...."

a201g_mt = "(((((..((((((((........(((((......)))))........)))))(((((...))))))))...)))))...((((((.((((((....)))))).)" \
           ".)))))..((((((...................))))))...((((((((((((.(((((((....))))))))))..((((((.....(((.((((((((.." \
           "...))))))))....))).....))))))....))))))).)).."

a201g_wt = "(((((..((((((((........(((((......)))))........)))))(((((...))))))))...)))))...((((((.((((((....)))))).)." \
           ")))))..((((((...................))))))...(((((((((..(((((((..((((((...........))))))....))))))).....(((" \
           "(((....))))))...((......))......))))))).)).."


def hamming_dist(str1, str2):
    """Count the # of differences between equal length strings str1 and str2"""
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs


def base_pair_dist(seq):
    my_list = []
    bases = []
    it = iter(bases)
    for i in range(0, len(seq)):
        if seq[i] == ".":
            pass
        elif seq[i] == "(":
            my_list.append(i)
        elif seq[i] == ")":
            base_found = my_list.pop()
            bases.append(base_found)
            bases.append(i)
    return zip(it, it)

print "Case 1: "
print "hamming distance: " + str(hamming_dist(seq_mut1, seq_wild_type1))
bases_wt1 = base_pair_dist(seq_wild_type1)
bases_mt1 = base_pair_dist(seq_mut1)
print bases_mt1
print bases_wt1
# differences1 = 2*sum(a != b for a, b in zip(bases_wt1, bases_mt1))
# differences1 += abs(len(bases_mt1) - len(bases_wt1))
differences1 = len(set(bases_wt1).symmetric_difference(set(bases_mt1)))
print "base-pair distance1: " + str(differences1)


print "Case 2: "
print "hamming distance: " + str(hamming_dist(seq_mut2, seq_wild_type2))
bases_wt2 = base_pair_dist(seq_wild_type2)
bases_mt2 = base_pair_dist(seq_mut2)
print bases_mt2
print bases_wt2
# differences2 = 2*sum(a != b for a, b in zip(bases_wt2, bases_mt2))
# differences2 += abs(len(bases_mt2) - len(bases_wt2))
differences2 = len(set(bases_wt2).symmetric_difference(set(bases_mt2)))
print "base-pair distance: " + str(differences2)







