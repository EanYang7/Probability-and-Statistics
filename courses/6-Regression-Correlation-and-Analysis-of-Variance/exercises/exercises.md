---
comments: true
tags:
  - 校订中……
---

# 练习

<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/6/exercises.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/6/exercises.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/6/exercises.pdf">下载 PDF</a>.</p>
    </embed>
</object>

1. 在模型 (2.6) 中用配方的方法 (不求助于求偏导数), 以决定最小二乘 估计 (2.12)和 (2.13), 并由此得出残差平方和的表达式 (2.23).
2. 在模型 (2.6) 中, 假定 (2.5) 成立, 仍记残差为 $\delta_{1}, \cdots, \delta_{n}$. 证明以下各 点: (a) $E\left(\delta_{i}\right)=0, i=1, \cdots, n$.

(b) $\delta_{1}, \cdots, \delta_{n}$ 不相互独立.

(c) $\operatorname{Var}\left(\delta_{i}\right)=\left(1-\frac{1}{n}-\left(X_{i}-\bar{X}\right)^{2} / S^{2}\right) \sigma^{2}$

$$
\left(S^{2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}\right)
$$

(d) $\operatorname{Cov}\left(\delta_{i}, \delta_{j}\right)=-\left(\frac{1}{n}+\left(X_{i}-\bar{X}\right)\left(X_{j}-\bar{X}\right) / S^{2}\right) \sigma^{2}, i \neq j$.

3. 设样本 $X_{1}, \cdots, X_{n} \sim N\left(a, \sigma^{2}\right), Y_{1}, \cdots, Y_{m} \sim N\left(b, \sigma^{2}\right), a, b, \sigma^{2}$ 都末 知, 为要估计 $b-a$ 或检验暇设 $H_{0}: b-a=c$ (c已知), 可利用线性回归的理 论去做. 指出具体怎样做的办法.
4. 考虑过原点的线性回归模型

$$
Y_{i}=b X_{i}+e_{i}, i=1, \cdots, n
$$

误差 $e_{1}, \cdots, e_{n}$ 仍假定满足条件 (2.5).

(a) 给出 $b$ 的最小二乘估计 $\hat{b}$.

（b）给出残差平方和 $R=\sum_{i=1}^{n} \delta_{i}^{2}$ 的表达式,并证明: $R /(n-1)$ 是误差方 差 $\sigma^{2}$ 的无偏估计. 这与不一定过原点的模型有何不同? 为何有这个不同?

(c) 用附录 $\mathrm{A}$ 中的方法, 证明当误差服从证态分布时, 有 $R / \sigma^{2} \sim \chi_{n-1}^{2}$.

(d) 给出回归系数 $b$ 的区间估计.

5. 考虑回归模型 (2.4), 而 $c_{1}, c_{2}$ 为已知常数. 假定 (2.5) 且设误差服从 正态分布,求 $c_{1} a+c_{2} b$ 的区间估计.
6. 从一元线性回归的讨论中出现儿个有趣而初等的数学问题. 现列举 如下请读者考虑:

(a) 由第 2 题的 (c), 根据方差非负, 可知: 对任意 $n$ 个实数 $X_{1}, \cdots, X_{n}$, 有

$$
\left(X_{i}-\bar{X}\right)^{2} / \sum_{j-1}^{n}\left(X_{j}-\bar{X}\right)^{2} \leqslant 1-\frac{1}{n}, i=1, \cdots, n
$$

等号在何时达到?

