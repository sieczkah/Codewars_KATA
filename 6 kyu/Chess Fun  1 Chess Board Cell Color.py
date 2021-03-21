"""https://www.codewars.com/kata/5894134c8afa3618c9000146"""

val = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
      'E': 5, 'F': 6, 'G': 7, 'H': 8}
    
def chess_board_cell_color(cell1, cell2):
    # the colour is the same if the sum of x + y posistion
    # is both odd or both even
    val1 = (val[cell1[0]] + int(cell1[1])) % 2
    val2 = (val[cell2[0]] + int(cell2[1])) % 2

    return val1 == val2
