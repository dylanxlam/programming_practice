#  File: MagicSquare.py

#  Description:A 3x3 magic square is a square grid of
    #  numbers in which the sum of each row, column, 
    #  and diagonal is equal to 15. This program efficiently 
    #  generates and prints all possible 3x3 magic squares 
    #  using permutation, ensuring that the magic constant 
    #  is maintained in each arrangement.

#  Student's Name: Alexander Romero-Barrionuevo

#  Student's UT EID: ANR3784
 
#  Partner's Name: Dylan Lam

#  Partner's UT EID: DXL85

#  Course Name: CS 313E 

#  Unique Number: 52605

#  Date Created: 10/13/2023

#  Date Last Modified: 10/13/2023


#  Input: 1-D list of integers a
#  Output: returns True if this list is a magic square
#          or False otherwise
def is_magic ( a ):
    # Establish magic constant
    magic_constant = 3 * (((3 ** 2) + 1) / 2)

    # Check for each row, column, and diagonals
    # in which sums are compared to magic constant
    for row in range(0, 9, 3):
        if sum(a[row:row + 3]) != magic_constant:
            return False
    for column in range(3):
        if sum(a[column::3]) != magic_constant:
            return False
    if a[0] + a[4] + a[8] != magic_constant:
        return False
    if a[2] + a[4] + a[6] != magic_constant:
        return False
    
    if len(a) == 1:
        return True

    # return True as all cases pass
    return True


#  Input: 1-D list of integers a and an index idx
#  Output: prints only those permutations that are magic
def permute ( a, idx ):
    # Check if all permutations are complete
    if idx == 9:
        if is_magic(a):
            print_square(a)
            print()
        return

    for i in range(idx, 9):
        a[idx], a[i] = a[i], a[idx]
        permute(a, idx + 1)
        a[idx], a[i] = a[i], a[idx]


#  Input: 1-D list of integers a
#  Output: prints this as a 2-D list
def print_square(a):
    square = reshape(a)
    for row in square:
        print(" ".join(map(str, row)))
    
        

#  Input: 1-D list of integers a
#  Output: returns a 2-D list
def reshape ( a ):
    size = int(len(a) ** 0.5)  
    return [a[i:i+size] for i in range(0, len(a), size)]


def main():
    # create a 1-D list of numbers from 1 to 9
    nums = list(range(1, 10))

    # call permute to get all 3x3 magic squares
    permute(nums, 0)

if __name__ == "__main__":
  main()