from data import Data 
from col import Col 

class Creation():
    """
    Summarizes a stream of numbers. 
    """
    def __init__(self, at: int = 0, txt: str = "") -> None:
        super().__init__()
        # representing column position
        if at: 
            self.at = at
        else: 
            self.at = 0 

        data = Data()

    def range(self, at, txt, lo, hi): 
        hiv = hi if hi != None else lo
        return {
            'at': at, 
            'txt': txt, 
            'lo': lo, 
            'hi': hiv, 
            'y': self.sym(None, None)
        }
    
    def rule(self, ranges, maxSize): 
        t = {}
        for _, range in enumerate(ranges): 
            t.append({'lo': range['lo'], 'hi': range['high'], 'at': range['at']})
            
        return self.prune(t, maxSize)
    
    def prune(self, rule, maxSize): 
        n = 0 
        for txt, ranges in enumerate(rule): 
            n = n + 1 
            if len(ranges) == maxSize[txt]: 
                n = n + 1 
                rule[txt] = None
        if n > 0: 
            return rule 

    def num(n: int, s: str): 

        ata = n if n is not None else 0 
        txta = s if s is not None else ""
        w = -1 if txta.find("-$") else 1
        
        config = {
            'at': ata, 
            'txt': txta, 
            'n': 0, 
            'hi': float('-inf'), 
            'lo': float('inf'), 
            'ok': True, 
            'has': {}, 
            'w': w
        }

        return config

    def sym(n: int, s: str): 
        at = n if n != None else 0
        txt = s if s != None else ""

        return {
            'at': n, 
            'txt': txt, 
            'n': 0, 
            'mode': None, 
            'most': 0, 
            'isSym': True, 
            'has': {}
        }


    def cols(self, ss, col): 
        cols = {
            'names': ss, 
            'all': [], 
            'x': [], 
            'y': []
        }
        for n, s in enumerate(ss): 
            cola = Col(n, s)
            if not cola.isIgnored: 
                if cola.isKlass: 
                    cols.klass = col
                if cola.isGoal: 
                    cols['y'] = cols['y'].append(col)
                else: 
                    cols['x'] = cols['x'].append(col)
            cols['all'] = cols['all'].append(cola)

        return cols 
