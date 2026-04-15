"""
基于 Word2Vec 的情感分析模型
学生信息：
- 姓名：
- 学号：
- 班级：
"""

import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from gensim.models import Word2Vec
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def review_to_wordlist(review, remove_stopwords=False):
    """
    将影评转换为单词列表
    """
    review_text = BeautifulSoup(review, "html.parser").get_text()
    review_text = re.sub("[^a-zA-Z]", " ", review_text)
    words = review_text.lower().split()
    
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if w not in stops]
    
    return words


def review_to_sentences(review, tokenizer, remove_stopwords=False):
    """
    将影评分割为句子列表
    """
    raw_sentences = tokenizer.tokenize(review.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append(review_to_wordlist(raw_sentence, remove_stopwords))
    
    return sentences


def make_feature_vec(words, model, num_features):
    """
    计算句子的特征向量（所有词向量的平均）
    """
    feature_vec = np.zeros((num_features,), dtype="float32")
    nwords = 0.
    index2word_set = set(model.wv.index_to_key)
    
    for word in words:
        if word in index2word_set:
            nwords += 1.
            feature_vec = np.add(feature_vec, model.wv[word])
    
    if nwords > 0:
        feature_vec = np.divide(feature_vec, nwords)
    
    return feature_vec


def get_avg_feature_vecs(reviews, model, num_features):
    """
    获取所有影评的特征向量
    """
    result = np.zeros((len(reviews), num_features), dtype="float32")
    
    for i in range(len(reviews)):
        if i % 1000 == 0:
            print(f"Processing review {i}/{len(reviews)}")
        result[i] = make_feature_vec(reviews[i], model, num_features)
    
    return result


def main():
    print("加载训练数据...")
    train = pd.read_csv("word2vec-nlp-tutorial/labeledTrainData.tsv/labeledTrainData.tsv", 
                        header=0, quoting=3)
    
    print("加载测试数据...")
    test = pd.read_csv("word2vec-nlp-tutorial/testData.tsv/testData.tsv", 
                       header=0, quoting=3)
    
    print("数据预处理...")
    train_reviews = []
    for i in range(len(train["review"])):
        train_reviews.append(review_to_wordlist(train["review"][i]))
    
    test_reviews = []
    for i in range(len(test["review"])):
        test_reviews.append(review_to_wordlist(test["review"][i]))
    
    print("训练 Word2Vec 模型...")
    num_features = 300
    min_word_count = 40
    num_workers = 4
    context = 10
    downsampling = 1e-3
    
    model = Word2Vec(
        train_reviews,
        workers=num_workers,
        vector_size=num_features,
        min_count=min_word_count,
        window=context,
        sample=downsampling
    )
    
    model.init_sims(replace=True)
    model.save("code/word2vec_model")
    
    print("生成训练特征向量...")
    train_feature_vecs = get_avg_feature_vecs(train_reviews, model, num_features)
    
    print("生成测试特征向量...")
    test_feature_vecs = get_avg_feature_vecs(test_reviews, model, num_features)
    
    print("训练随机森林分类器...")
    forest = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    forest.fit(train_feature_vecs, train["sentiment"])
    
    print("评估模型...")
    X_train, X_test, y_train, y_test = train_test_split(
        train_feature_vecs, train["sentiment"], test_size=0.2, random_state=42
    )
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))
    
    print("生成提交文件...")
    forest.fit(train_feature_vecs, train["sentiment"])
    result = forest.predict(test_feature_vecs)
    
    output = pd.DataFrame(data={"id": test["id"], "sentiment": result})
    output.to_csv("submission.csv", index=False, quoting=3)
    print("提交文件已保存：submission.csv")


if __name__ == "__main__":
    main()
