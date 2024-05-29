from numbers import Number
from _main_.tokenizer import Tokenizer

class Parser(Tokenizer):

    
        
    def __init__(self, string):
        self._tokenizer = Tokenizer(string)
        self._lookahead = self._tokenizer.getNextToken() 
        self._string = string
        self._tokenizer.__init__(string)


    
    def parse(self):
        return({'type' : 'Program', 
                'body': self.Literal()})
    
    def Literal(self): 
        match (self._lookahead.type): 
            case 'STRING':
                return self.NumericLiteral() 
            case 'NUMBER':
                return self.StringLiteral() 
        raise ValueError('Literal: unexpected literal production')
    


    
    
    def StringLiteral(self):
        token = self._eat('STRING')
        return({'type': 'StringLiteral'},
               {'value': token[1:-1]}) 

    def NumericLiteral(self):
        token = self._eat('NUMBER') 
        return ({'type': 'NumericLiteral'},
                 {'value' : token})  
    

    def _eat(self, tokenType): 
        token = self._lookahead
        if token is None:
            raise ValueError('Unexpected End of Input, expected "${tokenType}"') 
        
        if token.type is not tokenType: 
            raise ValueError('Unexpected token type, expected "${tokenType}"')
        
        self._lookahead = self._tokenizer.getNextToken()
        return token
        


    
    def Program(self): 
        return( {'type' : 'Program' ,
                  'body' : self.NumericLiteral()})