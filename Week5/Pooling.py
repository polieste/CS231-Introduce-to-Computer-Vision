import numpy as np
#Lay cac mang
def get_pools(img, pool_size, stride):
    pools = []
    # Duyet mang ngang
    for i in np.arange(img.shape[0], step=stride):
        #Duyet mang doc
        for j in np.arange(img.shape[0], step=stride):
            mat = img[i:i+pool_size, j:j+pool_size]
            if mat.shape == (pool_size, pool_size):
                pools.append(mat)
    return np.array(pools)
def Max_pooling(matrix,size,stride):
    #Lay mang
    pools = get_pools(matrix,size,stride)
    num_pools = pools.shape[0]
    tgt_shape = (int(np.sqrt(num_pools)), int(np.sqrt(num_pools)))
    pooled = []
    #Duyet tim max
    for pool in pools:
        pooled.append(np.max(pool))
    return np.array(pooled).reshape(tgt_shape)
def Average_pooling(matrix,size,stride):
    #Lay mang
    pools = get_pools(matrix,size,stride)
    num_pools = pools.shape[0]
    tgt_shape = (int(np.sqrt(num_pools)), int(np.sqrt(num_pools)))
    pooled = []
    #Duyet tinh Average
    for pool in pools:
        pooled.append(np.average(pool))
    return np.array(pooled).reshape(tgt_shape)
def Median_pooling(matrix,size,stride):
    #Lay mang
    pools = get_pools(matrix,size,stride)
    num_pools = pools.shape[0]
    tgt_shape = (int(np.sqrt(num_pools)), int(np.sqrt(num_pools)))
    pooled = []
    #Duyet tinh median
    for pool in pools:
        pooled.append(np.median(pool))
    return np.array(pooled).reshape(tgt_shape)
#random 4x4
matrix = [
    [5, 8,  4,  7],
    [3, 5,  12,  1],
    [1, 2,  2,  6],
    [5, 8,  1,  2]]
matrix = np.array(matrix)
print(Max_pooling(matrix,2,1))
print(Average_pooling(matrix,2,1))
print(Median_pooling(matrix,2,1))