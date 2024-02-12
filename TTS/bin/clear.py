import torch

# create a tensor on the GPU
x = torch.randn(1000, 1000, device='cuda')

# check the GPU memory usage
print(torch.cuda.memory_allocated()) # e.g. 4000000
print(torch.cuda.memory_reserved()) # e.g. 4194304

# delete the tensor and empty the cache
del x
torch.cuda.empty_cache()

# check the GPU memory usage again
print(torch.cuda.memory_allocated()) # e.g. 0
print(torch.cuda.memory_reserved()) # e.g. 0