"""
this module evaluates prefix operator boolean logic notation
e.g. and or var1 var2 xor var3 var4
"""
def stringVal(bool):
    if bool:
        return "true"
    else:
        return "false"
def convertBool(val,vars):
    if val == "false" or val == False:
        return False
    elif val == "true" or val == True:
        return True
    else:
        return convertBool(vars[val],vars)
def evaluate(exp,vars):
    """
    evaluates boolean expression exp with vars in dictionary vars
    exp: string
    vars: dict
    returns: boolean
    """
    #TODO this should raise a incorrectly formatted expression exception
    if type(exp).__name__ in ('str','unicode'):
        return evaluate(exp.split(),vars)
    
    operators = ("and","or")
    t = exp
    while 1:
        flag = False
        for i in range(len(t)):
            if t[i] in operators:
                if t[i+1] not in operators and t[i+2] not in operators:
                    if t[i] == "and":
                        #print "AND", convertBool(t[i+1],vars), convertBool(t[i+2],vars)
                        r = stringVal(convertBool(t[i+1],vars) and convertBool(t[i+2],vars))
                    elif t[i] == "or":
                        #print "OR", convertBool(t[i+1],vars), convertBool(t[i+2],vars)
                        r = stringVal(convertBool(t[i+1],vars) or convertBool(t[i+2],vars))
                    else:
                        raise Exception()
                        r = "false" #this case is impossible
                    t.pop(i+1)
                    t.pop(i+1)
                    t.pop(i)
                    t.insert(i,r)
                    flag = True
                    break
        if not flag:    #only one thing left
            if len(t) > 1:
                raise Exception()
                #return False
            if t[0] == "false":
                return False
            elif t[0] == "true":
                return True
            else:
                raise Exception()
                return False    #or raise error