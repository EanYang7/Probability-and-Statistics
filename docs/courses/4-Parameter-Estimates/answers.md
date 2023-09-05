---
comments: true
tags:
  - 校订中……
---
# 答案
<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/4/answers.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/4/answers.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/4/answers.pdf">下载 PDF</a>.</p>
    </embed>
</object>
# 第 四 章 

2. (a) 只须注意: 若 $c_{1}<c_{2}$, 则 $g(a)=\left|c_{1}-a\right|+\left|c_{2}-a\right|$ 当 且仅当 $c_{1} \leqslant a \leqslant c_{2}$ 时达到最小值 $c_{2}-c_{1}$. 故如把 $a_{1}, \cdots, a_{n}$ 按由小 到大排列为 $a_{(1)} \leqslant a_{(2)} \cdots \leqslant a_{(n)}$, 则将 $h(a)$ 写为 $\sum_{i=1}^{n}\left|a_{(i)}-a\right|=$ $\left(\left|a_{(1)}-a\right|+\left|a_{(n)}-a\right|\right)+\left(\left|a_{(2)}-a\right|+\left|a_{(n-1)}-a\right|\right)+\cdots$ 后, 可以看出: 为使此式达到最小, $a$ 必须落在下述这些区间的每一个 之内: $\left[a_{(1)}, a_{(n)}\right],\left[a_{(2)}, a_{(n-1)}^{-},\left[a_{(3)}, a_{(n-2)}\right], \cdots\right.$. 如 $n$ 为奇 数, 适合这条件的唯一的 $a$ 是 $a_{(n+1) / 2}$. 如 $n$ 为偶数, 则 $\left[a_{(n / 2)}\right.$, $\left.a_{(n / 2+1)}\right]$ 中任一数 $a$ 都适合这条件. 不论在何情况, 样本中位数 总在其列.

(b) 极大似然估计直接由 (a) 得出, 为样本中位数, 矩估计为 $\bar{X}$.

3. 总体均值为 $3 \theta / 2$, 故矩估计为 $2 \bar{X} / 3$. 样本 $\left(X_{1}, \cdots, X_{n}\right)$ 的似然函数为

$$
f\left(x_{1}, \cdots, X_{n}, \theta\right)=\left\{\begin{array}{l}
\theta^{-n}, \text { 当 } \theta \leqslant \min \left(X_{i}\right) \leqslant \max \left(X_{i}\right) \leqslant 2 \theta \\
0, \quad \text { 其他情况 }
\end{array}\right.
$$

可看出极大似然估计为 $\frac{1}{2} \max \left(X_{1}, \cdots, X_{n}\right)$.

4. 因为积分

$$
\int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi} \sigma}(x-a)^{2} \exp \left(-\frac{1}{2 \sigma^{2}}(x-a)^{2}\right) \mathrm{d} x
$$

是 $N\left(a, \sigma^{2}\right)$ 的方差, 为 $\sigma^{2}$, 故立即看出 $f(x ; a, \sigma)$ 为概率密度函 数. 由对称性知此分布均值为 $a$, 故 $a$ 的矩估计为 $\bar{X}$. 此分布的方 差为 $3 \sigma^{2}$, 故得 $\sigma^{2}$ 的矩估计为 $\frac{1}{3(n-1)} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$. 取似然函数的对数, 分别对 $a$. 和 $\sigma$ 求偏导数, 得到决定极大似 然估计的方程组

$$
\begin{gathered}
2 \sum_{i=1}^{n} \frac{1}{X_{i}-a}-\frac{n}{\sigma^{2}}(\bar{X}-a)=0 \\
\sigma^{2}=\frac{1}{3 n} \sum_{i=1}^{n}\left(X_{i}-a\right)^{2}
\end{gathered}
$$

一个叠代解法是: 先给定 $a$ 的初始值 $a_{0}$ (例如 $a_{0}=\bar{X}$, 但必须 $\bar{X}$ $\neq X_{i}$ 对任何 $i$ ), 由(1) 式解出 $\sigma^{2}$ 之值 $\sigma_{0}^{2}$. 以 $\sigma^{2}=\sigma_{0}^{2}$ 代人 (2) 式解 出 $a$ 的下一个值 $a_{1}$ (这是一个 $a$ 的二次方程), 以 $a=a_{1}$ 代入 (1) 解出 $\sigma^{2}$ 的下一个值 $\sigma_{1}^{2}$. 继续下去直到 $\left(a_{n}, \sigma_{n}^{2}\right)$ 与 $\left(a_{n+1}, \sigma_{n+1}^{2}\right)$ 之 差别小于指定界限为止.

