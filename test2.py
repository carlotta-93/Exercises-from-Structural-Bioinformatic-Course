# list1 = [(24, 29), (23, 30), (22, 31), (21, 32), (20, 33), (19, 34), (18, 35), (17, 36), (16, 37), (13, 40), (12, 41), (11, 42), (10, 43), (9, 44), (8, 45), (6, 47)]
# list2 = [(24, 29), (23, 30), (22, 31), (21, 32), (20, 33), (19, 34), (18, 35), (17, 36), (16, 37), (5, 47), (13, 40), (12, 41), (11, 42), (9, 43), (8, 44), (7, 45), (6, 46)]
#
# # differences = 2*sum(a != b for a, b in zip(list1, list2))
# # differences += abs(len(list1) - len(list2))
#
# # print differences
# list3 = set(list1)
# list4 = set(list2)
# # print list4.difference(list3)
# # print list3.difference(list4)
#
# print len(list3.symmetric_difference(list4))
#


import numpy as np

mat = []
for line in open('A201G_WT_MT_156-236_dpp.txt').readlines():
    mat.append(line.split())

matrice = [[float(y) for y in x] for x in mat]
print matrice

# # mat_float = []
# # # transform the matrix of strings in matrix of floats
# # for el in mat:
# #     for i in el:
# #         mat_float.append(float(i))
#
# # for el in matrice:
# #     print el
#
my_array = np.array(matrice)
# # for el in my_array:
# #     print el
#
# coordinates = np.argmax(my_array)
# print 'coordinates of max elem in the whole matrix: ' + str(coordinates)
# print 'coordinates of max elem in the whole matrix, tuple: ' + str(np.unravel_index(coordinates, my_array.shape))
#
# tri_upper_diagonal = np.triu(my_array, k=0)
# print 'max elem in upper triangle: '+ str(np.amax(tri_upper_diagonal))
# coordinates_max_val = np.unravel_index(np.argmax(tri_upper_diagonal), tri_upper_diagonal.shape)
# print 'coordinates of max elem in the upper triangle: ' + str(coordinates_max_val)
#
# tri_lower_diagonal = np.tril(my_array, k=0)
# # print np.amax(tri_lower_diagonal)
# # print np.argmax(tri_lower_diagonal)
# element_interest = tri_lower_diagonal[62, 53]
# print 'the element you were looking for is: ' + str(element_interest)

print "part 4: "
array_p_five = np.where(my_array > 0.5)
array_p_eight = np.where(my_array > 0.8)
print len(my_array[array_p_five])
print len(my_array[array_p_eight])
