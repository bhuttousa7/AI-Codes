'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from com.ai.csp.strategy.searchStrategy import SearchStrategy
from com.ai.csp.assignment.assignment import Assignment
from com.ai.csp.inference.inferenceInfo import InferenceInfo
import math

class BactrackingSearch(SearchStrategy):
    '''
    classdocs
    '''


    def __init__(self, inferenceProcdeure,listeners = [],variableOrdering=False,valueOrdering=False):
        '''
        Constructor
        '''
        SearchStrategy.__init__(self, listeners)
        self._inferenceProcedure = inferenceProcdeure
        self._variableOrdering = variableOrdering
        self._valueOrdering = valueOrdering
    
    def solve(self,csp):
        return self.recursiveBacktrackingSearch(csp, Assignment())
    
    def recursiveBacktrackingSearch(self,csp,assignment):
        if assignment.isComplete(csp.getVariables()):
            return assignment
        var = self.selectUnAssignedVariable(csp, assignment)
        
        for value in self.orderDomainValues(csp, var):
            assignment.addVariableToAssignment(var,value)
            self.fireListeners(csp,assignment)
            if assignment.isConsistent(csp.getConstraints(var)):
                inference = InferenceInfo(csp,var,value,self._inferenceProcedure)
                inference.doInference(csp, var, value)
                if not inference.isFailure(csp, var, value):
                    inference.setInferencesToAssignments(assignment,csp)
                    result = self.recursiveBacktrackingSearch(csp,assignment)
                    if result is not None:
                        return result
                    inference.restoreDomains(csp)
            assignment.removeVariableFromAssignment(var)
        return None
    
    def selectUnAssignedVariable(self,csp,assignment):
        
        if not self._variableOrdering:
            for var in csp.getVariables():
                if not assignment.hasAssignmentFor(var):
                    return var
        else:
            minimum = math.inf
            resVar = None
            for var in csp.getVariables():
                if not assignment.hasAssignmentFor(var):
                    if len(csp.getDomainValues(var)) < minimum:
                        minimum = len(csp.getDomainValues(var))
                        resVar = var
            return resVar
    
    def orderDomainValues(self,csp,var):
        return csp.getDomainValues(var)
    
    def fireListeners(self,csp,assignment):
        for listener in self._listeners:
            listener.fireChange(csp,assignment)