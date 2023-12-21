---
comments: true
tags:
  - 校订中……
---
# 答案

<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/3/answers.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/3/answers.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/3/answers.pdf">下载 PDF</a>.</p>
    </embed>
</object>
# 第三章 

1. 不直接利用对数正态分布密度算较方便. 按定义, 若 $X$ 为 对数正态分布, 则 $X=\mathrm{e}^{Y}, Y \sim N\left(a, \sigma^{2}\right)$. 于是可利用公式 (1.18). 这涉及计算形如

$$
\int_{-\infty}^{\infty} \mathrm{e}^{b x} \mathrm{e}^{-(x-a)^{2} / 2 \sigma^{2}} \mathrm{~d} x
$$

的积分. 把 $b x-(x-a)^{2} / 2 \sigma^{2}$ 写为 $-(x-c)^{2} / 2 \sigma^{2}+d$ 的形式, 其 中 $c=a+b \sigma^{2}$, 即不难算出上述积分.

2. 易见它只与区间之长 $b-a$ 有关(何故). 记 $\theta=(b-a) / 2$, 可就 $R(-\theta, \theta)$ 的情况算, 结果为 $9 / 5-3=-6 / 5$.
3. 设 $X$ 服从超几何分布(第二章例 1.4), 可把 $X$ 表为 $X_{1}+$ $\cdots+X_{n}$, 这是设想 $n$ 个产品一件一件抽出, $X_{i}=0$ 或 1 视第 $i$ 个 产品为合格品或否而定, 先证明

$$
\begin{aligned}
& P\left(X_{i}=1\right)=M / N, P\left(X_{i}=0\right)=1-M / N, i=1, \cdots, n \\
& P\left(X_{i}=1, X_{j}=1\right)=M(M-1) / N(N-1) \\
& P\left(X_{i}=1, X_{j}=0\right)=P\left(X_{i}=0, X_{j}=1\right) \\
& \quad=M(N-M) / N(N-1) \\
& P\left(X_{i}=0, X_{j}=0\right)=(N-M)(N-M-1) / N(N-1)
\end{aligned}
$$

当 $i \neq j$. 由此就不难算出 $E(X)=n M / N$ 及 $E\left(X^{2}\right)$ 把 $X^{2}=$ $\left(X_{1}+\cdots+X_{n}\right)^{2}$ 展开), 从而算出 $\operatorname{Var}(X)=\frac{N-n M}{N-1 N}\left(1-\frac{M}{N}\right) n$.

4. 在不放回时, $n$ 种情况 (用 1 把, 2 把, $\cdots, n$ 把) 都是等可 能, 即 $P(X=i)=1 / n, i=1, \cdots, n$. 故

$$
E(X)=\frac{1}{n} \sum_{i=1}^{n} i=\frac{1}{n} \frac{n(n+1)}{2}=\frac{n+1}{2}
$$

如有放回, 则 $X=$ 概率为 $p$ 是 $1 / n$ 的几何分布变量再加上 1 . 按 例 1.2 , 得 $E(x)=1+\frac{1-p}{p}=1+n-1=n$.

5. 作法与第 3 题相似 (实际上, 第 3 题为本题当 $a_{i}=0$ 或 1 时 的特例). 但此处 $X_{i}$ 的分布为

$$
P\left(X_{i}=a_{j}\right)=1 / N, j=1, \cdots, N, i=1, \cdots, n
$$

当 $i \neq j$ 时, $\left(X_{i}, X_{j}\right)$ 联合分布为

$$
P\left(X_{i}=a_{u}, X_{i}=a_{v}\right)=1 / N(N-1)(u \neq v)
$$

由此易算出 $E(\bar{X})=a$. 为算 $\operatorname{Var}(\bar{X})$, 要算. $E\left(X_{1}+\cdots+X_{n}\right)^{2}$. 有 $E\left(X_{i}^{2}\right)=\sum_{j=1}^{N} a_{j}^{2} / N$. 而由(2) 有

