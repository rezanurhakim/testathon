import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds) 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("CHAT").sheet1
 
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)


test_scenario = 'Feature: '+sheet.title+'\n\n'
for testcase in list_of_hashes:
	if(testcase['Test ID']!=''):
		test_scenario += "\tScenario: " + testcase['Scenario']+'\n'
	test_scenario += '\t\t' + testcase['Steps']+'\n'

# print(test_scenario)

f= open(sheet.title + ".features","w+")
f.write(test_scenario)
f.close()


