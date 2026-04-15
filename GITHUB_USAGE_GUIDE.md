# GitHub 实验管理快速指南

## ✅ 已完成的配置

1. ✅ Git 已安装（版本 2.46.0）
2. ✅ Git 用户名和邮箱已配置
   - 用户名：yuan-linyang
   - 邮箱：2548281676@qq.com
3. ✅ 本地 Git 仓库已初始化
4. ✅ 仓库结构已创建
   - `code/` - 实验代码目录
   - `report/` - 实验报告目录
   - `results/` - 实验结果目录
   - `README.md` - 仓库说明
   - `.gitignore` - Git 忽略规则
5. ✅ 远程仓库已连接
   - 仓库 URL: https://github.com/yuan-linyang/112304260141-yuanlinyang.git
6. ✅ 初始文件已提交

---

## 📝 日常使用流程

### 1️⃣ 每次实验完成后推送代码

```powershell
# 1. 将新文件/修改的文件添加到暂存区
git add .

# 2. 提交修改（务必写清楚提交说明）
git commit -m "实验 X：完成 XXX 功能"

# 3. 推送到 GitHub
git push origin master
```

**提交说明示例：**
- ✅ 好：`"实验 1：完成数据预处理和特征提取"`
- ✅ 好：`"实验 2：添加 SVM 分类器实现"`
- ❌ 差：`"update"`
- ❌ 差：`"test"`

---

### 2️⃣ 查看历史提交记录

```powershell
# 查看简洁的提交历史
git log --oneline

# 查看详细的提交历史
git log

# 查看最近 5 次提交
git log -5
```

---

### 3️⃣ 实验效果变差时回退

#### 方法 1：查看历史版本

```powershell
# 1. 查看提交历史，找到好的版本
git log --oneline

# 2. 查看某个版本的详情（替换 <commit-hash> 为实际版本号）
git show 9b4e375

# 3. 恢复到该版本（硬重置，会丢失之后的修改）
git reset --hard 9b4e375

# 4. 推送到 GitHub（强制推送）
git push -f origin master
```

#### 方法 2：保留当前状态，创建新分支

```powershell
# 1. 为当前状态创建备份分支
git branch backup-branch

# 2. 查看历史找到好的版本
git log --oneline

# 3. 恢复到好的版本
git reset --hard 9b4e375

# 4. 推送到 GitHub
git push -f origin master
```

---

### 4️⃣ 查看仓库状态

```powershell
# 查看哪些文件被修改了
git status

# 查看远程仓库信息
git remote -v

# 查看本地分支
git branch

# 查看提交历史
git log --oneline
```

---

## 🔐 安全注意事项

### ❌ 不要上传的内容

- 账号密码
- API Token
- 密钥文件（.pem, .key 等）
- 配置文件中的敏感信息（.env 文件）
- 过大的数据集文件（>50MB）
- 大模型文件（.h5, .pth 等）

### ✅ 应该上传的内容

- 实验代码
- 实验报告
- 实验结果截图
- 结果表格
- 日志文件（小型）

---

## 📁 仓库结构说明

```
112304260141-yuanlinyang/
├── code/                   # 实验代码
│   └── .gitkeep           # 占位文件，保持目录存在
├── report/                # 实验报告
│   └── .gitkeep
├── results/               # 实验结果
│   └── .gitkeep
├── word2vec-nlp-tutorial/ # 原始实验数据
├── .gitignore            # Git 忽略规则
└── README.md             # 仓库说明
```

---

## 💡 实用技巧

### 撤销上一次的提交

```powershell
# 撤销提交，但保留修改
git reset --soft HEAD~1

# 完全撤销提交和修改
git reset --hard HEAD~1
```

### 修改上一次的提交说明

```powershell
git commit --amend -m "新的提交说明"
```

### 查看文件差异

```powershell
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最新提交的差异
git diff --staged
```

---

## 🆘 常见问题

### Q: 推送失败怎么办？
A: 先执行 `git pull origin master` 拉取远程更新，解决冲突后再推送。

### Q: 误删了重要文件怎么办？
A: 使用 `git log` 找到删除前的版本，用 `git reset --hard <commit-hash>` 恢复。

### Q: 如何查看某个文件的历史？
A: `git log <文件名>` 可以查看该文件的所有修改历史。

### Q: 提交后发现漏了文件怎么办？
A: 添加文件后执行 `git commit --amend` 可以合并到上一次提交。

---

## 📞 需要 AI 帮助时

你可以直接告诉 AI：

1. **推送实验内容**：
   - "帮我推送这次实验的代码和报告"
   - "提交实验 1 的结果到 GitHub"

2. **查看历史记录**：
   - "查看最近的提交记录"
   - "找到实验 2 完成时的版本"

3. **回退版本**：
   - "实验效果变差了，帮我恢复到之前的好版本"
   - "回退到实验 1 完成时的状态"

---

**最后更新**: 2026-04-16
**仓库**: https://github.com/yuan-linyang/112304260141-yuanlinyang
