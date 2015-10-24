#!/usr/bin/python
# _moduleFunc for module private -- will not be imported
# __classFunc for class private -- it's not actually private, but it's tradition
import numpy as np
import math
# import cython # BE SURE TO STATIC TYPE WHAT NEEDS TO BE STATIC TYPED, BRUH

# Not using sigmoid right now
# def _sigmoid(x):
#     return 1 / (1 + math.exp(-x))
#
# def _dsigmoid(x):
#     return math.exp(x) / pow(1 + math.exp(x), 2)

def _dtanh(x):
    return 1 - pow(np.tanh(x), 2)

def _ddtanh(x):
    tanh_x = np.tanh(x)
    return 2 * (pow(tanh_x, 3) - tanh_x)

def _randND(*dims)
    return np.random.rand(dims)*2 - 1 # ayo, static type this

def _sum_sq_err(input, target):
    residue = input - target
    return 0.5 * np.dot(residue, residue)

class Net:
    """defines a neural network object"""

    def __init__(self, input_len, output_len, layer0_len, layer1_len, layer2_len):
        """This instantiates a neural network
        
        Args:
            self (obj) -- the object being instatiated itself, implicitly called
                            WIP           
        """
        self.input_len = input_len
        self.layer0_len = layer0_len
        self.layer1_len = layer1_len
        self.layer2_len = layer2_len
        self.output_len = output_len

        self.input = np.ones(input_len + 1).reshape(input_len + 1, 1)

        self.activation0 = np.ones(layer0_len + 1).reshape(layer0_len + 1, 1)
        self.activation1 = np.ones(layer1_len + 1).reshape(layer1_len + 1, 1)
        self.activation2 = np.ones(layer2_len + 1).reshape(layer2_len + 1, 1)

        self.hmap0 = np.tanh(self.activation0)
        self.hmap1 = np.tanh(self.activation1)
        self.hmap2 = np.tanh(self.activation2)

        self.output = np.zeros(output_len).reshape(output_len, 1)

        self.delta0 = np.zeros(layer0_len).respahe(layer0_len, 1)
        self.delta1 = np.zeros(layer1_len).reshape(layer1_len, 1)
        self.delta2 = np.zeros(layer2_len).reshape(layer2_len, 1)
        self.delta3 = np.zeros(output_len).reshape(output_len, 1)

        self.r_activation0 = np.zeros(layer0_len + 1).reshape(layer0_len + 1, 1)
        self.r_activation1 = np.zeros(layer1_len + 1).reshape(layer1_len + 1, 1)
        self.r_activation2 = np.zeros(layer2_len + 1).reshape(layer2_len + 1, 1)
        
        self.r_hmap0 = self.hmap0
        self.r_hmap1 = self.hmap1
        self.r_hmap2 = self.hmap2

        self.r_output = self.output

        self.r_delta0 = self.delta0
        self.r_delta1 = self.delta1
        self.r_delta2 = self.delta2
        self.r_delta3 = self.delta3

        self.weight0 = np.matrix(np.ones(input_len + 1, layer0_len))
        self.weight1 = np.matrix(np.ones(layer0_len + 1, layer1_len))
        self.weight2 = np.matrix(np.ones(layer1_len + 1, layer2_len))
        self.weight3 = np.matrix(np.ones(layer2_len + 1, output_len))
        
        self.g_weight0 = np.matrix(np.zeros(input_len + 1, layer0_len))
        self.g_weight1 = np.matrix(np.zeros(layer0_len + 1, layer1_len))
        self.g_weight2 = np.matrix(np.zeros(layer1_len + 1, layer2_len))
        self.g_weight3 = np.matrix(np.zeros(layer2_len + 1, output_len))

        self.r_weight0 = self.g_weight0
        self.r_weight1 = self.g_weight1
        self.r_weight2 = self.g_weight2
        self.r_weight3 = self.g_weight3

    def feedforward(self, input):
        """runs the net with given input and saves hidden activations"""
        if input.shape() != self.input_shape:
            raise ValueError("Input dimensions not match expected dimensions")
        
        self.input = input.append(1).T
        for j in range(self.layer0_len):
            self.activation0[j] = self.weight0[:,j] * input_b
        self.hmap0 = np.tanh(self.activation0)
        
        for k in range(self.layer1_len):
            self.activation1[k] = self.weight1[:,k] * self.hmap0
        self.hmap1 = np.tanh(self.activation1)
        
        for l in range(self.layer2_len):
            self.activation2[l] = self.weight2[:,l] * self.hmap1
        self.hmap2 - np.tanh(self.activation2)

        for m in range(self.output_len):
            self.output = self.weight3[:,m] * self.hmap2

        return self.output

   def __backprop(self, target):
        self.delta3 = self.output - target
        for m in range(self.output_len):
            for l in range(self.layer2_len + 1):
                self.g_weight3[l,m] = self.delta3[m] * self.hmap2[l]
        for l in range(self.layer2_len):
            for m in range(self.output_len):
                self.delta2[l] += self.delta3[m] * self.weight3[l,m]
            for k in range(self.layer1_len + 1):
                self.g_weight2[k,l] = self.delta2[l] * _dtanh(self.activation2[l]) * self.hmap1[k,l]
        for k in range(self.layer1_len):
            for l in range(self.layer2_len):
                self.delta1[k] += self.delta2[l] * _dtanh(self.activation2[l]) * self.weight2[k,l]
            for j in range(self.layer1_len + 1):
                self.g_weight1[j,k] = self.delta1[k] * _dtanh(self.activation1[k]) * self.hmap0[j,k]
        for j in range(self.layer0_len):
            for k in range(self.layer1_len):
                self.delta0[j] += self.delta1[k[ * _dtanh(self.activation1[k]) * self.weight1[j,k]
            for i in range(self.input_len + 1):
                self.g_weight0[i,j] = self.delta0[j] * _dtanh(self.activation0[j]) * self.input[i,j]

    def __r_pass(self):
        for j in range(self.layer0_len):
            for i in range(self.input_len + 1):
                self.r_activation0[j] += self.g_weight0[i,j] * self.input[i]
            self.r_hmap0[j] = _dtanh(self.activation0[j]) * self.r_activation[j]

        for k in range(self.layer1_len):
            for j in range(self.layer0_len + 1):
                self.r_activation1[k] += self.weight1[j,k] * self.r_hmap0[j] + self.g_weight1[j,k] * self.hmap0[j]
            self.r_hmap1[k] = _dtanh(self.activation1[k]) * self.r_activation1[k]

        for l in range(self.layer2_len):
            for k in range(self.layer1_len + 1):
                self.r_activation2[l] += self.weight2[k,l] * self.r_hmap1[k] + self.g_weight2[k,l] * self.hmap1[k]
            self.r_hmap2[l] = _dtanh(self.activation2[l]) * self.r_activation2[l]

        for m in range(self.output_len):
            for l in range(self.layer2_len + 1):
                self.r_output += self.weight2[l,m] * self.r_hmap2[l] + self.g_weight3[l,m] * self.hmap2[l]

        # more efficient to calculate deltas & Hessian-gradient product simultaneously
        self.r_delta3 = self.r_output
        for l in range(self.layer2_len):
            for m in range(self.output_len):
                self.r_delta2[l] += self.r_delta3[m] * self.weight3[l,m]
                self.r_delta2[l] += self.delta3[m] * self.g_weight3[l,m]

        for k in range(self.layer1_len):
            for l in range(self.layer2_len):
                self.r_delta1[k] += self.r_delta2[l] * _dtanh(self.activation2[l]) * self.weight2[l,m]
                self.r_delta1[k] += self.delta2[l] * _ddtanh(self.activation2[l]) * self.r_activation2[l] * self.weight2[l,m]
                self.r_delta1[k] += self.delta2[l] * _dtanhself.activation2[l]) * self.g_weight[l,m]
        for j in range(self.layer0_len):
            for k in range(self.layer1_len):
                self.r_delta0[j] += self.r_delta1[k] * _dtanh(self.activation1[k]) * self.weight1[j,k]
                self.r_delta0[j] += self.delta1[k] * _ddtanh(self.activation1[k] * self.r_activation1[k] * self.weight1[j,k]
                self.r_delta0[j] += self.delta[k] * _dtanh(self.activation1[k]) * self.g_weight1[j,k]

        for m in range(self.output_len):
            for l in range(self.layer2_len + 1):
                self.r_weight3[l,m] = self.r_delta3[m] * self.hmap2[l] 
                self.r_weight3[l,m] += self.delta3[m] * self.r_hmap2[l]

        for l in range(self.layer2_len):
            for k in range(self.layer1_len + 1):
                self.r_weight2[k,l] = self.r_delta2[l] * _dtanh(self.activation2[l]) * self.hmap1[k]
                self.r_weight2[k,l] += self.delta2[l] * _ddtanh(self.activation2[l]) * self.r_activation2[l] * self.hmap1[k]
                self.r_weight2[k,l] += self.delta2[l] * _dtanh(self.activation2[l]) * self.r_hmap1[k]

        for k in range(self.layer1_len):
            for j in range(self.layer0_len + 1):
                self.r_weight1[j,k] = self.r_delta1[k] * _dtanh(self.activation1[k]) * self.hmap0[j]
                self.r_weight1[j,k] += self.delta1[k] * _ddtanh(self.activation1[k]) * self.r_activation1[k] * self.hmap0[j]
                self.r_weight1[j,k[ += self.delta1[k[ * _dtanh(self.activation1[k]) * self.r_hmap0[j]

        for j in range(self.layer0_len):
            for i inrange(self.input_len):
                self.r_weight0[i,j] = self.r_delta0[j] * _dtanh(self.activation0[j]) * self.input[i]
                self.r_weight0[i,j] += self.delta0[j] * _ddtanh(self.activation0[j]) * self.r_activation0[j] * self.input[i]

    def __weight_CGD():
        
 
    def train_N(self, input, target, N):
        if target.shape() != self.output_len:
            raise ValueError("Target dimensions do not match output dimensions")    
        result = self.feedforward(input)
        for i in range(N - 1):
            self.__backprop(target)
            self.__r_pass()
            self.__weight_CGD()
            result - self.feedforward(input)
            print _sum_sq_err(result, target)
        return result
