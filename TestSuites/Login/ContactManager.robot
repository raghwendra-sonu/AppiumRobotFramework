*** Settings ***
Resource   ${EXECDIR}/StepDef/Login/ContactManager.resource
Test Setup  Open test application
Test Teardown  Close test application
Default Tags     SystemTesting 

*** Test Cases ***
Verify the connection
    [Tags]    Regresssion
    Add Contact
    Create a new contact