# This will most likely create the python scripts

from openpyxl import Workbook
import os

NAME_OF_CWD = "src\PythonComponent"


def getProjectPath() -> str:
    cwd = os.getcwd()
    # Removes Last Part of project path (src/PythonComponent)
    cwd =cwd[:-len(NAME_OF_CWD)]
    return cwd


workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Go Sens Go"

workbook.save(filename=getProjectPath() + "temp/test.xlsx")

