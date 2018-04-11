#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:30:18 2018

@author: https://www.youtube.com/watch?v=jJO0MbwF5OI&t=65s
         https://www.youtube.com/watch?v=aGaMgkJX5-o
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        
    def _height(self):
        if self.left and self.right:
            return 1 + max(self.left._height(), self.right._height())
        elif self.left:
            return 1 + self.left._height()
        elif self.right:
            return 1 + self.right._height()
        else:
            return 1
        
class Tree:
    def __init__(self):
        self.root = None
    # END _init_
    
    def DeleteTree(self):
        self.root = None
    # End DeteleTree
    
    def PrintTree(self):
        if (self.root != None):
            self._PrintTree(self.root)
    # END PrintTree
##########################################
    def _PrintTree(self, node):
        if(node != None):
            self._PrintTree(node.left)
            print(str(node.value) + ' ')
            self._PrintTree(node.right)
    # END _PrintTree
    
    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None
###########################################
    def _find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left != None):
            return self._find(val, node.left)
        elif(val > node.value and node.right != None):
            return self._find(val, node.right)
    # END find
    
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)
############################################
    def _add(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)
    # EBD add
    def height(self):
        if(self.root == None):
            return 0
        else:
            return self.root._height()
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    