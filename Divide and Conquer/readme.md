# Divide-and-Conquer Algorithm 

## Concept

> 1. **Divide** input into smaller subproblems.
> 2. **Conquer** the subproblems recursively.
> 3. **Combine** the solutions for the subproblems into a solution for the original problem.

Divide-and-conquer一句话总结就是“大事化小，小事化了”或者说“分而治之”。 要把一个复杂的大问题逐层化分为结构相同的多个小问题直到最基本的实例。然后解决基本问题并且合并结果来产生针对原问题的答案。这种操作一般需要递归 (Recursion) 的方法来实现。 

一个分治算法的例子是计算两个多位数乘法。 在这个问题中我们拥有的最基本的实例 (base) 为个位数乘法。然后我们要把多位数乘法用递归的手法一层一层最终化解为解决多个个位数乘法然后合并求解。一种Karatsuba乘法将会在后面详细解释。Merge Sort 也是一个例子来理解分治法。大体思路为把一个乱序数组不断分割直到每一组比较都只包含两个数。然后逐层合并小的比较结果到最后的sorted array。 

## Recursion  

To understand divide-and-conquer, it is necessary to learn the concept of  [recursion](https://en.wikipedia.org/wiki/Recursion).

> In mathematics and computer science, a class of objects or methods exhibit recursive behavior when they can be defined by two properties: 
> 1. A simple **base case** (or cases)—a **terminating scenario** that does not use recursion to produce an answer
> 2. A set of rules that reduce all other cases toward the base case

This pseudocode below generally describes a recursion process but not totally reasonable for the lack of details. What we should know is that **there should always be an exit or say a terminate condition for the recursion** to prevent the program calling itself infinite times.  

```python
# A pseudocode to desctibe a recursion process to decompose a problem
def recusionDecompose(input):
    if input == basecase: 			# Base case
        result = baseOperation(input)
        return result
    else:
        newInput = docompose(input)  # Recursive case
        recusionDecompose(newInput)
```

 **Note**: 在recursion中有两股力量在相互制衡，一股是不断增加的子问题数量，另一股是不断缩减的每个子问题的工作量。随着递归层级的深入，这两者的关系可能不会改变，例如MergeSort的每级工作量是与级数独立开来的, 也可能会发生改变。这个动态关系的理解是后面master method的核心推导思路。

### 

