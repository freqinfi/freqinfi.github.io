---
title: "Web Search"
excerpt: "Building a Search-Enabled Website using Search API<br><img src='/images/cp_ex1.PNG' width='500' height='300'>
"
collection: portfolio
---

<br>
<span style = "font-size:18px;"> 컴퓨터 프로그래밍 과목을 수강하면서 진행한 프로젝트에 대한 내용</span>
<br><br>
<img src='/images/cp_ex2.PNG' width="600" height="360" style="display: block; margin: 0 auto;" alt="Mecha Prize">

* <strong style = "color: blue; font-size:22px;">Introduction</strong><br>
<span style = "font-size:16px; color: gray;"><br> 구글의 Searh API를 이용하여 Search 홈페이지를 구현하였습니다. 이 과정에서 FrontEnd 코드를 수정, BackEnd 코드를 구현하고, API, json parsing을 이용하여 module간의 통신 구현하였습니다</span><br><br>

* <strong style = "color: blue; font-size:22px;">Experimental Procedure</strong><br>
<span style = "font-size:16px; color: gray;"><br> 실제 상자와 물체를 준비하여 DataSet을 직접 만들었습니다. 상자에 물체가 없는 경우, 충격을 주는 지점에서 물체가 먼 경우와 가까운 경우의 3가지 Class에서 Train data를 얻고, 이에 Gaussian noise를 추가하여 Ougmentation을 통해 데이터를 확장하였습니다. 이 Train data 통해 인공지능 모델을 학습하였습니다.</span><br>
<span style = "font-size:16px; color: gray;"><br> Feature의 경우에는 먼저 음파를 주파수 분석하였고, 두 가지 방법을 사용하였습니다. 0 ~ 1000Hz까지의 주파수의 Magnitude 분포를 이산적인 Feature로서 이용하는 방법과 Top 20개의 Peak 정보를 이용하는 방법을 사용하였습니다.</span><br>
<span style = "font-size:16px; color: gray;"><br> 먼저 T-sne와  PCA 방법을 이용하여 추출한 데이터를 축소하고, 분류 가능성을 판단해보았습니다. 머신러닝 모델의 경우에는 kNN, SVM 다중 분류, RandomForest, Naive Bayes를 사용하였고, 이를 학습시키고, Test set을 따로 만들어 두어 이에 대한 정확성을 계산하였습니다. 또한 Grid search를 이용하여 최적의 Parameter를 찾는 과정 또한 진행하였습니다. 결과적으로 얻은 정확성을 바탕으로 모델을 비교, 분석해보았습니다.</span><br><br>

* <strong style = "color: blue; font-size:22px;"> Presentation</strong><br>
    * [Material](/files/MFM/ML4ME_Final.pdf)
    * [Youtube](https://www.youtube.com/watch?v=YgvcL3sQxws)
    * [Dataset](/files/MFM/our_dataset.zip)
    * <strong> Contents</strong>
        * Generation of our Dataset
        * Feature Extraction methods and data visualization
        * Classification methods and comparison
        * Discussion