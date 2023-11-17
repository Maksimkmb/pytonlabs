import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./data/russia_losses_personnel.csv', sep=',')
data = data.fillna(0)


data_copy = data.copy()


first_value_to_save = data['personnel'][0]
data_copy['personnel'] = data_copy['personnel'].diff().fillna(first_value_to_save)

max_losses = data_copy['personnel'].max()
min_losses = data_copy['personnel'].min()
avg_losses = data_copy['personnel'].mean()


index_max_value = data_copy['personnel'].idxmax()
index_min_value = data_copy['personnel'].idxmin()
index_avg_value = data_copy['personnel'].sub(avg_losses).abs().idxmin()


train_size = len(data_copy)
train_data = data_copy['personnel'][:train_size]


def arima_forecast(data, p, d, q, steps_to_predict):
    forecast = []
    history = list(data)
    for i in range(len(data), len(data) + steps_to_predict):
        diff = [history[j] - history[j - 1] for j in range(1, len(history))]
        model = 0
        if d == 1:
            model = history[-1] + diff[-p] + sum(diff[-(q+1):-1])
        else:
            model = history[-1] + sum(diff[-p:]) + sum(diff[-(q+1):-1])
        forecast.append(model)
        history.append(model)
    return forecast


steps_to_predict = 500
forecast = arima_forecast(train_data, p=1, d=1, q=1, steps_to_predict=steps_to_predict)


forecast_index = range(train_size, train_size + steps_to_predict)
forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['personnel'])


plt.plot(range(train_size), train_data, label='Train')
plt.plot(forecast_index, forecast, label='Forecast', linestyle='--', color='red')
plt.xlabel('Дні')
plt.ylabel('Втрати русні')
plt.title('Прогноз втрат русні')


plt.bar(data_copy.index, data_copy['personnel'], alpha=0.5, label='Втрати русні')


plt.scatter(index_max_value, max_losses, marker='o', color='blue', label='Максимальні втрати')
plt.scatter(index_min_value, min_losses, marker='o', color='yellow', label='Мінімальні втрати')
plt.scatter(index_avg_value, avg_losses, marker='o', color='green', label='Середні втрати')


plt.legend()
plt.show()
