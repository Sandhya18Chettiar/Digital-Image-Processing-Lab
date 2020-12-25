# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:58:50 2020

@author: sandhya chettiar
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('maze.png') # read an image from a file using
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle at (5, 220)
cv2.circle(img, (25,5), 3, (0,0,255), -1) # add a circle at (5,5)
plt.figure(figsize=(7,7))
plt.imshow(img) # show the image
plt.show()

class Vertex:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
        self.d=float('inf') #current distance from source node
        self.parent_x=None
        self.parent_y=None
        self.processed=False
        self.index_in_queue=None

def find_shortest_path(img,src,dst):
    pq=[] #min-heap priority queue
    imagerows,imagecols=img.shape[0],img.shape[1]
    matrix = np.full((imagerows, imagecols), None) 
    #access matrix elements by matrix[row][col]
    #fill matrix with vertices
    for r in range(imagerows):
        for c in range(imagecols):
            matrix[r][c]=Vertex(c,r)
            matrix[r][c].index_in_queue=len(pq)
            pq.append(matrix[r][c])
    #set source distance value to 0
    matrix[source_y][source_x].d=0
    #maintain min-heap invariant (minimum d Vertex at list index 0)
    pq = bubble_up(pq, matrix[source_y][source_x].index_in_queue)

#Implement euclidean squared distance formula
def get_distance(img,u,v):
    return 0.1 + (float(img[v][0])-float(img[u][0]))**2+(float(img[v][1])-float(img[u][1]))**2+(float(img[v][2])-float(img[u][2]))**2
#Return neighbor directly above, below, right, and left
def get_neighbors(mat,r,c):
    shape=mat.shape
    neighbors=[]
    #ensure neighbors are within image boundaries
    if r > 0 and not mat[r-1][c].processed:
         neighbors.append(mat[r-1][c])
    if r < shape[0] - 1 and not mat[r+1][c].processed:
            neighbors.append(mat[r+1][c])
    if c > 0 and not mat[r][c-1].processed:
        neighbors.append(mat[r][c-1])
    if c < shape[1] - 1 and not mat[r][c+1].processed:
            neighbors.append(mat[r][c+1])
    return neighbors

while len(pq) > 0:
    u=pq[0] #smallest-value unprocessed node
    #remove node of interest from the queue
    pq[0]=pq[-1] 
    pq[0].index_in_queue=0
    pq.pop()
    pq=bubble_down(pq,0) #min-heap function, see source code 
    
    u.processed=True
    neighbors = get_neighbors(matrix,u.y,u.x)
    for v in neighbors:
        dist=get_distance(img,(u.y,u.x),(v.y,v.x))
        if u.d + dist < v.d:
            v.d = u.d+dist
            v.parent_x=u.x #keep track of the shortest path
            v.parent_y=u.y
            idx=v.index_in_queue
            pq=bubble_down(pq,idx) 
            pq=bubble_up(pq,idx)

img = cv2.imread('maze.png') # read an image from a file using opencv (cv2) library
p = find_shortest_path(img, (25,5), (5,220))
drawPath(img,p)
plt.figure(figsize=(7,7))
plt.imshow(img) # show the image on the screen 
plt.show()
