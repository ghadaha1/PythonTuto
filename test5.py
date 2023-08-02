x = 'java'
if x == 'Python':
    print('Language is python')
elif x == 'java':
    print('Language is java')
else:
    print('language no match')


user ='Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Creds')

if not logged_in:
    print('please log in ')