def login(name,pwd):
    if name=="RG" and pwd=="ILI":
        return "Login Success"
    else:
        return "Logout Failed"
    
msg1=login("RG","ILI")
msg2=login("SG","ILI")
print(msg1) 
print(msg2)