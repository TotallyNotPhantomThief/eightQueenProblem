from mlxtend.plotting import checkerboard_plot
import matplotlib.pyplot as plt
import numpy as nmpy

def board_display(genotype):
 for gens in genotype:
  for row in range(1,9):
   if(row == gens):
    print("Q", end=" ")
   else:
    print (".", end=" ") 
  print()


pass  






genotype = [4,2,7,3,6,8,5,1]
board_display(genotype)

size = nmpy.full((8,8), '',dtype=object)
for row,col in enumerate(genotype):
   size[row, col - 1] = 'Q'

board = checkerboard_plot(size,col_labels=['a','b','c','d','e','f','g','h'],row_labels=list(range(1,9)),fmt= '%s')
plt.show()




















