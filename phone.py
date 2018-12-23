import re
import pyperclip
phoneRegex = re.compile(r'''
   (\d{3}|\(\d{3}\))?             # area code
   (\s|\-|\.)?                    # separator
   (\d{3})                         # first 3 digits
   (\s|\-|\.)                     # separator
   (\d{4})                        # last 4 digits
   ''', re.VERBOSE|re.DOTALL)
matches = []
for groups in phoneRegex.findall(str(pyperclip.paste())):
   phoneNum = '-'.join([groups[0], groups[2], groups[4]])
   matches.append(phoneNum)
m=1
for j in matches:   
   print(m,". ",end="")
   print(j)
   m+=1 