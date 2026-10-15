#subroutine that constructs and evaluates a line that goes through the points (x0, f (x0)) and
#(x1, f (x1)) at a point α.

def linebetween(x0,fx0,x1,fx1):
    y = lambda alpha: x0 + ((fx1-fx0)/(x1-x0))*(alpha - x0)
    return y
