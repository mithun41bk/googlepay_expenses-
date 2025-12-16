class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends

        self.balances = {friend: 0 for friend in friends}

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)


        for participant in participants:
            self.balances[participant] -= split_amount


        self.balances[payer] += amount

    def calculate_settlements(self):
        creditors = []
        debtors = []


        for friend, balance in self.balances.items():
            if balance > 0:
                creditors.append((friend, balance))
            elif balance < 0:
                debtors.append((friend, -balance))

        print(f"\n--- Final Balances ---")
        print(self.balances)
        print("\n--- Optimized Settlements ---")

        while debtors and creditors:

            debtor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()

            payment = min(debt_amount, credit_amount)

            print(f"**{debtor} owes {creditor}: ₹{payment:.2f}**")


            if debt_amount > payment:
                remaining_debt = debt_amount - payment

                debtors.append((debtor, remaining_debt))


            if credit_amount > payment:
                remaining_credit = credit_amount - payment
                creditors.append((creditor, remaining_credit))


        if __name__ == "main":
            friends = input("enter the name of friends , seperated by commas:").split(",")
            friends = [friends.strip() for friend in friends ]
            expense_sharing = ExpenseSharing(friends)
            while True:
                payer = input("Enter the name of the person who paid (of 'done' to finish):")
                if payer.lower() == "done":
                    break
                amount = float(input("Enter the amount paid"))
                participants = input("Enter the name of participants for this expense, seperate")
                participants = [participants.strip() for participant in participants]
                expense_sharing.add_expense(payer,amount,participants)
                print("\n Finance settlemnt")
                expense_sharing.calculate_settlement()


