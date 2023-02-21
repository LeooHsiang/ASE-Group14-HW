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


def csv(sFilename,fun):
    """
        call `fun` on rows (after coercing cell text)
        :param sFilename: String of the file to read
        :param fun: function to call per each row
    """
    f = io.open(sFilename)
    while True:
        s = f.readline()
        if s:
            t=[]
            for s1 in re.findall("([^,]+)" ,s):
                t.append(coerce(s1))
            fun(t)
        else:
            return f.close()