5. 先算出

$$
\int_{0}^{\infty} \mathrm{e}^{-\dot{\lambda}} \cdot \mathrm{e}^{-\lambda} \lambda^{X} / X ! \mathrm{d} \lambda=1 / 2^{X+!}, X=0,1,2, \cdots .
$$

即知 $\lambda$ 的后验密度为 $2^{X+1} \mathrm{e}^{-2 \lambda} \lambda^{\mathrm{X}} / X$ ! 其均值, 即 $(X+1) / 2$, 为 $\lambda$ 的贝叶斯估计.

$\lambda$ 的 MVU 估计为 $X$. 当 $X$ 取大值 (具体说, $X \geqslant 2$ ) 时, 它大于 贝叶斯估计 $(X+1) / 2$. 请解释一下其原因.

6. 先算出样本 $\left(X_{1}, \cdots, X_{n}\right)$ 的边缘密度

$$
\int_{0}^{\infty} \lambda \mathrm{e}^{-\lambda} \lambda^{n} \mathrm{e}^{-n \lambda \bar{X}} \mathrm{~d} \lambda=(n+1) ! /(1+n \bar{X})^{n+2}
$$

由此算出 $\lambda$ 的后验密度的均值为

$$
\begin{aligned}
&\left\{(1+n \bar{X})^{n+2} /(n+1) !\right\} \int_{0}^{\infty} \mathrm{e}^{-\lambda} \lambda^{n+2} \mathrm{e}^{-n \lambda \bar{X}} \mathrm{~d} \lambda \\
&=(n+2) /(1+n \bar{X})
\end{aligned}
$$

这就是 $\lambda$ 的贝叶斯估计. 你对这个估计与通常估计 $\bar{X}$ 比较, 有何 评述?

7. (a)考虑 $N+1$ 个球, 自左至右排成一列, 如图 6. 现要从其 中拿出 $n+1$ 个, 拿法有 $\left(\begin{array}{c}N+1 \\ n+1\end{array}\right)$ 种. 将拿法作如下的分解: 固定列

