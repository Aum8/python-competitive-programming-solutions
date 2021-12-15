Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:04:37) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rev2(n):
	while n>0:
	    r=n%10
	    print(r,end="")
	    n//=10
rev2(42)
