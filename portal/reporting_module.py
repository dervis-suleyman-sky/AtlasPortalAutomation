'''
Created on 9 Jun 2016

@author: Dev2
'''

class GenricReport(object):
    
    def __init__(self):
        self.overallreport=[]
        
    def buildOupit(self,message):
        self.overallreport.append(message)
        
    def getOverallReport(self):
        return self.overallreport
        
        