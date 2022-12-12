import random

count = 0
start = input('choose the small number of range: ')
start = int(start)
end = input('choose the big number of range: ')
end = int(end)

r = random.randint(start, end)

while True:
	count = count + 1
	print('please enter the number from', start ,'to', end)
	number = input()
	number = int(number)
	if r > number and start < number:
		print('the number is bigger')
		start = number
	elif r < number and end > number:
		print('the number is smaller')
		end = number
	elif r == number:
		print('congraguation, you have guessed', count, 'time!')
		break
	else:
		print('please enter the number in the range')
		