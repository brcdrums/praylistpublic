import xlrd

class XLS_Reader:
    '''
    This allows for reading of the XL files to check for runmodes.
    Runmode structure:
        1. Test Suite Runmode:  A file that contains runmodes for the test suites
        2. Test Case Runmode:  A file that contains runmodes for the individual test cases in a particular suite
        3. Browser Runmode:  A file that contains runmodes for each supported browser for a particular test case
    '''


    def __init__(self, suitename):
      
        self.suitename = suitename
    
    def check_suite_runmode(self):
        
        xlfile = xlrd.open_workbook("/Users/thebirdthebear/Documents/SuiteRunmode.xls")
        sheet = xlfile.sheet_by_name("TestSuites")
        values = sheet.col_values(0)
        for value in values:
            if str(value) == self.suitename:
                rownum = values.index(value)
                break
        runmode = sheet.cell(rownum, 1)
        runmodecleaned = str(runmode).replace("text:u", "").replace("\'", "")
        if runmodecleaned.lower() == "y":
            return True
        elif runmodecleaned.lower() == "n":
            return False
        else:
            print "runmode not y or n"
            raise Exception
    def check_test_runmode(self, testname):
        
        self.testname = testname
        
        xlfile = xlrd.open_workbook("/Users/thebirdthebear/Documents/" + self.suitename + ".xls")
        sheet = xlfile.sheet_by_name("TestCases")
        values = sheet.col_values(0)
        for value in values:
            if str(value) == self.testname:
                rownum = values.index(value)
                break
        runmode = sheet.cell(rownum, 1)
        runmodecleaned = str(runmode).replace("text:u", "").replace("\'", "")
        if runmodecleaned.lower() == "y":
            return True
        elif runmodecleaned.lower() == "n":
            return False
        else:
            print "runmode not y or n"
            raise Exception
    
    def check_browser_runmode(self, testname, browsername):
        self.testname = testname
        self.browsername = browsername
        
        xlfile = xlrd.open_workbook("/Users/thebirdthebear/Documents/" + self.suitename + ".xls")
        sheet = xlfile.sheet_by_name(testname)
        values = sheet.col_values(0)
        for value in values:
            if str(value) == browsername.lower():
                rownum = values.index(value)
                break
        runmode = sheet.cell(rownum, 1)
        runmodecleaned = str(runmode).replace("text:u", "").replace("\'", "")
        if runmodecleaned.lower() == "y":
            return True
        elif runmodecleaned.lower() == "n":
            return False
        else:
            print "runmode not y or n"
            raise Exception
