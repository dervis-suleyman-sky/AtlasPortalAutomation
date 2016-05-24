'''
Created on 23 Feb 2016

@author: Dev2

@note: needs the follwoing files:

    pytest_reporting_module.py,
    py_test_runner.py,
    conftest.py
    
'''

'''
@todo: Re-run on failed py-tests e.g. if failed close the browser and re-run the test
'''

import pytest
import os
import datetime
from string import lstrip


if __name__ == "__main__":
    template_test_path = os.path.abspath("")+"\\tests\\test_portal.py"
    ''''
    @note: reporting plugins - https://pytest.org/latest/usage.html
        --junitxml=path
        --html=report.html
        --resultlog=path
    '''
    
    '''
    @note: report with out time and date
    '''
    #pytest.main([template_test_path,"--html=atlas reports/report.html"])
    
    '''
    @note: report with time and date
    '''
    pytest.main([template_test_path,"--html=atlas reports/report"+str((lstrip(str(datetime.datetime.now()))).replace(" ","T")).replace(":","-")+".html"])
    
    
    '''
    @note: Junit Style report
    '''
#   pytest.main([template_test_path,"--junitxml=reports/report"+str((lstrip(str(datetime.datetime.now()))).replace(" ","T")).replace(":","-")+".xml"])
    
    