![](https://cdn.mathpix.com/cropped/2023_07_12_6070d8b3dac0a83249f7g-03.jpg?height=111&width=791&top_left_y=293&top_left_x=604)

图 6

中的第 $m+1$ 个球 $a$. 将 $a$ 拿出, 并在 $a$ 左边拿出 $x$ 个 (拿法有 $\left(\begin{array}{c}m \\ x\end{array}\right)$ 种), 在 $a$ 右边拿出 $n-x$ 个 $\left(\right.$ 拿法有 $\left(\begin{array}{c}N-m \\ n-x\end{array}\right)$ 种). 因此这样的拿法有 $\left(\begin{array}{l}m \\ x\end{array}\right) \cdot\left(\begin{array}{c}N-m \\ n-x\end{array}\right)$ 种. 再让 $a$ 由位置 1 流动到 $N+$ $1(m$ 由 0 到 $N)$. 所得出的拿法显然无相重的并无遗漏的. 由此得 出所给的组合等式.

(b) 在所给先验分布之下, $X$ 的边缘分布为

$$
\begin{aligned}
P(X=x) & =\sum_{k=0}^{N} P(M=k) P_{k}(X=x) \\
& =\left[(N+1)\left(\begin{array}{l}
N \\
n
\end{array}\right)\right]^{-1} \sum_{k=0}^{N}\left(\begin{array}{l}
k \\
x
\end{array}\right)\left(\begin{array}{c}
M-k \\
n-x
\end{array}\right) \\
& =\left[(N+1)\left(\begin{array}{l}
N \\
n
\end{array}\right)\right]^{-1}\left(\begin{array}{l}
N+1 \\
n+1
\end{array}\right)=\frac{1}{n+1}
\end{aligned}
$$

$x=0,1, \cdots, n$. 如此得到 $M$ 的后验分布为

$$
\begin{gathered}
P(M=m \mid X)=\frac{n+1}{N+1}\left(\begin{array}{l}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-m \\
n-x
\end{array}\right) /\left(\begin{array}{l}
N \\
n
\end{array}\right) \\
m=0,1, \cdots, N
\end{gathered}
$$

此分布之均值，即

$$
\hat{\theta}(X)=\frac{n+1}{N+1} \sum_{m=0}^{N} m\left(\begin{array}{l}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-m \\
n-x
\end{array}\right) /\left(\begin{array}{l}
N \\
n
\end{array}\right)
$$

为 $M$ 的贝叶斯估计. 上式中的和等于

$$
\sum_{m=0}^{N}(m+1)\left(\begin{array}{c}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-m \\
n-x
\end{array}\right)-\sum_{m=0}^{N}\left(\begin{array}{c}
m \\
x
\end{array}\right)\left(\begin{array}{c}
N-m \\
n-x
\end{array}\right)
$$

第一项可化为 $(x+1)\left(\begin{array}{c}m+1 \\ x+1\end{array}\right)\left(\begin{array}{c}N+1-(m+1) \\ n+1-(x+1)\end{array}\right)$. 因此, 由 $(a)$ 中 证明的组合公式, (4) 中的两个和, 分别等于 $\left(\begin{array}{c}N+2 \\ n+2\end{array}\right)(x+1)$ 和 $\left(\begin{array}{c}N+1 \\ n+1\end{array}\right)$. 以此代人 (3) 式并化简, 即得所要的结果.

8. 考虑先验密度 $p^{a}(1-p)^{b}$ (可以是广义的). 得到贝旪斯估 计为 $(x+a+1) /(n+a+b+2)$, 取 $a=c-1, b=d-c-1$ 即可.
9. (a) $X(X-1) /[n(n-1)]$. (b) 若 $\hat{p}(X)$ 为 $g(p)$ 的无偏估 计, 则

$$
g(p)=E_{p} \hat{p}(x)=\sum_{i=0}^{n} \hat{p}(i)\left(\begin{array}{l}
n \\
i
\end{array}\right) p^{i}(1-p)^{n-i}
$$

而右边为 $p$ 的不超过 $n$ 阶的多项式. 由此可知, 像 $\mathrm{e}^{-p}, 1 /\left(1+p^{2}\right)$ 等, 都没有无偏估计. 还有一个有趣的事实: 令 $g_{1}(p)=p$, $g_{2}(p)=p^{n}, g_{3}(p)=p^{n+1}$, 则 $g_{1}(p), g_{2}(p)$ 都有无偏估计（㝍 (c)), 但 $g_{1}(p) \cdot g_{2}(p)=g_{2}(p)$ 则没有. (c) 只须证明: 对任何自然 数 $k \leqslant n, p^{k}$ 有无偏估计. 直接验证: $p^{k}$ 的无偏估计就是 $X(X-1)$ $\cdots(X-k+1) /[n(n-1) \cdots(n-k+1)]$ :

$$
\begin{aligned}
E[ & X(X-1) \cdots(X-k+1) / n(n-1) \cdots(n-k+1)] \\
= & \sum_{i=0}^{n}[i(i-1) \cdots(i-k+1) / n(n-1) \cdots(n-k+1)] \\
& \cdot\left(\begin{array}{l}
n \\
i
\end{array}\right) p^{i}(1-p)^{n-i} \\
= & \sum_{i=0}^{n} \frac{(n-k) !}{(i-k) !(n-i) !} p^{i}(1-p)^{n-i} \\
= & p^{k} \sum_{i=0}^{n}\left(\begin{array}{l}
n+k \\
i-k
\end{array}\right) p^{i-k}(1-p)^{n-i}
\end{aligned}
$$

令 $n-k=m, i-k=j$, 上式成为 $p^{k} \sum_{j=0}^{m}\left(\begin{array}{c}m \\ j\end{array}\right) p^{j}(1-p)^{m-j}=p^{k}$.

10. 依第一章 23 题, $\min \left(X_{1}, \cdots, X_{n}\right)$ 与 $\theta-\max \left(X_{1}, \cdots, X_{n}\right)$ 同分布. 因此二者之均值相同, 由此得

