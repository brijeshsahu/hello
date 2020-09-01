

#loopstr = "return List.of(new rList("Brijesh1"), new rList("Brijesh2"), new rList("Brijesh3"), new rList("Brijesh4"));"
# loopstr = "return List.of(new rList("Brijesh1"), new rList("Brijesh2")
# appendstr = ", new rList(" + '"' + "Brijesh" + i +'")'

def stringapp ():
    mainstring = "return List.of("
    for i in range (1,601):
        i = str(i)
        appendstr = ", new rList(" + '"' + "Brijesh" + i + '")'
        mainstring = mainstring+appendstr
        # print (mainstring)
    return mainstring
h=stringapp()
print(h)