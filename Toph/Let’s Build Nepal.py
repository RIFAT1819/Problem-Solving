def can_form_nepal(S):
    word = "nepal"
    for char in word:
        if char in S:
            index = S.index(char)
            S = S[:index] + S[index+1:]
        else:
            return False
    return True


def main():
    T = int(input())
    for _ in range(T):
        # Input string
        S = input().strip()

        # Check if "nepal" can be formed
        if can_form_nepal(S):
            print("Maile Nepal banauna sakchhu!!")
        else:
            print("Hami sabai milera Nepal Banau hai!!")

if __name__ == "__main__":
    main()
