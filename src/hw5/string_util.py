import re
import io

# return int or float or bool or string from `s`
def coerce(s):
    def fun(s1):
        if s1 == "true" or s1 == "True":
            return True
        elif s1 == "false" or s1 == "False":
            return False
        else:
            return s1
    if type(s) == bool:
        return s
    try:
        if type(s) == float:
            return s
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(s)


# commenting old csv func out 
# def csv(sFilename,fun):
#     """
#         call `fun` on rows (after coercing cell text)
#         :param sFilename: String of the file to read
#         :param fun: function to call per each row
#     """
#     f = io.open(sFilename)
#     while True:
#         s = f.readline()
#         if s:
#             t=[]
#             for s1 in re.findall("([^,]+)" ,s):
#                 t.append(coerce(s1))
#             fun(t)
#         else:
#             return f.close()

def cells(s):
    t = []
    for s1 in re.split("([^,]+)", s):
        t.append (coerce(s1))

def lines(sFilename, fun):
    src = io.open(sFilename)
    while true:
        s = src.readline()
        if s:
            fun(s)
        else:
            return src.close()

#not sure if this is right
def csv(filename, fun):
    lines(sFilename=filename, fun=fun(cells(lines)))

# emulate printf
# doesnt work correctly because string.format in python uses {} not % operators
# fmt function not used because of above, instead where function is used, the 
# formatting is done there
def fmt(self, sControl, *argv):
    return sControl.format(*argv)

# print `t` then return it
def oo(t):
    td = t.__dict__
    td['a'] = t.__class__.__name__
    td['id'] = id(t)
    print(dict(sorted(td.items())))

# convert `t` to a string. sort named keys. 
def o(t):
    if type(t)!=dict and type(t)!=list:
        return str(t)
    
    def fun(k,v):
        if(str(k).find('_')!=0):
            v = o(v)
            return ":" + str(k) + " " + o(v)
        
        else:
            return False
    array = []
    if type(t) == dict:
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
    elif type(t) == list:
        array = t
    return "{" + " ".join(str(val) for val in array) + "}"
