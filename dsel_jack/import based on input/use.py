file = open("generatedcode.py",'w')
file.truncate()
toimp = input()
file.write("import " + toimp + " as imp")
file.close()