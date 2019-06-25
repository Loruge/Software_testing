class New_hw():
    def return_name(self, name):
        return name

    def average(self, *args):
        my_list = []
        result = sum(args)/len(args)
        my_list.append(result)
        return my_list


test = New_hw()
test.return_name(name='Ruslan')
print(test.average(5, 7, 8, 9, 4))
