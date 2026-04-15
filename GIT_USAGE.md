# Git 常用命令速查表

## 每次实验后更新仓库的完整流程

### 1. 添加文件到暂存区
```bash
# 添加所有修改的文件
git add .

# 或者添加指定文件
git add code/experiment1.py
git add report/experiment1.md
```

### 2. 提交更改
```bash
# 提交并写明修改内容（不要只写 "update" 或 "test"）
git commit -m "完成实验 1：实现词袋模型，准确率 85%"
```

### 3. 推送到 GitHub
```bash
# 推送到远程仓库
git push
```

## 查看历史提交记录

```bash
# 查看简洁的提交历史
git log --oneline

# 查看详细的提交历史
git log

# 查看最近 5 次提交
git log -n 5
```

## 回退到历史版本

### 方法 1：查看历史版本
```bash
# 找到之前较好的版本的 commit ID（如 abc1234）
git log --oneline
```

### 方法 2：恢复之前的代码、结果和报告
```bash
# 方式 A：使用 reset 回退（会删除之后的提交）
git reset --hard abc1234
git push -f origin main  # 强制推送到 GitHub

# 方式 B：使用 revert 撤销（保留历史记录，推荐）
git revert abc1234..HEAD
git push origin main

# 方式 C：检出某个文件的旧版本
git checkout abc1234 -- code/experiment1.py
git commit -m "恢复 experiment1.py 到之前的版本"
git push
```

## 查看当前状态

```bash
# 查看哪些文件被修改了
git status

# 查看具体修改内容
git diff
```

## 常用场景示例

### 场景 1：完成一次实验后
```bash
cd 112304260141-yuanlinyang
git add .
git commit -m "完成实验 2：改进特征提取，F1 分数提升到 0.87"
git push
```

### 场景 3：实验效果变差，需要回退
```bash
# 1. 查看历史提交
git log --oneline

# 2. 找到效果变好时的 commit ID（假设是 def5678）
# 3. 恢复到该版本
git reset --hard def5678

# 4. 强制推送到 GitHub
git push -f origin main
```

### 场景 4：只想恢复某个文件
```bash
# 恢复单个文件到上一个版本
git checkout HEAD~1 -- code/model.py
git commit -m "恢复 model.py 到上一个版本"
git push
```

## 注意事项

1. **每次实验后都要提交**，不要等到最后一次一起传
2. **提交说明要写清楚**，例如：
   - ✅ "完成实验 1：实现 baseline 模型，准确率 78%"
   - ❌ "update"
   - ❌ "test"
3. **不要上传敏感信息**：账号密码、token、密钥等
4. **不要上传大文件**：数据集、大模型文件（已配置 .gitignore 自动忽略）
5. **保留实验过程**：不要只保留最终结果

## 仓库位置

- GitHub: https://github.com/yuan-linyang/112304260141-yuanlinyang
- 本地路径：D:\kaggle  词袋遇到\112304260141-yuanlinyang

## 配置信息

- 用户名：yuan-linyang
- 邮箱：2548281676@qq.com
