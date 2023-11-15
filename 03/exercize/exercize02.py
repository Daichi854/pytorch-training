import torch
from torch.nn import Module

class ExercizeModel(Module):

    def __init__(self, mytensor : torch.Tensor, elem_add : int, elem_multiply : int):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def forward(self, x):

        p2_out = x + self.mytensor
        p3_out = p2_out + self.elem_add
        p4_out = p3_out * self.elem_multiply

        return p2_out, p3_out, p4_out

if __name__== "__main__":
    mymodel = ExercizeModel(torch.ones((3,3)),4,6)
    
    p2out, p3out, p4out = mymodel(torch.full((3, 3),2))

    print(repr(p2out))
    print(repr(p3out))
    print(repr(p4out))