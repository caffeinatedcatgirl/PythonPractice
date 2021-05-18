# Each exlimation weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?
# If the left side is heavy, return "Right"; If the left side is heavy, return "Right"; If they are balanced, return "Balance".
# balance("!!","??") == "Right"
# balance("!??","?!!") == "Left"
# balance("!?!!","?!?") == "Left"
# balance("!!???!????","??!!?!!!!!!!") == "Balance"

def balance(left,right):
    lScore = balanceScore(left)
    rScore = balanceScore(right)
    if lScore > rScore:
        return "Left"
    elif lScore < rScore:
        return "Right"
    elif lScore == rScore:
        return "Balance"
    else:
        return "0xDEADBEEF"
def balanceScore(dasString):
    score = 0
    for char in str(dasString):
        if char == "!":
            score += 2
        elif char == "?":
            score += 3
    return score
            
def main():
    print(balance("!!","??"))
    print(balance("!??","?!!"))
    print(balance("!?!!","?!?"))
    print(balance("!!???!????","??!!?!!!!!!!"))

if __name__ == "__main__":
    main()