$$
\begin{aligned}
E\left(X_{i} X_{j}\right) & =\frac{1}{N(N-1)} \sum_{u \neq v} a_{u} a_{z} \\
& =\frac{1}{N(N-1)}\left[\sum_{u, v=1}^{N} a_{u} a_{i}-\sum_{k-1}^{N} a_{k}^{2}\right] \\
& =\frac{1}{N(N-1)}\left[(n a)^{2}-\sum_{k=1}^{v} a_{k}^{2}\right]
\end{aligned}
$$

再经过简单的整理, 可得

$$
\operatorname{Var}(\bar{X})=\frac{N-n}{N-1} \frac{1}{n N} \sum_{i=1}^{N}\left(a_{i}-a\right)^{2}
$$

6. 分析 $X$ 的构成, 它等于 $X_{1}+\cdots+X_{r}$, 其中 $X_{i}$ 是已登记了 $i-1$ 个不同数字的情况下, 再抽到一个末登记的数字所需要抽的 次数, 显然, $X_{1}=1$, 对 $i>1, X_{i}=$ 个个概率 $p$ 为 $1-\frac{i-1}{n}$ 的几 何分布变量加上. 1 . 由此用例 1.2 算出 $E\left(X_{i}\right)=n /(n-i+1)($ 此 式对 $i=1$ 也对), 故 $E(X)=\sum_{i=1}^{r} n /(n-i+1)$.
7. (a) 用全概率公式算 $p_{k}(r+1, n)$ : 先把 $r$ 个球随机放人 $n$ 盒. 如恰有 $k$ 个空盒 (概率为 $p_{k}(r, n)$ ), 则剩下一球必须落在已 有球的盒子(共 $n-k$ 个) 中, 其概率为 $(n-k) / n$; 或者恰有 $k+1$ 个空盒 (概率为 $p_{k+1}(r, n)$ ), 则剩下一球必须落在无球的盒子 里, 其概率为 $(k+1) / n$. 由此得题中之 $(1)$ 式.

(b) 把题中的 (1) 式两边乘以 $k$, 再对 $k=0,1, \cdots, n-1$, 相加, 在化简右边时注意.

$$
\begin{aligned}
& \sum_{k=0}^{n-1} k p_{k+1}(r, n)(k+1) \\
&= \sum_{k-1}^{n-1}(k+1)^{2} p_{k+1}(r, n) \\
&-\sum_{k=0}^{n-1}(k+1) p_{k+1}(r, n)
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{k=1}^{n} k^{2} p_{k}(r, n)-\sum_{k=1}^{n} k p_{k}(r, n) \\
& =\sum_{k=0}^{n-1} k^{2} p_{k}(r, n)-\sum_{k-0}^{n} k p_{k}(r, n)
\end{aligned}
$$

这样即得出右边之和为 $\left(1-\frac{1}{n}\right) m_{r}, m_{0}=n$ 显然, 因为, 不投球时 空盒数为 $n$.

8. 要全出 $C$, 使 $C \int_{-\infty}^{\infty}\left(1+x^{2}\right)^{-n} \mathrm{~d} x=1$. 令 $N=2 n-1$, 上 式化为 $C \int_{-\infty}^{\infty}\left(1+x^{2}\right)^{-(N+1) / 2} \mathrm{~d} x=1$. 令 $x=y / \sqrt{N}$. 上式化为 $\frac{C}{\sqrt{N}} \cdot \int_{-\infty}^{\infty}\left(1+\frac{y^{2}}{N}\right)^{-(N+1) / 2} \mathrm{~d} y=1$. 与自由度为 $N$ 的 $t$ 分布密度比 较, 即得 $\frac{C}{\sqrt{N}}=\Gamma\left(\frac{N+1}{2}\right) /\left(\Gamma\left(\frac{N}{2}\right) \sqrt{N \pi}\right)$. 故

