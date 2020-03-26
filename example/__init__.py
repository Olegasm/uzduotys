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
    compare_files(open("U1rez.txt").read(), open("1.txt").read())
    
def compare_files(output, correct):
    if output == correct:
        return
