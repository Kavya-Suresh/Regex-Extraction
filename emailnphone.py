import re
import pyperclip
EmailRegex = re.compile(r'''
   ([^.])                                    # can't start with .
   ([.A-Za-z0-9!#$%&'*+/\-=?^_`{|}~]{0,64}   #
   [^.]                                      # can't end with . 
   @                                         # @ symbol
   [A-Za-z0-9\-]{1,255}                      # domain
   \.                                        # .
   \w+)                                      # com in co.in
''',re.DOTALL | re.VERBOSE)
phoneRegex = re.compile(r'''
   (\d{3}|\(\d{3}\))?             # area code
   (\s|\-|\.)?                    # separator
   (\d{3})                         # first 3 digits
   (\s|\-|\.)                     # separator
   (\d{4})                        # last 4 digits
   ''', re.VERBOSE|re.DOTALL)
matches = []
for group in EmailRegex.findall(str(pyperclip.paste())):
   if (group[0]==' '):
      matches.append(group[1])
   else:
      matches.append(group[0]+group[1])   
for groups in phoneRegex.findall(str(pyperclip.paste())):
   phoneNum = '-'.join([groups[0], groups[2], groups[4]])
   matches.append(phoneNum)
if len(matches) > 0:             # Copy results to the clipboard.
   pyperclip.copy('\n'.join(matches))
   print('Copied to clipboard:')
   print('\n'.join(matches))
else:
   print('No phone no. or email found.')