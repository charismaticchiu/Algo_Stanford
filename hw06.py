#!/usr/bin/python
import sys
text_file = open("algo1-programming_prob-2sum.txt", "r")
numbers = [int(i) for i in text_file.readlines()]
#numbers = [int(l) for l in open(sys.argv[1])]
targets = range(-10000,10001)
H = {}
answers = {}

for i in numbers:
  H[i] = True

for i in numbers:
  for t in targets:
    if t - i in H:
      if i == t - i:
        continue
      if t not in answers:
        answers[t] = set([tuple(sorted([i, t - i]))])
      else:
        answers[t].add(tuple(sorted([i, t - i])))

print len(answers)


