import itertools

class ticket():
    def __init__(self, id, valid, price):
        self.id = id
        self.valid = valid
        self.price = price
    def __str__(self):
        return f'id:{self.id} val:{self.valid} price:{self.price}'

def cut(tickets, count):
    for i in range(min(31,count)):
        ticketsCount = 0
        for j in range(count):
            if tickets[j].valid == i:
                ticketsCount += 1
        while ticketsCount > i:
            cheapestPosition = -1
            cheapestPrice = 101
            for k in range(count):
                if tickets[k].valid == i and tickets[k].price < cheapestPrice:
                    cheapestPrice = tickets[k].price
                    cheapestPosition = k
            count -= 1
            tickets[cheapestPosition] = tickets[count]
            ticketsCount -= 1
    return count

count = int(input())
n = count
tickets = []

for i in range(count):
    val, pr = map(int, input().split())
    tickets.append(ticket(i,val,pr))
count = cut(tickets, count)
tickets = sorted(tickets[:count], key=lambda x: x.id)
MaxScore = 0
for el in itertools.permutations(tickets):
    profit = 0
    for i in range(count):
        if el[i].valid > i:
            profit += el[i].price*(el[i].valid-i)
    MaxScore = max(MaxScore,profit)

print(MaxScore)
