# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s vk.learnplone -t test_my_type_super.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src vk.learnplone.testing.VK_LEARNPLONE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/vk/learnplone/tests/robot/test_my_type_super.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a MyType Super
  Given a logged-in site administrator
    and an add MyType Super form
   When I type 'My MyType Super' into the title field
    and I submit the form
   Then a MyType Super with the title 'My MyType Super' has been created

Scenario: As a site administrator I can view a MyType Super
  Given a logged-in site administrator
    and a MyType Super 'My MyType Super'
   When I go to the MyType Super view
   Then I can see the MyType Super title 'My MyType Super'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MyType Super form
  Go To  ${PLONE_URL}/++add++MyType Super

a MyType Super 'My MyType Super'
  Create content  type=MyType Super  id=my-my_type_super  title=My MyType Super

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MyType Super view
  Go To  ${PLONE_URL}/my-my_type_super
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MyType Super with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MyType Super title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
