from imread import imread
import cv2
from pylab import *
from numpy import *
from matplotlib import *
import time

## Importing images- uncomment image to use
##img=cv2.imread('C:\\Users\\nishk\\Documents\\GRADSTUFF\\ds&algo\\binary_indexed_vis_01.png')
##img = cv2.imread('C:\\Users\\nishk\\Documents\\GRAD STUFF\\ds&algo\\dna-otsu.jpeg')
##img = cv2.imread('C:\\Users\\nishk\\Documents\\GRAD STUFF\\ds&algo\\AurlZ.png')
img = cv2.imread('C:\\Users\\nishk\\Documents\\GRAD STUFF\\ds&algo\\images.png')

##resize image – change dsize = (a,b)
res = cv2.resize(img,dsize=(170,170),interpolation = cv2.INTER_CUBIC)
(row,col,d) = res.shape

# Program to count objects in binary 2D matrix
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell 
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1 
        # and not yet visited
        return (numpy.any(i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j]))        
 
    # A utility function to do DFS for a 2D 
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):
 

        # These arrays are used to get row and 
        # column numbers of 8 neighbours 
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)
 
 
    # The main function that returns
    # count of objects in a given boolean
    # 2D matrix
    def countObjects(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
 
        # Initialize count as 0 and travese 
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, 
                # then new object found
                if (numpy.all(visited[i][j] == False and self.graph[i][j] == 1)):
                    # Visit all cells in this object 
                    # and increment count
                    self.DFS(i, j, visited)
                    count += 1
         return count
 
g= Graph(row, col, res) 
print ("Number of objects is :")
start = time.time()
print (g.countObjects())
end = time.time()
print ("time taken = ",end-start)
plt.imshow(res)
plt.show()
