class SumOfMidpoint(object):
    def __init__(self):
        self.ints = [4, 1, 7, 0, 3, 9]
        self.right_sum = 0
        self.left_sum = 0

    def list_split(self):
        division = int(len(self.ints) / 2)
        self.right_sum = (self.ints[division:])
        self.left_sum = (self.ints[:division])

    def inserts_the_sum_of_the_list_values(self):
        self.right_sum = sum(self.right_sum)
        self.left_sum = sum(self.left_sum)
        print(self.left_sum, self.right_sum)

    def check_if_sums_are_equivalent(self):
        if self.right_sum == self.left_sum:
            print('index', self.ints.index(0))
        if self.right_sum != self.left_sum:
            print('the sum are not equivalent')


apt = SumOfMidpoint()
apt.list_split()
apt.inserts_the_sum_of_the_list_values()
apt.check_if_sums_are_equivalent()
