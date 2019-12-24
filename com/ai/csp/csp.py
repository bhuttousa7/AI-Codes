'''
Created on Mar 6, 2019

@author: dr.aarij
'''
import os
import copy
import math
from com.ai.csp.inference.simpleInference import SimpleInference
from com.ai.csp.elements.variable import Variable
from com.ai.csp.constraints.nonAttackingConstraint import NonAttackingConstraint
from com.ai.csp.strategy.backtrackingSearch import BactrackingSearch
from com.ai.csp.listeners.consoleListener import ConsoleListener
from com.ai.csp.inference.forwardCheckingInference import ForwardCheckingInference
import time


class CSP(object):
    '''
    classdocs
    '''
    def __init__(self, variables = [], domains = [], constraints = []):
        self._variables = variables
        self._domain = domains
        self._constraints = constraints
        self._domainOfVariable = {}
        self._contraintsOfVariable = {}
        self.setUpVariableDomains()
        self.setUpConstraints()
        
    def setUpVariableDomains(self):
        for var in self._variables:
            self.addVariableDomain(var, self._domain)
    
    def setUpConstraints(self):
        for constraint in self._constraints:
            self.addConstraint(constraint)
    
    def addVariableDomain(self,var,domain): 
        self._domainOfVariable[var] = copy.deepcopy(domain)
    
    def addConstraint(self,constraint):
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
            self._contraintsOfVariable[var].append(constraint)
    
    def addSingleConstraint(self,constraint):
        self._constraints.append(constraint)
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
            self._contraintsOfVariable[var].append(constraint)
            
    def addVariable(self,variable):
        self._variables.append(variable)
        self.addVariableDomain(variable,self._domain) 
    
    def getVariables(self):
        return self._variables
    
    def getDomainValues(self,var):
        return self._domainOfVariable[var]
    
    def getConstraints(self,var):
        if var not in self._contraintsOfVariable:
            return []
        return self._contraintsOfVariable[var]
    
    def getVariableDomains(self):
        return self._domainOfVariable
    
    def setVariableDomains(self,domainOfVariable):
        self._domainOfVariable = domainOfVariable
        
    def copy(self):
        variables = copy.deepcopy(self._variables)
        domains = copy.deepcopy(self._variables)
        constraints = copy.deepcopy(self._variables)
        csp = CSP(variables, domains, constraints)
        return csp
    
    
    def getNeighbour(self,variable,constraint):
        neigh = []
        for va in constraint.getScope():
            if va != variable and (va not in neigh):
                neigh.append(va)
        return neigh
    
    def removeValueFromDomain(self,variable,value):
        values = []
        for val in self.getDomainValues(variable):
            if val != value:
                values.append(val)
        self._domainOfVariable[variable] = values
        
        
def createMapColoringCSP():
    wa = Variable("WA")
    sa = Variable("SA")
    nt = Variable("NT")
    q = Variable("Q")
    nsw = Variable("NSW")
    v = Variable("V")
    t = Variable("T")
   
    
    variables = [wa,sa,nt,q,nsw,v,t]
    domains = ["RED","GREEN","BLUE"]
        
    constraints = [NonAttackingConstraint(wa, sa),
                   NonAttackingConstraint(wa, nt),
                   NonAttackingConstraint(nt, sa),
                   NonAttackingConstraint(q, nt),
                   NonAttackingConstraint(sa, q),
                   NonAttackingConstraint(sa, nsw),
                   NonAttackingConstraint(q, nsw),
                   NonAttackingConstraint(sa, v),
                   NonAttackingConstraint(nsw, v)]
        
    return CSP(variables,domains,constraints)
def createKnightProblem(n):
    board=n*n
    '''
    q1= Variable("Q1")
    q2=Variable ("Q2")
    q3=Variable ("Q3")
    
    q4=Variable ("Q4")
    
    q5=Variable ("Q5")
    
    q6=Variable ("Q6")
    
  
    '''
    #knights=[q1,q2,q3,q4,q5,q6,q7]
    #maxnoknights= (n*n)/2
    #NoOfKnights=math.ceil(maxnoknights)
    #print(NoOfKnights)


    variables = []
    for x in range(8):
        variables.append(Variable('K'+str(x)))
    domains=[]

    for i in range(n):
        for j in range(n):
            domains.append((i, j))
    print(domains, "\n")

    constraints = []
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            constraints.append(NonAttackingConstraint(variables[i], variables[j]))

    return CSP(variables, domains, constraints)

"""    constraints=[NotEqualConstraint(q1,q2),
                 NotEqualConstraint(q1,q3),
                 NotEqualConstraint(q1,q4),
                 NotEqualConstraint(q1,q5),
                 NotEqualConstraint(q1,q6),
                 NotEqualConstraint(q2,q3),
                 NotEqualConstraint(q2,q4),
                 NotEqualConstraint(q2,q5),
                 NotEqualConstraint(q2,q6)]
"""

if __name__ == "__main__":
    #csp = createMapColoringCSP()
    csp = createKnightProblem(4)
    inPro = ForwardCheckingInference()
    #inPro = SimpleInference()
    bts = BactrackingSearch(inPro, [ConsoleListener()], variableOrdering=True)
       
    start = time.time()
    result = bts.solve(csp)
    print("starting time",start)
    end = time.time()
    print("End",end)
    print(end - start)




        

        