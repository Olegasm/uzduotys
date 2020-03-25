import check50
import check50.c

@check50.check()
def exists():
    """hello.c egzistuoja"""
    check50.exists("U1.c")
    check50.include("1.txt")
    
@check50.check(exists)
def compiles():
    """U1.c kompiliuojasi"""
    check50.c.compile("U1.c", lcs50=True)

@check50.check(exists)
def isOutput():
    """Rastas U1rez.txt"""
    check50.exists("U1rez.txt") 

@check50.check(isOutput)
def test1():
    """Programa pateikia teisingą rezultatą"""
    out = check50.run("./U1 U1rez.txt")
