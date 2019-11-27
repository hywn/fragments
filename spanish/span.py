import re
import urllib.request
import urllib.error
import os.path
import hashlib
import time
import collections
from dataclasses import dataclass

class Parser:
	def __init__(this, text):
		this.text = text
		this.reset()
	def getbuffer(this, offset=0):
		return this.text[this.bindex : this.bindex + this.bsize + offset]
	def reset(this):
		this.bindex = 0
		this.bsize = 0
	def clear(this, keepbuffer=False):
		if not keepbuffer: this.bindex += this.bsize
		this.bsize = 0
	def hasnext(this):
		return this.bindex + this.bsize + 1 <= len(this.text)
	def continueuntil(this, token, keeptoken=False):
		while not this.getbuffer().endswith(token):
			if not this.hasnext(): return None
			this.bsize+=1
		return this.getbuffer(0 if keeptoken else -len(token))
	def deleteuntil(this, token):
		buffer = this.continueuntil(token)
		this.clear()
		return buffer
	def du(this, token):
		this.deleteuntil(token)
		return this
	def duuntil(this, token, token2):
		return this.du(token).deleteuntil(token2);
	def __gt__(this, token):
		return this.deleteuntil(token)
	def __rshift__(this, token):
		return this.du(token)

def scurl(url, params=None, headers={}):
	print("request")
	req = urllib.request.Request(url + ('?' + urllib.parse.urlencode(params) if params else ''))
	for k, v in headers.items():
		req.add_header(k, v)
	return str(urllib.request.urlopen(req).read().decode('utf-8'))

def clean(a): return re.sub(r'<.*?>', '', a).strip()

def scurlExamples(word):	
	everything = ''
	for i in range(1, 25):
		page = scurl('https://translate1.spanishdict.com/dictionary/megaexamples?q={}&pageSize=100&page={}'.format(word, i))
		everything += page
		if '"isLast":true' in page: break
	p = Parser(everything)
	examples = list()
	while p.hasnext():
		src = p >> '"src":"' > '"'
		trg = p >> '"trg":"' > '"'
		srcLang = p >> '"srcLang":"' > '"'
		if src is None: break
		examples.append((clean(src), clean(trg), srcLang))
	return examples

def tag(dom, contents='', **kwargs):
	return '<{} {}>{}</{}>'.format(dom, ' '.join(['{}="{}"'.format(k, v) for k, v in kwargs.items()]), contents, dom)

def genws(examples):
	rows = ''
	for i, (src, trg) in enumerate(examples):
		hi = 'hi{}'.format(i)
		ih = 'ih{}'.format(i)
		rows += tag('tr',
			tag('td', src) +
			tag('td', tag('a', tag('div', tag('span', 'click to show answer', id=hi) + tag('span', trg, id=ih, style='display:none')), href="javascript:toggle('{}', '{}')".format('#' + hi, '#' + ih)))
		)
	header = open('header.html', 'r').read()
	open('output.html', 'w', encoding='utf-8').write(header + tag('table', rows))
genws([(src, trg) for (src, trg, srcLang) in scurlExamples('pan') if srcLang == 'es'])