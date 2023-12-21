---
comments: true
tags:
  - 校订中……
---
# 练习
<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/4/exercises.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/4/exercises.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/4/exercises.pdf">下载 PDF</a>.</p>
    </embed>
</object>
# 习 题 

1. 设 $X_{1}, \cdots, X_{n}$ 是抽自负二项分布的样本, 求 $p$ 的矩估计与极大似然 估计。
2. (a) 设 $a_{1}, \cdots, a_{n}$ 是 $n$ 个实数, 定义函数 $h(a)=\sum_{i=1}^{n}\left|a_{i}-a\right|$. 证 明:当 $a$ 为 $a_{1}, \cdots, a_{n}$ 的样本中位数 (见 4.29) 式) 时, $h(a)$ 达到最小值. (b) 设 $X_{1}, \cdots, X_{n}$ 为自具概率密度函数 $\frac{1}{2} \mathrm{e}^{-|x-\theta|}$ 中抽出的样本 (这个分布叫拉 普拉斯分布), 求参数 $\theta$ 的矩估计与极大似然估计.
3. 设 $X_{1}, \cdots, X_{n}$ 为抽自均匀分布 $R(\theta, 2 \theta)$ 的样本, 求 $\theta$ 的矩估计与极 大似然估计。
4. (a) 证明

$$
\begin{gathered}
f(x ; a, \sigma)=\left(\sqrt{2 \pi} \sigma^{3}\right)^{-1}(x-a)^{2} \exp \left(-\frac{1}{2 \sigma^{2}}(x-a)^{2}\right) \\
-\infty<x<\infty
\end{gathered}
$$

作为 $x$ 的函数是概率密度, 其中 $a, \sigma$ 为参数, $-\infty<a<\infty, \sigma>0$.

(b) 设 $X_{1}, \cdots, X_{n}$ 为抽自此总体的样本, 求 $a$ 和 $\sigma^{2}$ 的矩估计.

(c) 列出 $a, \sigma^{2}$ 的极大似然估计所满足的方程,并指出一种叠代求解的 方法.

5. 设 $X$ 为抽自波哇松分布 $P(\lambda)$ 的样本 (样本大小为 1 ), 参数 $\lambda$ 有先验 密度 $h(\lambda)=\mathrm{e}^{-\lambda}($ 当 $\lambda>0 . h(\lambda)=0$ 当 $\lambda \leqslant 0)$. 试求 $\lambda$ 的贝旪斯估计.

- 204 • 6. 设 $X_{1}, \cdots, X_{n}$ 为抽自指数分布的样本. 分布中的参数 $\lambda$ 有先验密度 $h(\lambda)=\lambda \mathrm{e}^{-\lambda}$ 当 $\lambda>0, h(\lambda)=0$ 当 $\lambda \leqslant 0$. 求 $\lambda$ 的贝叶斯估计.

7. (a) 设 $N, n, m$ 都是自然数, $n \leqslant N$. 证明组合公式 (注意: $\left(\begin{array}{l}a \\ b\end{array}\right)=0$ 当 $a<b$ )

$$
\sum_{m=0}^{N}\left(\begin{array}{c}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-m \\
n-x
\end{array}\right)=\left(\begin{array}{c}
N+1 \\
n+1
\end{array}\right), x=0,1, \cdots, n
$$

（b）设 $X$ 为抽自超儿何分布

$$
P_{M}(X=x)=\left(\begin{array}{c}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-M \\
n-x
\end{array}\right) /\left(\begin{array}{l}
N \\
n
\end{array}\right)
$$

的样本, $M$ 为末知参数, 其先验分布为

$$
P(M=k)=1 /(N+1), k=0,1, \cdots, N
$$

试利用 (a) 的结果证明: $M$ 的贝叶斯估计为

$$
\hat{M}(x)=(N+2)(X+1) /(n+2)-1
$$

