import sys
import os

def translatePDE(input):
    filein = "input/functions/" + input + ".txt"
    fileout = "output/functions/" + input + "-out.txt"
    f = open(filein,'r')
    filedata = f.read()
    f.close()          
    newdata = "//" + input +"-start\n"
    newdata += filedata   

    if "float" in input:
        print(newdata)
        input = input.replace("float/", "")
        newdata = newdata.replace("float "+ input, "public float " + input)
   
   
    if "char" in input:
        input = input.replace("char/", "")
        newdata = newdata.replace("char "+ input, "public char " + input)

    if "boolean" in input:
        input = input.replace("boolean/", "")
        newdata = newdata.replace("boolean "+ input, "public boolean " + input)
        
    if "int" in input:
        input = input.replace("int/", "")
        newdata = newdata.replace("int "+ input, "public int " + input)
        
    if "String" in input:
        input = input.replace("String/", "")
        newdata = newdata.replace("String "+ input, "public String " + input)
        
    if "void" in input:
        input = input.replace("void/", "")
        newdata = newdata.replace("void "+ input, "public void " + input)
   
    keys = open("input/replace/myParent.txt",'r')
    for line in keys:
        newdata = newdata.replace(line.rstrip('\n'), "myParent."+line.rstrip('\n'))

    keys = open("input/replace/PApplet.txt",'r')
    for line in keys:
        newdata = newdata.replace(line.rstrip('\n'), "PApplet."+line.rstrip('\n'))

    keys = open("input/replace/Math.txt",'r')
    for line in keys:
        newdata = newdata.replace(line.rstrip('\n'), "Math."+line.rstrip('\n'))

    newdata = newdata.replace("color", "int")        
    newdata += "\n//" + input +"-end\n"
    f = open(fileout,'w')
    f.write(newdata)
    f.close()
    return;

os.remove("LyceoCodeLib/CodeLib/processing-library-template-master/src/Lyceo/CodeLib/CodeLib.java")
F = open("LyceoCodeLib/CodeLib/processing-library-template-master/src/Lyceo/CodeLib/CodeLib.java",'a')
with open("input/functionList.txt", 'r') as s:

    #first write the essentials in the lib
    F.write("package template.library;\n")
    F.write("import processing.core.*;\n")
    F.write("import processing.core.PApplet;\n")


    F.write("public class CodeLib{\n")
    
    F.write("private PApplet myParent;\n")
    
    v = open("input/vars/vars.txt")
    data = "//vars \n"
    for line in v:
        data += line.replace(line, "private " + line)
    data += "\n"
    F.write(data)
    for line in s:
        translatePDE(input = line.rstrip('\n'))
        p = open("output/functions/" + line.rstrip('\n') + "-out.txt")
        data = p.read()
        F.write(data)
        p.close()

    #end it with the right amount of closing brackets
    F.write("\n}\n")