$$
C=\Gamma(n) /\left(\Gamma\left(\frac{2 n-1}{2}\right) \sqrt{\pi}\right)
$$

此密度关于 0 对称, 故其均值为 0 , 方差为 $C \int_{-\infty}^{\infty} x^{2}\left(1+x^{2}\right)^{-n} \mathrm{~d} x$ $=2 C \int_{0}^{\infty} x^{2}\left(1+x^{2}\right)^{-n} \mathrm{~d} x$. 这个积分经变数代换 $t=1 /\left(1+x^{2}\right)(x$ $=\sqrt{(1-t) / t})$ 可化为 $\beta$ 积分.

9. 由第二章 22 题可知 $Y_{1}$ 的密度函数为 $2 \Phi(x) \varphi(x)$, 这里 $\Phi, \varphi$ 分别是 $N(0,1)$ 的分布和密度函数, 故

$$
\begin{aligned}
E\left(Y_{1}\right) & =2 \int_{-\infty}^{\infty} x \Phi(x) \varphi(x) \mathrm{d} x \\
& =2 \int_{-\infty}^{\infty} x \varphi(x)\left[\int_{-\infty}^{x} \varphi(y) \mathrm{d} y\right] \mathrm{d} x \\
& =2 \iint_{|y<x|} x \varphi(x) \varphi(y) \mathrm{d} x \mathrm{~d} y \\
& =\frac{1}{\pi} \iint_{\mid y<x !} x e^{-\left(x^{2}+y^{2}\right) / 2} \mathrm{~d} x \mathrm{~d} y
\end{aligned}
$$

积分区域在图 4 中直线 $l$ 的下方, 化成极坐标后, 有

$$
\begin{aligned}
& \iint_{y<x} x e^{-\left(x^{2}+y^{2}\right) / 2} \mathrm{~d} x \mathrm{~d} y=\int_{-3 \pi / 4}^{\pi / 4} \cos \theta \mathrm{d} \theta \\
& \int_{0}^{\infty} r^{2} \mathrm{e}^{-r^{2} / 2} \mathrm{~d} r=\sqrt{2} \cdot(\sqrt{2 \pi} / 2)=\sqrt{\pi}
\end{aligned}
$$

因而得 $E\left(Y_{1}\right)=1 / \sqrt{\pi}$. 由于 $Y_{1}+Y_{2}=X_{1}$ $+X_{2}$, 知 $E\left(Y_{2}\right)=-E\left(Y_{1}\right)=-1 / \sqrt{\pi}$.

