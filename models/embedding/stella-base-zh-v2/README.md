---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- mteb
model-index:
- name: stella-base-zh-v2
  results:
  - task:
      type: STS
    dataset:
      type: C-MTEB/AFQMC
      name: MTEB AFQMC
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 44.62083443545288
    - type: cos_sim_spearman
      value: 46.72814628391134
    - type: euclidean_pearson
      value: 45.11522093816821
    - type: euclidean_spearman
      value: 46.72818648900957
    - type: manhattan_pearson
      value: 44.98820754682395
    - type: manhattan_spearman
      value: 46.63576705524296
  - task:
      type: STS
    dataset:
      type: C-MTEB/ATEC
      name: MTEB ATEC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 49.543902370260234
    - type: cos_sim_spearman
      value: 51.22161152883018
    - type: euclidean_pearson
      value: 53.49586541060596
    - type: euclidean_spearman
      value: 51.22161490583934
    - type: manhattan_pearson
      value: 53.51023339947787
    - type: manhattan_spearman
      value: 51.22426632538443
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (zh)
      config: zh
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 39.644
    - type: f1
      value: 37.67897186741224
  - task:
      type: STS
    dataset:
      type: C-MTEB/BQ
      name: MTEB BQ
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 61.96416237112325
    - type: cos_sim_spearman
      value: 64.80484064041543
    - type: euclidean_pearson
      value: 63.281983537100594
    - type: euclidean_spearman
      value: 64.80483024694405
    - type: manhattan_pearson
      value: 63.266046412399426
    - type: manhattan_spearman
      value: 64.79643672829964
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringP2P
      name: MTEB CLSClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 40.25857488823951
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/CLSClusteringS2S
      name: MTEB CLSClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 37.17501553349549
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv1-reranking
      name: MTEB CMedQAv1
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 84.69751849160603
    - type: mrr
      value: 87.16257936507937
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/CMedQAv2-reranking
      name: MTEB CMedQAv2
      config: default
      split: test
      revision: None
    metrics:
    - type: map
      value: 85.31468551417655
    - type: mrr
      value: 87.74658730158731
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 24.181
    - type: map_at_10
      value: 35.615
    - type: map_at_100
      value: 37.444
    - type: map_at_1000
      value: 37.573
    - type: map_at_3
      value: 31.679000000000002
    - type: map_at_5
      value: 33.854
    - type: mrr_at_1
      value: 37.108999999999995
    - type: mrr_at_10
      value: 44.653
    - type: mrr_at_100
      value: 45.647
    - type: mrr_at_1000
      value: 45.701
    - type: mrr_at_3
      value: 42.256
    - type: mrr_at_5
      value: 43.497
    - type: ndcg_at_1
      value: 37.108999999999995
    - type: ndcg_at_10
      value: 42.028999999999996
    - type: ndcg_at_100
      value: 49.292
    - type: ndcg_at_1000
      value: 51.64
    - type: ndcg_at_3
      value: 37.017
    - type: ndcg_at_5
      value: 38.997
    - type: precision_at_1
      value: 37.108999999999995
    - type: precision_at_10
      value: 9.386999999999999
    - type: precision_at_100
      value: 1.536
    - type: precision_at_1000
      value: 0.183
    - type: precision_at_3
      value: 20.93
    - type: precision_at_5
      value: 15.268999999999998
    - type: recall_at_1
      value: 24.181
    - type: recall_at_10
      value: 51.961999999999996
    - type: recall_at_100
      value: 82.122
    - type: recall_at_1000
      value: 98.059
    - type: recall_at_3
      value: 36.730000000000004
    - type: recall_at_5
      value: 42.884
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/CMNLI
      name: MTEB Cmnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 76.23571858087793
    - type: cos_sim_ap
      value: 84.75290046905519
    - type: cos_sim_f1
      value: 77.70114942528735
    - type: cos_sim_precision
      value: 73.05475504322767
    - type: cos_sim_recall
      value: 82.97872340425532
    - type: dot_accuracy
      value: 76.23571858087793
    - type: dot_ap
      value: 84.75113928508674
    - type: dot_f1
      value: 77.70114942528735
    - type: dot_precision
      value: 73.05475504322767
    - type: dot_recall
      value: 82.97872340425532
    - type: euclidean_accuracy
      value: 76.23571858087793
    - type: euclidean_ap
      value: 84.75289931658567
    - type: euclidean_f1
      value: 77.70114942528735
    - type: euclidean_precision
      value: 73.05475504322767
    - type: euclidean_recall
      value: 82.97872340425532
    - type: manhattan_accuracy
      value: 76.17558628983764
    - type: manhattan_ap
      value: 84.75764676597448
    - type: manhattan_f1
      value: 77.73437499999999
    - type: manhattan_precision
      value: 72.52480259161773
    - type: manhattan_recall
      value: 83.75029226093056
    - type: max_accuracy
      value: 76.23571858087793
    - type: max_ap
      value: 84.75764676597448
    - type: max_f1
      value: 77.73437499999999
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 67.43900000000001
    - type: map_at_10
      value: 76.00099999999999
    - type: map_at_100
      value: 76.297
    - type: map_at_1000
      value: 76.29899999999999
    - type: map_at_3
      value: 74.412
    - type: map_at_5
      value: 75.177
    - type: mrr_at_1
      value: 67.65
    - type: mrr_at_10
      value: 76.007
    - type: mrr_at_100
      value: 76.322
    - type: mrr_at_1000
      value: 76.324
    - type: mrr_at_3
      value: 74.464
    - type: mrr_at_5
      value: 75.265
    - type: ndcg_at_1
      value: 67.65
    - type: ndcg_at_10
      value: 79.85600000000001
    - type: ndcg_at_100
      value: 81.34400000000001
    - type: ndcg_at_1000
      value: 81.44200000000001
    - type: ndcg_at_3
      value: 76.576
    - type: ndcg_at_5
      value: 77.956
    - type: precision_at_1
      value: 67.65
    - type: precision_at_10
      value: 9.283
    - type: precision_at_100
      value: 0.9990000000000001
    - type: precision_at_1000
      value: 0.101
    - type: precision_at_3
      value: 27.749000000000002
    - type: precision_at_5
      value: 17.345
    - type: recall_at_1
      value: 67.43900000000001
    - type: recall_at_10
      value: 91.781
    - type: recall_at_100
      value: 98.84100000000001
    - type: recall_at_1000
      value: 99.684
    - type: recall_at_3
      value: 82.719
    - type: recall_at_5
      value: 86.038
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 25.354
    - type: map_at_10
      value: 79.499
    - type: map_at_100
      value: 82.416
    - type: map_at_1000
      value: 82.451
    - type: map_at_3
      value: 54.664
    - type: map_at_5
      value: 69.378
    - type: mrr_at_1
      value: 89.25
    - type: mrr_at_10
      value: 92.666
    - type: mrr_at_100
      value: 92.738
    - type: mrr_at_1000
      value: 92.74
    - type: mrr_at_3
      value: 92.342
    - type: mrr_at_5
      value: 92.562
    - type: ndcg_at_1
      value: 89.25
    - type: ndcg_at_10
      value: 86.97
    - type: ndcg_at_100
      value: 89.736
    - type: ndcg_at_1000
      value: 90.069
    - type: ndcg_at_3
      value: 85.476
    - type: ndcg_at_5
      value: 84.679
    - type: precision_at_1
      value: 89.25
    - type: precision_at_10
      value: 41.9
    - type: precision_at_100
      value: 4.811
    - type: precision_at_1000
      value: 0.48900000000000005
    - type: precision_at_3
      value: 76.86699999999999
    - type: precision_at_5
      value: 65.25
    - type: recall_at_1
      value: 25.354
    - type: recall_at_10
      value: 88.64999999999999
    - type: recall_at_100
      value: 97.56
    - type: recall_at_1000
      value: 99.37
    - type: recall_at_3
      value: 57.325
    - type: recall_at_5
      value: 74.614
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 48.3
    - type: map_at_10
      value: 57.765
    - type: map_at_100
      value: 58.418000000000006
    - type: map_at_1000
      value: 58.43899999999999
    - type: map_at_3
      value: 54.883
    - type: map_at_5
      value: 56.672999999999995
    - type: mrr_at_1
      value: 48.3
    - type: mrr_at_10
      value: 57.765
    - type: mrr_at_100
      value: 58.418000000000006
    - type: mrr_at_1000
      value: 58.43899999999999
    - type: mrr_at_3
      value: 54.883
    - type: mrr_at_5
      value: 56.672999999999995
    - type: ndcg_at_1
      value: 48.3
    - type: ndcg_at_10
      value: 62.846000000000004
    - type: ndcg_at_100
      value: 65.845
    - type: ndcg_at_1000
      value: 66.369
    - type: ndcg_at_3
      value: 56.996
    - type: ndcg_at_5
      value: 60.214999999999996
    - type: precision_at_1
      value: 48.3
    - type: precision_at_10
      value: 7.9
    - type: precision_at_100
      value: 0.9259999999999999
    - type: precision_at_1000
      value: 0.097
    - type: precision_at_3
      value: 21.032999999999998
    - type: precision_at_5
      value: 14.180000000000001
    - type: recall_at_1
      value: 48.3
    - type: recall_at_10
      value: 79.0
    - type: recall_at_100
      value: 92.60000000000001
    - type: recall_at_1000
      value: 96.7
    - type: recall_at_3
      value: 63.1
    - type: recall_at_5
      value: 70.89999999999999
  - task:
      type: Classification
    dataset:
      type: C-MTEB/IFlyTek-classification
      name: MTEB IFlyTek
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 47.895344363216616
    - type: f1
      value: 34.95151253165417
  - task:
      type: Classification
    dataset:
      type: C-MTEB/JDReview-classification
      name: MTEB JDReview
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 84.78424015009381
    - type: ap
      value: 52.436279969597685
    - type: f1
      value: 79.49258679392281
  - task:
      type: STS
    dataset:
      type: C-MTEB/LCQMC
      name: MTEB LCQMC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 70.2307617475436
    - type: cos_sim_spearman
      value: 76.88912653700545
    - type: euclidean_pearson
      value: 75.47976675486538
    - type: euclidean_spearman
      value: 76.88912210059333
    - type: manhattan_pearson
      value: 75.45834919257487
    - type: manhattan_spearman
      value: 76.8669208121889
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/Mmarco-reranking
      name: MTEB MMarcoReranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 28.047948482579244
    - type: mrr
      value: 26.63809523809524
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 65.837
    - type: map_at_10
      value: 74.72
    - type: map_at_100
      value: 75.068
    - type: map_at_1000
      value: 75.079
    - type: map_at_3
      value: 72.832
    - type: map_at_5
      value: 74.07000000000001
    - type: mrr_at_1
      value: 68.009
    - type: mrr_at_10
      value: 75.29400000000001
    - type: mrr_at_100
      value: 75.607
    - type: mrr_at_1000
      value: 75.617
    - type: mrr_at_3
      value: 73.677
    - type: mrr_at_5
      value: 74.74199999999999
    - type: ndcg_at_1
      value: 68.009
    - type: ndcg_at_10
      value: 78.36
    - type: ndcg_at_100
      value: 79.911
    - type: ndcg_at_1000
      value: 80.226
    - type: ndcg_at_3
      value: 74.825
    - type: ndcg_at_5
      value: 76.9
    - type: precision_at_1
      value: 68.009
    - type: precision_at_10
      value: 9.463000000000001
    - type: precision_at_100
      value: 1.023
    - type: precision_at_1000
      value: 0.105
    - type: precision_at_3
      value: 28.075
    - type: precision_at_5
      value: 17.951
    - type: recall_at_1
      value: 65.837
    - type: recall_at_10
      value: 89.00099999999999
    - type: recall_at_100
      value: 95.968
    - type: recall_at_1000
      value: 98.461
    - type: recall_at_3
      value: 79.69800000000001
    - type: recall_at_5
      value: 84.623
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 68.08675184936112
    - type: f1
      value: 65.51466585063827
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (zh-CN)
      config: zh-CN
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 73.22461331540013
    - type: f1
      value: 72.675432030145
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 49.2
    - type: map_at_10
      value: 55.394
    - type: map_at_100
      value: 55.883
    - type: map_at_1000
      value: 55.93900000000001
    - type: map_at_3
      value: 53.733
    - type: map_at_5
      value: 54.778000000000006
    - type: mrr_at_1
      value: 49.3
    - type: mrr_at_10
      value: 55.444
    - type: mrr_at_100
      value: 55.933
    - type: mrr_at_1000
      value: 55.989
    - type: mrr_at_3
      value: 53.783
    - type: mrr_at_5
      value: 54.827999999999996
    - type: ndcg_at_1
      value: 49.2
    - type: ndcg_at_10
      value: 58.501999999999995
    - type: ndcg_at_100
      value: 61.181
    - type: ndcg_at_1000
      value: 62.848000000000006
    - type: ndcg_at_3
      value: 55.143
    - type: ndcg_at_5
      value: 57.032000000000004
    - type: precision_at_1
      value: 49.2
    - type: precision_at_10
      value: 6.83
    - type: precision_at_100
      value: 0.815
    - type: precision_at_1000
      value: 0.095
    - type: precision_at_3
      value: 19.733
    - type: precision_at_5
      value: 12.76
    - type: recall_at_1
      value: 49.2
    - type: recall_at_10
      value: 68.30000000000001
    - type: recall_at_100
      value: 81.5
    - type: recall_at_1000
      value: 95.0
    - type: recall_at_3
      value: 59.199999999999996
    - type: recall_at_5
      value: 63.800000000000004
  - task:
      type: Classification
    dataset:
      type: C-MTEB/MultilingualSentiment-classification
      name: MTEB MultilingualSentiment
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 71.66666666666666
    - type: f1
      value: 70.92944632461379
  - task:
      type: PairClassification
    dataset:
      type: C-MTEB/OCNLI
      name: MTEB Ocnli
      config: default
      split: validation
      revision: None
    metrics:
    - type: cos_sim_accuracy
      value: 70.00541418516514
    - type: cos_sim_ap
      value: 75.16499510773514
    - type: cos_sim_f1
      value: 73.09435517099301
    - type: cos_sim_precision
      value: 59.932432432432435
    - type: cos_sim_recall
      value: 93.66420274551214
    - type: dot_accuracy
      value: 70.00541418516514
    - type: dot_ap
      value: 75.16499510773514
    - type: dot_f1
      value: 73.09435517099301
    - type: dot_precision
      value: 59.932432432432435
    - type: dot_recall
      value: 93.66420274551214
    - type: euclidean_accuracy
      value: 70.00541418516514
    - type: euclidean_ap
      value: 75.16499510773514
    - type: euclidean_f1
      value: 73.09435517099301
    - type: euclidean_precision
      value: 59.932432432432435
    - type: euclidean_recall
      value: 93.66420274551214
    - type: manhattan_accuracy
      value: 70.11369788846778
    - type: manhattan_ap
      value: 75.1259071890593
    - type: manhattan_f1
      value: 72.91399229781771
    - type: manhattan_precision
      value: 61.294964028776974
    - type: manhattan_recall
      value: 89.96832101372756
    - type: max_accuracy
      value: 70.11369788846778
    - type: max_ap
      value: 75.16499510773514
    - type: max_f1
      value: 73.09435517099301
  - task:
      type: Classification
    dataset:
      type: C-MTEB/OnlineShopping-classification
      name: MTEB OnlineShopping
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 91.38000000000002
    - type: ap
      value: 89.12250244489272
    - type: f1
      value: 91.36604511107015
  - task:
      type: STS
    dataset:
      type: C-MTEB/PAWSX
      name: MTEB PAWSX
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 24.231255568030463
    - type: cos_sim_spearman
      value: 29.6964906904186
    - type: euclidean_pearson
      value: 30.166130502867016
    - type: euclidean_spearman
      value: 29.69614167804371
    - type: manhattan_pearson
      value: 30.166606116745935
    - type: manhattan_spearman
      value: 29.62681453661945
  - task:
      type: STS
    dataset:
      type: C-MTEB/QBQTC
      name: MTEB QBQTC
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 34.88835755574809
    - type: cos_sim_spearman
      value: 37.3797926051053
    - type: euclidean_pearson
      value: 35.46629492698549
    - type: euclidean_spearman
      value: 37.37987510604593
    - type: manhattan_pearson
      value: 35.4953353526957
    - type: manhattan_spearman
      value: 37.41397231689605
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (zh)
      config: zh
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 67.79575721136626
    - type: cos_sim_spearman
      value: 69.02068400784196
    - type: euclidean_pearson
      value: 68.30675023447176
    - type: euclidean_spearman
      value: 69.02068400784196
    - type: manhattan_pearson
      value: 69.91284259797827
    - type: manhattan_spearman
      value: 70.31717787763641
  - task:
      type: STS
    dataset:
      type: C-MTEB/STSB
      name: MTEB STSB
      config: default
      split: test
      revision: None
    metrics:
    - type: cos_sim_pearson
      value: 79.05026785034129
    - type: cos_sim_spearman
      value: 79.62719014756249
    - type: euclidean_pearson
      value: 79.13305301290063
    - type: euclidean_spearman
      value: 79.62710682651051
    - type: manhattan_pearson
      value: 79.07012559140433
    - type: manhattan_spearman
      value: 79.58333069893605
  - task:
      type: Reranking
    dataset:
      type: C-MTEB/T2Reranking
      name: MTEB T2Reranking
      config: default
      split: dev
      revision: None
    metrics:
    - type: map
      value: 66.34533369244325
    - type: mrr
      value: 75.93632792769557
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 26.995
    - type: map_at_10
      value: 76.083
    - type: map_at_100
      value: 79.727
    - type: map_at_1000
      value: 79.798
    - type: map_at_3
      value: 53.455
    - type: map_at_5
      value: 65.747
    - type: mrr_at_1
      value: 89.536
    - type: mrr_at_10
      value: 91.972
    - type: mrr_at_100
      value: 92.07
    - type: mrr_at_1000
      value: 92.07499999999999
    - type: mrr_at_3
      value: 91.52900000000001
    - type: mrr_at_5
      value: 91.806
    - type: ndcg_at_1
      value: 89.536
    - type: ndcg_at_10
      value: 83.756
    - type: ndcg_at_100
      value: 87.468
    - type: ndcg_at_1000
      value: 88.16199999999999
    - type: ndcg_at_3
      value: 85.349
    - type: ndcg_at_5
      value: 83.855
    - type: precision_at_1
      value: 89.536
    - type: precision_at_10
      value: 41.713
    - type: precision_at_100
      value: 4.994
    - type: precision_at_1000
      value: 0.515
    - type: precision_at_3
      value: 74.81400000000001
    - type: precision_at_5
      value: 62.678
    - type: recall_at_1
      value: 26.995
    - type: recall_at_10
      value: 82.586
    - type: recall_at_100
      value: 94.726
    - type: recall_at_1000
      value: 98.276
    - type: recall_at_3
      value: 55.106
    - type: recall_at_5
      value: 69.096
  - task:
      type: Classification
    dataset:
      type: C-MTEB/TNews-classification
      name: MTEB TNews
      config: default
      split: validation
      revision: None
    metrics:
    - type: accuracy
      value: 51.25200000000001
    - type: f1
      value: 49.43760438233612
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringP2P
      name: MTEB ThuNewsClusteringP2P
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 62.18575394560257
  - task:
      type: Clustering
    dataset:
      type: C-MTEB/ThuNewsClusteringS2S
      name: MTEB ThuNewsClusteringS2S
      config: default
      split: test
      revision: None
    metrics:
    - type: v_measure
      value: 57.97489103903411
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 52.2
    - type: map_at_10
      value: 63.23800000000001
    - type: map_at_100
      value: 63.788
    - type: map_at_1000
      value: 63.800999999999995
    - type: map_at_3
      value: 61.016999999999996
    - type: map_at_5
      value: 62.392
    - type: mrr_at_1
      value: 52.2
    - type: mrr_at_10
      value: 63.23800000000001
    - type: mrr_at_100
      value: 63.788
    - type: mrr_at_1000
      value: 63.800999999999995
    - type: mrr_at_3
      value: 61.016999999999996
    - type: mrr_at_5
      value: 62.392
    - type: ndcg_at_1
      value: 52.2
    - type: ndcg_at_10
      value: 68.273
    - type: ndcg_at_100
      value: 70.892
    - type: ndcg_at_1000
      value: 71.207
    - type: ndcg_at_3
      value: 63.794
    - type: ndcg_at_5
      value: 66.268
    - type: precision_at_1
      value: 52.2
    - type: precision_at_10
      value: 8.39
    - type: precision_at_100
      value: 0.96
    - type: precision_at_1000
      value: 0.098
    - type: precision_at_3
      value: 23.933
    - type: precision_at_5
      value: 15.559999999999999
    - type: recall_at_1
      value: 52.2
    - type: recall_at_10
      value: 83.89999999999999
    - type: recall_at_100
      value: 96.0
    - type: recall_at_1000
      value: 98.4
    - type: recall_at_3
      value: 71.8
    - type: recall_at_5
      value: 77.8
  - task:
      type: Classification
    dataset:
      type: C-MTEB/waimai-classification
      name: MTEB Waimai
      config: default
      split: test
      revision: None
    metrics:
    - type: accuracy
      value: 86.67999999999999
    - type: ap
      value: 69.96366657730151
    - type: f1
      value: 84.92349905611292
