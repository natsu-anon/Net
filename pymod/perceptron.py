#!usr/bin/python

import numpy as np
import numpy.random as nr
import onehot as oh


class Perceptron:


    def __init__(self, x_len, in_len, h_len, w_scale, peek):
        self.x_len = x_len
        self.in_len = in_len
        self.h_len = h_len
        self.peek = peek
        self.clip_mag = 5

        self.wi = w_scale * nr.randn(h_len, in_len)
        self.wh = w_scale * nr.randn(h_len, h_len)
        if peek:
            self.wp = w_scale * nr.randn(h_len, x_len)
        self.wb = w_scale * nr.randn(h_len, 1)

        self.reset()
        self.grad_reset()


    def ff(self, data, *p):
        h_arg = np.dot(self.wi, data)
        h_arg += np.dot(self.wh, self.h)
        if self.peek:
            p = np.array(p).reshape(self.x_len, 1)
            h_arg += np.dot(self.wp, p)
        self.h = np.tanh(h_arg + self.wb)
        return self.h


    def bp(self, top_err, epsilon, data, h_cur,  h_prev, *p):
        # print epsilon.shape
        # print top_err.shape
        # print h_cur.shape
        delta =  top_err + epsilon
        delta = ( 1 - np.square(h_cur)) * delta
        self.gi += np.dot(delta, data.T)
        self.gh += np.dot(delta, h_prev.T)
        if self.peek:
            p = np.array(p).reshape(self.x_len, 1)
            self.gp += np.dot(delta, p.T)
        self.gb += delta
        return np.dot(self.wi.T, delta), np.dot(self.wh.T, delta)

    def clip_grads(self):
        grad = [self.gi, self.gh, self.gb]
        if self.peek:
            grad += [self.gp]
        for g in grad:
            np.clip(g, -self.clip_mag, self.clip_mag, out=g)


    def adagrad(self, step_size):
        weight = [self.wi, self.wh, self.wb]
        grad = [self.gi, self.gh, self.gb]
        mem = [self.mi, self.mh, self.mb]
        if self.peek:
            weight += [self.wp]
            grad += [self.gp]
            mem += [self.mp]
        for w, g, m in zip(weight, grad, mem):
            m += np.square(g)
            w -= step_size * g / np.sqrt(m + 1e-8)

    def reset(self):
        self.h = np.zeros((self.h_len, 1))


    def grad_reset(self):
        self.gi = np.zeros_like(self.wi)
        self.gh = np.zeros_like(self.wh)
        if self.peek:
            self.gp = np.zeros_like(self.wp)
        self.gb = np.zeros_like(self.wb)


    def mem_reset(self):
        self.mi = np.zeros_like(self.wi)
        self.mh = np.zeros_like(self.wh)
        if self.peek:
            self.mp = np.zeros_like(self.wp)
        self.mb = np.zeros_like(self.wb)

    def set_clip(self, val):
        self.clip_mag = val