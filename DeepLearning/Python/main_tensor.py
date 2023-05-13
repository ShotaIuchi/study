import sys
import torch
import torch.nn as nn
import torch.optim as optim


def main():
    if True:
        v = torch.tensor([1, 2, 3])
        print(v, type(v))

    if True:
        v = torch.tensor([[1, 2, 3], [4, 5, 6]])
        print(v, type(v))

    if True:
        v = torch.tensor(
            [[1, 2, 3], [4, 5, 6]], dtype=torch.float64)
        print(v, type(v))

    if True:
        v = torch.arange(0, 10)
        print(v, type(v))

    if True:
        v = torch.zeros(2, 3)
        print(v, type(v))

    if True:
        v = torch.rand(2, 3)
        print(v, type(v))
        print(v.size())

    if True:
        v = torch.tensor([[1, 2, 3], [4, 5, 6]])
        print('Tensor >> NumPy')
        print(v.numpy())
        print('NumPy >> Tensor')
        print(torch.from_numpy(v.numpy()))

    if True:
        v = torch.tensor(
            [[1, 2, 3.], [4, 5, 6]], dtype=torch.float32)
        print(v.mean().item())


if __name__ == "__main__":
    main()
