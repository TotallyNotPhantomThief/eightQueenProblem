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






















