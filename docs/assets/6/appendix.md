# A. (2.22) 式的证明 

注意到两个行向量 $(n$ 维)

$$
\begin{aligned}
& b_{1}^{\prime}=\left(\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}}, \cdots, \frac{1}{\sqrt{n}}\right), \\
& b_{2}^{\prime}=\left(\frac{X_{1}-\bar{X}}{S_{x}}, \frac{X_{2}-\bar{X}}{S_{x}}, \cdots, \frac{X_{n}-\bar{X}}{S_{x}}\right)
\end{aligned}
$$

都是单位长 (注意 (2.16) 式) 且正交, 可以补充 $n-2$ 个行向量 $b_{3}^{\prime}$, $\cdots, b_{n}^{\prime}$, 使方阵

$$
B=\left(\begin{array}{c}
b_{1}^{\prime} \\
b_{2}^{\prime} \\
\vdots \\
b_{n}^{\prime}
\end{array}\right)
$$

为正交方阵.作变换

$$
\left(\begin{array}{c}
Z_{1} \\
Z_{2} \\
\vdots \\
Z_{n}
\end{array}\right)=B\left(\begin{array}{c}
Y_{1} \\
Y_{2} \\
\vdots \\
Y_{n}
\end{array}\right)
$$

则因为 $Y_{1}, Y_{1}, \cdots, Y_{n}$ 独立，各有方差为 $\sigma^{2}$ 的正态分布，按第二 章的附录 A 中的引理的证法, 易证得 $Z_{1}, \cdots, Z_{n}$, 也独立, 并各有 方差为 $\sigma^{2}$ 的正态分布.

现证明:

$$
E\left(Z_{i}\right)=0, i \geqslant 3
$$

为此, 记 $b_{i}^{\prime}=\left(b_{i 1}, \cdots, b_{i n}\right)$, 则

$$
\begin{aligned}
E\left(Z_{i}\right) & =\sum_{j=1}^{n} b_{i j} E\left(Y_{j}\right)=\sum_{j=1}^{n} b_{i j}\left(\beta_{0}+\beta_{1}\left(X_{i}-\bar{X}\right)\right) \\
& =\beta_{0} \sum_{j=1}^{n} b_{i j}+\beta_{1} \sum_{j=1}^{n} b_{i j}\left(X_{i}-\bar{X}\right)
\end{aligned}
$$

因为 $b_{i}$ 与 $b_{1}, b_{2}$ 都正交, 上式右边两个和都为 0 . 由此证明了(1) 式.

另外注意

$$
\begin{aligned}
Z_{1} & =\frac{1}{\sqrt{n}}\left(Y_{1}+\cdots+Y_{n}\right)=\sqrt{n} \bar{Y} \\
Z_{2} & =\frac{1}{S_{x}} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} \\
Z_{2}^{2} & =\frac{1}{S_{x}^{2}} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} \cdot \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} \\
& =\hat{\beta}_{1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}
\end{aligned}
$$

由于正交变换使平方和不变, 有

$$
\begin{aligned}
& Y_{1}^{2}+\cdots+Y_{n}^{2}=Z_{1}^{2}+\cdots+Z_{n}^{2} \\
= & n \bar{Y}^{2}+\hat{\beta}_{1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}+\sum_{i=\mathbf{3}}^{n} Z_{i}^{2}
\end{aligned}
$$

将此式与 (2.23) 式结合, 得

$$
\sum_{i=1}^{n} \delta_{i}^{2}=\sum_{i=3}^{n} Z_{i}^{2}=\sigma^{2} \sum_{i=3}^{n} Z_{i}^{2} / \sigma^{2}
$$

由于 $Z_{3} / \sigma, Z_{4} / \sigma, \cdots, Z_{n} / \sigma$ 是独立同分布的 $N(0,1)$ 变量, 有 $\left(Z_{3}^{2}\right.$ $\left.+\cdots+Z_{n}^{2}\right) / \sigma^{2}-\chi_{n-2}^{2}$. 于是证明了 $(2.22)$.

## 1. B.(2.16)式的证明

由于 $Z_{1}, Z_{2}, \cdots, Z_{n}$ 独立, 知 $Z_{2}$ 与 $\sum_{i=3}^{n} Z_{i}^{2}$ 独立. 又 $Z_{2}$ 为有方 差 $\sigma^{2}$ 的正态分布而 $\sum_{i=3}^{n} Z_{i}^{2} / \sigma^{2} \sim \chi_{n-2}^{2}$, 故按 $t$ 分布的定义有

$$
\frac{Z_{2}-E\left(Z_{2}\right)}{\sigma} / \sqrt{\frac{1}{n-2} \frac{1}{\sigma^{2}} \sum_{i=3}^{n} Z_{i}^{2}} \sim t_{n-2}
$$

但 $\sum_{i=3}^{n} Z_{i}^{2} /(n-2)=\sum_{i=1}^{n} \delta_{i}^{2} /(n-2)=\hat{\sigma}^{2}$, 而因 $E \hat{\beta}_{1}=\beta_{1}$, 有

$$
Z_{2}-E\left(Z_{2}\right)=\hat{\beta}_{1} S_{x}-E\left(\hat{\beta}_{1} S_{x}\right)=\left(\hat{\beta}_{1}-\beta_{1}\right) S_{x}
$$

故

$$
\frac{Z_{2}-E\left(Z_{2}\right)}{\sigma} / \sqrt{\frac{1}{n-2} \frac{1}{\sigma^{2}} \sum_{i=3}^{n} Z_{i}^{2}}=\left(\hat{\beta}_{1}-\beta_{1}\right) /\left(\hat{\sigma} S_{x}^{-1}\right)
$$

此式与 (2) 式结合, 即证明了 (2.26).

