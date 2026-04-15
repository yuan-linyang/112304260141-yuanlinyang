# 机器学习实验仓库

## 学生信息
- **姓名**：
- **学号**：
- **班级**：

## 仓库说明

本仓库用于管理机器学习课程实验，包含实验代码、实验报告和实验结果。

## 仓库结构

```
├── code/           # 实验代码
├── report/         # 实验报告
├── results/        # 实验结果（截图、表格、日志等）
├── word2vec-nlp-tutorial/  # 原始实验数据
└── README.md       # 仓库说明
```

## 实验项目

### 实验 1：基于 Word2Vec 的情感预测
- **比赛**：Bag of Words Meets Bags of Popcorn
- **比赛链接**：https://www.kaggle.com/c/word2vec-nlp-tutorial
- **代码**：[code/word2vec_sentiment_analysis.py](code/word2vec_sentiment_analysis.py)
- **报告**：[report/实验 2_Word2Vec 情感预测报告.md](report/实验 2_Word2Vec 情感预测报告.md)
- **完成日期**：2026-04-16

## 使用指南

### 1. 克隆仓库
```bash
git clone <仓库 URL>
cd <仓库目录>
```

### 2. 更新实验内容
每次实验完成后，执行以下步骤：
```bash
# 添加修改的文件
git add .

# 提交修改（请写清楚提交说明）
git commit -m "实验 X：完成 XXX 功能"

# 推送到 GitHub
git push origin master
```

### 3. 查看历史版本
```bash
# 查看提交历史
git log

# 查看某个版本的详情
git show <commit-hash>
```

### 4. 恢复到历史版本
如果实验效果变差，可以恢复到之前较好的版本：
```bash
# 查看历史提交
git log

# 恢复到指定版本（硬重置）
git reset --hard <commit-hash>

# 或者创建新分支保留当前状态
git checkout -b backup-branch
git checkout master
git reset --hard <good-commit-hash>
```

## 注意事项

- 每次实验后都要提交，不要等到最后一次一起传
- 提交内容要完整：代码、报告、结果尽量同步更新
- 提交说明要写清楚，不要只写"update""test"
- 不要上传账号密码、token、密钥等敏感信息
- 不要随便上传过大的数据集和大模型文件
- 保留实验过程，不要只保留最终结果

## 实验记录

| 实验编号 | 实验名称 | 完成日期 | 提交说明 |
|---------|---------|---------|---------|
| 实验 1   | 基于 Word2Vec 的情感预测 | 2026-04-16 | 初始化实验仓库 |
