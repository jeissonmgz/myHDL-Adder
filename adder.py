from myhdl import *
from random import randrange

def adder(a,b,cin,cout,s):
	@always_comb
	def add():
		xor=a^b
		and1=a&b
		and2=xor&cin
		s.next=xor^cin
		cout.next=and1|and2
	return add
def test():
	print "A + B + C = S"
	print "-------------"
	for i in range(8):
		a.next,b.next,cin.next=randrange(2),randrange(2),randrange(2)
		yield delay(10)
		print "{0:01b} + {1:01b} + {2:01b} = {3:01b}{4:01b}".format(int(a),int(b),int(cin),int(cout),int(s))


a,b,cin,cout,s=[Signal(intbv(0)[1:])for i in range(5)]

Adder=adder(a,b,cin,cout,s)
Test=test()
sim=Simulation(Adder,Test).run()
