# 附 录 

## 1. A. 公式 (4.25) 的证明

## 2. 由等式

$$
\int_{0}^{\infty} u^{x+y-1} v^{x-1} \mathrm{e}^{-u(1+v)} \mathrm{d} v=\mathrm{e}^{-u} u^{y-1} \int_{0}^{\infty}(u v)^{x-1} \mathrm{e}^{u u} u \mathrm{~d} v
$$

出发, 作变数代换 $\omega=u v$, 知右边的积分等于 $\int_{0}^{\infty} \omega^{x-1} \mathrm{e}^{-\omega} \mathrm{d} \omega$ 即 $\Gamma(x)$. 于是

$$
\int_{0}^{\infty} u^{x+y-1} v^{x-1} \mathrm{e}^{-u(1+v)} \mathrm{d} v=\mathrm{e}^{-u} u^{y-1} \Gamma(x)
$$

两边对 $u$ 从 0 到 $\infty$ 积分,得

$$
\Gamma(x) \Gamma(y)=\int_{0}^{\infty}\left[\int_{0}^{\infty} u^{x+y-1} \mathrm{e}^{-u(1+v)} \mathrm{d} u\right] v^{x-1} \mathrm{~d} v
$$

对里面的积分作变数代换 $t=u(1+v)$, 有

$$
\begin{aligned}
& \int_{0}^{\infty} u^{x+y-1} \mathrm{e}^{-u(1+v)} \mathrm{d} u \\
= & (1+v)^{-(x+y)} \int_{0}^{\infty} \mathrm{e}^{-t} t^{x+y-1} \mathrm{~d} t \\
= & (1+v)^{-(x+y)} \Gamma(x+y)
\end{aligned}
$$

代人上式得

$$
\Gamma(x) \Gamma(y)=\Gamma(x+y) \int_{0}^{\infty} v^{x-1}(1+v)^{-(x+y)} \mathrm{d} v
$$

作变数代换 $t=v /(1+v)$. 当 $v$ 由 0 变到 $\infty$ 时, $t$ 由 0 变到 1 . 又

$$
\begin{aligned}
& v^{(x-1)}(1+v)^{-(x+y)} \\
= & (v /(1+v))^{x-1}(1+v)^{-(y+1)} \\
= & t^{x-1}(1-t)^{y+1}
\end{aligned}
$$

因而 $v=t /(1-t)$, 有 $\mathrm{d} v=(1-t)^{-2} \mathrm{~d} t$. 故

$$
\int_{0}^{\infty} v^{x-1}(1+v)^{-(x+y)} \mathrm{d} v=\int_{0}^{1} t^{x-1}(1-t)^{y-1} \mathrm{~d} t=\beta(x, y)(2)
$$

由 (1),(2) 两式即得 $(4.25)$.

## 3. B. $(4.33)-(4.36)$ 的证明

这个证明要求读者对正交方阵有初步知识. 先证明下面的预 备事实:

引理 设 $X_{1}, X_{2}, \cdots, X_{n}$ iid, $\sim N\left(\mu, \sigma^{2}\right)$. 记 $\bar{X}=\sum_{i=1}^{n} X_{i} / n$. 则

a. $\sqrt{n}(\bar{X}-\mu) / \sigma \sim N(0,1)$,

b. $\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2} \sigma^{2} \sim \chi_{n-1}^{2}$,

c. $\bar{X}$ 与 $\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$ 独立.

证 找一个 $n$ 阶正交方阵 $A$, 其第一行各元都是 $1 / \sqrt{n}$. 作正 交变换

$$
\left(\begin{array}{c}
Y_{1} \\
\vdots \\
Y_{n}
\end{array}\right)=A\left(\begin{array}{c}
X_{1} \\
\vdots \\
X_{n}
\end{array}\right)
$$

由于 $A$ 为正交变换, 它不改变平方和, 即 $\sum_{i=1}^{n} X_{i}^{2}=\sum_{i=1}^{n} Y_{i}^{2}$. 又因 正交方阵的行列式为 1 , 根据公式 (4.15), 注意到 $\left(X_{1}, \cdots, X_{n}\right)$ 的 密度函数为

$$
\begin{aligned}
& (\sqrt{2 \pi} \sigma)^{-n} \exp \left[-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}\right] \\
= & (\sqrt{2 \pi} \sigma)^{-n} \exp \left[-\frac{1}{2 \sigma^{2}}\left(\sum_{i=1}^{n} x_{i}^{2}-2 \mu \sum_{i=1}^{n} x_{i}+n \mu^{2}\right)\right]
\end{aligned}
$$

以及 $\sum_{i=1}^{n} x_{i}=\sqrt{n} y_{1}$ (这是因为 $A$ 的第一行各元都是 $1 / \sqrt{n}$, 因而 $\left.y_{1}=\left(x_{1}+\cdots+x_{n}\right) / \sqrt{n}\right)$, 得知 $\left(Y_{1}, \cdots, Y_{n}\right)$ 的密度函数为

$$
\begin{aligned}
(\sqrt{2 \pi} \sigma)^{-n} \exp \left[-\frac{1}{2 \sigma^{2}}\left(\sum_{i=1}^{n} y_{i}^{2}-2 \mu \sqrt{n} y_{1}+n \mu^{2}\right)\right] \\
=(\sqrt{2 \pi} \sigma)^{-1} \mathrm{e}^{-\left(y_{1}-\sqrt{n} \mu\right)^{2} / 2 \sigma^{2}} \cdot(\sqrt{2 \pi} \sigma)^{-1} \mathrm{e}^{-y_{2}^{2} / \sigma^{2}} \ldots \\
\cdot(\sqrt{2 \pi} \sigma)^{-1} \mathrm{e}^{-y_{n}^{2} / 2 \sigma^{2}}
\end{aligned}
$$

