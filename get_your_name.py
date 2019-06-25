class New_hw():
    def return_name(self, name):
        self.name = name

    def numbers(self):
        number = []
        user_input = input('Enter numbers\n')
        user_input.split(',')
        new_i = int(user_input)
        result = sum(number)/len(number)
        return result


test = New_hw()
test.return_name(name='Ruslan')
test.numbers()
