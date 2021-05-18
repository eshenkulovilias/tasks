# import unittest
#
#
# def add(x1, x2):
#     return x1 + x2
#
#
# def multiply(x1, x2):
#     return x1 * x2
#
#
# def subtract(x1, x2):
#     return x1 - x2
#
#
# def divide(x1, x2):
#     if x2 != 0:
#         return x1 / x2
#
#
# class TestCalculator(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(4, 7), 11)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(10, 5), 5)
#
#     def test_multiply(self):
#         self.assertEqual(multiply(3, 7), 21)
#
#     def test_divide(self):
#         self.assertEqual(divide(10, 2), 5)
#

text = 'Advertising companies say advertising is necessary and important. It informs people about new products. ' \
       'Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. ' \
       'Sometimes they are mini-dramas and we wait for the next program in the mini-drama. ' \
       'Advertising can educate, too. Adverts tell us about new, healthy products. ' \
       'And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. ' \
       'Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. ' \
       'They say that advertising is bad for children. Adverts make children ‘pester’ ' \
       'their parents buy things for them. Advertisers know we love our children and want to give them everything. ' \
       'So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is ' \
       'advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people ' \
       'waste their money.'

count_of_letter1 = text.count('s')
count_of_letter2 = text.count('t')
print(count_of_letter1, count_of_letter2)

text = text.lower()
# print(text)
lst = text.split()
# print(lst)
for i in lst:
    if i[:6] == 'advert':
        i = 'qwe'
print(lst)