8. 设 $X$ 为抽自二项分布 $B(n, p)$ 的样本, $n$ 已知, $p$ 为末知参数. 证明: 对任何常数 $c, d, d>_{c}>0$, 可找到 $p$ 的先验分布 (可以为广义的), 使 $p$ 的贝 叶斯估计为 $(X+c) /(n+d)$.
9. 设 $X$ 为抽自二项分布 $B(n, p)$ 的样本, $n$ 已知, 而 $p$ 为末知参数（a) 作 $p^{2}$ 的一个无偏估计. (b) 证明: 若 $g(p)$ 有无偏估计存在, 则 $g(p)$ 必是 $p$ 的不超过 $n$ 阶的多项式. (c) 反过来, 对 $p$ 的任一不超过 $n$ 阶的多项式 $g(p)$, 它的无偏估计必存在.
10. 设 $X_{1}, \cdots, X_{n}$ 为抽自 $R(0, \theta)$ 的样本. (a) 证明: $\hat{\theta}_{1}=\max \left(X_{1}, \cdots\right.$, $\left.X_{n}\right)+\min \left(X_{1}, \cdots, X_{n}\right)$ 是 $\theta$ 的一个无偏估计. (b) 证明: 对适当选择的参数 $c_{n}, \hat{\theta}_{2}=c_{n} \min \left(X_{1}, \cdots, X_{n}\right)$ 是 $\theta$ 的无偏估计. 但这个估计的方差比另外两个 无侮估计 $\hat{\theta}_{3}=\bar{X}$ 和 $\hat{\theta}_{4}=\frac{n+1}{n} \max \left(X_{1}, \cdots, X_{n}\right)$ 都大(除非 $\left.n=1\right)$.
11. 设 $X$ 为抽自波哇松分布 $P(\lambda)$ 的样本. (a) 证明: $g(\lambda)=\mathrm{e}^{-2 \lambda}$ 的唯 的无偏估计 $\hat{\theta}(X)$ 为: $\hat{\theta}_{1}(X)=1$ 当 $X$ 为偶数, $\hat{\theta}_{1}(X)=-1$ 当 $X$ 为奇数. (b) 你认为 (a)中的估计是否合理? 如不合理,试提出一个合理的估计.
12. 设 $X_{1}, \cdots, X_{n}$ 为抽自正态总体 $N\left(a, \sigma^{2}\right)$ 的样本, 则已知 $\hat{\theta}_{1}=$ $\frac{1}{n-1} \sum_{1}^{n}\left(X_{i}-\bar{X}\right)^{2}$ 为 $\sigma^{2}$ 之一无偏估计. 证明: $\hat{\theta}_{2}=\frac{n-1}{n+1} \hat{\theta}_{1}$ 虽非 $\sigma^{2}$ 的无偏 估计, 但 $\hat{\theta}_{2}$ 的均方误差较小, 即: $E\left(\hat{\theta}_{2}-\sigma^{2}\right)^{2}<E\left(\hat{\theta}_{1}-\sigma^{2}\right)^{2}$. 本题及 11 题都 说明: 无偏估计不一定是最好的选择.
13. 设在 12 题中 $a$ 已知. (a) 则 $\hat{\theta}_{3}=\frac{1}{n} \sum_{i=1}^{n}\left(X_{i}-a\right)^{2}$ 也是 $\sigma^{2}$ 的无偏 估计. 且其方差小于上题中的估计 $\widehat{\theta}_{1}$ 的方差. (b) 进一步证明: $\hat{\theta}_{3}$ 是 $\sigma^{2}$ 的 MVU 估计。
14. 设 $X_{1}, \cdots, X_{n}$ 是从具概率密度函数

