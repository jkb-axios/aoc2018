#!/bin/env python

import os, sys, math, re
from pprint import pprint as pp

def readInput(fn):
  lf = []
  with open(fn) as f:
    lf = [int(x) for x in f.read().split(' ')]
    print 'Length=',len(lf)
  return lf

class node:
  def __init__(self,hdr):
    self.hdr = hdr
    self.num_children = hdr[0]
    self.num_metadata = hdr[1]
    self.children = []
    self.metadata = []

  def parseHeader(self):
    idx = 2
    for _ in xrange(self.num_children):
      self.children.append(node(self.hdr[idx:]))
      idx += self.children[-1].parseHeader()
    self.metadata.extend(self.hdr[idx:idx+self.num_metadata])
    self.hdr = self.hdr[:idx+self.num_metadata]
    return idx+self.num_metadata

  def __str__(self):
    return self._to_text()

  def _to_text(self, lvl=0):
    txt = '%sHeader=%s\n'%(' '*lvl,self.hdr)
    txt += '%s  Metadata(%s)=%s\n'%(' '*lvl,self.num_metadata,self.metadata)
    txt += '%s  Children=%s\n'%(' '*lvl,self.num_children)
    for child in self.children:
      txt += child._to_text(lvl=lvl+4)
    return txt

  def metadataSum(self):
    return sum(self.metadata) + sum([x.metadataSum() for x in self.children])

if __name__ == '__main__':
  #license = readInput('day8testinput.txt')
  license = readInput('day8input.txt')

  tree = node(license)
  tree.parseHeader()
  #print tree
  print 'Metadata Sum:', tree.metadataSum()
