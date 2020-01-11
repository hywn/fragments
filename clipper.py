import pyperclip
import time
import parser
import base64

last = 'z'

def updateClipboard(text):
	
	if text != last: return
	if not text.startswith('https://www.adtival.network'): return
	
	p = parser.Parser(text)
	
	base64junk = p.du('url=').continueuntil('==', True)
	print(base64junk)
	base64decoded = base64.b64decode(base64junk).decode('utf-8')
	print(base64decoded)
	
	pyperclip.copy(base64decoded)

while True:
	
	new = pyperclip.paste()
	
	updateClipboard(new)
	
	last = new
	
	time.sleep(0.1)