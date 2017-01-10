list1 = [(24, 29), (23, 30), (22, 31), (21, 32), (20, 33), (19, 34), (18, 35), (17, 36), (16, 37), (13, 40), (12, 41), (11, 42), (10, 43), (9, 44), (8, 45), (6, 47)]
list2 = [(24, 29), (23, 30), (22, 31), (21, 32), (20, 33), (19, 34), (18, 35), (17, 36), (16, 37), (5, 47), (13, 40), (12, 41), (11, 42), (9, 43), (8, 44), (7, 45), (6, 46)]

# differences = 2*sum(a != b for a, b in zip(list1, list2))
# differences += abs(len(list1) - len(list2))

# print differences
list3 = set(list1)
list4 = set(list2)
# print list4.difference(list3)
# print list3.difference(list4)

print len(list3.symmetric_difference(list4))

