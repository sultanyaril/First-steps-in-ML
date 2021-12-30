class BankCard:
    def __init__(self, total_sum):
        self.total_sum = total_sum

    def __getattr__(self, name):
        if self.total_sum == 0:
            raise ValueError("Not enough money to learn the balance")
        self.total_sum -= 1
        return self.total_sum

    def __repr__(self):
        return "To learn the balance you should put the money on \
the card, spent some money or get the bank data. The last \
procedure is not free and costs 1 dollar."

    def __call__(self, sum_spent):
        if self.total_sum < sum_spent:
            return ValueError("Not enough money to spent " + str(sum_spent) + "dollars")
        self.total_sum -= sum_spent
        print("You spent", sum_spent, "dollars.", self.total_sum, "dollars are left.")

    def put(self, sum_put):
        self.total_sum += sum_put;
        print("You put", sum_put, "dollars.", self.total_sum, "dollars are left.")
    
#    def balance(self):
#        if self.total_sum == 0:
#            raise ValueError("Not enough money to learn the balance")
#        self.total_sum -= 1
#        return self.total_sum
 
if __name__ == "__main__":
    a = BankCard(10)
    print(a)
    a(5)
    print(a.balance)
