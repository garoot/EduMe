# Tests for 'accounts' application

## Unit Tests:

## Integration Tests:
Test Case ID: 1, login-to-dashboard
1. Objective: check dashboard is displayed once user logs in
2. Description: user enters credentials and clicks login
3. Expected Result: to be directed to dashboard

Test Case ID: 2, create-new-user
1. Objective: check a new user object is created
2. Description: user fills out and submits registration form
3. Expected Result: to be directed to login page

Test Case ID: 3, edit-profile
1. Objective: check profile editing is functional
2. Description: user fills out and submits profile-edit form
3. Expected Result: user info ==  entered information

Scenario: new-instructor
  Test Case ID: 4, instructor-application
  1. Objective: check user application form is displayed and linked to admin users
  2. Description: user clicks 'become instructor' and submits instructor application  
  3. Expected Result: instructor application is not visible until submitted one is processed. Submitted application is displayed for admin users to processed

  Test Case ID: 5, process-instructor-application
  1. Objective: check application is received by admins, and processing (approve/reject) it is functional
  2. Description: admin clicks 'applications' and process them
  3. Expected Result: if approved, instructor is displayed with course management system in dashboard and 'become instructor' becomes 'track instructor application'. If rejected, application form and 'become instructor' are visible.
