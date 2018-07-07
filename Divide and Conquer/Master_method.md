# Master Method 

# Concept 

In the analysis of algorithms, the master theorem provides a cookbook solution in asymptotic terms (using Big O notation) for recurrence relations of types that occur in the analysis of many divide and conquer algorithms.  Note that not all recurrence relations can be solved with Master concept. The master method concerns recurrence relation as 

$$
T(n) \leq a \cdot T(\frac{n}{b})+O(n^d)
$$

- $n$ is size of problem
- $a$ is number of recursive calls (subproblems in the recursion)
- $n/b$ is size of subproblem
- $O(n^d)$ is the cost  upper bound of the work done outside the recursive calls, which includes the cost of **dividing the problem** and the cost of **merging the solutions** to the subproblems.  (This part needs further discussion)
- $d$ is the exponent in running time of "combine step" 

>  The master method is described as 
>  $$
>  T(n) = \left\{
>  \begin{array}{}
>  &O(n^d \text{log}n)          & { \text{if} ~~a=b^d } &[Case~1]\\
>  &O(n^d)           & {\text{if} ~~a< b^d} &[Case~2]\\
>  &O(n^{log_ba})           & {\text{if} ~~a>b^d} &[Case~3]
>  \end{array} \right.
>  $$
>


# Proof

The first step is to investigate the the work load on each level of the recursion process. The recursion tree below helps to visualize this process. The uppermost node represents the outermost recursion call, denoted as the root of the tree. The bottom level refers to leaves, which are bases in the recursion. 

![](http://imagecloud.nos-eastchina1.126.net/Algorithm/divide-and-conquer/recursion_tree.JPG)

At certain level j, we have
- $a^j$: number of subproblems
- $n/b^j$: size of each subproblem in level $j$ 

Then the work load can be calculated as 


>$$
>\text{work at level $j$} \leq a^j \cdot c \cdot \left[ \frac{n}{b^j}\right]^d
>$$
>$$
>\text{work at level $j$} \leq cn^d \cdot \left[ \frac{a}{b^d}\right]^j
>$$
>

The the total work done containing all levels is 

> $$
> \text{total work} \leq cn^d \cdot \sum_{j=0}^{log_bn} \left[\frac{a}{b^d}\right]^j
> $$
>

- $a$: the rate of *subproblem proliferation* (RSP)    
- $b^d$: the rate of *work shrinkage* (RWS)    

> 1)  If RSP < RWS then the amount of work performed is decreasing with the recursion level j.
>
> 2)  If RSP > RWS then the amount of work performed is increasing with the recursion level j.
>
> 3)  If RSP = RWS then the amount of work performed is the same at every recursion level.         

**Case 1**

Calculation for Case 1 is straightforward.

> $$
> \text{total work} \leq cn^d \cdot \sum_{j=0}^{log_bn} \left[\frac{a}{b^d}\right]^j = cn^d \cdot \underbrace{(1+1+1+ \dots+1)}_{\text{1+log$_bn$ times}} = cn^d \cdot \text{log}_bn
> $$
>

---

Before we start the calculation of Case 2 and 3, we need to understand *Geometric Series* which will be applied in further proof.

**Geometric Series**

>$$
>1+r+r^2+\cdots r^k = \frac{r^{k+1}-1}{r-1} \leq  \left\{
>\begin{array}{}
>&\frac{1}{1-r} = \text{const} & &r<1  \\
>&\frac{r^{k+1}}{r-1} = r^k\cdot \frac{r}{r-1} & & r>1
>\end{array} \right.
>$$
>

When $r<1$, the series is dominated by the first term $1$, while when $r>1$ the series is dominated by the last term $r^k$

---

**Case 2**

In this case $r= \left[\frac{a}{b^d}\right]<1$

> $$
> cn^d \cdot \sum_{j=0}^{log_bn} r^j  = O(n^d)
> $$
>

**Case 3**

In this case $r= \left[\frac{a}{b^d}\right]>1$

> $$
> cn^d \cdot \sum_{j=0}^{log_bn} r^j  = O(n^d\cdot r^{log_bn}) = O(n^d \cdot \left(\frac{a}{b^d}\right)^{log_bn}) = O(a^{\text{log}_bn}) = O(n^{\text{log}_ba})
> $$
>

## References

- [Master theorem (analysis of algorithms)](https://en.wikipedia.org/wiki/Master_theorem_)
- [Case on Recursion Tree](https://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/lec20.html)
  