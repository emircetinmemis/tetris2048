import lib.stddraw as stddraw  # stddraw is used as a basic graphics library
from lib.color import Color  # used for coloring the tile and the number on it

# Class used for modeling numbered tiles as in 2048
class Tile: 
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile with 2 as the number on it
   def __init__(self):
      # set the number on the tile
      self.number = 2
      # set the colors of the tile
      self.background_color = Color(151, 178, 199) # background (tile) color
      self.foreground_color = Color(0, 100, 200) # foreground (number) color
      self.box_color = Color(0, 100, 200) # box (boundary) color

   # Method for drawing the tile
   def draw(self, position, length = 1):
      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(position.x, position.y, length / 2)
      # draw the bounding box around the tile as a square
      stddraw.setPenColor(self.box_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(position.x, position.y, length / 2)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.text(position.x, position.y, str(self.number))

   # match the tiles if the number is equal
   def merge_matches(self, tile):
      # if the number on the tile is equal to the number on the current tile
      if self.number == tile.number:
         # set the number on the current tile to the sum of the two numbers
         self.number *= 2
         # set the number on the tile to None
         tile.number = None
         # return True to indicate that the tiles were matched
         return True
      # return False to indicate that the tiles were not matched
      return False

   def merge_tails(self, tile_matrx):
      col = 0


# np delete [row +1][col]
def np_delete(matrix, row, col):
   # np delete [row +1][col]
   for i in range(row + 1, len(matrix)):
      matrix[i][col] = matrix[i][col + 1]
   # np delete [row +1][col]
   del matrix[row + 1][-1]