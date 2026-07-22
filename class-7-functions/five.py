def outer():
    print("Outer function started")

    def inner():
        print("Inner Function") 

    return inner() 

inner=outer()
print(inner)
print(type(inner))
inner()

