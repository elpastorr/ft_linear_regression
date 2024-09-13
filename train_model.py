import csv
import matplotlib.pyplot as plt

def graphData(mileages, prices, theta0, theta1) -> None:
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.plot(mileages, prices, 'ro')
	plt.plot(mileages, [theta0 + theta1 * x for x in mileages])
	plt.show()

def main() -> None:
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

	try:
		avgKm = sum(mileages) / len(mileages)	#avg: average
		avgPrice = sum(prices) / len(prices)

		errorKms = []
		for row in mileages:
			errorKms.append(row - avgKm)

		errorPrices = []
		for row in prices:
			errorPrices.append(row - avgPrice)

		sum_error_km_sqrd = 0
		for row in errorKms:
			sum_error_km_sqrd += row * row

		product = 0
		for i in range(len(mileages)):
			product += errorKms[i] * errorPrices[i]

		theta1 = product / sum_error_km_sqrd
		theta0 = avgPrice - (theta1 * avgKm)

	except:
		print("Error: data corrupted")
		file.close()
		exit()

	file.close()

	thetas = [theta0, theta1]
	output = open("thetas.csv", 'w')
	writer = csv.writer(output)
	writer.writerow(thetas)
	output.close()

	print("Training completed !")
	graphData(mileages, prices, theta0, theta1)


if __name__ == '__main__':
    main()
