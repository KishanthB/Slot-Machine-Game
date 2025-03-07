import random
def spin_row():
    symbols=["🍒","🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("**************")
    print(" ".join(row))
    print("**************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*200
        elif row[0]=="🍉":
            return bet*300
        elif row[0]=="🍋":
            return bet*400
        elif row[0]=="🔔":
            return bet*1000
        elif row[0]=="⭐":
            return bet*10000
    return 0

def main():
    print("PYTHON SLOT MACHINES ")
    print("***********************")
    print("🍒","🍉","🍋","🔔","⭐")
    print("***********************")
    Balance=100

    while Balance>0:
        print(f"Current Balance: ${Balance}")
        Bet=input("Place Your Bet: $")
        if not Bet.isdigit():
            print("Invalid Bet")
            continue
        Bet=int(Bet)
        if Bet>Balance:
            print("Insuffecient Balance")
            continue
        if Bet<=0:
            print("Bet must be greater than 0")
            continue
        Balance-=Bet
        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=get_payout(row,Bet)
        if payout>0:
            print(f"You Won : ${payout}")
        else:
            print("You Lost! Try Again")
        Balance+=payout
        choice=input("Do You Want to Continue? (Y/N): ").upper()
        if choice=="Y":
            continue
        else:
            break
    print("********************************")
    print(f"Your New Balance is: ${Balance}")
    print("********************************")

    print("************")
    print("THANK YOU!!!")
    print("************")


if __name__=="__main__":
    main()