因此, $\left(Y_{1}, \cdots, Y_{n}\right)$ 的密度可分解为 $n$ 个函数的乘积, 每个函数只 依赖一个变量. 据定理 3.2 , 即知 $Y_{1}, Y_{2}, \cdots, Y_{n}$ 独立, 且

$$
Y_{1} \sim N\left(\sqrt{n} \mu, \sigma^{2}\right), Y_{i} \sim N\left(0, \sigma^{2}\right), i=2, \cdots, n
$$

再据定理 3.3, $Y_{1}$ 与 $Y_{2}^{2}+\cdots+Y_{n}^{2}$ 独立, 但

$$
\begin{aligned}
& \sum_{i=2}^{n} Y_{i}^{2}=\sum_{i=1}^{n} Y_{i}^{2}-Y_{1}^{2} \\
= & \sum_{i=1}^{n} X_{i}^{2}-\left(\sum_{i=1}^{n} X_{i}\right)^{2} / n=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}
\end{aligned}
$$

而 $Y_{1}=\sqrt{n} \bar{X}$. 这证明了 c. a 和 $\mathrm{b}$ 由 (3), (4) 及卡方分布的定义立 即得出.引理证毕.

有了这个引理就不难得出 (4.33)-(4.36). 事实上, (4.33) 就 是这引理的 b. 为证 $(4.34)$, 注意 $\sqrt{n}(\bar{X}-\mu) / \sigma$ 服从正态分布 $N(0,1)$, 由引理的 $\mathrm{b}, S / \sigma$ 的分布与 $\sqrt{\chi_{n-1}^{2} /(n-1)}$ 的分布相同. 又按引理的 $\mathrm{c}, \sqrt{n}(\bar{X}-\mu)$ 与 $S$ 独立. 于是由 $t$ 分布的定义即得 (4.34). (4.35) 由引理的 $\mathrm{b}$ 及 $F$ 分布的定义得出.

(4.36) 的证明略复杂一些. 暂记 $Z_{1}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}, Z_{2}=$ $\sum_{i=1}^{m}\left(Y_{j}-\bar{Y}\right)^{2}$. 据引理的 $\mathrm{c}, \bar{X}$ 与 $Z_{1}$ 独立, $\bar{Y}$ 与 $Z_{2}$ 独立, 又因 $X_{1}$, $\cdots, X_{n}, Y_{1}, \cdots, Y_{m}$ 全体独立, 故 $\bar{X}, \bar{Y}, Z_{1}, Z_{2}$ 四者独立. 因为 $\bar{X} \sim$ $N\left(\mu_{1}, \sigma^{2} / n\right), \bar{Y} \sim N\left(\mu_{2}, \sigma^{2} / m\right), \sigma^{2}$ 为 $\sigma_{1}^{2}$ 和 $\sigma_{2}^{2}$ 的公共值，据例 4.8 , 知 $\bar{X}-\bar{Y} \sim N\left(\mu_{1}-\mu_{2}, \sigma^{2} / n+\sigma^{2} / m\right)$, 因而 $\sqrt{\frac{n+m}{n m}} \frac{1}{\sigma}[(\bar{X}$ $\left.-\bar{Y})-\left(\mu_{1}-\mu_{2}\right)\right] \sim N(0,1)$. 又据 (4.33), 有 $Z_{1} / \sigma^{2} \sim \chi_{n-1}^{2}$, $Z_{2} / \sigma^{2} \sim \chi_{m-1}^{2}$, 因 $Z_{1}, Z_{2}$ 独立, 按卡方分布的性质, 有 $\left(Z_{1}+Z_{2}\right) /$ $\sigma^{2} \sim \chi_{n+m-2}^{2}$. 因 $\bar{X}, \bar{Y}, Z_{1}, Z_{2}$ 四者独立，按第二章定理 3.3, 知

$$
\begin{aligned}
& W_{1}=\sqrt{\frac{n+m}{n m}} \frac{1}{\sigma}\left[(\bar{X}-\bar{Y})-\left(\mu_{1}-\mu_{2}\right)\right] \text { 与 } \\
& W_{2}=\left[\frac{1}{(n+m-2) \sigma^{2}}\left(Z_{1}+Z_{2}\right)\right]^{1 / 2} \text { 二者独立 }
\end{aligned}
$$

按 $t$ 分布的定义知, $W_{1} / W_{2} \sim t_{n+m-2}$. 这就证明了(4.36).

可以注意一下这些结果中的自由度数目. 在 $(4.33), \sum_{i=1}^{n}\left(X_{i}-\right.$ $\bar{X})^{2}$ 为 $n$ 个量的平方和, 为何自由度只有 $n-1$ ? 这是因为, $X_{1}-$ $\bar{X}, \cdots, X_{n}-\bar{X}$ 这 $n$ 个量并不能自由变化, 而是受到一个约束, 即 $\sum_{i=2}^{n}\left(X_{i}-\bar{X}\right)=0$. 这使它的自由度少了一个.(4.36) 中的自由度 是 $n+m-2$ 也一样地解释: 一共有 $n+m$ 个量 $X_{i}-\bar{X}(i=1, \cdots$, $n)$ 和 $Y_{j}-\bar{Y}(j=1, \cdots, m)$ 取平方和. 它们受到两个结束, 即 $\sum\left(X_{i}-\bar{X}\right)=0, \Sigma\left(Y_{j}-\bar{Y}\right)=0$. 少了两个自由度, 故自由度 不为 $n+m$ 而为 $n+m-2$.

在第四章例 3.2 中, 将给自由度这个概念以另一个解释. 不言 而喻, 不同的解释只是形式上的差别, 实质并无不同.

