(lambda x:print("\n".join((lambda y:[*y,*y[::-1][1:]])(list(dict.fromkeys([x[0:i].strip() for i in range(1,len(x)+1)]))))))(input("> "))