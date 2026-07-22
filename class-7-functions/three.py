def outer():
    print("Outer function started")

    def login():
        print("Login Success") 
    def logout():
        pass 
    def inner():
        print("Inner Function") 

outer()
#how to invoke inner function from outside?
#login,logout,inner - inner functions