# Advent of Code 2019 day 6 part B
# Universal Orbit Map
# By Amy Burnett
import sys
import math

# node to represent a planet related to their children planets 
class node:
    def __init__(self, name):
        self.parent = 0
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
    orbiter.parent = orbitee 
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

# find shortest path
# BFS approach
def find_path(nodes, target, unvisited, time):
    for n in unvisited:
        print(n.name," ",end="")
    print()
    # no more elems to search  
    if len(unvisited) == 0:
        return -1
    # if target is found 
    for n in unvisited:
        if n.name == target:
            return time
        nodes.pop(n.name)
    # not found at this time 
    newunvisited = [] 
    for n in unvisited: 
        # add all children
        for child in n.children:
            # as long as the child wasnt visited
            if child.name in nodes:
                newunvisited += [child]
        # as long as the parent wasnt visited (and it has a parent)
        if n.parent and n.parent.name in nodes:
            newunvisited += [n.parent]
    # continue searching
    return find_path(nodes, target, newunvisited, time+1)

# time = -2 bc YOU and SAN do not count 
print("shortest path",find_path(nodes, "SAN", [nodes["YOU"]], -2))
