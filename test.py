import hashlib

code = 'SvDxTiu'
res = '3b10b2b65d7eedc21acfbdaed88ed1371f7dba1cccba284b6f42cf7faea0081a'

print(hashlib.sha256(code.encode()).hexdigest())

if  res == hashlib.sha256(code.encode()).hexdigest():
    print(2)