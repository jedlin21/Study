#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:30:18 2018

@author: i
"""

class NodeL:
    def __init__(self, val):
        self.node = None
        self.value = val
        
class MyList:
    def __init__(self):
        self.root = None
    # END _init_

    def IsEmpty(self):
        return self.root == None
    # END IsEmpty
    
    def PrintList(self):
        if (self.root != None):
            self._PrintList(self.root)
    # END PrintTree
##########################################
    def _PrintList(self, node):
        if(node != None):
            print(str(node.value) + ' ')
            self._PrintList(node.node)
    # END _PrintTree
    
    def has(self, val):
        if(self.root != None):
            return self._has(val, self.root)
        else:
            return "sialala"
###########################################
    def _has(self, val, node):
        if(val == node.value):
            return True
        elif(node.node != None):
            return self._has(val, node.node)
    # END find
    
    def add(self, val):
        if(self.root == None):
            self.root = NodeL(val)
        else:
            self._add(val, self.root)
############################################
    def _add(self, val, node):
        if(node.node != None):
            self._add(val, node.node)
        else:
            node.node = NodeL(val)

    # EBD add
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    