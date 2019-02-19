class Paperboy:

        # experince means the number of papers they have delivered
    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.papers_delivered = experience
        self.earnings = earnings

    def __str___(self):
        return "This is a paperboy. Their name is {}, they have delivered {} papers so far and have earned {} dollars".format(self.name, self.papers_delivered, self.earnings)

    def quota(self):
        return (self.papers_delivered * 0.5 + 50)

    def deliver(self, start_address, end_address):
        total_houses = end_address - start_address + 1
        new_quota = self.quota()
        if total_houses == new_quota:                #if you met your quoata for the day
            money_gained = (0.25 * total_houses)
        elif total_houses < new_quota:               # if you fell beneath your quota
            money_gained = (0.25 * total_houses) - 2
        elif total_houses > new_quota:               #if you exceeded your quota you will get a bonus
            money_gained = (0.25 * total_houses) + (0.50 * (total_houses - new_quota))

        self.papers_delivered += total_houses
        self.earnings += money_gained
        return money_gained

    def report(self):
        return "I'm {} and I've delivered {} papers so far and I have earned {:.2f} so far!" .format(self.name,self.papers_delivered,self.earnings)

tommy = Paperboy("Tommy")

print(tommy.quota()) #  50
print(tommy.deliver(101, 160)) # 20
print(tommy.earnings) # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $20.00 so far!"

print(tommy.quota()) # 80
print(tommy.deliver(1, 75)) # 16.75
print(tommy.earnings)# 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $36.75 so far!"
