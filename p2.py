from p1 import Stack
def icp(item):
    if item in"+-":
        return 1
    elif item in "*/%":
        return 2
    elif item=="^":
        return 3
    elif item in "()":
        return 4
def isp(item):
    if not item or item in "()":
        return 0
    elif item in "+-":
        return 1
    elif item in "*/%":
        return 2
    elif item=="^":
        return 3
    
def intopre(infix):
    op=Stack()
    infix=infix[::-1]
    prefix=""
    for item in infix:
        if item in '+-*/%^()':
            past=op.pop()
            if not past:
                op.push(item)
            else :
                if item=="(":
                    while past!=")":
                        prefix+=past
                        past=op.pop()
                else:
                    while past and icp(item)<=isp(past):
                        prefix+=past
                        past=op.pop()
                    op.push(past)
                    op.push(item)
        else:
            prefix+=item
            
    past=op.pop ()
    while past:
        prefix+=past
        past=op.pop()
        prefix=prefix[::-1]
    return prefix

def intopost(infix):
    op=Stack()
    postfix=""
    for item in infix:
        if item in '+-*/%^()':
            past=op.pop()
            if not past:
                op.push(item)
            else :
                if item==")":
                    while past!="(":
                        postfix+=past
                        past=op.pop()
                else:
                    while past and icp(item)<=isp(past):
                        postfix+=past
                        past=op.pop()
                    op.push(past)
                    op.push(item)
        else:
            postfix+=item
            
    past=op.pop ()
    while past:
        postfix+=past
        past=op.pop()
    return postfix

def posttoin(postfix):
    op=Stack()
    for item in postfix:
        if item in '+-*/%^':
            oprand2=op.pop()
            oprand1=op.pop()
            newoprand='('+ oprand1+item+oprand2+')'
            op.push(newoprand)
        else:
            op.push(item)   
    infix = op.pop()
    return infix

def pretoin(prefix):
    op=Stack()
    #prefix reverse -> postfix
    for item in prefix[::-1]:
        if item in '+-*/%^':
            oprand2=op.pop()
            oprand1=op.pop()
            newoprand=')'+ oprand1+item+oprand2+'('
            op.push(newoprand)
        else:
            op.push(item)   
    infix = op.pop()
    infix = infix[::-1]
    return infix

def pretopost(prefix):
    infix=pretoin(prefix)
    postfix=intopost(infix)
    return postfix

def posttopre(postfix):
    infix=posttoin(postfix)
    prefix=intopre(infix)
    return prefix

def evaluate(expression,format):
    op=Stack()
    if format=='infix':
        expression=intopost(expression)
    if format=='prefix' :
        expression=pretopost(expression)
    for item in expression:
        if item in '+-*/%^' :
            oprand2=float(op.pop())
            oprand1=float(op.pop())
            if item=='+':
                op.push(oprand1+oprand2)
            elif item=='-':
                op.push(oprand1-oprand2)
            elif item=='*':
                op.push(oprand1*oprand2)
            elif item=='/':
                op.push(oprand1/oprand2)
            elif item=='%':
                op.push(oprand1%oprand2)
            elif item=='^':
                op.push(oprand1**oprand2)
        else:
            op.push(item)
    ans=op.pop()
    return ans