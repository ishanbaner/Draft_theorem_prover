# About
Draft_theorem_prover is a simple algorithm-based theorem prover that uses first-order logic. It's still in its basic form, involving operations like and, not, or, and implies, and needs improvements. Any comments on the same will be extremely helpful. Below are a few examples showing how the prover works.

## Example 1
```
Prove.assumeTrue('a')
Prove.assumeFalse('b')
Prove.proof(['a','imp',['a','or','b']])
```
## Output 1
```
I|= a  imp  ['a', 'or', 'b']
I|= a  imp  I|= ['a', 'or', 'b']
True
I|= a  or  b
I|= a  or  I|= b
True  or  False
True
---------------------------
True  imp  True
['a', 'imp', ['a', 'or', 'b']] |= True
---------------------------
Final answer: True
'''
