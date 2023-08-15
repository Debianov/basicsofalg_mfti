"""Решение из интернетов."""

import sys
from collections import deque
 
def prec(c):
 
	if c == '*' or c == '/':
		return 3
	if c == '+' or c == '-':
		return 4
	if c == '&':
		return 8
	if c == '^':
		return 9
	if c == '|':
		return 10
	return sys.maxsize

def isOperand(c):
   return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
 
def infixToPostfix(infix):
	if not infix or not len(infix):
		return True
	s = deque()
	postfix = ''
	for c in infix:
		if c == '(':
			s.append(c)
		elif c == ')':
			while s[-1] != '(':
				postfix += s.pop()
			s.pop()
		elif isOperand(c):
			postfix += c
		else:
			while s and prec(c) >= prec(s[-1]):
				postfix += s.pop()
			s.append(c)
	while s:
		postfix += s.pop()
	return postfix
 
infix = '(2-3)*(12-10)+4/2'
postfix = infixToPostfix(infix)
print(postfix)