$$
E\left[\min \left(X_{1}, \cdots, X_{n}\right)+\max \left(X_{1}, \cdots, X_{n}\right)\right]=\theta
$$

这证明了 $(\mathrm{a})$. 又由第二章 22 题知 $\min \left(X_{1}, \cdots, X_{n}\right)$ 的概率密度为 $\frac{1}{\theta} n\left(1-\frac{x}{\theta}\right)^{n-1}$ (当 $0<x<\theta$, 此外为 0 ), 其均值为 $\theta /(n+1)$. 由 此可知, 令 $C_{n}=n+1$, 则 $C_{n} \min \left(X_{1}, \cdots, X_{n}\right)$ 为 $\theta$ 的无偏估计. 这 证明了 (b). 为证 $(\mathrm{c})$, 只须算出 $\operatorname{Var}\left(C_{n} \min \left(X_{1}, \cdots, X_{n}\right)\right)=(n+$ $1)^{2} \frac{n}{\theta} \int_{0}^{\theta} x^{2}\left(1-\frac{x}{\theta}\right)^{n-1} \mathrm{~d} x-\theta^{2}=n \theta^{2} /(n+2)$. 与j例 3.5 比较即 得(问: 由 $C_{n} \min \left(X_{1}, \cdots, X_{n}\right)$ 的方差表达式看出这个估计之不合 理处, 在什么地方? - $n$ 愈大, 其方差非但不下降, 反而上升, 即 样本愈多,估计误差愈大了).

11. (a) 有

$$
E[\hat{\theta}(x)]=\sum_{i=0}^{\infty} \hat{\theta}(i) \frac{\mathrm{e}^{-\lambda}}{i !} \lambda^{i}=\mathrm{e}^{-2 \lambda}
$$

得

$$
\sum_{i=0}^{\infty} \hat{\theta}(i) \frac{\lambda^{i}}{i !}=\mathrm{e}^{-\lambda}=\sum_{i=0}^{\infty}(-1)^{i} \frac{\lambda^{i}}{i !} \text {, 因此 } \hat{\theta}(i)=(-1)^{i}
$$

这估计之不合理显然,一个合理的估计可取为 $\mathrm{e}^{-2 x}$.

12. 利用 $E\left(\chi_{n}^{2}\right)=n, \operatorname{Var}\left(\chi_{n}^{2}\right)=2 n$. 由于 $(n-1) \hat{\theta}_{1} / \sigma^{2} \sim$ $\chi_{n-1}^{2}$, 知

$$
\begin{aligned}
E\left[\hat{\theta}_{1}-\sigma^{2}\right]^{2} & =(n-1)^{-2} \sigma^{4} E\left[(n-1) \hat{\theta}_{1} / \sigma^{2}-(n-1)\right]^{2} \\
& =(n-1)^{-2} \sigma^{4} \operatorname{Var}\left(\chi_{n-1}^{2}\right)=2 \sigma^{4} /(n-1)
\end{aligned}
$$

另一方面, 有

$$
\begin{aligned}
& E\left(\frac{n-1}{n+1} \hat{\theta}-\sigma^{2}\right)^{2}=\left(E\left(\frac{n-1}{n+1} \hat{\theta}\right)-\sigma^{2}\right)^{2}+\operatorname{Var}\left(\frac{n-1}{n+1} \hat{\theta}\right) \\
& \quad=\left(\frac{2}{n+1}\right)^{2} \sigma^{4}+\left(\frac{n-1}{n+1}\right)^{2} \operatorname{Var}\left(\hat{\theta}_{1}\right) \\
& \quad=\left(\frac{2}{n+1}\right)^{2} \sigma^{4}+\left(\frac{n-1}{n+1}\right)^{2} \frac{2}{n-1} \sigma^{4}=\frac{2}{n+1} \sigma^{4}
\end{aligned}
$$

由此得出要证的结果.

13. 与 12 题一样, 用 $\operatorname{Var}\left(\chi_{n}^{2}\right)=2 n$, 有

$$
\operatorname{Var}\left(\hat{\theta}_{3}\right)=\frac{\sigma^{4}}{n^{2}} \operatorname{Var}\left(\chi_{n}^{2}\right)=\frac{2}{n} \sigma^{4}<\operatorname{Var}\left(\hat{\theta}_{1}\right)
$$

