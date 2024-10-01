import csv
import matplotlib.pyplot as plt

def graphData(mileages, prices, theta0, theta1) -> None:
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.plot(mileages, prices, 'ro')
	plt.plot(mileages, [theta0 + theta1 * x for x in mileages])
	plt.show()

def normalizeData(data):
	norm_data = []
	for i in range(len(data)):
		norm_data.append((data[i] - min(data)) / (max(data) - min(data)))
	return norm_data

def predictPrice(mileage, thetas):
	return (thetas[0] + (thetas[1] * mileage))

def	getErrors0(mileages, prices, thetas):
	errors = 0
	for i in range(len(mileages)):
		errors += predictPrice(mileages[i], thetas) - prices[i]
	return errors

def	getErrors1(mileages, prices, thetas):
	errors = 0
	for i in range(len(mileages)):
		errors += (predictPrice(mileages[i], thetas) - prices[i]) * mileages[i]
	return errors

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

def	writeThetas(thetas):
	output = open("thetas.csv", 'w')
	writer = csv.writer(output)
	writer.writerow(thetas)
	output.close()	

def main() -> None:
	mileages, prices = getData()

	normalized_mileages = normalizeData(mileages)
	normalized_prices = normalizeData(prices)

	m = len(mileages)
	tmp_thetas = [0, 0]
	learning_rate = 0.1
	iteration_nb = 1000
	for _ in range(iteration_nb):
		thetas = tmp_thetas
		errors0 = getErrors0(normalized_mileages, normalized_prices, thetas)
		errors1 = getErrors1(normalized_mileages, normalized_prices, thetas)
		tmp_thetas[0] -= learning_rate * 1 / m * errors0
		tmp_thetas[1] -= learning_rate * 1 / m * errors1

	writeThetas(thetas)
	print("Training completed !")
	graphData(normalized_prices, normalized_mileages, thetas[0], thetas[1])

if __name__ == '__main__':
	main()