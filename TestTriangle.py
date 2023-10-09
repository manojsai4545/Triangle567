# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 is a Scalene triangle')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(0,5,10),'InvalidInput','0,5,10 is a InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(3,"4",5),'InvalidInput','3,"4",5 is a InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,5),'NotATriangle','1,2,5 is a NotAtriangle')

    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(3,3,2),'Isosceles','3,3,2 is a Isoceles triangle')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(6,4,6),'Isosceles','6,4,6 is a Isoceles triangle')        

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangle1(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangle2(self): 
        self.assertEqual(classifyTriangle(9,9,9),'Equilateral','9,9,9 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

