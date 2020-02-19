class DeadFish(object):
    def __init__(self):
        self.command_options = ['i', 'd', 's', 'o']
        self.commands_user = 0

    def methods_for_your_value(self):
        print(self.command_options[0], '- increments the value')
        print(self.command_options[1], '- decrements the value')
        print(self.command_options[2], '- squares the value')
        print(self.command_options[3], '- outputs the value into the return array')
        while len(self.command_options) > 0:
            user = input('>> ')
            if user == self.command_options[0]:
                self.commands_user += 1
            elif user == self.command_options[1]:
                self.commands_user -= 1
            elif user == self.command_options[2]:
                self.commands_user *= self.commands_user
            elif user == self.command_options[3]:
                self.commands_user = [self.commands_user]
            elif self.commands_user not in self.command_options:
                print('this value could not be used')
            print('your worth', self.commands_user)


settings = DeadFish()
settings.methods_for_your_value()
