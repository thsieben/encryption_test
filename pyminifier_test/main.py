import helper

# This function imports from another file
def main():
    """
    All main does is print. Testing with pyminifier.
    """

    print("Hello world!")
    H = helper.Helper(3, 4)
    H.printA()

if __name__ == '__main__':
    main()
