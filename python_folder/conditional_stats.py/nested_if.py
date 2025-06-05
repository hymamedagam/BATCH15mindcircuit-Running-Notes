if True:
    print("I am outer if")
    if True:
        print("I am inner if")
    else:
        print("I am inner else")
else:
    print("I am outer else")