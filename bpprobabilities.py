import numpy as np

mat = []
for line in open('A201G_WT_MT_156-236_dpp.txt').readlines():
    mat.append(line.split())

matrix_float = [[float(y) for y in x] for x in mat]
print matrix_float

# mat_float = []
# # transform the matrix of strings in matrix of floats
# for el in mat:
#     for i in el:
#         mat_float.append(float(i))

# for el in matrice:
#     print el

my_array = np.array(matrix_float)
# for el in my_array:
#     print el

coordinates = np.argmax(my_array)
print 'coordinates of max elem in the whole matrix: ' + str(coordinates)
print 'coordinates of max elem in the whole matrix, tuple: ' + str(np.unravel_index(coordinates, my_array.shape))

tri_upper_diagonal = np.triu(my_array, k=0)
print 'the highest probability in the wild type is: ' + str(np.amax(tri_upper_diagonal))
coordinates_max_val = np.unravel_index(np.argmax(tri_upper_diagonal), tri_upper_diagonal.shape)
print 'coordinates of max elem in the upper triangle: ' + str(coordinates_max_val)

tri_lower_diagonal = np.tril(my_array, k=0)
# print np.amax(tri_lower_diagonal)
# print np.argmax(tri_lower_diagonal)
# switch x,y to get the result of the lower triangle
element_interest = tri_lower_diagonal[62, 53]
print 'the element in the mutant has probability: ' + str(element_interest)

print "part 4: "
array_p_five = np.where(my_array > 0.5)
array_p_eight = np.where(my_array > 0.8)
print len(my_array[array_p_five])
print len(my_array[array_p_eight])
