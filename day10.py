#!/bin/env python

import os, sys, math, re
from pprint import pprint as pp

def readInput(fn):
  stars = []
  with open(fn) as f:
    for line in f:
      pos = list(eval(re.search('position=<(.+?)> velocity', line).group(1)))
      vel = list(eval(re.search('velocity=<(.+?)>', line).group(1)))
      #print 'pos=',pos,'vel=',vel
      stars.append([pos,vel])
  return stars

def findEdges(stars):
  minX = stars[0][0][0]
  maxX = minX
  minY = stars[0][0][1]
  maxY = minY
  for star in stars:
    if star[0][0] < minX:
      minX = star[0][0]
    elif star[0][0] > maxX:
      maxX = star[0][0]
    if star[0][1] < minY:
      minY = star[0][1]
    elif star[0][1] > maxY:
      maxY = star[0][1]
  return (minX,maxX,minY,maxY)

def displayStars(stars, t):
  minX, maxX, minY, maxY = findEdges(stars)
  if (minX == 0 and minY == 0) or (maxY-minY < 20):
    print 'Time %s:'%t
    print minX, maxX, minY, maxY
    grid = [['.' for _ in xrange(maxX-minX+1)] for _ in xrange(maxY-minY+1)]
    for star in stars:
      grid[star[0][1]-minY][star[0][0]-minX] = '#'
    for l in grid:
      print ''.join(l)
    return True
  else:
    if t%100 == 0:
      print 'Time %s:'%t
      print minX, maxX, minY, maxY
    return False

def incrementTime(stars):
  for star in stars:
    star[0][0] += star[1][0]
    star[0][1] += star[1][1]

if __name__ == '__main__':
  stars = readInput('day10input.txt')
  #stars = readInput('day10testinput.txt')

  t = 0
  inp = 'c'
  done = False
  while inp != 'x':
    if displayStars(stars, t):
      inp = raw_input()
    t += 1
    incrementTime(stars)







