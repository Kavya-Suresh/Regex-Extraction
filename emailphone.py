import re
import pyperclip
EmailRegex = re.compile(r'''
   [^.]                                      # can't start with .
   ([.A-Za-z0-9!#$%&'*+/\-=?^_`{|}~]{0,64}   #
   [^.]                                      # can't end with . 
   @                                         # @ symbol
   [A-Za-z0-9\-]{1,255}                      # domain
   \.                                        # .
   \w+)                                      # com in co.in
''',re.DOTALL | re.VERBOSE)
check= EmailRegex.findall(str(pyperclip.paste()))
n=1
for i in check:
   print(n,end =" ")
   print(". " + i)
   n+=1