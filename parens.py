def addParen(count, before, after, l):
	if count == 1:
		l.append(before + "()" + after)
	else:
		addParen(count - 1, before+"()", after, l)
		addParen(count - 1, before+"(", ")" + after, l)
		addParen(count - 1, before, "()" + after, l)

l = []
addParen(3, "", "", l)
print(set(l))
