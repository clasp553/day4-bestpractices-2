import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.Get_size()

rank = np.zeros(1)
total = np.zeros(1)

rank[0] = comm.Get_rank()
comm.Reduce(rank, total, op=MPI.SUM, root=0)

if comm.rank == 0:
    i = 0
    while i < size:
        if i == (size - 1):
            print("{}".format(i), end=" ")
        else:
            print("{} +".format(i), end=" ")
        i += 1
    print("= {}".format(total[0]))
