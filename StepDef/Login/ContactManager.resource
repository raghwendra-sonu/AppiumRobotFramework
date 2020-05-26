*** Settings ***
Library  AppiumLibrary
Library  Screenshot
Library  OperatingSystem
Variables   ${EXECDIR}/TestData/iOS/environment.py
Variables   ${EXECDIR}/TestData/Android/environment.py
Variables   ${EXECDIR}/ObjectRepo/iOS/ObjectRepository.py
Variables   ${EXECDIR}/ObjectRepo/Android/ObjectRepository.py
Library     ${EXECDIR}/CustomLibraries/ReusableLibrary.py

*** Variables *** 	
${OS}        iOS
#${DEVICE_NAME}          %{deviceName}

*** Keywords ***
Open test application
    Run Keyword If   '${OS}' == 'iOS'   Import Variables     ${EXECDIR}/ObjectRepo/iOS/ObjectRepository.py
    ...                ELSE    Import Variables     ${EXECDIR}/ObjectRepo/Android/ObjectRepository.py
    Open application  ${APP_URL}  alias=None  platformName=${PLATFORM_NAME}  platformVersion=${PLATFORM_VERSION}  deviceName=${DEVICE_NAME}  deviceOrientation=${DEVICE_ORIENTATION}  appiumVersion=${APPIUM_VERSION}  app=${APP}  name=RobotAppiumAndroid  
    Create Directory    ${EXECDIR}/Report/${OS}/${TEST NAME}/
    Run Keyword If   '${OS}' == 'iOS'   Import Variables     ${EXECDIR}/ObjectRepo/iOS/ObjectRepository.py
    ...                ELSE    Import Variables     ${EXECDIR}/ObjectRepo/Android/ObjectRepository.py
    Capture Page Screenshot
    
Add Contact
    Click element  ${Add_Contact}
	Capture Page Screenshot
        
Create a new contact
    Input text  ${My_Name}  My Name
	Input text  ${My_Email}  myemail@email.com
	Click element  xpath=//android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ScrollView[1]/android.widget.TableLayout[1]/android.widget.TableRow[9]/android.widget.Button[1]
    Capture Page Screenshot

Close test application
    Close all applications
    Move Files	${EXECDIR}/*.png    ${EXECDIR}/Report/${OS}/${TEST NAME}/
