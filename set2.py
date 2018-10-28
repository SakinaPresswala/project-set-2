from nltk.tokenize import word_tokenize
import numpy as np

def data_stream():
    """Stream the data in 'leipzig100k.txt' """
    with open('leipzig100k.txt', 'r') as f:
        for line in f:
            for w in word_tokenize(line):
                if w.isalnum():
                    yield w
   
def bloom_filter_set():
    """Stream the data in 'Proper.txt' """
    with open('Proper.txt', 'r') as f:
        for line in f:
            yield line.strip()



############### DO NOT MODIFY ABOVE THIS LINE #################


# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.

def uhf(rng):
    """Returns a hash function that can map a word to a number in the range
    0 - rng
    """
    a = np.random.randint(1,p)
    b = np.random.randint(0,p)
    return lambda x: ((a*x+b)%p)%m

############### 

################### Part 1 ######################
import nltk
nltk.download('punkt')
from bitarray import bitarray
size = 2**18   # size of the filter

a=uhf(2059859,262144)
b=uhf(2059861,262144)
c=uhf(2059879,262144)
d=uhf(2059891,262144)
e=uhf(2059913,262144)
hash_fns = [a,b,c,d,e]  # place holder for hash functions
bit_array=bitarray(size)
bit_array.setall=0
bloom_filter = bit_array

k=[]
for i in data_stream():
    k.append(i)
	
N=[]
for i in bloom_filter_set():
    N.append(i)
	
num_words = len(k)         # number in data stream = 2059856
num_words_in_set = len(N)  # number in Bloom filter's set = 32657

for word in bloom_filter_set(): # add the word to the filter by hashing etc.
    for h in H:
        num=h(int(word,36))
        bloom_filter[num]==1
print(len(bloom_filter))

M=[]
for word in data_stream():  # check for membership in the Bloom filter
    for h in H:
       # num = h(int(word,36))
        if bloom_filter[h(int(word,36))] == 0:
            break
        elif bloom_filter[h(int(word,36))] == 1:
            continue
    M.append(word)
print(len(M))
     
FP=len(set(M)-set(N))
FP

print('Total number of words in stream = %s'%(num_words,))
print('Total number of words in stream = %s'%(num_words_in_set,))
      
################### Part 2 ######################
import random
num_features=2059856
def findPrime(n):
    """Returns a prime number larger than n
    """
    def isPrime(k):
        import math
        for divisor in range(2, round(math.sqrt(n)-0.5)):
            if k%divisor==0:
                return False
        return True
    if n%2==0:
        candidate = n+1
    else:
        candidate = n
    while not isPrime(candidate):
        candidate += 2
    return candidate   

hash_range = 24 # number of bits in the range of the hash functions
fm_hash_functions = [None]*35  # Create the appropriate hashes here
p=findPrime(num_features)

def uhf(p, m):
    a = random.randint(1,p-1)
    b = random.randint(0,p-1)
    return lambda x: ((a*x+b)%p)%m

hash_range = 24  # number of bits in the range of the hash functions
num_hashes = 35
'''
h1=[np.vectorize(uhf(p,2**hash_range))(range(num_features))]
len(h1[0])
'''
hashes=[np.vectorize(uhf(p,2**hash_range))(range(num_features)) for
                                            _ in range(num_hashes)]
len(hashes)

def binary(n):
    return bin(n)

binary_hashes=[]
for i in range(len(hashes)):
    vf= (np.vectorize(binary)(hashes[i]))
    binary_hashes.append(vf)
    
print(len(binary_hashes))
print(binary_hashes[0])
'''
fm_hash_functions = [np.vectorize(uhf(p,2**hash_range))(range(num_features))]*35  # Create the appropriate hashes here
fm_hash_functions[2]
'''
     
def num_trailing_bits(n):
    """Returns the number of trailing zeros in bin(n)
    n: integer
    """
    return len(n)- len(n.rstrip('0'))

#num_trailing_bits('1001000')  #returns 3

trailing_zeros=[]
for i in range(len(binary_hashes)):
    vf= (np.vectorize(num_trailing_bits)(binary_hashes[i]))
    trailing_zeros.append(vf)
print(trailing_zeros[:5])
A=np.vstack(trailing_zeros)
A[2,:]
max_zeros=np.amax(A,axis = 1)
max_zeros.shape
#estimate of distinct elements = 2^20 =1048576
  
num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))
def num_trailing_bits(n):
    """Returns the number of trailing zeros in bin(n)

    n: integer
    """
    pass

num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))

################### Part 3 ######################
sample=np.random.choice(2059856,513)
#sample
#variables=[]
d={}
for i in sample:
    d[i]=k[i]
print(len(d))
'''
for i in sample:
    variables.append(k[i])
print(len(variables))

sample
'''
var_reservoir = [0]*512
second_moment = 0
third_moment = 0

d1={}
for key,value in d.items():
    L1 = k[key:]
    d1[key]=L1.count(value)
print(len(d1))

estimates=[]

for v in d1.values():
    i == 2059856(2*v - 1)
    
    estimates.append( i)

print(len(estimates))


# You can use numpy.random's API for maintaining the reservoir of variables

#for word in data_stream(): # Imoplement the AMS algorithm here
#    pass 
      
print("Estimate of second moment = %s"%(second_moment,))
print("Estimate of third moment = %s"%(third_moment,))


