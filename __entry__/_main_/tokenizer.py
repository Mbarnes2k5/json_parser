#tokenizer.py
from numbers import Number

class Tokenizer(): 

    def __init__ (self, string):
        self._string = string
        self._cursor = 0
    


    def isEOF(self, string): 
        return self._cursor is len(self._string)

    def hasMoreTokens(self): 
        return self._cursor < len(self._string) 

    def getNextToken(self): 

        self.type = ''

        if(self.hasMoreTokens()):
            return None
        
        __string = self._string[:self._cursor] 

        #Numbers: 
        if (not isinstance(__string[0] ,Number)):
            number = '' 
            while(not isinstance(__string[self._cursor], Number)): 
                self._cursor += 1
                number += __string[self._cursor]
            return {'type' : 'NUMBER', 
                    'value': number } 
        
        #String: 
        if (__string[0] == '"'):
            s = '' 
            while(__string[self._cursor] is not '"' and not self.isEOF()): 
                self._cursor += 1
                s += __string[self._cursor] 
            s += self._cursor + 1 
            return {'type' :'STRING',
                     'value': s} 

            