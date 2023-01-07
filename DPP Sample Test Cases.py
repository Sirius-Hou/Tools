## WRITTEN ASSIGNMENT 3 Q2
## Sequence of Resolution [## MANUAL INPUT REQUIRED ##]
seq = ["R", "P", "Q", "W"]
num = len(seq)

## Set of clauses [## MANUAL INPUT REQUIRED ##]
## FORMAT: ("SYMBOL", NEGATION?("N":YES; 0:NO))
##  Sample: ("P", "N") -> ¬P
S = [[("P", "N"), ("Q", "N"), ("R", "N"), ("W", "N")],
     [("P", "N"), ("Q", "N"), ("R", 0), ("W", 0)],
     [("P", "N"), ("Q", "N"), ("R", "N"), ("W", 0)],
     [("P", 0), ("Q", "N"), ("R", "N"), ("W", "N")],
     [("P", 0), ("Q", 0), ("R", "N")],
     [("P", 0), ("Q", 0), ("W", "N")],
     [("P", "N"), ("R", 0), ("W", 0)],
     [("Q", "N"), ("R", 0), ("W", 0)],
     [("P", "N"), ("Q", 0)],
     [("P", 0), ("Q", "N")],
     [("R", 0)]]


## TUTORIAL 5 Q5
## Sequence of Resolution [## MANUAL INPUT REQUIRED ##]
seq = ["P", "Q", "R", "S", "T"]
num = len(seq)

## Set of clauses [## MANUAL INPUT REQUIRED ##]
## FORMAT: ("SYMBOL", NEGATION?("N":YES; 0:NO))
##  Sample: ("P", "N") -> ¬P
S = [[("P", 0), ("R", "N")],
     [("Q", 0), ("R", "N")],
     [("Q", 0), ("S", "N")],
     [("P", "N"), ("T", 0)],
     [("Q", "N"), ("T", "N")],
     [("Q", "N"), ("R", 0), ("T", 0)],
     [("P", 0), ("S", 0), ("T", "N")],
     [("P", "N"), ("Q", 0), ("R", 0)],
     [("Q", 0), ("R", 0), ("S", 0), ("T", 0)]]
