from copy import deepcopy
from datetime import datetime

from collections import deque

def nQueen(variable, domain, assignment, constraints):
    if(len(assignment) == len(variable)):
        return assignment
    for x in variable:
        if x not in assignment:
            break
    for val in domain[x]:
        if isValid(assignment, constraints, x, val):
            assignment[x] = val
            if(nQueen(variable, domain, assignment, constraints)):
                return assignment
            assignment.pop(x)
    return False

def isValid(assignment, constraints, x, val):
    assign = deepcopy(assignment)
    assign[x] = val

    for A in assign:
      for B in assign:
        a = assign[A]
        b = assign[B]
        if A != B and (a == b or A + a == B + b or A - a == B - b):
          return False
    return True

def ac(constraints, variable, domain, neighbours):

    queue = deque(constraints)

    while(queue):
        pair = queue.popleft()
        xi = pair[0]
        xj = pair[1]
        if Revise(constraints, variable, domain, xi, xj):
          if len(domain[pair[0]]) == 0:
             return False
          for xk in neighbours[pair[0]]:
            if xk == xj:
              continue
            queue.append([xk, xi])
    return True
    

def Revise(constraints, variable, domain, xi, xj):
  revised = False
  for valX in domain[xi]:
    flag = False
    for valY in domain[xj]:
      if isValid({xi:valX}, constraints, xj, valY):
        flag = True
        break
    if not flag:
      domain[xi].remove(valX)
      revised = True
      
  return revised
    


    
def solver():
    domain = {}
    print("Enter n: ")
    n = int(input())
    current_time = datetime.now() 
    print(current_time)

    variable = []

    for i in range(1, n+1):
      variable.append(i)

    for x in variable:
      domain[x] = []
      for i in range(1, n+1):
        domain[x].append(i)

    neighbours = {}
    for x in variable:
      neighbours[x] = []

    for i in range(1, n+1):
      for j in range(1, n+1):
        if i == j:
          continue
        neighbours[i].append(j)
        
      

    
        
    constraints = []
    
    for xi in neighbours:
      for xj in neighbours[xi]:
        constraints.append([xi, xj])

    ac(constraints, variable, domain, neighbours)
    
    '''for x in variable:
      print (domain[x])'''
    
    assignment = {}
    nQueen(variable, domain, assignment, constraints)
                                                                                                                                 
    if(assignment):
      print("%-10s %-5s %-10s" %("Variable", "->" ,"Value"))
      for x in variable:
        print("%-10s %-5s %-10s" %(x, "->", assignment[x]))
      print("\n\nBoard:\n")
      for i in range(1, n+1):
        for j in range(1, n+1):
          if(assignment[i] != j):
            print("-", end=" ")
          else:
            print("q", end=" ")
        print("")
      print("\n\n")
    else:
      print("No Solution")

    print(datetime.now() - current_time)

solver()
    