from Utilities.datastructure import BinaryTreeNode
def binary_count_runner():
    #utility_obj = Utility()
    binary_obj = BinaryTreeNode()
    print('Enter How many nodes you want to insert into list')
    try:
        nodes_count=int(input("Enter How many nodes you want to insert into the list"))
    except:
        print("Enter Number of nodes in integer only")
    nodes_list = []
    print('Now Enter all test cases')
    for i in range(0, nodes_count):
        nodes_list.append(int(input()))

    result = binary_obj.count_binary_search_tree(nodes_list)
    print("No of Binary tree possible in each test case is as follows")
    for i in result:
        print(i)


if __name__ == "__main__":
    binary_count_runner()