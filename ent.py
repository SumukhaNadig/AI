def extend(s, var, val):
    s2 = s.copy()
    s2[var] = val
    return s2

KB = 'A&B'
query = 'A'

model = {'A':'False','B':'False','C':'False'}


def findsymb(exp):
	li = []
	for s in exp:
		if s.isalpha():
			li.append(s)

	return li


def tt_entails(KB,query):
	distch = findsymb(query)
	return tt_check(KB,query,distch,model)

def tt_check(KB,query,symb,model):
	if len(symb) == 0:
		if pl_true(KB, model):
			return pl_true(query, model)
		else:
			return True
	else:
		P, rest = symb[0], symb[1:]
		return (tt_check(KB, query, rest, extend(model, P, True)) and tt_check(KB, query, rest, extend(model, P, False)))

def pl_true(exp,model):
	return eval(exp.replace('&', ' and ').replace('|', ' or ').replace('!', ' not ').replace('A',str(model['A'])).replace('B',str(model['B'])).replace('C',str(model['C'])))

ab = tt_entails(KB,query)
print(str(ab))








