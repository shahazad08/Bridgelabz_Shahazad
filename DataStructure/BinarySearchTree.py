from Utilities.datastructure import BinarySearchTree
def binarysearchtree():
    b=BinarySearchTree()
    try:
        x=int(input("Enter the Number of Nodes:"))
    except ValueError:
        print("Enter integer value")
    b.count(x)


if __name__ == "__main__":
    binarysearchtree()

