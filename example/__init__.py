import check50
import check50.c
import filecmp

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
    
@check50.check(compiles)
def test1():
    """tikrina rezultatą"""
    check50.run("./U1 U1rez.txt")
    compare_files("U1rez.txt","1.txt")
    
def compare_files(output, correct):
    if filecmp.cmp(output, correct):
        return 
    raise check50.Mismatch("U1rez.txt", "Nesutampa rezultatas", help=help)
