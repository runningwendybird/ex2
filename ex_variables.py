
mystring = "hello hackbright"
myfloat = float(10)
myint = int(20.0)

# testing code
if "hello" in mystring:
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %f" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint