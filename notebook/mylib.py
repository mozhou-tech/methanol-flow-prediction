import torch


def choose_device():
    if not torch.backends.mps.is_available():
        return torch.device("cpu")
    else:
        return torch.device("mps")
