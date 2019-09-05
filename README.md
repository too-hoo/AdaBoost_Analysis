# AdaBoost:使用AdaBoost对房价进行预测

## 总结
1、在使用AdaBoost回归分析对波士顿的房价进行了预测后。因为这是个回归分析的问题，所以可以直接使用sklearn中的AdaBoostRegressor即可，如果是分类。我们使用AdaBoostClassifier。

2、另外可以将AdaBoost分类器、弱分类器和决策分类器做了对比，可以看出经过多个弱分类器组合形成的AdaBoost强分类器，准确率是要明显高于决策树算法。所以AdaBoost的优势在于框架的本身，它通过一种迭代的机制让原本性能不强的分类器组合起来，形成一个强的分类器。

3、其实在实际中，也能找到类似的案例。IBM服务器最求的是单个服务器性能的强大，比如说打造超级服务器。而Google在创建集群的时候，利用了很多的PC级的服务器，将它们组成集群，整体的性能远比一个超级服务器的性能强大。也就是“三个臭皮匠，顶个诸葛亮”。这也就是AdaBoost的价值所在吧。

4、AdaBoost实战
- 工具
    - 构造
        - 分类：AdaBoostClassifier
        - 回归：AdaBoostRegressor
    - 参数
        - base_estimator:弱分类器，可以指定，默认是决策树模型
        - n_estimators：算法的最大迭代次数，也就是分类器的个数
        - learning_rate:学习率，取值在0-1之间，默认是1.0
        - algorithm：采用哪种Boosting算法，默认采用的是SAMME.R
        - random_state:代表随机数种子的设置，默认是None
        - loss:代表损失函数的设置，默认是linear
- 数据集
    - 数据集：506条房屋数据，每条数据包含13个指标，以及房屋的价格
    - 使用AdaBoost回归分析，并与决策树回归，KNN回归结果进行比较
- AdaBoost与决策树的对比
    - AdaBoost使用的弱分类器默认是决策树模型
    - 准确率：AdaBoost>决策树>弱分类器
    - 弱分类器错误率很高，但是将多个弱分类器组合形成的AdaBoost性能要明显好于决策树分类器模型。