这证明了 (a). 为证 (b), 要用克拉美一劳不等式, 以 $\sigma^{2}$ 作 $\theta, g(\theta)=$ $\theta$. 算出

$$
I\left(\sigma^{2}\right)=E\left[\frac{1}{2 \sigma^{2}}-\frac{1}{2 \sigma^{4}}(X-a)^{2}\right]^{2}=1 /\left(2 \sigma^{4}\right)
$$

于是 $\sigma^{2}$ 的无偏估计之方差下界为

$$
1 /\left(n I\left(\sigma^{2}\right)\right)=2 \sigma^{4} / n
$$

与 $\operatorname{Var}\left(\hat{\theta}_{3}\right)$ 相同. 由此证明了所要的结果.

$$
\text { 注: 若令 } \hat{\theta}_{4}=\frac{1}{n+2} \sum_{i=1}^{n}\left(X_{i}-a\right)^{2} \text {. 由 } 12 \text { 题的证法, } \hat{\theta}_{4} \text { 的均方 }
$$

误差为 $2 \sigma^{4} /(n+2)$, 比 $\hat{\theta}_{3}$ 的均方误差 (即 $\operatorname{Var}\left(\hat{\theta}_{3}\right)$ ) 小. 由此例可 知, MVU 估计的均方误差不一定是最小的.

14. (a)因为作变换 $x=\sqrt{y / \theta}$ 可得

$$
\begin{aligned}
\int_{0}^{\infty} x^{2} \mathrm{e}^{-\theta x 2} \mathrm{~d} x & =\theta^{-3 / 2} \int_{0}^{\infty} y^{1 / 2} \mathrm{e}^{-y / 2 \mathrm{~d} y} \\
& =\frac{1}{2} \theta^{-3 / 2} \Gamma(3 / 2)=\frac{1}{4} \sqrt{\pi} \theta^{-3 / 2}
\end{aligned}
$$

即知 $E\left(X_{i}^{2}\right)=\frac{1}{2 \theta}$. 故令 $C=2$ 即可. 其次, 算出

$$
\operatorname{Var}\left(\frac{2}{n} \sum_{i=1}^{n} X_{i}^{2}\right)=\frac{4}{n} \operatorname{Var}\left(X_{1}^{2}\right)=2 /\left(n \theta^{2}\right)
$$

再用克拉美-劳不等式, 先算出

$$
I(\theta)=E\left[\frac{1}{2 \theta}-X^{2}\right]^{2}=1 /\left(2 \theta^{2}\right)
$$

而 $g(\theta)=1 / \theta$, 故 $g^{\prime}(\theta)=-1 / \theta^{2}$ 而

$$
\left(g^{\prime}(\theta)\right)^{2} / n I(\theta)=\theta^{-4} /\left(\frac{1}{2} n \theta^{-2}\right)=2 /\left(n \theta^{2}\right)=\operatorname{Var}\left(\frac{2}{n} \sum_{i=1}^{n} X_{i}^{2}\right)
$$

于是证明了所要的结果. 15. (a) 用第三章定理 $3.1,2^{\circ}$, 有

$$
\begin{aligned}
& \operatorname{Var}\left(\frac{\hat{\theta}_{1}+\hat{\theta}_{2}}{2}\right)=E\left[\frac{1}{2}\left(\hat{\theta}_{1}-\theta\right)+\frac{1}{2}\left(\hat{\theta}_{2}-\theta\right)\right]^{2} \\
= & \frac{1}{4}\left[E\left(\hat{\theta}_{1}-\theta\right)^{2}+E\left(\hat{\theta}_{2}-\theta\right)^{2}\right]+\frac{1}{2} E\left[\left(\hat{\theta}_{1}-\theta\right)\left(\hat{\theta}_{2}-\theta\right)\right] \\
\leqslant & \frac{1}{4}\left[E\left(\hat{\theta}_{1}-\theta\right)^{2}+E\left(\hat{\theta}_{2}-\theta\right)^{2}\right]+\frac{1}{2}\left[E\left(\hat{\theta}_{1}-\theta\right)^{2}\right. \\
& \left.\cdot E\left(\hat{\theta}_{2}-\theta\right)^{2}\right]^{\frac{1}{2}}
\end{aligned}
$$

