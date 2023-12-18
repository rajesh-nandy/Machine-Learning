import numpy as np
import kth_smallest_select as ks
import kth_smallest_random_select as krs
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(columns = ['K' ,'Input_Size', 'Input_Set_Number', 'Algortithm', 'No._of_Comparisons' , 'No._of_Reccursion Call', 'Time_taken'])

for s in range(1,21):
    sample = np.random.randint(2000, size=(70000))

    length  = [1000, 5000, 10000, 20000, 30000, 50000, 60000]
    pos = [50, 100, 250, 389, 453, 578, 677, 867, 235, 945]
    for k in pos:
        l_compc_s, l_compc_rs = [], []
        l_rc_s, l_rc_rs = [], []
        l_t_s, l_t_rs = [], []
        
        for i in length:
            p = sample[0:i]
            z_s, rc_s, compc_s, t_s= ks.KthSmallest(p, len(p),k)
            z_rs, rc_rs, compc_rs, t_rs = krs.KthSmallest(p, len(p),k)
            l_compc_s.append(compc_s)
            l_compc_rs.append(compc_rs)
            l_rc_s.append(rc_s)
            l_rc_rs.append(rc_rs)
            l_t_s.append(t_s)
            l_t_rs.append(t_rs)
            

            data = [k, i, s,  "Select", compc_s, rc_s, t_s ]
            df.loc[len(df)] = data
            data = [k, i, s,  "Random Select", compc_rs, rc_rs, t_rs ]
            df.loc[len(df)] = data

            print("k=",k,"th element =", z_s, rc_s, compc_s, t_s)
            print("k=",k,"th element =", z_rs, rc_rs, compc_rs, t_rs)
        
        

        
        if(s == 1):
            title = "k="+ str(k)+ "th smallest element "
            plt.title(title)
            plt.xlabel("Sample size", color="blue",fontsize=14)
            plt.ylabel("No. of Compariosns", color="green",fontsize=14)
            plt.plot(length, l_compc_s, color ="red", label = "select algorithm")
            plt.plot(length, l_compc_rs, color ="blue", label = "randomized select algorithm")
            plt.legend()
            plt.show()

df.to_csv("kth_Smallest.csv", index=False)
print(df)
