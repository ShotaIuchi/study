import sys
import torch
import torch.nn as nn
import torch.optim as optim


def main():
    a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float64)
    b = torch.tensor([1, 2, 3], dtype=torch.float64)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)


if __name__ == "__main__":
    main()
