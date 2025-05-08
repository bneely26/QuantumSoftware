import numpy as np
import math      
import copy as cp       


class BitString:

    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        str1 = str(self.config)
        str2 = str(other.config)
        return str1 == str2
    
    def __len__(self):
        return len(self.config)

    def on(self):
        count = 0
        for i in self.config:
            if(self.config[i] == 1):
                count+=1
            
        return count


    def off(self):
        count = 0
        for i in self.config:
            if(self.config[i] == 0):
                count+=1
            
        return count


    def flip_site(self,i):
        if(self.config[i] == 0):
            self.config[i] = 1
        else:
            self.config[i] = 0

    
    def integer(self):
        twoPower = len(self.config)-1
        index = 0
        num = 0
        while index < len(self.config):
            num += self.config[index] * (2**twoPower)
            index+=1
            twoPower-=1
        return num



    def set_config(self, s:list[int]):
        self.config = s
    def __str__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def set_integer_config(self, dec:int):
        my_list = []
        highest_2 = len(self.config)-1
        while highest_2 >= 0:
                if(2** highest_2 > dec):
                    my_list.append(0)
                    highest_2 -= 1
                else:
                    my_list.append(1)
                    dec -= 2**highest_2
                    highest_2-=1
        self.set_config(my_list)
        return self.config

            
