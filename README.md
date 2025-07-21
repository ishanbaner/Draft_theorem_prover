# About
Draft_theorem_prover is a simple algorithm-based theorem prover that uses first-order logic. It's still in its basic form and needs improvements. Comments and suggestions are always welcome. Below are a few examples showing how the prover works.

## Example 1
Considering the expression (a => (a or b)), assuming 'a' to be True and 'b' to be False
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
```

## Example 2
Considering the expression (p => r), assuming 'p => q' and 'q => r'.
```
Prove.assumeTrue(['P','imp','Q'])
Prove.assumeTrue(['Q','imp','R'])
Prove.proof(['P','imp','R'])
```
## Output 2
```
I|= P  imp  R
Assming  P  true
I|= P  imp  I|= R
True
True
True  imp  True
['P', 'imp', 'R'] |= True
---------------------------
Final answer: True
```
# Immediate improvements planning
Along with fixing a few bugs, I need to add operators like for all and exists.
