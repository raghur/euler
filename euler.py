#! /usr/bin/python
from math import sqrt, log, pow
from operator import add, mul
import operator
from datetime import datetime
import itertools
import sys
def fibo(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def is_prime(n):
    """
    Arguments:
    - `p`: the number to check for prime
    """
    if n ==1:
        return False
    elif n % 2 == 0:
        return False
    for i in xrange(3, int(sqrt(n)+1), 2):
        if n%i ==0:
            return False
    return True

def mingt(seq, mv):
    """ find minimum in seq which is greater than min"""
    # print seq, mv
    alt_seq = [ v for v in seq if v > mv]
    return min(alt_seq)

def maxlt(seq, mv):
    alt_seq = [v for v in seq if v < mv]
    return max(alt_seq)

def permutations(seq, reversed=False):
    """
    """
    def next_permutation(perm, reversed):
        i = len(perm) -1
        if reversed:
            comp = operator.lt
            findfn = maxlt
        else:
            comp = operator.gt
            findfn = mingt
        while i > 0  and comp(perm[i-1], perm[i]):
            i -= 1
        candidate = findfn(perm[i:], perm[i-1])
        index = perm.index(candidate, i)
        perm[i-1],perm[index] = perm[index],perm[i-1]
        # print "Sorted Tail: ", sorted(perm[i:])
        return perm[:i] + sorted(perm[i:], reverse=reversed)
    p = sorted(seq)
    if reversed: p.reverse()
    endLoop = p[:]
    while True:
        if type(seq) != type(""):
            yield p[:]
        else:
            yield ''.join(p)
        p = next_permutation(p,reversed)
        if p == endLoop:
            break


def prime_sieve(max):
    """
    Prime number  under a certain max value
    Arguments:
    - `max`:
    """
    primes = [2] + range(3,max,2)
    i = 0
    while  i < len(primes):
        j = 0 
        while primes[j] <= int(sqrt(primes[i])):
            if primes[j] !=0  and primes[i] % primes[j]  ==0:
                primes[i] = 0
                break
            j = j+1
        i = i +1
    return [i for i in primes if i != 0]

def gen_series_until_max(gen,maxval):
    i = 0
    v = gen(i)
    while v < maxval:
        yield v
        i = i + 1
        v = gen(i)
        

def prime_fac(n):
    i = 2
    maxval = n/i + 1
    while i < maxval:
        if n % i ==0:
            yield i
            n = n / i
	    maxval = n + 1
        else:
            i = i + 1

def uniq(generator):
    seen = set()
    for i in generator:
        if not i in seen:
            seen.add(i)
            yield i 

def problem_01():
    """
    print sum of all multiples of 2 or 5 within 100.
    """
    l = [i for i in range(100) if i %2 ==0 or i%5 ==0]
    return reduce (lambda x,y: x + y, l)


def problem_02():
    """
    sum of all even terms in the fibonacci series until 4 mil.
    """
    gen = (i for i in gen_series_until_max(fibo, 4000000) if i % 2 == 0)
    return reduce (lambda x, y: x + y, gen)

def problem_03(n):
    """
    find largest prime factor of the given number.
    Arguments:
    - `n`:
    """
    l = [i for i in prime_fac(n)]
    print l
    return max(l)
    
def findMinFactor(p, d):
    """
    given a number p and a divisor d, finds the minimum n such that p*n mod d == 0
    Arguments:
    - `p`:
    - `d`:
    """
    pfacs = [i for i in prime_fac(p)]
    dfacs = [i for i in prime_fac(d)]
    if len(dfacs) == 0:
        dfacs = [d]
    for i,v  in zip(range(len(dfacs)), dfacs):
        if v in pfacs:
            dfacs[i] =1
            del pfacs[pfacs.index(v)]
    print p, d, dfacs
    return reduce(lambda x, y:x*y, dfacs)

def problem_05(num):
    """
    
    """
    product = num
    for i in range(num,0, -1):
        if product % i != 0:
            m = findMinFactor(product, i)
            product = product * m
    return product
                                    
def problem_06(m):
    """
    
    Arguments:
    - `m`:
    """

    sumofsquares = reduce(add, [x**2 for x in range(1,m+1)])
    sumofnos = reduce(add, [x for x in range(1,m+1)])
    diff= sumofnos**2 - sumofsquares
    return diff

def nthPrime(n):
    """
    
    Arguments:
    - `n`:
    """
    p_n = round(n*log(n)+n*(log(log(n)) - 0.9385))
    print p_n
    return p_n
    
def problem_07(n):
    """
    
    Arguments:
    - `n`: The nth prime to find.
    """
    prime_candidate = nthPrime(n)
    facs = [i for i in prime_fac(prime_candidate)]
    while len(facs) != 0:
        prime_candidate-=1
        facs = [i for i in prime_fac(prime_candidate)]
    return prime_candidate

def problem_08():
    """
    """
    nstr = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
    nstr = ''.join(nstr.strip().split("\n"))
    print nstr
    maxproduct = 0
    maxsubstr = 0
    for i in range(len(nstr) - 5):
        num = nstr[i:i+5]
        product = reduce(mul, [int(c) for c in num])
        if product > maxproduct:
            maxproduct = product
            maxsubstr = num
    return maxsubstr, maxproduct

def problem_09(target):
    """
    
    Arguments:
    - `target`:
    """
    c2 = [(i, i**2) for i in range(1, target+1)]
    print c2

def problem_10(max):
    """
    find sum of primes under max.
    Arguments:
    - `max`:
    """
    return reduce (add, prime_sieve(max))
    

def problem_11():
    """
    find largest product by multiplying 4 nos in horizontal, vertical or diagonal - either up or down.
    """
    ntable = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

def problem_12(count):
    """
    
    Arguments:
    - `count`:
    """
    i =3
    d = num_factors(triangle_number(i))
    while d < count:
        i+=1
        d = num_factors(triangle_number(i))
    print i, d
    return triangle_number(i)

def problem_13():
    """First 10 digits of the sum of the following 100 50 digit nos.
    """
    
    nstr = """
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
    arr = nstr.strip().split("\n");
    narr = [int(s) for s in arr]
    from operator import add
    return reduce (add, narr)

def problem_15():
    """Find the number of non backtracking paths.
    Solution: Every path has n horizontal moves and n vertical moves to form a path of length 2n. so its a question of permutaions. 2n!/n!n!
    """
    return factorial(2*20)/(factorial(n)*factorial(n))

def problem_16():
    """sum of digits of 2^1000
    """
    return reduce(add, [int(i) for i in str(2**1000)])

def max_sum_path(n_triangle):
    """
    """
    n_arr = [l.split(" ") for l in n_triangle.strip().split("\n")]
    for index,value in enumerate(n_arr):
        n_arr[index][:] = [int(i) for i in value]
    for row in xrange(len(n_arr)-2, -1, -1):
        for i,val in enumerate(n_arr[row]):
            n_arr[row][i] = val + max(n_arr[row+1][i],n_arr[row+1][i+1])
    return n_arr[0][0]
    


def problem_18():
    """ Find the path with the largest sum
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    Solution: start from the base and find the sum of the subtree at each row.
    The sum of a node = node val + max(left subtree, right subtree)
    """


    n_triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    return max_sum_path(n_triangle)
    
    
def factorial(n):
    if n==0 or n == 1: return 1
    facn = reduce (mul, xrange(1, n+1))
    return facn

def problem_19():
    """
    """
    count = 0
    for year in xrange(1901, 2001):
        for month in xrange(1,13):
            if datetime(year, month, 1).weekday() == 6:
                count+=1
    return count

def problem_20(n):
    """find the sum of digits in n!
    
    Arguments:
    - `n`:
    """
    return reduce(add, [int(i) for i in str(factorial(n))])

def num_factors(n):
    """
    gives number of factors for n.
    if n can be factorized as a^p*b^q then factors = (p+1)*(q+1)
    """
    facs = [i for i in prime_fac(n)]
    i = 0
    factors = 1
    while len(facs) > 0:
        power = facs.count(facs[0])
        factors *= (power +1)
        for j in range(power):
            facs.remove(facs[0])
    return factors

def divisors(n):
    return proper_divisors(n).union([n])

def proper_divisors(n):
    """
    """
    facs = [i for i in prime_fac(n)]
    divisors = set()
    for n in xrange(1, len(facs)):
        divisors = divisors.union([reduce(mul,list(t)) for t in [i for i in itertools.combinations(facs,n)]])
    return divisors.union([1])

def problem_21():
    """
    """
    sum = 0
    for i in xrange(1, 10000):
        di = reduce(add, proper_divisors(i))
        if i!=di and reduce(add, proper_divisors(di)) == i:
            sum+=(i+di)
            print i, proper_divisors(i), di, proper_divisors(di)
    return sum/2

def problem_22(filename="names.txt"):
    name_arr = eval("[" + open(filename, "r").readline().strip() + "]")
    name_arr.sort()
    # print name_arr[:10]
    sum = 0
    for i,val in enumerate(name_arr):
        sum += (i+1)* reduce (add, [ord(c) - 64 for c in val])
    return sum

def problem_25(num_digits = 1000):
    """
    """
    fn = 1
    fn_1 = 0
    fib = fn+fn_1
    i = 2
    while(len(str(fib))) < num_digits:
        i+=1
        fn_1 = fn
        fn = fib
        fib = fn+ fn_1
    print fib
    return i

def problem_26(n=1000):
    """Find the value of d < 1000 for which 1/d contains the longest recurring cycle."""
    
    def reciprocal_digit_gen(k):
        """ generate subsequent digits of the fractional part of a reciprocal of k"""
        iters = 0
        lastrem = 1
        cache = []
        found = False
        while lastrem != 0 and not found:
            digit = lastrem *10/k
            cache.append(lastrem *10)
            lastrem = (lastrem *10) % k
            if lastrem *10  in cache:
                found = True
                return len(cache[cache.index(lastrem *10):])
        return 0

    maxlen = 0
    k = 0
    for i in xrange (2, n):
        l = reciprocal_digit_gen(i) 
        if l  >  maxlen:
            maxlen = l
            k = i
    print "%s  Length=%s" % (k,maxlen)
    return (k, maxlen)
            
def triangle_number(n):
    return n*(n+1)/2
def pentagonal(n):
    return n*(3*n -1)/2
def hexagonal(n):
    return n*(2*n -1)
def problem_28(side_length=1000):
    """
    sum of digits along the diagonal of a 1001* 1001 spiral.
    21  22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    The series formed is 1, 3, 5, 7, 9, 13, 17, 21, 25,....
    ie 4 terms in each ring, with a steps of 2, 4, 6, 8....
    Arguments:
    - `side_length`:
    """
    sum, start_val = 1L, 1
    for i in xrange(2, side_length,2):
        sum+= reduce(add, range(start_val+i, start_val + 4*i +1, i))
        start_val += 4*i
    return sum

def problem_29():
    """
    number of unique items in the set a^b for 2<=a<=100, 2<=b <=100
    """
    for a in xrange(2,101):
        s=s.union([a**b for b in xrange(2,101)])
    return len(s)

def problem_32():
    """
    """
    products = set()
    for s in permutations("123456789"):
        if int(s[:2])*int(s[2:5]) == int(s[-4:]) or \
                int(s[:3]) * int(s[3:5]) == int(s[-4:]) or \
                int(s[:1]) * int(s[1:5]) == int(s[-4:]) or \
                int(s[:4]) * int(s[4:5]) == int(s[-4:]):
            products.add(int(s[-4:]))
    print products
    return reduce(add, products)

def problem_34():
    """
    """
    sum = 0
    for i in xrange(3, 7*factorial(9)):
        sumfacs = reduce(add, [factorial(int(d)) for d in str(i)])
        if sumfacs == i:
            print i
            sum+=i
    return sum
            
def rotate_num(n):
    """
    """
    j = n
    k = 10
    while j%k != j: k *= 10
    m = k/10
    rot  = 0
    while rot!=n:
        digit = j % 10
        rot = digit *m + j/10
        yield rot
        j = rot
    
def problem_35(max=1000000):
    count = 0
    primes = set(prime_sieve(max))
    for prime in primes:
        found = True
        for rotation in rotate_num(prime):
            if rotation not in primes:
                found = False
        if found:
            print prime
            count += 1
    return count
def problem_37(n=11):
    """
    
    Arguments:
    - `count`:
    """
    def truncatable_prime_gen(n):
        count, start_val = 0, 11
        while count < n:
            if is_truncatable_prime(start_val):
                yield start_val
                count +=1
            start_val+=2
            # if start_val % 1000 == 1:
            #     print start_val
    return reduce(add, truncatable_prime_gen(n))
        
invalid_num_set = set("012468")
def is_truncatable_prime(p):
    k = 10
    prime = p
    while prime > 0 and is_prime(prime):
        prime =  prime/10
        # rem = prime % 10
        # print prime, rem
        # if p > 100 and rem % 2 == 0:
        #     return False
    if prime == 0:
        prime = p % 10
        while prime != p and is_prime(prime):
            k = k *10
            prime = p % k
        return prime == p
    else:
        return False




def problem_40():
    """
    """
    s = ''
    g = itertools.count(1)
    while len(s) < 1000000:
        s += str(g.next())
    positions = [10,100,1000,10000,100000,1000000]
    digits = [int(s[i-1]) for i in positions]
    return reduce(mul, digits)

def problem_41():
    """ find the largest  n pandigital prime"""
    s = "1234567"
    found = False
    p = ""
    while not found:
        for i in permutations(s, True):
            if is_prime(int(i)):
                found = True
                p  = i
                break
        s = s[:-1]
    return p
def problem_42(filename="words.txt"):
    words = eval("[" + file(filename,"r").readline() + "]")
    score={}
    for word in words:
        score[word] = reduce(add, [ord(c) - 64 for c in word])
    tnos = [i for i in gen_series_until_max(triangle_number, max(score.values()))]
    count = 0
    for k,v in score.items():
        if v in tnos:
            count+=1
    return count

def problem_43():
    """
    """
    def gen_divisible_pandigitals():
        divisors = [2,3,5,7,11,13,17]
        for n in permutations([0,1,2,3,4,5,6,7,8,9]):
            if n[0] == 0:
                continue
            d_idx = len(divisors) - 1
            found = True
            for x in xrange(10, 3, -1):
                sub = int(''.join([str(i) for i in n[x-3:x]]))
                if sub % divisors[d_idx] != 0:
                    found = False
                    break
                d_idx -=1
            if found: yield int(''.join([str(d) for d in n]))
    return reduce(add, [i for i in gen_divisible_pandigitals()])
                     
def problem_45():
    """Find the next triangle number that is also pentagonal and hexagonal after 40755 = T285 = P165 = H143
    """
    t= 285 + 1
    
    while True:
       tnext = triangle_number(t) 
       p= int(sqrt(2.0*tnext/3))
       h = int(sqrt(1.0 * tnext/2))
       pnext = pentagonal(p)
       while pnext < tnext:
           p += 1
           pnext = pentagonal(p)
       hnext = hexagonal(h)
       while hnext <  tnext:
           h += 1
           hnext = hexagonal(h)
       if pnext == hnext and hnext == tnext:
           return t,p,h,tnext,pnext,hnext
       t += 1



def problem_48(n):
    return str(reduce(add, [i**i for i in xrange(1, 1001)]))[-10:]

def is_permutation(p,q):
    result = (set(str(p)) == set(str(q)))
    return result
    
def problem_49():
    """
    """
    def prime_seq():
        primes = [i for i  in prime_sieve(10000) if i > 1000]
        cmp_set = set(primes)
        for i,p in enumerate(primes):
            for pnext in primes[i+1:]:
                if (pnext + (pnext - p)) in cmp_set:
                    yield p, pnext, pnext + (pnext-p)
    

    for i,j,k  in prime_seq():
        if is_permutation(i,j) and is_permutation(j,k):
            yield i,j,k

def problem_52():
    """
    """
    n = 1
    while True:
        p = [n*i for i in xrange(1, 7)]
        found = True
        for i in xrange(len(p) - 2):
            if not is_permutation(p[i], p[i+1]):
                found = False
                break
        if found:
            print n
            break
        n += 1

def problem_53():
    total = 0
    for n in xrange(1, 101):
        for r in xrange(1, n+1):
            if factorial(n)/(factorial(r)*factorial(n-r)) > 1000000:
                total +=1
    return total


def problem_55(limit = 10000):
    """
    """
    def is_lychrel(x):
        has_palindrome = False
        for i in xrange(50):
            x += int(str(x)[::-1])
            if x == int(str(x)[::-1]):
                has_palindrome = True
                break
        return not has_palindrome

    count  = 0
    for i in xrange(1, limit+1):
        if is_lychrel(i): count+=1
    return count

def problem_56():
    """
    """
    sum, max, fa,fb = 0,0,0,0
    for a in xrange(90,100):
        for b in xrange(90,100):
            sum = reduce(add, [int(i) for i in str(a**b)])
            if sum > max: max, fa,fb = sum, a, b
    print max, fa, fb
    return max
    

    

def problem_67(filename="triangle.txt"):
    """same as problem 18 with a larger triangle.
    """
    triangle =  open(filename,"r").read()
    return max_sum_path(triangle)

def problem_81(filename="matrix.txt"):
    file = open(filename,"r")
    matrix=[eval("[" + line.strip() + "]") for line in file]
    lastrow = matrix[-1]
    for i in xrange(len(lastrow) -2, -1, -1):
        lastrow[i] += lastrow[i+1]
    for row in xrange(len(matrix) -2, -1 , -1):
        matrix[row][-1] += matrix[row+1][-1]
    for i in xrange(len(matrix) -2, -1, -1):
        for j in xrange(len(matrix[i])-2, -1, -1):
            matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1])
    return matrix[0][0]

def problem_82(filename="problem_82.txt"):
    matrix = [eval("[" + line.strip() + "]") for line in open(filename,"r")]

def problem_9():
    """ Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000."""
    for a in xrange(1,1000):
        for b in xrange(1,1000):
            csqrd = a*a + b*b
            c = sqrt(csqrd)
            if (a+b+c) == 1000:
                print a, b, c
                return reduce(mul, (a, b, c))

def problem_11():
    data = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
    matrix = [[int(s) for s in line.split(" ")] for line in data.split("\n")]
    product =1
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            hprod = reduce(mul, matrix[i][j:j+4])
            vprod = 1
            for r in xrange(i, i+4):
                if r < 20:
                    vprod *= matrix[r][j]
                else:
                    break
            dprod = 1
            for r in xrange(0, 4):
                if i + r < 20 and j + r<20:
                    dprod *= matrix[i+r][j+r]
                else:
                    break
            dprod2 = 1
            for r in xrange(0,4):
                if i -r >=0 and j +r < 20:
                    dprod2 *= matrix[i-r][j+r]
                else:
                    break
            product = max(product,hprod,vprod,dprod,dprod2)
            # print "matrix[%s][%s]=%s: %s, %s, %s, %s" % (i,j, matrix[i][j], hprod, vprod, dprod, dprod2)
    return product
    
def problem_14(limit=1000000):
    cache = {}
    def seqlen(n):
        l = 0
        nt = n
        while n != 1:
            if n in cache:
                l+= cache[n]
                break
            if n % 2 ==0:
                n = n/2
            else:
                n = 3*n + 1
            l+=1
        cache[nt] = l
        return l
    return max(((i,seqlen(i)) for i in xrange(1, limit)), key=lambda(s):s[1])

def problem_39(limit=1000):
    def triplet_count(p):
        count = 0
        for a in xrange(1, p):
            for b in xrange(1, a):
                c = sqrt(a**2 +b**2)
                if c > p/2:
                    break
                if a + b + c  == p:
                    count+=1
        return count

    return max(((i,triplet_count(i)) for i in xrange(1, limit+1)), key=lambda(s):s[1])

def problem_36(limit=1000000):
    binary={'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
    def toBinaryStr(x):
        octStr = "%o" % x
        binstr = ''.join([binary[s] for s in octStr])
        if binstr[0:2] =='00':
            binstr = binstr[2:]
        elif binstr[0] == '0':
            binstr = binstr[1:]
        return binstr
        # binstr=''
        # while x > 0:
        #     binstr += str(x % 2)
        #     x = x / 2
        # return binstr
    
    total = 0
    for i in xrange(1, limit, 2):
        decstr = str(i)
        binstr = toBinaryStr(i)
        if decstr == decstr[::-1] and binstr == binstr[::-1]:
            print i,binstr
            total += i
    return total


def problem_50(limit=1000000):
    prime_list = prime_sieve(4000)
    sum_prime, max_prime, chain,max_chain = 0,0,0,0
    for i, p in enumerate(prime_list[:20]):
        if max_chain > len(prime_list) - i:
            break
        for j in xrange(len(prime_list)-1, i, -1):
            if prime_list[j] > limit:
                continue
            sum_prime = reduce(add, prime_list[i:j])
            if sum_prime < limit  and is_prime(sum_prime):
                if j - i > max_chain:
                    max_chain = j - i
                    max_prime = sum_prime
                    print sum_prime, max_chain, prime_list[i:j]
                break
    return max_prime, max_chain

def problem_33():
    """
    http://projecteuler.net/index.php?section=problems&id=33
    """
    product = 1
    for numerator in xrange(11,100):
        for denominator in xrange(numerator + 1,100):
            num_digits = [int(i) for i in str(numerator)]
            den_digits = [int(i) for i in str(denominator)]
            common = filter(lambda(x) :  x in den_digits, num_digits)
            if len(common) > 0 and common[0] <> 0:
                num_digits.remove(common[0])
                n2 = int(num_digits[0])
                den_digits.remove(common[0])
                d2 = float(den_digits[0])
                if d2 <>0  and n2/d2 == numerator/float(denominator):
                    print numerator, "/", denominator
                    product *= d2
    return product
                
def problem_44():
    """
    http://projecteuler.net/index.php?section=problems&id=44
    """
    def gen_pentagonal(n):
        return (i*(3*i-1)/2 for i in xrange(1, n))
    
    def is_pentagonal(pk):
        i = (sqrt(24*pk + 1) + 1)/6.0
        return i == int(i)

    plist = [i for i in gen_pentagonal(10000)]
    print plist[-2:]
    # print plist
    for dis in xrange(1,len(plist)/2):
        for j in xrange(len(plist) - dis):
            s = plist[j] + plist[j+dis]
            d = plist[j+dis] - plist[j]
            if is_pentagonal(s) and is_pentagonal(d):
                print j, j+dis, plist[j], plist[j+dis], s, d 

def sum_proper_divisors(n):
    """
    """
    i, s = 2, 1
    while i < int(sqrt(n)) + 1:
        if n % i == 0:
            s += i
            if i <> n/i:
                s += n/i
        i +=1
    
    return s

    


def problem_23(limit=30000):
    """
    
    """
    def is_abundant(k):
        return sum_proper_divisors(k) > k
    abundant_list = filter(is_abundant, xrange(1,limit))
    abundant_nos = set(abundant_list)
    print 0 in abundant_nos
    print len(abundant_list), abundant_list[1:10]
    abundant_list = []
    asum = 0
    for candidate in xrange(1, limit):
        if not any(((candidate - k) in abundant_nos for k in abundant_nos)):
            print candidate
            asum += candidate
    return asum

def problem_31(denominations=[1,2, 5,10, 20, 50, 100, 200], total = 200):
    sum = 0
    for l in xrange(1, len(denominations)):
        c = itertools.combinations(denominations, l)
        # matches = filter(lambda x: reduce(add, x) == total, c)
        # print l, matches
        # sum += len(matches)
        lc = [k for k in c]
        print "Possible sets of length %s" % l, lc, len(lc)
        ways = [possible_sums(i, 200) for i in lc]
        for t,w in itertools.izip(lc, ways):
            print t, w
        sum += reduce(add, ways)
    return sum

def possible_sums(l, total):
    if len(l) == 0 or total ==0:
        return 0
    elif len(l) == 1:
        if total % l[0] ==0:
            return 1
        else:
            return 0
    else:
        s = 0
        for i in xrange(1, total/l[-1]+1):
            # print l[:-1], total - l[-1]*i
            s += possible_sums(l[:-1], total - l[-1]*i)
        # print l, total,  s
        return s

def problem_47(maxlen = 4):
    found = False
    i = 2*3*5*7 + 1
    while not found:
        # facs = [len([j for j in uniq(prime_fac(i+k))]) for k in xrange(0,maxlen)]
        d = 4
        for t in range(i+3, i-1 , -1):
            k = len(list(uniq(prime_fac(t))))
            if k  < 4:
                i = t + 1
                break
            else:
                d -= 1
        if d ==0:
            found = True
            print list(xrange(i, i + maxlen))
        if i % 1000 == 0:
            print i

from fractions import Fraction
def problem_57(maxterms = 1000):
    sNext = Fraction(3,2)
    count = 0
    for i in xrange(2, 1000):
        sNext = 1 + 1/(1 + sNext)
        if len(str(sNext.numerator)) > len(str(sNext.denominator)):
            # print sNext
            count += 1
    return count

def problem_58(pct = 0.10):
    def spiral():
        t, d =1, 1
        while True:
            for i in range(4):
                yield t
                t += d*2
            d +=1
    prime, total = 0, 0
    last_term  = 1
    for k in spiral():
        if is_prime(k):
            prime +=1
        total +=1
        if total % 1000 == 0:
            print prime*1.0/total
        if total >  13 and prime*1.0/total < pct:
            return k - last_term + 1
        last_term = k

def problem_27():
    """Find the product of the coefficients, a and b, for
    the quadratic n^2 +an +b expression that produces the maximum 
    number of primes for consecutive values of n, starting with n = 0.
    """
    maxchain, a_final, b_final  = 0,0,0
    for a in xrange(-1000, 1001):
        for b in xrange(-1000, 1001):
            l, n = 0,0
            while True:
                v = n*n + a*n +b
                if v > 0 and is_prime(v):
                    n = n+1
                    l = l + 1
                else:
                    break
            if n > maxchain:
                maxchain = n
                a_final, b_final = a, b
    return  maxchain, a_final, b_final, a_final*b_final
        
def problem_46():
    """What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """
    i = 9
    while True:
        while is_prime(i):
            i+=2
        found = False
        for j in xrange(i-2, 0, -2):
            if not is_prime(j):
                continue
            square = (i-j)/2
            if int(sqrt(square)) == sqrt(square):
                # print "%s=%s + 2 X %s^2" % (i,j, sqrt(square))
                i += 2
                found = True
                break
        if not found:
            return i

def problem_92():
    """
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
    """
    def nextTerm(k):
        sum = 0
        while k > 0:
            digit = k % 10
            sum += digit*digit
            k = k /10
        return sum

    count = 0
    endSet1 = set([1])
    # print endSet1,endSet89, 1 in endSet1, tempSet, 2 in endSet1
    for i  in xrange (1, 10000000):
        finished = False
        n = i
        while not finished:
            if n in endSet1:
                endSet1.add(i)
                finished = True
            elif n < i and not n in endSet1:
                count += 1
                finished = True
            elif n == 89:
                finished = True
                count += 1
            else:
                # n = reduce(add, [int(d)*int(d) for d in str(n)])
                n = nextTerm(n)
    # print len(endSet1), len(endSet89)
    return count

def problem_59(filename="cipher1.txt"):
    """@todo: Docstring for problem_59

    :filename: @todo
    :returns: @todo

    """
    byteArr = eval ("[" + open(filename, "r").read() + "]")
    key = []
    for pos in xrange(0,3):
        keychar = 0
        maxval = 0
        for k in xrange(ord("a"), ord("z")+1):
            count = 0
            for c in xrange (pos, len(byteArr), 3):
                char = byteArr[c] ^ k
                if char >= ord('A') and char <= ord('Z') \
                    or char >= ord('a') and char <= ord('z'):
                        count = count + 1
            if count > maxval:
                maxval, keychar = count, k
        print pos, maxval, chr(keychar)
        key.append(keychar)
    sum_ascii = 0
    for idx, val in enumerate(byteArr):
    	sys.stdout.write (chr(val ^ key[idx % 3]))
    	sum_ascii = sum_ascii + (val ^ key[idx % 3])
    return sum_ascii




    
if __name__ == '__main__':
    # print "Problem 01: ", problem_01()
    # print "Problem 02: ", problem_02()
    # print "Problem 03: ", problem_03(600851475143)
    # print "Problem 05: ", problem_05(20)
    # print "Problem 06: ", problem_06(100)
    # print "Problem 07: ", problem_07(10001)
    # print "Problem 08: ", problem_08()
    # print "Problem 09: ", problem_09(1000)
    # print "Problem 10: ", problem_10(20000)
    # print "Problem 11: ", problem_11()
    # print "Problem 13: ", problem_13()
    # print "Problem 14: ", problem_14(1000000)
    # print "Problem 18: ", problem_18()
    # print "Problem 22: ", problem_22()
    # print "Problem 26: ",  problem_26()
    # print "Problem 33: ", problem_33()
    # print "Problem 36: ",  problem_36()
    # print "Problem 39: ",  problem_39()
    # print "Problem 44: ", problem_44()
    # print "Problem 45: ",  problem_45()
    # print "Problem 50: ", problem_50(1000000)
    # print "Problem 67: ", problem_67()
    # print "Problem 9: ", problem_9()
    # print "Problem 23: ", problem_23()
    # print "Problem 31: ", problem_31()
    # print "Problem 47: ", problem_47()
    # print "Problem 57: ", problem_57()
    # print "Problem 58: ", problem_58()
    # print "Problem 27: ", problem_27()
    # print "Problem 46: ", problem_46()
    #print "Problem 92: ", problem_92()
    print "Problem 59: ", problem_59()