由于 $\hat{\theta}_{1}, \hat{\theta}_{2}$ 都是 $\theta$ 的 MVU 估计, 其方差相同且都达到最小值 $c(\theta)$. 由上式得

$$
\operatorname{Var}\left(\frac{\hat{\theta}_{1}+\hat{\theta}_{2}}{2}\right) \leqslant \frac{1}{4}[c(\theta)+c(\theta)]+\frac{1}{2} c(\theta)=c(\theta)
$$

即无偏估计 $\left(\hat{\theta}_{1}+\hat{\theta}_{2}\right) / 2$ 的方差不大于最小值 $c(\theta)$, 因而它必为 MVU 估计.

(b) 用反证法, 若 $a \hat{\theta}+b$ 不为 $a \theta+b$ 的 MVU 估计, 则可以找 到 $a \theta+b$ 的一个无偏估计 $\hat{\theta}_{1}$, 使

$$
\operatorname{Var}_{\theta_{0}}\left(\hat{\theta}_{1}\right)<\operatorname{Var}_{\theta_{0}}(a \hat{\theta}+b)=a^{2} \operatorname{Var}_{\theta_{0}}(\hat{\theta})
$$

至少对一个 $\theta$ 值 $\theta_{0}$. 令 $\hat{\theta}_{2}=\left(\hat{\theta}_{1}-b\right) / a$, 则 $\hat{\theta}_{2}$ 为 $\theta$ 的无偏估计, 且

$$
\operatorname{Var}_{\theta_{0}}\left(\hat{\theta}_{2}\right)=\frac{1}{a^{2}} \operatorname{Var}_{\theta_{0}}\left(\hat{\theta}_{1}\right)<\frac{1}{a^{2}} a^{2} \operatorname{Var}_{\theta_{0}}(\theta)=\operatorname{Var}_{\theta_{0}}(\hat{\theta})
$$

即无偏估计 $\hat{\theta}_{2}$ 的方差, 当 $\theta=\theta_{0}$ 时比无偏估计 $\hat{\theta}$ 的方差还小. 这与 $\hat{\theta}$ 的是 $\theta$ 的 MVU 估计矛盾.

16. $E\left(\sum_{i=1}^{n} c_{i} X_{i}\right)=\sum_{i=1}^{n} c_{i} E\left(X_{i}\right)=\theta \sum_{i=1}^{n} c_{i}=\theta$, 故 $\sum_{i=1}^{k} c_{i} X_{i}$ 为无 偏估计, 其方差为 $\left(\sigma^{2}=\operatorname{Var}\left(X_{i}\right)\right)$

$$
\operatorname{Var}\left(\sum_{i=1}^{n} c_{i} X_{i}\right)=\sum_{i=1}^{n} c_{i}^{2} \operatorname{Var}\left(X_{i}\right)=\sigma^{2} \sum_{i=1}^{k} c_{i}^{2}
$$

$$
=\sigma^{2}\left[\sum_{i=1}^{n}\left(c_{i}-1 / n\right)^{2}+1 / n\right] \geqslant \sigma^{2} / n
$$

等号当且仅当 $c_{1}=\cdots=c_{n}=1 / n$ 时才成立.

17. 因为 $\max \left(X_{1}, \cdots, X_{n}\right)$ (记为 $\hat{\theta}$ ) 的密度函数为 $n x^{n-1} / \theta^{n}$ (当 $0<x<\theta$, 此外为 0 ). 故

$$
\begin{aligned}
& P_{\theta}\left(\hat{\theta} \leqslant \theta \leqslant c_{n} \hat{\theta}\right)=P_{\theta}\left(\theta / c_{n} \leqslant \hat{\theta} \leqslant \theta\right) \\
& \quad=\int_{\theta / c n}^{\theta} n x^{n-1} \mathrm{~d} x / \theta^{n}=\left(\theta^{n}-\left(\theta / c_{n}\right)^{n}\right) / \theta^{n}=1-c_{n}^{-n}
\end{aligned}
$$

要此值等于 $1-\alpha$, 只须取 $c_{n}=\left(\frac{1}{1-\alpha}\right)^{1 / n}$.

