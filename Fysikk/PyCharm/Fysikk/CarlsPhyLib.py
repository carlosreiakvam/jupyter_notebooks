from numpy.polynomial import Polynomial as P


#TODO: returner printout for vi, vj, ai og aj
# a + bt + ct^2 + dt^3
def polyDeriv(a, b, c, d, t,m):
    ri = P([d, c, b, a])
    ri = P.deriv(ri,m)
    return ri(t)

#TODO: lag funksjon som regner vektorlengde basert på x,y verdier
# typ sqrt(x^2 + y^2)
