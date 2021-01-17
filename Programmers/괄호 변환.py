def solution(p):
    if p == '':
        return ''
    if is_right(p):
        return p

    return dfs(p)


def dfs(v):
    
    for i in range(1, len(v) + 1):
        if is_balanced(v[:i]):
            concat = dfs(v[i:]) or ''

            if is_right(v[:i]):
                return v[:i] + concat
            else:
                return '(' + concat + ')' + make_reverse(v[1:i-1])


def is_balanced(s):
    return s.count('(') == s.count(')')


def is_right(s):
    stack = []
    try:
        for i in s:
            if i == "(":
                stack.append('foo')
            else:
                stack.pop()
    except:
        return False
    return True

def make_reverse(s):
    res = []
    for i in s:
        if i == "(":
            res.append(")")
        else:
            res.append("(")
            
    return ''.join(res)