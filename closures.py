def greeter(prefix): #called as factory function
    def greet(name):
        print(f"{prefix} {name}")
    return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")
goodbye("Kyle")