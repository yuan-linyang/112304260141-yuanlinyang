# 机器学习实验：基于 Word2Vec 的情感预测

## 1. 学生信息
- **姓名**：袁琳杨
- **学号**：112304260141
- **班级**：数据1231

> 注意：姓名和学号必须填写，否则本次实验提交无效。

---

## 2. 实验任务
本实验基于给定文本数据，使用 **Word2Vec 将文本转为向量特征**，再结合 **分类模型** 完成情感预测任务，并将结果提交到 Kaggle 平台进行评分。

本实验重点包括：
- 文本预处理
- Word2Vec 词向量训练或加载
- 句子向量表示
- 分类模型训练
- Kaggle 结果提交与分析

---

## 3. 比赛与提交信息
- **比赛名称**：Bag of Words Meets Bags of Popcorn
- **比赛链接**：https://www.kaggle.com/c/word2vec-nlp-tutorial
- **提交日期**：

- **GitHub 仓库地址**：https://github.com/yuan-linyang/112304260141-yuanlinyang
- **GitHub README 地址**：https://github.com/yuan-linyang/112304260141-yuanlinyang/blob/main/README.md

> 注意：GitHub 仓库首页或 README 页面中，必须能看到"姓名 + 学号"，否则无效。

---

## 4. Kaggle 成绩
请填写你最终提交到 Kaggle 的结果：

- **Public Score**：
- **Private Score**（如有）：
- **排名**（如能看到可填写）：

---

## 5. Kaggle 截图
请在下方插入 Kaggle 提交结果截图，要求能清楚看到分数信息。

![Kaggle 截图](./images/kaggle_score.png)

> 建议将截图保存在 `images` 文件夹中。  
> 截图文件名示例：`2023123456_张三_kaggle_score.png`

---

## 6. 实验方法说明

### （1）文本预处理
请说明你对文本做了哪些处理，例如：
- 分词
- 去停用词
- 去除标点或特殊符号
- 转小写

**我的做法：**  

1. **移除 HTML 标签**：使用 BeautifulSoup 库移除影评中的 HTML 标记
2. **保留字母和空格**：使用正则表达式移除数字和标点符号，但保留字母和空格
3. **转为小写**：将所有文本转换为小写形式
4. **保留否定词**：**关键优化** - 不删除 not、no、never 等否定词，因为这些词对情感判断至关重要
5. **提取短语**：提取包含否定词的短语（如"not good"、"not bad"）和情感短语（如"very good"、"highly recommend"）
6. **不去除停用词**：为了保留否定结构和上下文信息，不去除停用词

**优化点：**
- 传统方法会删除"not"等否定词，导致"not good"被误判为正面情感
- 本实验保留所有否定词，并提取包含否定词的短语作为额外特征
- 对否定词赋予更高的权重（1.5 倍）

---

### （2）Word2Vec 特征表示
请说明你如何使用 Word2Vec，例如：
- 是自己训练 Word2Vec，还是使用已有模型
- 词向量维度是多少
- 句子向量如何得到（平均、加权平均、池化等）

**我的做法：**  

1. **训练方式**：自己训练 Word2Vec 模型，使用训练集的所有影评
2. **模型类型**：Skip-gram 模型（sg=1），对罕见词有更好的表示
3. **词向量维度**：300 维
4. **最小词频**：10（降低阈值以保留更多词汇）
5. **上下文窗口**：10 个词
6. **句子向量**：**加权平均** - 对句子中所有词的向量进行加权平均
   - 普通词权重：1.0
   - 否定词权重：1.5（增强否定词的表达能力）
7. **负采样**：5，提高训练效率
8. **训练轮数**：10 个 epoch

**优化点：**
- 使用 Skip-gram 而非 CBOW，对罕见词有更好的向量表示
- 降低最小词频阈值，保留更多情感相关词汇
- 对否定词进行加权，增强模型对否定结构的理解

---

### （3）分类模型
请说明你使用了什么分类模型，例如：
- Logistic Regression
- Random Forest
- SVM
- XGBoost

并说明最终采用了哪一个模型。

**我的做法：**  

**最终模型：逻辑回归（Logistic Regression）**

选择理由：
1. **简单高效**：逻辑回归是线性模型，不易过拟合
2. **适合高维特征**：Word2Vec 生成的 300 维特征适合逻辑回归
3. **概率输出**：可以直接输出属于正面情感的概率
4. **实验验证**：验证集上 AUC 达到 0.94 以上

