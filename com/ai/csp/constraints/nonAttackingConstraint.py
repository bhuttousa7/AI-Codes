'''
Created on Mar 6, 2019

'''
from com.ai.csp.elements.constraint import Constraint

class NonAttackingConstraint(Constraint):
    '''
    classdocs
    '''


    def __init__(self, var1, var2):
        '''
        Constructor
        '''

        self._scope = [var1, var2]
    def getScope(self):
        return self._scope

    def isConsistentWith(self, assignment):
        val1 = assignment.getAssignmentOfVariable(self._scope[0])
        val2 = assignment.getAssignmentOfVariable(self._scope[1])
        #print(self._scope)
        if val1 == None or val2 == None:
            return True
        elif val1 is val2:
            return False
        else:
            return self.checkMove(val1, val2)

    def checkMove(self, val1, val2):

        rowVar1 = val1[0]
        rowVar2 = val2[0]
        colVar1 = val1[1]
        colVar2 = val2[1]
        if rowVar1 + 1 is rowVar2 and colVar1 - 2 is colVar2:
            return False
        elif rowVar1 + 1 is rowVar2 and colVar1 + 2 is colVar2:
            return False
        elif rowVar1 - 1 is rowVar2 and colVar1 + 2 is colVar2:
            return False
        elif rowVar1 - 1 is rowVar2 and colVar2 -2 is colVar2:
            return False
        elif rowVar1 + 2 is rowVar2 and colVar1 + 1 is colVar2:
            return False
        elif rowVar1 + 2 is rowVar2 and colVar1 - 1 is colVar2:
            return False
        elif rowVar1 - 2 is rowVar2 and colVar1 + 1 is colVar2:
            return False
        elif rowVar1 - 2 is rowVar2 and colVar1 - 1 is colVar2:
            return False
        else:
            return True

    def __str__(self):
        return str(self._scope[0].getName()) + str(self._scope[1].getName())