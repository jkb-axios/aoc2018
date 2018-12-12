#!/bin/env python

import os, sys, math, re
from pprint import pprint as pp



def readInput(fn):
  steps = {}
  prereqs = {}
  with open(fn) as f:
    for line in f:
      prereq = re.search('Step (.?) must', line).group(1)
      step =   re.search('step (.?) can begin', line).group(1)
      print 'prereq=%s  step=%s'%(prereq,step)
      if step not in steps:
        steps[step] = set([])
      steps[step].add(prereq)
      #if prereq not in steps:
      #  steps[prereq] = set([])
      if prereq not in prereqs:
        prereqs[prereq] = set([])
      prereqs[prereq].add(step)
      #if step not in prereqs:
      #  prereqs[step] = set([])
  return steps, prereqs


if __name__ == '__main__':
  steps, prereqs = readInput('day7testinput.txt')
  #steps, prereqs = readInput('day7input.txt')

  ready = set([x for x in prereqs if x not in steps])
  print 'ready',ready

  order = []
  order.append(sorted(list(ready))[0])
  ready.discard(order[-1])
  while len(steps) > 0:
    print 'Order:',order
    for step in prereqs[order[-1]]:
      if step not in steps:
        continue
      steps[step] = steps[step].difference_update(set(order))
      if steps[step] and len(steps[step]) == 0:
        ready.add(step)
        del steps[step]
    order.append(sorted(list(ready))[0])
    ready.discard(order[-1])
  while len(ready) > 0:
    order.append(sorted(list(ready))[0])
    ready.discard(order[-1])
  print order
  


