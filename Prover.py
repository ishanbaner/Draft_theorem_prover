class Prover:

    def __init__(self):
       self.vars=[]
       self.lemmas=[]
       self.vals={}

    def addVars(self,v):
        self.vars+=[v]

    def Printvars(self):
        print(self.vars)

    def addLemmas(self,lemma):
        self.lemmas+=[lemma]

    def assumeTrue(self,block):
        if isinstance(block, str):
            self.vals[block]=True
            self.addVars(block)
        else:
            self.addLemmas(block)
            if block[1]=='and':
                self.assumeTrue(block[0])
                self.assumeTrue(block[2])
            if block[1]=='imp':
                if block[0] in self.vals.keys() and self.vals[block[0]]:  
                    self.assumeTrue(block[2])

    def assumeFalse(self,block):
        if isinstance(block, str):
            self.vals[block]=False
            self.addVars(block)
        else:
            self.addLemmas(block)
            if block[1]=='or':
                self.assumeFalse(block[0])
                self.assumeFalse(block[2])
    
    def checker(self,block):
        if block==True:
            return(True)
        if block==False:
            return(False)
        if isinstance(block, str):
            if block in self.vars:
                return(self.vals[block])
        else:
            if block[1]=='and':
                return(self.checker(block[0]) and self.checker(block[2])) 
            elif block[1]=='or':
                return(self.checker(block[0]) or self.checker(block[2]))
            elif block[0]=='not':
                return(not self.checker(block[1]))
            elif block[1]=='imp':
            
                if self.checker(block[0])==True and self.checker(block[2])==False:
                    return(False)
                if self.checker(block[0])==True and self.checker(block[2])==True:
                    return(True)
                if self.checker(block[0])==False:
                    return(True)
                if self.checker(block[2])==True:
                    return(True)
                
    
    def proof(self,block):
        if isinstance(block, str):
            if block in self.vars:
                print(self.vals[block])
                return(self.vals[block])
        else:
            if block[1]=='and':
                if isinstance(block[0], str) and isinstance(block[2], str):
                    print('I|=',block[0],' and ',block[2])
                    print('I|=',block[0],' and ','I|=',block[2])
                    print(self.checker(block[0]),' and ',self.checker(block[2])) 
                    print((self.checker(block[0])) and (self.checker(block[2])))
                    print("---------------------------")
                    return((self.checker(block[0])) and (self.checker(block[2])))
                else:
                    print('I|=',block[0],' and ',block[2])
                    print('I|=',block[0],' and ','I|=',block[2])
                    print(self.proof(block[0]),' and ',self.proof(block[2]))
                    print((self.checker(block[0])) and (self.checker(block[2])))
                    print("---------------------------")
                    return((self.checker(block[0])) and (self.checker(block[2])))

            elif block[1]=='or':
                if isinstance(block[0], str) or isinstance(block[2], str):
                    print('I|=',block[0],' or ',block[2])
                    print('I|=',block[0],' or ','I|=',block[2])
                    print(self.checker(block[0]),' or ',self.checker(block[2]))
                    print((self.checker(block[0])) or (self.checker(block[2])))
                    print("---------------------------")
                    return((self.checker(block[0])) or (self.checker(block[2])))
                else:
                    print('I|=',block[0],' or ',block[2])
                    print('I|=',block[0],' or ','I|=',block[2])
                    print(self.proof(block[0]),' or ',self.proof(block[2]))
                    print((self.checker(block[0])) or (self.checker(block[2])))
                    print("---------------------------")
                    print("Final answer:",self.checker(block))
                    return((self.checker(block[0])) or (self.checker(block[2])))

            elif block[0]=='not':
                if isinstance(block[1], str):
                    print('I|=',' not ',block[1])
                    print(not self.checker(block[1]))
                    print("---------------------------")
                    return(not (self.checker(block[1])))
                else:
                    print('I|=',' not ',block[1])
                    print('I|= not ',self.proof(block[1]))
                    print(not self.checker(block[1]))
                    print("---------------------------")
                    print("Final answer:",self.checker(block))
                    return(not (self.checker(block[1])))

            elif block[1]=='imp':
                print('I|=',block[0],' imp ',block[2])
                if self.checker(block)==None and self.checker(block[0])==None:
                    print("Assming ",block[0]," true")
                    self.assumeTrue(block[0])
                for i in range(len(self.lemmas)):
                    for j in range(len(self.lemmas)):
                        self.assumeTrue(self.lemmas[j])
                if self.checker(block[2])==None:
                    print("Not provable")
                else:
                    print('I|=',block[0],' imp ','I|=',block[2])
                    print(self.proof(block[0]),' imp ',self.proof(block[2]))
                    print(block,"|=",self.checker(block))
                    print("---------------------------")
                print("Final answer:",self.checker(block))
                return(self.checker(block))

Prove = Prover()

#Test cases

#Prove.assumeTrue('a')
#Prove.assumeFalse('b')
#Prove.proof([['a', 'imp', 'b'], 'imp', [['a', 'and', ['not', 'b']], 'imp', 'a']])

#Prove.assumeTrue('a')
#Prove.proof(['a', 'and', ['not', 'a']])

#Prove.proof(['p','imp',['q','imp','p']])

#Prove.assumeTrue(['P','imp','Q'])
#Prove.assumeTrue(['Q','imp','R'])
#Prove.proof(['P','imp','R'])

#Prove = Prover()
#Prove.assumeTrue('a')
#Prove.proof(['a', 'imp', ['a', 'or', 'b']])
