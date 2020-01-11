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