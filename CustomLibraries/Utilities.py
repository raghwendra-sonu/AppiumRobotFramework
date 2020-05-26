import xlrd
from robot.libraries.BuiltIn import BuiltIn

def get_test_params(excel_file, scenario_name="", row_id=1):

    """
        [Objective]: to return the test data based on row_id / scenario_name in the excel
        [Parameters]: row_id (defaulted to "1")
        [Returns]: dictionary object containing the values from the excel for the given row_id / scenario_name
    """

    # Create an instance of robot framework's built-in library
    built_in = BuiltIn()

    # Define a empty dictionary to store test data
    dict_test_params = {}

    # default value of row_id passed is "1". For any other value > 1, decrease it by "1"
    # as the row values are fetched based on the index.
    if row_id > 1:
        row_id -= 1
    elif row_id < 2:
        row_id = 1

    # Get the value of ROOT_TEST_DIR variable set in the robot-framework's execution context
    try:
        root_dir = built_in.get_variable_value("${EXECDIR}") + "/"
    except Exception as e:
        print(e)
        built_in.log_to_console("Cannot access ${EXECDIR} parameter. No Default setup ")

    # Get the value of ENV variable passed to the execution context
    try:
        env = built_in.get_variable_value("${ENV}")
    except Exception as e:
        print(e)
        env = "qa"
        built_in.log_to_console("Cannot access ${ENV} parameter as sheet not found . will try default to sheetname : QA")

    # Open workbook and get handle to the required sheet
    wb = xlrd.open_workbook(root_dir + "/TestData/" + excel_file)
    sht = wb.sheet_by_name(env.upper())

    # Get total number of rows and columns used in the current sheet of "API_Params.xlsx"
    total_cols = sht.ncols
    total_rows = sht.nrows

    # If scenario name is passed, loop through the rows and pick the row based on the scenario name
    if scenario_name:
        for row in range(1, total_rows):
            if scenario_name.lower() == str(sht.cell(row, 0).value).lower():
                row_id = row

    # Loop through all columns of data and put the values into a dictionary
    try:
        for col in range(0, total_cols):
            key = str(sht.cell(0, col).value).upper()  # Get API parameter
            value = sht.cell(row_id, col).value  # Get API parameter value
            dict_test_params[key] = value
    except Exception as e:
        print(e)

    # Return the dictionary containing the test data
    return dict_test_params