---


**新闻 | News**

**[2024-04-06]** 开源[puff](https://huggingface.co/infgrad/puff-base-v1)系列模型，**专门针对检索和语义匹配任务，更多的考虑泛化性和私有通用测试集效果，向量维度可变，中英双语**。

**[2024-02-27]** 开源stella-mrl-large-zh-v3.5-1792d模型，支持**向量可变维度**。

**[2024-02-17]** 开源stella v3系列、dialogue编码模型和相关训练数据。

**[2023-10-19]** 开源stella-base-en-v2 使用简单，**不需要任何前缀文本**。

**[2023-10-12]** 开源stella-base-zh-v2和stella-large-zh-v2, 效果更好且使用简单，**不需要任何前缀文本**。

**[2023-09-11]** 开源stella-base-zh和stella-large-zh

欢迎去[本人主页](https://huggingface.co/infgrad)查看最新模型，并提出您的宝贵意见！

## stella model


stella是一个通用的文本编码模型，主要有以下模型：

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Language | Need instruction for retrieval? |
|:------------------:|:---------------:|:---------:|:---------------:|:--------:|:-------------------------------:|
| stella-large-zh-v2 |      0.65       |   1024    |      1024       | Chinese  |               No                |
| stella-base-zh-v2  |       0.2       |    768    |      1024       | Chinese  |               No                |
|  stella-large-zh   |      0.65       |   1024    |      1024       | Chinese  |               Yes               |
|   stella-base-zh   |       0.2       |    768    |      1024       | Chinese  |               Yes               |

完整的训练思路和训练过程已记录在[博客](https://zhuanlan.zhihu.com/p/655322183)，欢迎阅读讨论。

**训练数据：**

1. 开源数据(wudao_base_200GB[1]、m3e[2]和simclue[3])，着重挑选了长度大于512的文本
2. 在通用语料库上使用LLM构造一批(question, paragraph)和(sentence, paragraph)数据

**训练方法：**

1. 对比学习损失函数
2. 带有难负例的对比学习损失函数(分别基于bm25和vector构造了难负例)
3. EWC(Elastic Weights Consolidation)[4]
4. cosent loss[5]
5. 每一种类型的数据一个迭代器，分别计算loss进行更新

stella-v2在stella模型的基础上，使用了更多的训练数据，同时知识蒸馏等方法去除了前置的instruction(
比如piccolo的`查询:`, `结果:`, e5的`query:`和`passage:`)。

**初始权重：**\
stella-base-zh和stella-large-zh分别以piccolo-base-zh[6]和piccolo-large-zh作为基础模型，512-1024的position
embedding使用层次分解位置编码[7]进行初始化。\
感谢商汤科技研究院开源的[piccolo系列模型](https://huggingface.co/sensenova)。

stella is a general-purpose text encoder, which mainly includes the following models:

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Language | Need instruction for retrieval? |
|:------------------:|:---------------:|:---------:|:---------------:|:--------:|:-------------------------------:|
| stella-large-zh-v2 |      0.65       |   1024    |      1024       | Chinese  |               No                |
| stella-base-zh-v2  |       0.2       |    768    |      1024       | Chinese  |               No                |
|  stella-large-zh   |      0.65       |   1024    |      1024       | Chinese  |               Yes               |
|   stella-base-zh   |       0.2       |    768    |      1024       | Chinese  |               Yes               |

The training data mainly includes:

1. Open-source training data (wudao_base_200GB, m3e, and simclue), with a focus on selecting texts with lengths greater
   than 512.
2. A batch of (question, paragraph) and (sentence, paragraph) data constructed on a general corpus using LLM.

The loss functions mainly include:

1. Contrastive learning loss function
2. Contrastive learning loss function with hard negative examples (based on bm25 and vector hard negatives)
3. EWC (Elastic Weights Consolidation)
4. cosent loss

Model weight initialization:\
stella-base-zh and stella-large-zh use piccolo-base-zh and piccolo-large-zh as the base models, respectively, and the
512-1024 position embedding uses the initialization strategy of hierarchical decomposed position encoding.

Training strategy:\
One iterator for each type of data, separately calculating the loss.

Based on stella models, stella-v2 use more training data and remove instruction by Knowledge Distillation.

## Metric

#### C-MTEB leaderboard (Chinese)

|     Model Name     | Model Size (GB) | Dimension | Sequence Length | Average (35) | Classification (9) | Clustering (4) | Pair Classification (2) | Reranking (4) | Retrieval (8) | STS (8) |
|:------------------:|:---------------:|:---------:|:---------------:|:------------:|:------------------:|:--------------:|:-----------------------:|:-------------:|:-------------:|:-------:|
| stella-large-zh-v2 |      0.65       |   1024    |      1024       |    65.13     |       69.05        |     49.16      |          82.68          |     66.41     |     70.14     |  58.66  |
| stella-base-zh-v2  |       0.2       |    768    |      1024       |    64.36     |       68.29        |      49.4      |          79.95          |     66.1      |     70.08     |  56.92  |
|  stella-large-zh   |      0.65       |   1024    |      1024       |    64.54     |       67.62        |     48.65      |          78.72          |     65.98     |     71.02     |  58.3   |
|   stella-base-zh   |       0.2       |    768    |      1024       |    64.16     |       67.77        |      48.7      |          76.09          |     66.95     |     71.07     |  56.54  |

#### Reproduce our results

Codes:

```python
import torch
import numpy as np
from typing import List
from mteb import MTEB
from sentence_transformers import SentenceTransformer


class FastTextEncoder():
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name).cuda().half().eval()
        self.model.max_seq_length = 512

    def encode(
            self,
            input_texts: List[str],
            *args,
            **kwargs
    ):
        new_sens = list(set(input_texts))
        new_sens.sort(key=lambda x: len(x), reverse=True)
        vecs = self.model.encode(
            new_sens, normalize_embeddings=True, convert_to_numpy=True, batch_size=256
        ).astype(np.float32)
        sen2arrid = {sen: idx for idx, sen in enumerate(new_sens)}
        vecs = vecs[[sen2arrid[sen] for sen in input_texts]]
        torch.cuda.empty_cache()
        return vecs


if __name__ == '__main__':
    model_name = "infgrad/stella-base-zh-v2"
    output_folder = "zh_mteb_results/stella-base-zh-v2"
    task_names = [t.description["name"] for t in MTEB(task_langs=['zh', 'zh-CN']).tasks]
    model = FastTextEncoder(model_name)
    for task in task_names:
        MTEB(tasks=[task], task_langs=['zh', 'zh-CN']).run(model, output_folder=output_folder)

```

#### Evaluation for long text

经过实际观察发现，C-MTEB的评测数据长度基本都是小于512的，
更致命的是那些长度大于512的文本，其重点都在前半部分
这里以CMRC2018的数据为例说明这个问题：

```
question: 《无双大蛇z》是谁旗下ω-force开发的动作游戏？

passage：《无双大蛇z》是光荣旗下ω-force开发的动作游戏，于2009年3月12日登陆索尼playstation3，并于2009年11月27日推......
```

passage长度为800多，大于512，但是对于这个question而言只需要前面40个字就足以检索，多的内容对于模型而言是一种噪声，反而降低了效果。\
简言之，现有数据集的2个问题：\
1）长度大于512的过少\
2）即便大于512，对于检索而言也只需要前512的文本内容\
导致**无法准确评估模型的长文本编码能力。**

为了解决这个问题，搜集了相关开源数据并使用规则进行过滤，最终整理了6份长文本测试集,他们分别是：

- CMRC2018，通用百科
- CAIL，法律阅读理解
- DRCD，繁体百科，已转简体
- Military，军工问答
- Squad，英文阅读理解，已转中文
- Multifieldqa_zh，清华的大模型长文本理解能力评测数据[9]

处理规则是选取答案在512长度之后的文本，短的测试数据会欠采样一下，长短文本占比约为1:2，所以模型既得理解短文本也得理解长文本。
除了Military数据集，我们提供了其他5个测试数据的下载地址：https://drive.google.com/file/d/1WC6EWaCbVgz-vPMDFH4TwAMkLyh5WNcN/view?usp=sharing

评测指标为Recall@5, 结果如下：

|     Dataset     | piccolo-base-zh | piccolo-large-zh | bge-base-zh | bge-large-zh | stella-base-zh | stella-large-zh | 
|:---------------:|:---------------:|:----------------:|:-----------:|:------------:|:--------------:|:---------------:|
|    CMRC2018     |      94.34      |      93.82       |    91.56    |    93.12     |     96.08      |      95.56      | 
|      CAIL       |      28.04      |      33.64       |    31.22    |    33.94     |     34.62      |      37.18      | 
|      DRCD       |      78.25      |       77.9       |    78.34    |    80.26     |     86.14      |      84.58      | 
|    Military     |      76.61      |      73.06       |    75.65    |    75.81     |     83.71      |      80.48      | 
|      Squad      |      91.21      |      86.61       |    87.87    |    90.38     |     93.31      |      91.21      | 
| Multifieldqa_zh |      81.41      |      83.92       |    83.92    |    83.42     |      79.9      |      80.4       | 
|   **Average**   |      74.98      |      74.83       |    74.76    |    76.15     |   **78.96**    |    **78.24**    | 

**注意：** 因为长文本评测数据数量稀少，所以构造时也使用了train部分，如果自行评测，请注意模型的训练数据以免数据泄露。

## Usage

#### stella 中文系列模型

stella-base-zh 和 stella-large-zh: 本模型是在piccolo基础上训练的，因此**用法和piccolo完全一致**
，即在检索重排任务上给query和passage加上`查询: `和`结果: `。对于短短匹配不需要做任何操作。

stella-base-zh-v2 和 stella-large-zh-v2: 本模型使用简单，**任何使用场景中都不需要加前缀文本**。

stella中文系列模型均使用mean pooling做为文本向量。

在sentence-transformer库中的使用方法：

```python
# 对于短对短数据集，下面是通用的使用方式
from sentence_transformers import SentenceTransformer

sentences = ["数据1", "数据2"]
model = SentenceTransformer('infgrad/stella-base-zh-v2')
print(model.max_seq_length)
embeddings_1 = model.encode(sentences, normalize_embeddings=True)
embeddings_2 = model.encode(sentences, normalize_embeddings=True)
similarity = embeddings_1 @ embeddings_2.T
print(similarity)
```

直接使用transformers库：

```python
from transformers import AutoModel, AutoTokenizer
from sklearn.preprocessing import normalize

model = AutoModel.from_pretrained('infgrad/stella-base-zh-v2')
tokenizer = AutoTokenizer.from_pretrained('infgrad/stella-base-zh-v2')
sentences = ["数据1", "数据ABCDEFGH"]
batch_data = tokenizer(
    batch_text_or_text_pairs=sentences,
    padding="longest",
    return_tensors="pt",
    max_length=1024,
    truncation=True,
)
attention_mask = batch_data["attention_mask"]
model_output = model(**batch_data)
last_hidden = model_output.last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0)
vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]
vectors = normalize(vectors, norm="l2", axis=1, )
print(vectors.shape)  # 2,768
```

#### stella models for English

developing...

## Training Detail

**硬件：** 单卡A100-80GB

**环境：** torch1.13.*; transformers-trainer + deepspeed + gradient-checkpointing

**学习率：** 1e-6

**batch_size：** base模型为1024，额外增加20%的难负例；large模型为768，额外增加20%的难负例

**数据量：** 第一版模型约100万，其中用LLM构造的数据约有200K. LLM模型大小为13b。v2系列模型到了2000万训练数据。

## ToDoList

**评测的稳定性：**
评测过程中发现Clustering任务会和官方的结果不一致，大约有±0.0x的小差距，原因是聚类代码没有设置random_seed，差距可以忽略不计，不影响评测结论。

**更高质量的长文本训练和测试数据：** 训练数据多是用13b模型构造的，肯定会存在噪声。
测试数据基本都是从mrc数据整理来的，所以问题都是factoid类型，不符合真实分布。

**OOD的性能：** 虽然近期出现了很多向量编码模型，但是对于不是那么通用的domain，这一众模型包括stella、openai和cohere,
它们的效果均比不上BM25。

## Reference

1. https://www.scidb.cn/en/detail?dataSetId=c6a3fe684227415a9db8e21bac4a15ab
2. https://github.com/wangyuxinwhy/uniem
3. https://github.com/CLUEbenchmark/SimCLUE
4. https://arxiv.org/abs/1612.00796
5. https://kexue.fm/archives/8847
6. https://huggingface.co/sensenova/piccolo-base-zh
7. https://kexue.fm/archives/7947
8. https://github.com/FlagOpen/FlagEmbedding
9. https://github.com/THUDM/LongBench


