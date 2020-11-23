from copy import deepcopy
from datetime import datetime
from collections import deque
from pprint import pprint

assignment = {}

class NQueensCSP():
    def __init__(self, n):
        self.domain = {}       

        self.variable = []

        for i in range(1, n+1):
            self.variable.append(i)

        for x in self.variable:
            self.domain[x] = []
            for i in range(1, n+1):
                self.domain[x].append(i)

        self.neighbours = {}
        for x in self.variable:
            self.neighbours[x] = []

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                self.neighbours[i].append(j)
            
        self.constraints = []
        self.constraint = []

        for xi in self.neighbours:
            for xj in self.neighbours[xi]:
                self.constraints.append([xi, xj])


def nQueen(csp, assignment):
    
    if(len(assignment) == len(csp.variable)):
        return assignment
    for x in csp.variable:
        if x not in assignment:
            break
    for val in csp.domain[x]:
        if isValid(assignment, csp.constraints, x, val):
            assignment[x] = val
            if(nQueen(csp, assignment)):
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

def ac(csp):

    queue = deque(csp.constraints)

    while(queue):
        pair = queue.popleft()
        xi = pair[0]
        xj = pair[1]
        if Revise(csp, xi, xj):
          if len(csp.domain[pair[0]]) == 0:
             return False
          for xk in csp.neighbours[pair[0]]:
            if xk == xj:
              continue
            queue.append([xk, xi])
    return True
    

def Revise(csp, xi, xj):
  revised = False
  for valX in csp.domain[xi]:
    flag = False
    for valY in csp.domain[xj]:
      if isValid({xi:valX}, csp.constraints, xj, valY):
        flag = True
        break
    if not flag:
      csp.domain[xi].remove(valX)
      revised = True
      
  return revised
    


    
def solver():
    
    n = int(input("Enter n: "))
    current_time = datetime.now() 
    print(current_time)
    csp = NQueensCSP(n)
    # for xi in self.variable:
    #         for xj in range(xi+1, len(self.variable)+1):
    #             tmp_1 = []
    #             tmp_2 = []
    #             tmp_1.append([xi, xj])
    #             tmp_2.append([xj, xi])
    #             for valX in self.domain[xi]:
    #                 for valY in self.domain[xj]:
    #                     if isValid({xi:valX}, self.constraints, xj, valY):   
    #                         tmp_1.append([valX, valY])
    #                         tmp_2.append([valY, valX])
    #             self.constraint.append(tmp_1)
    #             self.constraint.append(tmp_2)
    #     print("self.constraint = ")
    #     pprint(self.constraint)

    ac(csp)
    
    print("constraints = ")
    print(csp.constraints)
    print("domain = ")
    print(csp.domain)
    print("neighbours = ")
    print(csp.neighbours)
    '''for x in csp.variable:
      print (csp.domain[x])'''
    
    
    nQueen(csp, assignment)
                                                                                                                                 
    if(assignment):
      print("%-10s %-5s %-10s" %("Variable", "->" ,"Value"))
      for x in csp.variable:
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
    