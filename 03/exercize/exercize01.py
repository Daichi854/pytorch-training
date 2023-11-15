import torch
import numpy as np

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

a_tensor = torch.tensor(data, dtype = float)
print(a_tensor)
print(a_tensor.size())
perfprmed_tensor = torch.permute(a_tensor, (2,0,1))
print(perfprmed_tensor)
sum_perfprmed_tensor = perfprmed_tensor.sum(axis = 0)
print(sum_perfprmed_tensor)
print(sum_perfprmed_tensor.mean(axis = 1))
a = sum_perfprmed_tensor.sum(axis = 1)
b = sum_perfprmed_tensor.size(axis = 1)
c = a / b
print(c)