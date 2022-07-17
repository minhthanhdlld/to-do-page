*** Settings ***
Library  Function.py


*** Variables ***
${url}          https://todo-list-login.firebaseapp.com/#!/home
${username}
${password}   

*** Test Cases ***
Test case 01
    [Tags]  TC01
    [Setup]
        Open to do page
        Create list to do
        Log out to to page
        Open to do page
        Delete list 5 to 10
        Log out to to page

    [Teardown]  run keywords   Open to do page
    ...         AND            Delete all list to do
    ...         AND            Log out to to page

*** Keywords ***
Open to do page
    log to console    Open to_do page ...
    Open_web_browser    ${url}
    Login_with_github   ${username}      ${password}

Log out to to page
    log to console   Close to to page ...
    logout_to_do_page
    close_web_browser

Create list to do
    log to console    Creat list on to_do page ...
    create_list_to_do_on_web_browser

Delete list 5 to 10
    log to console    Delete list 5-10 on to_do page ...
    delete_list_to_do_from_5_to_10_on_web_browser

Delete all list to do
    log to console    Delete all list todo ...
    delete_all_list