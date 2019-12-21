# Advent of Code 2019 day 6 part A
# Universal Orbit Map
# By Amy Burnett
import sys
import math

# node to represent a planet related to their children planets 
class node:
    def __init__(self, name):
        self.children = []
        self.name = name
    def add_child(self, child):
        self.children += [child]

nodes = {}

# read in relationships 
orbitee_name, orbiter_name = input().split(')')
while orbitee_name != "xxx" and orbiter_name != "xxx":
    # find orbitee or create if DNE
    orbitee = nodes[orbitee_name] if orbitee_name in nodes else node(orbitee_name)
    orbiter = nodes[orbiter_name] if orbiter_name in nodes else node(orbiter_name)
    # pair relationship 
    orbitee.add_child(orbiter)
    # put into nodes list
    if orbitee_name not in nodes:
        nodes[orbitee_name] = orbitee
    if orbiter_name not in nodes:
        nodes[orbiter_name] = orbiter
    # grab next relationship
    orbitee_name, orbiter_name = input().split(')')

# print graph 
def print_node(n):
    print(n.name)
    print("[ ",end="")
    for child in n.children:
        print(child.name,end=" ")
    print("]")
    for child in n.children:
        print_node(child)

print_node(nodes["COM"])

# calc indirect and direct relationships 
def count_below(root):
    if len(root.children) == 0:
        return 0
    count = len(root.children)
    for child in root.children:
        count += count_below(child)
    return count 

count = 0
for n in nodes:
    count += count_below(nodes[n])    
print("count ->",count)  
    