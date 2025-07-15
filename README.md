# About
Draft_theorem_prover is a simple algorithms based theorem prover that uses first order logic. It's still in it's basic form, involing operations like and, not, or and implies, and need improvements. Any comments on the same will be extremely helpful. Below, are few examples, showing how the prover works.

#Example 1
```Prove.assumeTrue('a')
Prove.assumeFalse('b')
Prove.proof([['a', 'imp', 'b'], 'imp', [['a', 'and', ['not', 'b']], 'imp', 'a']])