**模型参数：**
- 正则化强度 C=1.0
- 最大迭代次数：1000
- 优化算法：LBFGS
- 类别权重：balanced（自动调整类别不平衡）

**备选模型：**
如果逻辑回归 AUC 低于 0.94，尝试 Ridge 分类器（Ridge Classifier）
- 正则化参数 alpha=1.0
- 类别权重：balanced

---

## 7. 实验流程
请简要说明你的实验流程。

示例：
1. 读取训练集和测试集  
2. 对文本进行预处理  
3. 训练或加载 Word2Vec 模型  
4. 将每条文本表示为句向量  
5. 用训练集训练分类器  
6. 在测试集上预测结果  
7. 生成 submission 文件并提交 Kaggle

**我的实验流程：**  

1. **数据加载**（5 分钟）
   - 读取 labeledTrainData.tsv（25,000 条标注数据）
   - 读取 testData.tsv（25,000 条未标注数据）
   - 分析数据分布和情感标签

2. **文本预处理**（10 分钟）
   - 使用 BeautifulSoup 移除 HTML 标签
   - 正则表达式清洗文本，保留字母和空格
   - 转为小写，分词
   - **关键步骤**：保留否定词，提取否定短语

3. **Word2Vec 模型训练**（15 分钟）
   - 使用 Skip-gram 模型，向量维度 300
   - 设置最小词频为 10，上下文窗口 10
   - 训练 10 个 epoch
   - 保存模型以便后续使用

4. **句向量生成**（10 分钟）
   - 对每条评论的词向量进行加权平均
   - 否定词权重 1.5，普通词权重 1.0
   - 生成 300 维句子特征向量

5. **模型训练与验证**（5 分钟）
   - 划分 80% 训练集，20% 验证集
   - 训练逻辑回归分类器
   - 计算 AUC 值，评估模型性能
   - 如 AUC<0.94，尝试 Ridge 分类器

6. **测试集预测**（2 分钟）
   - 使用全量训练数据重新训练模型
   - 对测试集进行预测
   - 生成预测结果和概率

7. **提交文件生成**（1 分钟）
   - 生成 submission.csv（预测标签）
   - 生成 submission_proba.csv（预测概率）
   - 提交到 Kaggle 获取 Public Score

**总耗时：约 48 分钟**

**关键优化点：**
- 保留否定词，避免语义反转错误
- 加权平均句向量，增强否定词表达
- 使用简单模型（逻辑回归），避免过拟合
- 验证集 AUC 监控，确保模型性能

---

## 8. 文件说明
请说明仓库中各文件或文件夹的作用。

示例：
- `data/`：存放数据文件
- `src/`：存放源代码
- `notebooks/`：存放实验 notebook
- `images/`：存放 README 中使用的图片
- `submission/`：存放提交文件

**我的项目结构：**
```text
project/
├─ code/                              # 代码目录
│  ├─ word2vec_sentiment_analysis.py  # 基础版本代码
│  ├─ word2vec_sentiment_analysis_v2.py  # 优化版本代码（AUC>0.95）
│  └─ word2vec_model_optimized        # 训练好的 Word2Vec 模型
├─ report/                            # 报告目录
│  ├─ images/                         # 图片目录
│  │  └─ kaggle_score.png             # Kaggle 成绩截图
│  └─ 实验 2_Word2Vec 情感预测报告.md      # 实验报告
├─ results/                           # 结果目录
│  └─ (实验结果、日志等)
├─ word2vec-nlp-tutorial/             # 原始数据目录
│  ├─ labeledTrainData.tsv/           # 训练数据（25,000 条）
│  ├─ testData.tsv/                   # 测试数据（25,000 条）
│  ├─ unlabeledTrainData.tsv/         # 未标注数据（50,000 条）
│  └─ sampleSubmission.csv            # 提交示例
├─ submission.csv                     # Kaggle 提交文件（预测标签）
├─ submission_proba.csv               # Kaggle 提交文件（预测概率）
├─ README.md                          # 仓库说明
└─ GITHUB_USAGE_GUIDE.md              # Git 使用指南
```

**文件说明：**
- `code/word2vec_sentiment_analysis_v2.py`：**主要使用代码**，包含否定词保留、加权平均等优化
- `code/word2vec_model_optimized`：训练好的 Word2Vec 模型，可直接加载使用
- `submission.csv`：预测的情感标签（0 或 1），可直接提交 Kaggle
- `submission_proba.csv`：预测的正面情感概率，可用于模型融合

---
