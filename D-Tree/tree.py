import pandas as pd
import numpy as np 
import networkx as nx
import itertools
from matplotlib import pyplot as plt
from treelib import Node, Tree

class node:
    def __init__(self, feature = None, threshold = None, right = None, left = None, *, value = None):
        self.feature = feature
        self.threshold = threshold
        self.right = right
        self.left = left
        self.value = value



class tree:
    def __init__(self):
        self.root = node()
        self.g = Tree()
        self.n = 0
        

    
    def _split_list(self, list1):
        splits = []
        for i in range(1, len(list1) + 1):
            combinations = itertools.combinations(list1, i)

            for combination in combinations:
                splits.append(list(combination))

        return splits

    def _gini_index(self, p):
        if(len(p.iloc[:, 0].unique()) == 1):
            probabilities = p.value_counts(normalize=True)
            gini_value = 1 - np.sum(probabilities**2)
            m = (p.iloc[:, 0].unique()).tolist()
            return [gini_value, m]
        
        elif(p.iloc[:, 0].dtypes == 'O'):
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
            return [weighted_gini_value, [str(mean)]]




    def _select_next_feature(self, x, feature_set, target):
        weight_list = []
        for i in feature_set:
            print("Calculating genie of ", i)
            g = self._gini_index(x[[i, target]])
            
            weight_list.append(g)
        
        
        
        
            
        z = weight_list.index(min(weight_list))
        return feature_set[z], weight_list[z][1]
        
    
    
    
    def grow_tree(self, x, parent_node, threshold, feature_set, target ):
        parent_node.threshold = threshold
        if(len(x[target].unique()) == 1):
            print("reached a leaf node!!")
            parent_node.value = x[target].unique()[0]
        else:
            feature, split = self._select_next_feature(x, feature_set, target)
            #print(feature, split)
            
            if(len(x[feature].unique()) == 1):
                print("reached a leaf node with approx value!!")
                parent_node.value = x[target].mode()[0]
                
            
            else:
                if(x[feature].dtypes == 'O'):
                    right = x[x[feature].isin(split)]
                    left = x[~x[feature].isin(split)]
                else:
                    s = float(split[0])
                    right = x[x[feature] > s]
                    left = x[~x[feature] <= s]

                parent_node.feature = feature
                parent_node.right = node()
                parent_node.left = node()
                self.grow_tree(right, parent_node.right, split, feature_set, target)
                self.grow_tree(left, parent_node.left, split, feature_set, target)
                
    def _prediction(self, x):
        check_node = node()
        check_node = self.root
        print("test", x[check_node.feature])
        
        while(check_node.value is None):
            print(check_node.feature)
            
            z = x[check_node.feature]
            
            if(z in (check_node.right.threshold)):
                check_node = check_node.right
            else:
                check_node = check_node.left
        

        #print(check_node.value, x['income'])
        return check_node.value


    def predict_data(self, X):
        pred = []
        for each_line in X.index:
            z = X.loc[each_line]
            pred.append(self._prediction(z))

       
        return pred


    def tree_display(self, current_node, s=" "):
        if(current_node.value is None):
            print(current_node.feature,": ", current_node.right.threshold)
            s = s + "--> "
            print(s, end = "")
            self.tree_display(current_node.right, s)
            print(s, end = "")
            self.tree_display(current_node.left)

        else:
            print(s, "class: ", current_node.value)
            


    def _treecreation(self, n1, current_node):
        n2 = self.n
        self.n += 1
        
        if(current_node.value is None):
            self.g.create_node(current_node.feature, self.n, parent = n1)
            self._treecreation(n2, current_node.right)
            self._treecreation(n2, current_node.left)
        else:
            self.g.create_node(current_node.value, self.n, parent = n1)
            
            
        

        
    def tree_visualization(self):
        self.g.create_node(self.root.feature, self.n)
        self._treecreation(self.n, self.root.right)
        self._treecreation(self.n, self.root.left)
        print(self.g)