(b) 在 6.2 节 6.2 .3 段末尾处提到的断言: 若 $X_{1}, X_{2}, \cdots$, 是一串实数, 记 $\bar{X}_{n}=\left(X_{1}+\cdots+X_{n}\right) / n, S_{n}^{2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$, 则对任何固定的实数 $a$, 有 $\left(a-\vec{X}_{n}\right)^{2} / S_{n}^{2} \rightarrow 0$ 当 $n \rightarrow \infty$. 这个事实的统计意义已在 6.2 节 (6.2.3) 段中说 明过了. （c）我们已证明:在模型 (2.6)及假定 (2.5)之下, $\operatorname{Var}\left(\hat{\beta}_{1}\right)=\sigma^{2} / S^{2}, S^{2}$ $=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$. 当然, 方差息小愈好. 故如限制试验点 $X_{i}$ 只能取在某有限 区间 $[A, B]$ 内, 就有一个如何配置这些点, 以使 $S^{2}$ 达到最大的问题. 证明这 问题的解是: 若 $n$ 为偶数 $2 m$, 则取 $X_{1}, \cdots, X_{n}$ 中有 $m$ 个 $A$ 及 $m$ 个 $B$; 若 $n$ 为奇数 $2 m+1$, 则取 $X_{1}, \cdots, X_{n}$ 中有 $m$ 个 $A$ (或 $B$ ), $m+1$ 个 $B$ (或 $A$ ). 不 过, 在实用上, 这个设计并不一定被采用, 除非我们对回归函数为线性函数这 一点绝无疑义. 因为, 这个设计只采用两个自变量值, 它无法借助于观察数据 去发现真实的回归函数与线性函数的可能的偏差.

7. 证明 6.3 节 6.3 .1 段末尾处多元回归系数最小二乘估计的三个性 质.
8. 设 $\left(X_{1}, Y_{1}\right), \cdots,\left(X_{n}, Y_{n}\right)$ 是从二维正态总体 $N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho\right)$ 中抽 出的样本, 以 $r$ 记样本相关系数. 用以下的思路证明当 $\rho=0$ 时, $\sqrt{n-2} r /$ $\sqrt{1-r^{2}}-t_{n-2}$ : 固定 $X_{1}, \cdots, X_{n}$, 考虑 $Y_{1}, \cdots, Y_{n}$ 的条件分布, 因为 $\rho=0$ 表 示 $X_{i}, Y_{i}$ 独立, 故 $Y_{1}, \cdots, Y_{n}$ 的条件分布即是其无条件分布, 即 $Y_{1}, \cdots, Y_{n}$ 独立, 有公共分布 $N\left(b, \sigma_{2}^{2}\right)$. 这可写为回归模型.

$$
Y_{i}=b+\beta_{1} X_{i}+e_{i}, i=1, \cdots, n
$$

回归系数 $\beta_{1}=0, e_{i} \sim N\left(0, \sigma^{2}\right), \sigma^{2}=\sigma_{2}^{2}$. 然后在这个模型中使用 (2.26) (记住 $\left.\beta_{1}=0\right)$ ), 证明 (2.26) 式左边正好就是 $\sqrt{n-2} r / \sqrt{1-r^{2}}$. 这样就证明了在给 定 $X_{1}, \cdots, X_{n}$ 的条件下, $\sqrt{n-2} r / \sqrt{1-r^{2}}$ 的条件分布总是 $t_{n-2}$ 与 $X_{1}, \cdots$, $X_{n}$ 无关. 因此 $\sqrt{n-2} r / \sqrt{1-r^{2}}$ 的无条件分布就是 $t_{n-2}$. 其所以要在给定 $X_{1}, \cdots, X_{n}$ 的条件下来考虑, 是因为线性模型 (1) 有关的理论, 特别是 (2.26) 式, 都是在 $X_{i}$ 为常数的情况下给出的.

9 考虑下面的统计模型: 样本 $X_{1}, \cdots, X_{n}, Y_{1}, \cdots, Y_{n}$ 独立, $X_{i} \sim N\left(d_{i}\right.$ $\left.+a, \sigma^{2}\right), Y_{i} \sim N\left(d_{i}+b, \sigma^{2}\right), i=1, \cdots, n$. 这里 $d_{1}, \cdots, d_{n}$ 和 $a, b, \sigma^{2}$ 都末知， 要检验假设 $H_{0}: a=b$.

（a）试通过使用 $Z_{i}=Y_{i}-X_{i}, i=1, \cdots, n$, 用 $t$ 检验来处理这个问题.

(b) 说明: 这个模型事实上是一个随机区组试验模型,共有 $n$ 个区组, 区 组大小为 2 . 写出化到这样一种模型的过程.

(c) 用随机区组模型的 $F$ 检验来处理 $H_{0}$ 的检验问题, 证明它与用 (a) 中 的方法得到的一致. 10. 验证一下,下面的表是正交表:

| 行 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 1 | 1 | 2 | 2 |
| 3 | 1 | 1 | 1 | 2 | 2 | 2 | 2 |
| 4 | 1 | 2 | 2 | 2 | 2 | 1 | 1 |
| 5 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
| 6 | 2 | 2 | 1 | 1 | 2 | 2 | 1 |
| 7 | 2 | 1 | 2 | 2 | 1 | 2 | 1 |
| 8 | 2 | 2 | 1 | 2 | 1 | 1 | 2 |

按正交表命名法,这个表的名称应是什么? 它在用来安排试验时受到哪 些限制? 现如有三个两水平因子 $A, B, C$, 共做 8 次试验, 并分两个区组做, 这试验如何用这张表安排? 写出其方差分析表.
