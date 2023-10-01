import pandas as pd
import numpy as np 
import itertools

class node:
    def __init__(self, feature = None, threshold = None, right = None, left = None, *, value = None):
        self.feature = feature
        self.threshold = threshold
        self.right = right
        self.left = left
        self.value = value



class tree:
    def __init__(self):
        self.root = None

    
    def _split_list(self, list1):
        splits = []
        for i in range(1, len(list1) + 1):
            combinations = itertools.combinations(list1, i)

            for combination in combinations:
                splits.append(list(combination))

        return splits

    def _gini_index(self, p):
        
        if(p.iloc[:, 0].dtypes == 'O'):
            l = p.iloc[:, 0].unique()
            splits = self._split_list(l)[:-1]
            G = []
            for i in range(len(splits)//2):
                #print(splits[i], splits[-(i+1)])
                left, right = p[p.iloc[:, 0].isin(splits[i])], p[p.iloc[:, 0].isin(splits[-(i+1)])]

                probabilities = left.iloc[:, 1].value_counts(normalize=True)
                left_gini = 1 - np.sum(probabilities**2)
                probabilities = right.iloc[:, 1].value_counts(normalize=True)
                right_gini = 1 - np.sum(probabilities**2)
                left_weight, right_weight = len(left)/len(p), len(right)/len(p)

                weighted_gini_value = left_gini*left_weight + right_gini*right_weight
                G.append(weighted_gini_value)
                

            s = G.index(min(G))
            return [min(G), splits[s]]
            

        else:
            mean = p.iloc[:, 0].mean()
            left, right = p[p.iloc[:, 0]< mean], p[p.iloc[:, 0]>= mean]
            probabilities = left.iloc[:, 1].value_counts(normalize=True)
            left_gini = 1 - np.sum(probabilities**2)
            probabilities = right.iloc[:, 1].value_counts(normalize=True)
            right_gini = 1 - np.sum(probabilities**2)
            left_weight, right_weight = len(left)/len(p), len(right)/len(p)

            weighted_gini_value = left_gini*left_weight + right_gini*right_weight
            return [weighted_gini_value, mean]




    def _select_next_feature(self, x, feature_set, target):
        weight_list = []
        for i in feature_set:
            print("Calculating genie of ", i)
            g = self._gini_index(x[[i, target]])
            
            weight_list.append(g)
        
        z = weight_list.index(min(weight_list))
        print(weight_list)
        return feature_set[z], weight_list[z][1]
        
    
    
    
    def grow_tree(self, x, feature_set, target ):
        feature, split = self._select_next_feature(x, feature_set, target)
        print(feature, split)
        

