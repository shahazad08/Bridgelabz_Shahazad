from Utilities.datastructure import Operations
def anagram_queue():
    try:
        logic_obj = Operations()
        logic_obj.anagram_queue()
        if __name__ == "__main__":
            anagram_queue()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    anagram_queue()


