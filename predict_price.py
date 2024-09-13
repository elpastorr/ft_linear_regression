import csv

def predictPrice(mileage):
	try:
		file = open("thetas.csv", 'r')
		reader = csv.reader(file)
	except:
		print("Error: missing thetas.csv")
		exit()
	thetas = []
	try:
		for row in reader:
			thetas = row
		theta0 = float(thetas[0])
		theta1 = float(thetas[1])
	except:
		print("Error: missing theta data")
		file.close()
		exit()
	file.close()
	return (theta0 + (theta1 * mileage))

def main() -> None:
	check = False
	while check == False :
		mileage = input("Enter mileage: ")
		try:
			nb_mileage = float(mileage)
			if (nb_mileage >= 0):
				check = True
			else:
				print("Error: negative mileage")
		except:
			print("Error: not a valid number")
	print(predictPrice(nb_mileage))

if __name__ == '__main__':
    main()