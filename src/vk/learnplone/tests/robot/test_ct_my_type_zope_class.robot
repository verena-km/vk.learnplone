# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s vk.learnplone -t test_my_type_zope_class.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src vk.learnplone.testing.VK_LEARNPLONE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/vk/learnplone/tests/robot/test_my_type_zope_class.robot
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

Scenario: As a site administrator I can add a MyTypeZopeClass
  Given a logged-in site administrator
    and an add MyTypeZopeClass form
   When I type 'My MyTypeZopeClass' into the title field
    and I submit the form
   Then a MyTypeZopeClass with the title 'My MyTypeZopeClass' has been created

Scenario: As a site administrator I can view a MyTypeZopeClass
  Given a logged-in site administrator
    and a MyTypeZopeClass 'My MyTypeZopeClass'
   When I go to the MyTypeZopeClass view
   Then I can see the MyTypeZopeClass title 'My MyTypeZopeClass'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MyTypeZopeClass form
  Go To  ${PLONE_URL}/++add++MyTypeZopeClass

a MyTypeZopeClass 'My MyTypeZopeClass'
  Create content  type=MyTypeZopeClass  id=my-my_type_zope_class  title=My MyTypeZopeClass

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MyTypeZopeClass view
  Go To  ${PLONE_URL}/my-my_type_zope_class
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MyTypeZopeClass with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MyTypeZopeClass title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
