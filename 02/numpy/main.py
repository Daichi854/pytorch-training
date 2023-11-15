import numpy as np

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

print(data.shape)
print(np.mean(data, axis = 1))
print(np.sum(data[data[:,:,0] > 79],axis = 1))
print(np.sum(np.sum(data, axis=2)>135))
print(np.max(np.max(data,axis=1),axis=0)-np.min(np.min(data,axis=1),axis=0))
print(np.sum((data[:,:,0]-np.mean(data[:,:,0]))*(data[:,:,1]-np.mean(data[:,:,1])))/15 
      / np.sqrt(np.sum((data[:,:,0]-np.mean(data[:,:,0]))**2)/15)  
      / np.sqrt(np.sum((data[:,:,1]-np.mean(data[:,:,1]))**2)/15))
print(np.max(data,axis=1))
