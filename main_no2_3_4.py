import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import kstest, norm

df = pd.read_csv('Walmart.csv',usecols=['Store','Date','Weekly_Sales','Holiday_Flag','Temperature','Fuel_Price','CPI','Unemployment'])

class Nomor2() :
    weekly_sales = df['Weekly_Sales']
    fuel_price = df['Fuel_Price']
    alpha = 0.05

    print('Nomor 2\n')

    statistic, p_value = kstest(weekly_sales, norm.fit(weekly_sales))
    print("Uji Normalitas Weekly Sales:")
    print(f"Statistic: {statistic}")
    print(f"P-value: {p_value}")
    if p_value > alpha:
        print("Weekly Sales didistribusikan secara normal")
    else:
        print("Weekly Sales tidak didistribusikan secara normal")

    statistic, p_value = kstest(fuel_price, norm.fit(fuel_price))
    print("Uji Normalitas Fuel Price:")
    print(f"Statistic: {statistic}")
    print(f"P-value: {p_value}")
    if p_value > alpha:
        print("Fuel Price didistribusikan secara normal")
    else:
        print("Fuel Price tidak didistribusikan secara normal")

class Nomor3() :
    print()
    print('Nomer 3')
    print('3a')
    correlation = df[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr()
    print("Nilai korelasi antara variabel independen dan variabel dependen:")
    print(correlation['Weekly_Sales'])
    
    print('3b')    
    correlation = df[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr()
    negative_correlations = correlation[correlation['Weekly_Sales'] < 0]
    negative_correlations = negative_correlations['Weekly_Sales'].drop('Weekly_Sales', errors='ignore')
    if negative_correlations.empty:
        print("Tidak ada pasangan variabel independen dan dependen dengan korelasi negatif.")
    else:
        print("Pasangan variabel independen dan dependen dengan korelasi negatif:")
        print(negative_correlations)

class Nomor4() :
    print()
    print('Nomer 4')
    data = df[['Fuel_Price', 'Weekly_Sales']]

    X = data[['Fuel_Price']]
    y = data['Weekly_Sales']

    model = LinearRegression()
    model.fit(X, y)

    a = model.intercept_
    b = model.coef_[0]

    print("Model regresi: y = {} + {}x".format(a, b))
    data = df[['Fuel_Price', 'Weekly_Sales']]

    X = data[['Fuel_Price']]
    y = data['Weekly_Sales']

    model = LinearRegression()

    model.fit(X, y)
    y_pred = model.predict(X)
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')

    plt.xlabel('Fuel_Price')
    plt.ylabel('Weekly_Sales')
    plt.title('Linear Regression')

    plt.legend()

    plt.show()