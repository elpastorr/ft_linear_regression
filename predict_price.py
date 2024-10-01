import csv

def normalize(mileages, mileage):
	return ((mileage - min(mileages)) / (max(mileages) - min(mileages)))

def denormalize(prices, price):
	return ((price * (max(prices) - min(prices))) + min(prices))

def	getThetas():
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
	if (theta0 == 0 and theta1 == 0):
		print("Warning, model not trained !")
	return (theta0, theta1)

def	getData():
	try:
		file = open("data.csv", 'r')
		reader = csv.reader(file)
		data = []
		for row in reader:
			data.append(row)
		data.remove(data[0])

		mileages = []
		prices = []
		for row in data:
			mileages.append(float(row[0]))
			prices.append(float(row[1]))
	except:
		print("Error: missing data")
		file.close()
		exit()

	if len(mileages) == 0 or len(prices) == 0:
		print("Error: missing data")
		file.close()
		exit()

	file.close()	
	return(mileages, prices)

def predictPrice(mileage):
	theta0, theta1 = getThetas()
	mileages, prices = getData()
	return (denormalize(prices, theta0 + (theta1 * normalize(mileages, mileage))))

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

	print("Price :", predictPrice(nb_mileage))

if __name__ == '__main__':
    main()