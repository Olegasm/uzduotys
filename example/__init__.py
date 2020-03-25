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
    check_file(out, open("1.txt").read())

def check_file(output, correct):
    if output == correct:
        return
    
    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)    
