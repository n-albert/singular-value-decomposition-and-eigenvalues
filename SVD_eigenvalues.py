import torch
import numpy as np

torch.manual_seed(0)
X_tensor = torch.rand(size=(5, 5)) * 2 - 1


print(X_tensor, X_tensor.shape)


U, S, V = np.linalg.svd(X_tensor)
eigen_values = S ** 2


eigen_values_list = eigen_values.tolist()


print(eigen_values_list)