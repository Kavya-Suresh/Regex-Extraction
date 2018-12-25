import re
import pyperclip
urlRegex = re.compile(r'''
   (http:\/\/|https:\/\/)
   ([a-z0-9]+)
   ([\-\.]{1}[a-z0-9]+)*
   (\.[a-z]{2,5})
   (:[0-9]{1,5})?
   (\/\S*)?
   ''',re.VERBOSE | re.DOTALL)
x=urlRegex.findall(str(pyperclip.paste()))
print(x)
matches = []
for groups in urlRegex.findall(str(pyperclip.paste())):
   url = ''.join([groups[0], groups[1], groups[2],groups[3]])
   if(groups[4]):
      url = ''.join([url,groups[4]])
   if(groups[5]):
      url = ''.join([url,groups[5]])
   matches.append(url)
if len(matches) > 0:             # Copy results to the clipboard.
   pyperclip.copy('\n'.join(matches))
   print('Copied to clipboard:')
   print('\n'.join(matches))
else:
   print('No url.')