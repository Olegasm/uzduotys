import check50
import check50.c

@check50.check()
def exists():
    """hello.c egzistuoja"""
    check50.exists("U1.c")
    check50.include("1.txt")
    
@check50.check(exists)
def compiles():
    """U1.c kompiliuojasi."""
    check50.c.compile("U1.c", lcs50=True)
    
@check50.check(compiles)
def test1():
    """Atspausdina korektišką rezultatą"""
    check_file(open("U1rez.txt").read(), open("1.txt").read())

def check_file(output, correct):
    if output == correct:
        return
