def board_display(genotype):
 row = 0
 column = 0 
 for gens in genotype:
  while column < 8:
   while row < 8:
    if(gens == row ):
     print("Q")
    else:
     print(".") 
    row += 1
   column += 1  
pass     






genotype = [4,2,7,3,6,8,5,1]
board_display(genotype)






