18. (a) 只要 $c+d=1$, 则 $c \bar{X}+d \bar{Y}$ 为 $\theta$ 的无偏估计, 其方差 为 $c^{2} \sigma_{1}^{2} / n+d^{2} \sigma_{2}^{2} / m$. 把此式在 $c+d=1$ 的约束下求最小值, 结 果为

$$
c=\left(\sigma_{2}^{2} / m\right) /\left(\sigma_{1}^{2} / n+\sigma_{2}^{2} / m\right), d=\left(\sigma_{1}^{2} / n\right) /\left(\sigma_{1}^{2} / n+\sigma_{2}^{2} / m\right)
$$

对这个 $c, d$ 有

$$
(c \bar{X}+d \bar{Y}-\theta) / A \sim N(0,1)
$$

其中 $A^{2}=\left(\sigma_{1}^{2} / n \cdot \sigma_{2}^{2} / m\right) /\left(\sigma_{1}^{2} / n+\sigma_{2}^{2} / m\right)$. 于是得到 $\theta$ 的置信系 数 $1-\alpha$ 的区间估计为 $c \bar{X}+d \bar{Y} \pm A u_{\alpha / 2}$.

19. 考虑

$$
2 \lambda_{1} n \bar{X} / 2 \lambda_{2} m \bar{Y}=Z
$$

分子分母独立, 分别服从卡方分布 $\chi^{\frac{2}{2} n}$ 和 $\chi^{\frac{2}{2}}, m$. 故

$$
P\left(F_{2 n, 2 m}\left(1-\frac{\alpha}{2}\right) \leqslant \frac{\lambda_{1} \bar{X}}{\lambda_{2} \bar{Y}} \leqslant F_{2 n, 2 m}\left(\frac{\alpha}{2}\right)\right)=1-\alpha
$$

此式可改写为

$$
P\left(\frac{\bar{X}}{\bar{Y}} / F_{2 n, 2 m}\left(\frac{\alpha}{2}\right) \leqslant \frac{\lambda_{2}}{\lambda_{1}} \leqslant \frac{\bar{X}}{\bar{Y}} / F_{2 n, 2 m}\left(1-\frac{\alpha}{2}\right)\right)=1-\alpha
$$

即得 $\lambda_{2} / \lambda_{1}$ 的置信区间.

20. $\left(\theta, X_{1}, X_{2}\right)$ 的联合分布密度为

$$
f\left(\theta, X_{1}, X_{2}\right)=\mathrm{e}^{-\theta} \mathrm{e}^{\theta-x_{1}} \mathrm{e}^{\theta-x_{2}}, 0<\theta \leqslant \min \left(X_{1}, X_{2}\right)
$$

- $386 \cdot$ 由此得出 $\left(X_{1}, X_{2}\right)$ 的边缘密度 为 $\int_{0}^{\min \left(X_{1}, X_{2}\right)} \mathrm{e}^{\theta} \mathrm{d} \theta \mathrm{e}^{-\left(X_{1}+X_{2}\right)}=$ $\mathrm{e}^{-\left(X_{1}+X_{2}\right)}\left[\mathrm{e}^{\min \left(X_{1}, X_{2}\right)}-1\right]$, 而 $\theta$ 的后验密度为

$$
h\left(\theta \mid X_{1}, X_{2}\right)=\mathrm{e}^{\theta} /\left[\mathrm{e}^{\min \left(X_{1}, X_{2}\right)}-1\right], 0<\theta \leqslant \min \left(X_{1}, X_{2}\right)
$$

此外为 0 . 这密度在上述区间内随 $\theta$ 上升而上升. 故要找一个最短 的区间 $[a, b]$ 使 $\int_{a}^{b} h\left(\theta \mid X_{1}, X_{2}\right) \mathrm{d} \theta=1-\alpha, b$ 必须取为 $\min \left(X_{1}\right.$, $X_{2}$ ). 因

$$
\int_{a}^{\min \left(X_{1}, X_{2}\right)} \mathrm{e}^{\theta} \mathrm{d} \theta=\mathrm{e}^{\min \left(X_{1}, X_{2}\right)}-\mathrm{e}^{a}
$$

知 $a$ 必须取为 $\log \left[\alpha \mathrm{e}^{\min \left(X_{1}, X_{2}\right)}+1-\alpha\right]$.

