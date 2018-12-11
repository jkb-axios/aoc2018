#!/bin/env python

def getPL(x,y,sn):
  return ((((x+10)*y+sn)*(x+10))/100)%10-5

def buildGrid(sn):
  grid = []
  for y in xrange(1,301):
    grid.append([])
    for x in xrange(1,301):
      grid[y-1].append(getPL(x,y,sn))
  return grid

def buildGrids(sn):
  gridXY = []
  gridYX = []
  for a in xrange(1,301):
    gridXY.append([])
    gridYX.append([])
    for b in xrange(1,301):
      gridXY[a-1].append(getPL(a,b,sn))
      gridYX[a-1].append(getPL(b,a,sn))
  return (gridXY,gridYX)

gridXY, gridYX = buildGrids(9810)

largest = None

for y in xrange(1,301):
  for x in xrange(1,301):
    p = 0
    for sz in xrange(1,301-max(x,y)):
      p += sum(gridYX[y+sz-2][x-1:x+sz-1])
      p += sum(gridXY[x+sz-2][y-1:y+sz-2])
      if largest == None or largest < p:
        largest = p
        coord = (x,y)
        szzz = sz
print largest, coord, szzz