![](https://cdn.mathpix.com/cropped/2023_07_12_4b9419d9f76f2c706c45g-5.jpg?height=399&width=443&top_left_y=286&top_left_x=1269)

10 . 卡方分布的方差为其为值的 2 倍, 故若 $X_{1}$ 和 $X_{2}$ 分别服从卡方分布 $\chi_{m}^{2}$ 和 约 4 $\chi_{n}^{2}$, 则因 $X_{1}, X_{2}$ 独立, 将有

$$
E\left(X_{1}+b X_{2}\right)=m+b n, \operatorname{Var}\left(X_{1}+b X_{2}\right)=2 m+2 b^{2} n
$$

要后一值为前者的 2 倍, 只有在 $b=0$ 或 1 时才行.

11. 化为极坐标, 则 $Z$ 与 $r$ 无关而只是 $\theta$ 的函数, 再利用第二 章例 3.6 中得出的 $\theta \sim R(0,2 \pi)$.
12. 先设 $F$ 有密度 $f$, 则 $F(x)=\int_{0}^{x} f(y) \mathrm{d} y$ (因 $X$ 只取非负 值, $f(y)=0$, 当 $y<0)$. 故

$$
\begin{aligned}
& \int_{0}^{\infty}[1-F(x)] \mathrm{d} x=\int_{0}^{\infty}\left[\int_{0}^{\infty} f(y) \mathrm{d} y-\int_{0}^{x} f(y) \mathrm{d} y\right] \mathrm{d} x \\
= & \int_{0}^{\infty} \int_{x}^{\infty} f(y) \mathrm{d} y \mathrm{~d} x=\int_{0}^{\infty}\left[\int_{0}^{y} \mathrm{~d} x\right] f(y) \mathrm{d} y \\
= & \int_{0}^{\infty} y f(y) \mathrm{d} y=E(X)
\end{aligned}
$$

若 $P(X=k)=p_{k}, k=0,1,2, \cdots$, 则当 $i<x<i+1$ 时. 有 $F(x)=P(X \leqslant x)=P(X=0,1, \cdots, i)=\sum_{j=0}^{i} p_{j}$. 故 $1-F(x)$ $=\sum_{j=i+1}^{\infty} p_{j}$. 因此

$$
\begin{aligned}
& \int_{0}^{\infty}[1-F(x)] \mathrm{d} x=\sum_{i=0}^{\infty} \int_{i}^{i+1} \cdot[1-F(x)] \mathrm{d} x=\sum_{i=0}^{\infty} \sum_{j=i+1}^{\infty} p_{j} \\
& =\left(p_{1}+p_{2}+\cdots\right)+\left(p_{2}+p_{3}+\cdots\right)+\left(p_{3}+\cdots\right)+\cdots \\
& =p_{1}+2 \cdot p_{2}+3 \cdot p_{3}+\cdots=E(X)
\end{aligned}
$$

13. 证明要用到重要的施瓦茨不等式

$$
E\left(X^{2}\right) E\left(Y^{2}\right) \geqslant(E(X Y))^{2}
$$

此实际上在定理 3.1 的 $2^{\circ}$ 中已证明了: 只须把 (3.3) 式中的 $m_{1}$, $m_{2}$ 改为 0 , 则 (3.4) 式即成为此处的 (3) 式. 等号成立的条件为 $X$, $Y$ 有线性关系, 即存在常数 $c$, 使 $Y=c X$ 或 $X=c Y$.

现把 (3) 式用于 $X=\sqrt{X_{2}}, Y=1 / \sqrt{X_{2}}$, 即得 $E\left(\frac{1}{X_{2}}\right) \geqslant$ $\frac{1}{E\left(X_{2}\right)}$. 等号当且仅当有常数 $c$, 使 $\sqrt{X_{2}}=c / \sqrt{X_{2}}$, 即 $X_{2}=$ 常数 $c$. 现因 $X_{1}, X_{2}$ 独立知 $X_{1}, 1 / X_{2}$ 独立, 故

$$
E\left(X_{1} / X_{2}\right)=E\left(X_{1}\right) E\left(1 / X_{2}\right) \geqslant E\left(X_{1}\right) / E\left(X_{2}\right)=1
$$

(因为 $\left.E\left(X_{1}\right)=E\left(X_{2}\right)\right)$ 等乓只在 $X_{1}, X_{2}$ 皆只取一个常数 $c$ 为值 时成立.

14. 令 $Y_{i}=X_{i} /\left(X_{1}+\cdots+X_{n}\right), i=1, \cdots, n$. 则因 $X_{1}, \cdots, X_{n}$ 独立同分布, 易知 $Y_{1}, \cdots, Y_{n}$ 同分布 (不独立). 故 $E\left(Y_{1}\right)=$ $E\left(Y_{2}\right)=\cdots=E\left(Y_{n}\right)$. 但 $Y_{1}+\cdots+Y_{n}=1$, 故 $E\left(Y_{i}\right)=1 / n$.
15. 把次数 $X$ 记为 $X_{\mathrm{I}}+\cdots+X_{n}, X_{i}=1$ 或 0 , 视第 $i$ 次试验 中 $A$ 发生与否而定. 则对两串试验而言, $X_{1}, \cdots, X_{n}$ 都独立, 而分 㭁为

第一串: $P\left(X_{i}=1\right)=p, P\left(X_{i}=0\right)=1-p$

第二串: $P\left(X_{i}=1\right)=p_{i}, P\left(X_{i}=0\right)=1-p_{i}$

对第一串有 $E(X)=p_{1}+\cdots+p_{n}=n p$, 对第二串也有 $E(X)=$ $n p, \cdots$ 者同, 对方差而言, 则

第一串: 为 $\sigma_{1}^{2}=n p(1-p)$

第二串: 为 $\sigma_{2}^{2}=\sum_{i=1}^{n} p_{i}\left(1-p_{i}\right)$

有

$$
\sigma_{1}^{2}-\sigma_{2}^{2}=\sum_{i=1}^{n} p_{i}^{2}-n p^{2}=\sum_{i=1}^{n}\left(p_{i}-p\right)^{2} \geqslant 0
$$

等号当且仅当 $p_{1}=\cdots=p_{n}=p$ 时成立. 直观上.看这结果的解释如下: 如果 $p_{1}+\cdots+p_{n}=n p$ 而 $p_{1}, \cdots$ $p_{n}$ 不相同而较分散,则其中会有一些比 $p$ 更接近 0 或 1 . 而这导 致方差的降低,因为, $p_{i}\left(1-p_{i}\right)$ 当 $p_{i} \approx 0$ 或 1 时很小.

16. 因 $0 \leqslant X \leqslant 1$, 故 $0 \leqslant E(X) \leqslant 1$, 以及 $X^{2} \leqslant X$. 故 $\operatorname{Var}(X)=E\left(X^{2}\right)-E^{2}(X) \leqslant E(X)-E^{2}(X)=E X(1-E X)$ 但函数 $x(1-x)$ 在 $0 \leqslant x \leqslant 1$ 内不超过 $1 / 4$, 而 $0 \leqslant E X \leqslant 1$, 故证明 了 $\operatorname{Var}(X) \leqslant 1 / 4$.

从上面推理可知, 为要成立等号, 有两个条件要满足: $X^{2}=$ $X, E X=1 / 2$. 前一条件决定了 $X$ 只能取 0,1 为值. 后一条件决定 了 $P(X=0)=P(X=1)=1 / 2$. 这是唯一达到等号的情况.

对一般情况 $a \leqslant X \leqslant b$, 可令 $Y=(X-a) /(b-a)$. 则 $0 \leqslant Y$ $\leqslant 1$ 因而 $\operatorname{Var}(Y) \leqslant 1 / 4$. 但 $\operatorname{Var}(X)=(b-a)^{2} \operatorname{Var}(Y)$, 故有 $\operatorname{Var}(X) \leqslant(b-a)^{2} / 4$. 等号只在下述情况成立: $P(X=a)=P(X$ $=b)=1 / 2$.

17. 分别以 $X, Y$ 记二人到达的时间, 则等的时间为 $|X-Y|$. 而平均等待时间为

$$
\begin{gathered}
\int_{0}^{6060}|x-y| / 3600 \mathrm{~d} x \mathrm{~d} y=20 \text { (分钟) } \\
\text { 18. 在计算 } \int_{0}^{\infty}|x-m| f(x) \mathrm{d} x \text { 时分为 } \int_{0}^{m}(m-x) f(x) \mathrm{d} x \\
+\int_{m}^{\infty}(x-m) f(x) \mathrm{d} x . \\
19 . \text { 任取 } a \neq m \text {. 例如 } a<m \text {, 则 } \\
E|X-a|-E|X-m| \\
=\int_{-\infty}^{\infty}[|x-a|-|x-m|] f(x) \mathrm{d} x \\
=\int_{-\infty}^{m}[|x-a|-|x-m|] f(x) \mathrm{d} x \\
+\int_{m}^{\infty}[|x-a|-|x-m|] f(x) \mathrm{d} x
\end{gathered}
$$

在 $-\infty<x \leqslant m$ 内有 $|x-a|-|x-m| \geqslant-m-a$. 故 第一积分 $\geqslant-(m-a) \int_{-\infty}^{m} f(x) \mathrm{d} x \geqslant-\frac{1}{2}(m-a)(m$ 的定 义!) 而在 $m<x<\infty$ 内有 $|x-a|-|x-m|=(m-a)$, 故

$$
\text { 第二积分 }=(m-a) \int_{m}^{\infty} f(x) \mathrm{d} x=\frac{1}{2}(m-a)
$$

![](https://cdn.mathpix.com/cropped/2023_07_12_4b9419d9f76f2c706c45g-8.jpg?height=431&width=596&top_left_y=641&top_left_x=293)

图 5

二 者相加, 得 $E|X-a|$

$-E|X-m| \geqslant 0$. 对 $a>m$ 的情 况也类似处理 (请读者完成).

21. 计算 $Y=X_{1} X_{2}$ 的分布 函数 $F(y)=P(Y \leqslant y)$. 事件 $\{Y$ $\leqslant y\}$ 相应于 $\left(X_{1}, X_{2}\right)$ 落在图 5 中 的区域 $A$ 或 $B$ 内. 因此有

$$
F(y)=\iint_{A} f\left(x_{1}\right) g\left(x_{2}\right) \mathrm{d} x_{1} \mathrm{~d} x_{2}+\iint_{B} f\left(x_{1}\right) g\left(x_{2}\right) \mathrm{d} x_{1} \mathrm{~d} x_{2}
$$

固定 $x_{1}$ 先对 $x_{2}$ 积分,得

$$
\begin{aligned}
F(y)= & \int_{0}^{\infty} f\left(x_{1}\right)\left[\int_{-\infty}^{y / x_{1}} g\left(x_{2}\right) \mathrm{d} x_{2}\right] \mathrm{d} x_{1} \\
& +\int_{-\infty}^{0} f\left(x_{1}\right)\left[\int_{y / x_{1}}^{\infty} g\left(x_{2}\right) \mathrm{d} x_{2}\right] \mathrm{d} x_{1}
\end{aligned}
$$

两边对 $y$ 求导, 得 $Y$ 的密度函数 $h(y)$ 为

$$
h(y)=\int_{0}^{\infty} \frac{1}{x_{1}} f\left(x_{1}\right) g\left(\frac{y}{x_{1}}\right) \mathrm{d} x_{1}-\int_{-\infty}^{0} \frac{1}{x_{1}} f\left(x_{1}\right) g\left(\frac{y}{x_{1}}\right) \mathrm{d} x_{1}
$$

计算 $E(Y)=\int_{-\infty}^{\infty} y h(y) \mathrm{d} y$. 注意当 $x_{1}>0$ 时有

$$
\int_{-\infty}^{\infty} y g\left(\frac{y}{x_{1}}\right) \mathrm{d} y=x_{1}^{2} \int_{-\infty}^{\infty} y g(y) \mathrm{d} y=x_{1}^{2} E\left(X_{2}\right)
$$

而当 $x_{1}<0$ 时有

$$
\int_{-\infty}^{\infty} y g\left(\frac{y}{x_{1}}\right) \mathrm{d} y=-x_{1}^{2} \int_{-\infty}^{\infty} y g(y) \mathrm{d} y=-x_{1}^{2} E\left(X_{2}\right)
$$

因此

$$
\begin{aligned}
E(Y)= & \int_{-\infty}^{\infty} y h(y) \mathrm{d} y=E\left(X_{2}\right)\left(\int_{0}^{\infty} x_{1} f\left(x_{1}\right) \mathrm{d} x_{1}\right. \\
& \left.+\int_{-\infty}^{0} x_{1} f\left(x_{1}\right) \mathrm{d} x_{1}\right)=E\left(X_{2}\right) E\left(X_{1}\right)
\end{aligned}
$$

