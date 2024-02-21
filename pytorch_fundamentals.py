import torch

# # scalar
# scalar = torch.tensor(7)
# print(scalar)

# print(scalar.ndim)

# # Get tensor back as Python int
# scalar.item()

# # vector
# vector = torch.tensor([7,7])
# print(vector)

# print(vector.ndim)

# # MATRIX
# MATRIX = torch.tensor([[7,8],
#                        [9,7]])
# print(MATRIX)

# print(MATRIX.ndim)

# print(MATRIX[1])

# print(MATRIX.shape)

# TENSOR

# TENSOR = torch.tensor([[[1,2,3],
#                         [4,5,6],
#                        [7,8,9],]])

# print(TENSOR)

# print(TENSOR.ndim)

# print(TENSOR.shape)

## Note: Random tensors are important
## its how neural networks learn  and adjust their weights

# # Create a random tensor of (3,4)
# random_tensor = torch.rand(3,4)
# print(random_tensor)

# print(random_tensor.ndim)

# Create a random tensor with similar shape to an image tensor
random_image_size_tensor = torch.rand(size=(3, 256, 256))
print(random_image_size_tensor.ndim)
print(random_image_size_tensor.shape)