21. 由 $(n-1) S^{2} / \sigma^{2}-\chi_{n-1}^{2}$, 从卡方分布密度的形式, 不难算 出 $S / \sigma$ 的密度函数 $g(s)$ 为: $g(s)=0$ 当 $s \leqslant 0$, 而

$$
g(s)=\frac{(n-1)^{(n-1) / 2}}{2^{(n-3) / 2} \Gamma\left(\frac{n-1}{2}\right)} \mathrm{e}^{-\frac{(n-1) / s^{2}}{2}} S^{n-2}, s>0
$$

为计算 $E(S)=\sigma \int_{0}^{\infty} s g(s) \mathrm{d} s$, 只须在积分

$$
\int_{0}^{\infty} s^{n-1} \exp \left(-\frac{(n-1) s^{2}}{2}\right) \mathrm{d} s
$$

中作变数代换 $t=(n-1) s^{2} / 2$ 以化为 $\Gamma$ 积分即可.

22. 作代换 $Y_{i}=\left(X_{i}-\theta_{1}\right) /\left(\theta_{2}-\theta_{1}\right), i=1, \cdots n$. 则 $Y_{1}, \cdots$, $Y_{n}$ 独立同分布, 其公共分布为 $[0,1]$ 上的均匀分布 $R(0,1)$, 与 $\theta_{1}, \theta_{2}$ 无关. 故 $E\left(S_{Y}\right)=E \sqrt{\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2} /(n-1)}$ 也与 $\theta_{1}, \theta_{2}$ 无关. 记为 $d_{n}$. 有 $S=\sqrt{\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2} /(n-1)}=\left(\hat{\theta}_{2}-\hat{\theta}_{1}\right) S_{Y}$, 故 $E(S)=d_{n}\left(\theta_{2}-\theta_{1}\right)$. 现有

$$
\begin{aligned}
& E\left(\bar{X}-c_{n} S\right)=\left(\hat{\theta}_{1}+\hat{\theta}_{2}\right) / 2-c_{n} d_{n}\left(\hat{\theta}_{2}-\hat{\theta}_{1}\right) \\
& E\left(\bar{X}+c_{n} S\right)=\left(\hat{\theta}_{1}+\hat{\theta}_{2}\right) / 2+c_{n} d_{n}\left(\hat{\theta}_{2}-\hat{\theta}_{1}\right)
\end{aligned}
$$

取 $C_{n}=1 /\left(2 d_{n}\right)$. 此两式分别成为 $\hat{\theta}_{1}$ 和 $\hat{\theta}_{2}$. 要求出 $C_{n}$, 必须算出 $d_{n}=E\left(S_{Y}\right)$. 这不容易。

23. 设此结论不对, 则存在 $\theta$ 的无偏估计 $T_{n}$, 使对于 $\left(\theta, \sigma^{2}\right)$ 的某个值 $\left(\theta_{0}, \sigma_{0}^{2}\right)$, 有

$$
\operatorname{Var}_{\theta_{0}, \sigma_{0}^{2}}\left(T_{n}\right)<\operatorname{Var}_{\theta_{0}}, \sigma_{0}^{2}(\bar{X})=\sigma_{0}^{2} / n
$$

把 $X_{1}, \cdots, X_{n}$ 看作为抽自正态总体 $N\left(\theta, \sigma_{0}^{2}\right)$ 的样本, $\theta$ 末知而 $\sigma_{0}^{2}$ 已知. 这时, $\bar{X}$ 和 $T_{n}$ 仍然是 $\theta$ 的无偏估计. 且因此处方差 $\sigma_{0}^{2}$ 已 知. $\bar{X}$ 是 $\theta$ 的 MVU 估计. 因此对一切 $\theta$ 应有

$$
\operatorname{Var}_{\theta, \sigma_{0}^{2}}\left(T_{n}\right) \geqslant \operatorname{Var}_{\theta, \sigma_{0}^{2}}^{2}(\bar{X})=\sigma_{0}^{2} / n
$$

令 $\theta=\theta_{0}$, 即得到与前式矛盾的结果, 这证明了 $\bar{X}$ 仍是 $\theta$ 的 MVU 估计。

