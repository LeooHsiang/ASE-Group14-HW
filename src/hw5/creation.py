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

    def num(n: int, s: str): 
        if n is not None: 
            ata = n 
        else: 
            ata = 0 

        if s is not None:
            txta = s 
        else: 
            txta = ""

        if txta.find("-$"): 
            w = -1
        else: 
            w = 1
        
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

    def col(self, n: int, s: str):

        if s.find("[A-Z]"): 
            col = self.num(n, s)
        else: 
            col = self.sym(n, s)
        
        if col.txt.find("X$"): 
            col.isIgnored = True
        else: 
            col.isIgnored = False

        if col.txt.find("!$"): 
            col.isKlass = True
        else: 
            col.isKlass = False
        
        if col.txt.find("[!+-]$"): 
            col.isGoal = True
        else: 
            col.isGoal = False

        return col 