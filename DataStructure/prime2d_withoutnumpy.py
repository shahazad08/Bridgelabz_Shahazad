from Utilities.datastructure import PrimeAnagram
def is_prime():
    try:
        p=PrimeAnagram()
        p.prime_number_2d_array()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    is_prime()