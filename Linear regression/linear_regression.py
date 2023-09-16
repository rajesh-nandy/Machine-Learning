from sklearn.datasets import make_regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax


class LinearRegression:
    def __init__(self):
        self.parameters = {}

    def forward_propagation(self, train_input):
        m = self.parameters['m']
        c = self.parameters['c']
        predictions = np.multiply(m, train_input) + c
        return predictions

    def cost_function(self, predictions, train_output):
        cost = (train_output-predictions)**2
        return cost
    
    
    def backward_propagation(self, train_input, train_output, predictions):
        derivatives = {}
        df = (train_output - predictions) * -1
        dm = np.mean(np.multiply(train_input, df))
        dc = np.mean(df)
        derivatives['dm'] = dm
        derivatives['dc'] = dc
        return derivatives

    def update_parameters(self, derivatives, learning_rate):
        self.parameters['m'] = self.parameters['m'] - learning_rate * derivatives['dm']
        self.parameters['c'] = self.parameters['c'] - learning_rate * derivatives['dc']

    def train(self, train_input, train_output, learning_rate, iters):
            #initialise random parameters
            self.parameters['m'] = np.random.uniform(0,1) * -1
            self.parameters['c'] = np.random.uniform(0,1) * -1
            #initialise loss
            self.loss = []
            
            rows = 4
            columns = 5
            k = 1
            fig = plt.figure()
            
            fig.tight_layout(pad=5)
            #iterate
            for i in range(iters):
                #forward propagation
                predictions = self.forward_propagation(train_input)
    
                #cost function
                c= self.cost_function(predictions, train_output)

                cost = np.mean(c)

                if(i % 1000 == 0):
                    fig.add_subplot(rows, columns, k)
                    plt.plot(c , "*")
                    plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
                    k += 1
                    plt.title("iteration = " + str(i))
                #append loss and print
                self.loss.append(cost)
                print("Iteration =", i+1, "Loss = ", cost, end = "\t")

                #back propagation
                derivatives = self.backward_propagation(train_input, train_output, predictions)
    
                #update parameters
                self.update_parameters(derivatives, learning_rate)
                print(self.parameters)
            plt.suptitle("Error graph in the various phases of training\n(showing error for each training input)")
            plt.show()
            

            return self.parameters, self.loss
            






# generate regression dataset
x, y = make_regression(n_samples=1000, n_features= 1, noise=5)
# plot regression dataset

train_input = np.array(x[0:800])
train_output  = np.array(y[0:800]).reshape(800,1)

plt.plot(train_input, train_output, '+', label='Training input set')
plt.xlabel('Training input')
plt.ylabel('Training Output')
plt.legend()
plt.show()


test_input = np.array(x[800:1000])
test_output = np.array(y[800:1000]).reshape(200,1)


linear_reg = LinearRegression()
#Training with various learning rate
learning_rate = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.0001]

for l in learning_rate:
    parameters, loss = linear_reg.train(train_input, train_output, l, 20000)
    #Change in Cost through training
    plt.plot(loss)
    plt.suptitle('Change in cost through the iterations \nFor learning rate = '+ str(l))
    plt.xlabel('Training input')
    plt.ylabel('cost')
    plt.show()

#Predicted  model on training data
y_est = train_input*parameters['m'] + parameters['c']
plt.plot(train_input, train_output, '+', label='Training input set')
plt.plot(train_input, y_est,  label='Predicted curve')
plt.xlabel('Training input')
plt.ylabel('Training Output')
plt.suptitle('Predicted model')
plt.legend()
plt.show()

#Prediction on test data
y_pred = test_input*parameters['m'] + parameters['c']

# Plot the regression line with actual data pointa
plt.plot(test_input, test_output, '+', label='Actual values')
plt.plot(test_input, y_pred, label='Predicted values')
plt.xlabel('Test input')
plt.ylabel('Test Output or Predicted output')
plt.suptitle('Testing out the model')

plt.legend()
plt.show()

