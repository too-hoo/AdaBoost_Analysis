from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor

# 加载数据
data = load_boston()
# 分割数据
train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.25, random_state=33)
# 使用AdaBoost回归模型
regressor = AdaBoostRegressor()
regressor.fit(train_x, train_y)
# 回归测试集预测
pred_y = regressor.predict(test_x) 
# 计算均方误差
mse = mean_squared_error(test_y, pred_y)
print("房价预测结果", pred_y)
print("均方误差 = ",round(mse,2))

# AdaBoost与其他的分类器的对比

# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_boston
# from sklearn.metrics import mean_squared_error
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.ensemble import AdaBoostRegressor

# # 加载数据
# data = load_boston()
# # 分割数据(训练，测试交替：训练-测试；训练-测试)
# train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.25, random_state=33)

# # 使用决策树回归模型
# dec_regressor = DecisionTreeRegressor()
# dec_regressor.fit(train_x, train_y)
# pred_y = dec_regressor.predict(test_x)
# mse = mean_squared_error(test_y, pred_y)
# print("决策树均方误差 =",round(mse,2))
# # 使用KNN回归模型
# knn_regressor = KNeighborsRegressor()
# knn_regressor.fit(train_x, train_y)
# pred_y = knn_regressor.predict(test_x)
# mse = mean_squared_error(test_y, pred_y)
# print("KNN均方误差 = ", round(mse, 2))