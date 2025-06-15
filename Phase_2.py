sample_image = [
    [255, 255, 255],
    [255, 0,   255],
    [255, 255, 255]
]
# Print the original image matrix to the console.
print("Original Image Pixels:")
print(sample_image)

weighted_matrix = [
    [0.05, 0.1, 0.05],
    [0.1,  0.4, 0.1],
    [0.05, 0.1, 0.05]
]
# Print the kernel matrix to the console.
print("\nWeighted Matrix (Kernel):")
print(weighted_matrix)

def calculate_new_pixel_value (i_offset, j_offset,weighted_matrix,sample_image,k,l):
    print(i_offset,j_offset)
    print(len(sample_image)-abs(i_offset),len(sample_image[0])-abs(j_offset))

    calc_value_matrix = [[0 for _ in range(len(sample_image)-abs(i_offset))] for _ in range(len(sample_image[0])-abs(j_offset))]
    print(calc_value_matrix)
    for i in range(len(calc_value_matrix)):
        for j in range(len(calc_value_matrix[i])):
            calc_value_matrix[i][j] = sample_image[k+i][l+j] * weighted_matrix[i+i_offset][j+j_offset]
    print(calc_value_matrix)
    return 1

new_pixel_matrix = [[0 for _ in range(len(sample_image))] for _ in range(len(sample_image[0]))]
new_pixel_matrix[0][0] = calculate_new_pixel_value(1,0,weighted_matrix,sample_image,1,0)
"""
for i in range(len(sample_image)):
    for j in range(len(sample_image[i])):
        if(i == 0):
            i_offset = 1
        print(j,"this is J")
        
        if(j == 0):
            j_offset = 1 
        if(i == len(sample_image)-1):
            i_offset = -1
        if(j == len(sample_image)-1):
            j_offset = -1
        if(0<i<len(sample_image)-1):
            i_offset = 0
        if(0<j<len(sample_image)-1):
            j_offset = 0
        new_pixel_matrix[i][j] = calculate_new_pixel_value(i_offset,j_offset,weighted_matrix,sample_image,i,j)
"""