$$
f(x, \theta)=\left\{\begin{array}{cc}
2 \sqrt{\theta / \pi} \exp \left(-\theta x^{2}\right), & x>0 \\
0, & x \leqslant 0
\end{array}\right.
$$

的总体中抽出的样本. 证明: 对适当选择的常数 $C, \hat{\theta}=C \sum_{i=1}^{n} X_{i}^{2} / n$ 是 $1 / \theta$ 的 MVU 估计.

15. (a) 若 $\hat{\theta}_{1}, \hat{\theta}_{2}$ 都是 $\theta$ 的 MVU 估计,则 $\left(\hat{\theta}_{1}+\hat{\theta}_{2}\right) / 2$ 也是. (b) 若 $\hat{\theta}$ 是 $\theta$ 的 MVU 估计而 $a \neq 0$ 和 $b$ 都是已知常数,则 $a \hat{\theta}+b$ 是 $a \theta+b$ 的 MVU 估计.
16. 设 $X_{1}, \cdots, X_{n}$ 为从某一个具均值 $\theta$ 而方差有限的总体中抽出的样 本, 证明: 对任何常数 $c_{1}, \cdots, c_{n}$, 只要 $\sum_{i=1}^{n} c_{n}=1$, 则 $\sum_{i=1}^{n} c_{i} X_{i}$ 必是 $\theta$ 的无偏估 计. 但是, 只有在 $c_{1}=c_{2}=\cdots=c_{n}=1 / n$ 时, 方差达到最小 (指在上述形式的 估计类中达到最小. 实际可以证明: $\bar{X}$ 在 $\theta$ 的一切无偏估计类中方差也达到 最小).
17. 设 $X_{1}, \cdots, X_{n}$ 为抽自均匀分布 $R(0, \theta)$ 中的样本. 证明: 对任给的 $1-\alpha(0<1-\alpha<1)$, 可找到常数 $c_{n}$, 使 $\left[\max \left(X_{1}, \cdots, X_{n}\right), c_{n} \max \left(X_{1}, \cdots\right.\right.$, $\left.\left.X_{n}\right)\right]$ 为 $\theta$ 的一个置信系数 $1-\alpha$ 的区间估计.
18. 设 $X_{1}, \cdots, X_{n}$ 和 $Y_{1}, \cdots, Y_{m}$ 分别是抽自正态总体 $N\left(\theta, \sigma_{1}^{2}\right)$ 和 $N(\theta$, $\left.\sigma_{2}^{2}\right\rangle$ 的样本, $\sigma_{1}^{2}$ 和 $\sigma_{2}^{2}$ 都已知. (a) 找常数 $c, d$, 使 $\hat{\theta}=c \bar{X}+d \bar{Y}$ 为 $\theta$ 的无偏 估计. 并使其方差最小 (在所有形如 $a \bar{X}+b \bar{Y}$ 的无偏估计类中最小). (b) 基于 $\hat{\theta}$,作出 $\theta$ 的置信系数为 $1-\alpha$ 的置信区间.
19. 设 $X_{1}, \cdots, X_{n}$ 是抽自具参数 $\lambda_{1}$ 的指数分布的样本, $Y_{1}, \cdots, Y_{m}$ 是抽 自具参数为 $\lambda_{2}$ 的指数分布的样本, 试求 $\lambda_{2} / \lambda_{1}$ 的区间估计.
20. 设 $X_{1}, X_{2}$ 为抽自具密度函数

$$
f(x, \theta)=\left\{\begin{array}{l}
\mathrm{e}^{9-x}, x \geqslant \theta \\
0, x<\theta
\end{array}\right.
$$

的总体的样本. 参数 $\theta$ 的先验密度为

$$
h(\theta)=\left\{\begin{array}{l}
\mathrm{e}^{-\theta}, \theta>0 \\
0, \theta \leqslant 0
\end{array}\right.
$$

求 $\partial$ 的以叶斯区间估计.

21. 证明 (3.2) 式.
22. 设 $X_{1}, \cdots, X_{n}$ 为抽自均匀分布总体 $R\left(\theta_{1}, \theta_{2}\right)$ 的样本. 证明: 存在只 依粨 J $n$ 的常数 $c_{n}$, 使 $\bar{X}-c_{n} S$ 和 $\bar{X}+c_{n} S$ 分别是 $\theta_{1}$ 和 $\theta_{2}$ 的无偏估计.
23. 设 $X_{1}, \cdots, X_{n}$ 为抽自正态总体 $N\left(\theta, \sigma^{2}\right)$ 的样本, $\theta$ 和 $\sigma^{2}$ 都末知. 证 ㅂ]: $\bar{X}$ 仍为 $\theta$ 的 MVU 估计.
