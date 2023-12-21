节)

$$
\text { 1. 用公式 }\left(\begin{array}{l}
n \\
0
\end{array}\right)-\left(\begin{array}{l}
n \\
1
\end{array}\right)+\left(\begin{array}{l}
n \\
2
\end{array}\right)-\cdots+(-1)^{n}\left(\begin{array}{l}
n \\
n
\end{array}\right)=0 \text { (见 } 1.2
$$

2. 先用全概率公式得出 $p_{n}$ 的逆推公式

$$
p_{n}=p\left(1-p_{n-1}\right)+(1-p) p_{n-1}
$$

此式推导如下: 若第一次试验 $A$ 发生(概率为 $p$ ), 则剩下 $n-1$ 次

- 364 . 试验应出奇数个 $A$, 概率等于 $1-p_{n-1}$. 若第一次试验中 $A$ 不发 生 (概率为 $1-p$ ), 则剩下 $n-1$ 次试验应出偶数个 $A$, 概率等于 $p_{n-1}$. 又当 $n=1$ 时 $p_{n}=p_{1}=1-p$, 而 $\frac{1}{2}\left[1+(1-2 p)^{n}\right]$ 当 $n=1$ 时也为 $1-p$. 故当 $n=1$ 时正确. 设当 $n-1$ 时正确, 则 $p_{n-1}=$ $\frac{1}{2}\left[1+(1-2 p)^{n-1}\right]$. 以此代人上式, 即得 $p_{n}=\frac{1}{2}[1+(1-$ $2 p)^{n}$ ]. 故当 $n$ 时亦正确.

3. 答案为 $\left(\begin{array}{c}2 n \\ n\end{array}\right) / 2^{2 n}$. 用公式 $\sum_{i=0}^{n}\left(\begin{array}{c}n \\ i\end{array}\right)^{2}=\left(\begin{array}{c}2 n \\ n\end{array}\right)$. 此式可由第一 章(2.5) 式中令 $m=k=n$, 并注意 $\left(\begin{array}{c}n \\ n-i\end{array}\right)=\left(\begin{array}{l}n \\ i\end{array}\right)$ 而得到.
4. 赌博至多在 $2 a-1$ 局结束, 让二人赌 $2 a-1$ 局, 则只要甲 胜 $a$ 局或更多则甲胜, 否则甲败, 故甲胜的概率为 $\sum_{i=a}^{2 a-1} b(i ; 2 a-1$, $p)$. 当 $p=1 / 2$ 时, 由 $b(i ; 2 a-1,1 / 2)=b(2 a-1-i ; 2 a-1$, $1 / 2)$ 即知上式为 $1 / 2$. 另外由二人赌技相同 $(p=1 / 2)$, 及胜负 规则对二人是公平的, 知二人有相同的获胜概率, 即 $1 / 2$.
5. 考察比值

$$
\frac{b(k ; n, p)}{b(k+1 ; n, p)}=\frac{k+1}{n-k} \frac{1-p}{p}
$$

如果 $p \leqslant(n+1)^{-1}$, 则此比值总 $\geqslant 1$. 若 $p \geqslant n /(n+1)$, 则总 $\leqslant 1$. 若 $(n+1)^{-1}<p<n /(n+1)$, 则当 $k$ 小时大于 1 , 从某个 $k$ 开始 则 $\leqslant 1$. 其转折处即达到最大之 $k$. 为 $[(n+1) p]$ ( [ $a]$ 表不超过 $a$ 的最大整数), 当 $(n+1) p$ 不为整数; 为 $(n+1) p$ 及 $(n+1) p-1$ (在这两个值处同时达到最大), 如 $(n+1) p$ 为整数.

6. 以 $p_{i j}$ 记“恰有第 $i, j$ 盒不空, 其余都空”的概率. 先证明所 求概率 $p=\left(\begin{array}{c}12 \\ 2\end{array}\right) p_{12}$. 而后证明

$$
p_{12}=\left(\frac{1}{6}\right)^{10}-2\left(\frac{1}{12}\right)^{10}
$$

“全在 1,2 盒内” 的概率一“全在 1 盒内” 的概率= “全在 2 盒内” 的

## 1. 概率).

7. (a) $p$ 大了, $X$ 取大值的概率上升而取小值的概率下降. 故 $\{X \leqslant k\}$ 的概率当 $p$ 上升时只能下降. (b) 考察一个试验, 有三个 可能的结果: $A_{1}, A_{2}, A_{3}$, 其概率分别为 $p_{1}, p_{2}-p_{1}$ 和 $1-p_{2}$, 记 $A=A_{1}+A_{2}$. 以 $X_{i}$ 记 $n$ 次试验中 $A_{i}$ 发生的次数, $i=1,2$, 则 $X_{1}-$ $B\left(n, p_{1}\right), X_{1}+X_{2}-B\left(n, p_{2}\right)$. 故

$$
\begin{aligned}
P\left(X_{1} \leqslant k\right) & =\sum_{i=0}^{k} b\left(i ; n, p_{1}\right), \\
P\left(X_{1}+X_{2} \leqslant k\right) & =\sum_{i=0}^{k} b\left(i ; n, p_{2}\right)
\end{aligned}
$$

因为当 $X_{1}+X_{2} \leqslant k$ 时必有 $X_{1} \leqslant k$, 故 $P\left(X_{1}+X_{2} \leqslant k\right) \leqslant P\left(X_{1} \leqslant\right.$ $k)$, 即当 $p_{1}<p_{2}$ 时有

$$
\sum_{i=0}^{k} b\left(i ; n, p_{2}\right) \leqslant \sum_{i=0}^{k} b\left(i ; n, p_{1}\right)
$$

(c) 写出 $f(p)=\sum_{i=0}^{k}\left(\begin{array}{l}n \\ i\end{array}\right) p^{i}(1-p)^{n-i}$. 逐项求导数. 注意

$$
\begin{aligned}
& \mathrm{d}\left(\begin{array}{l}
n \\
i
\end{array}\right) p^{i}(1-p)^{n-i} / \mathrm{d} p \\
= & i\left(\begin{array}{l}
n \\
i
\end{array}\right) p^{i-1}(1-p)^{n-i}-(n-i) \cdot\left(\begin{array}{l}
n \\
i
\end{array}\right) p^{i}(1-p)^{n-i-1}
\end{aligned}
$$

令 $i=0,1, \cdots, k$ 相加, 只剩下一项 $-(n-k)\left(\begin{array}{l}n \\ k\end{array}\right) p^{k}(1-p)^{n-k-1}$, 证明它与 $\frac{n !}{k !(n-k-1) !} \int_{0}^{1-p} t^{k}(1-t)^{n-k-1} \mathrm{~d} t$ 的导数同. 又当 $p=1$ 时此积分为 0 , 而 $P(X \leqslant k)$ 也为 $0($ 因 $k<n)$. 故二者必相 等).

8. 由于 $B(2, p)$ 有三个可能值 $0,1,2$, 而 $X_{1}, X_{2}$ 独立同分 布, 故 $X_{1}, X_{2}$ 必都只有 2 个可能值 (否则 $X_{1}+X_{2}$ 的取值个数可 能会小于 3 或大于 3 . 这两个可能值必为 0,1 . 因为, 设可能值为 $a, b, a<b$, 则 $2 a=0,2 b=2, a+b=1$. 记 $p_{1}=P\left(X_{1}=1\right), p_{2}=$ $P\left(X_{2}=1\right)$ 则

$$
p^{2}=P\left(X_{1}+X_{2}=2\right)=P\left(X_{1}=1\right) P\left(X_{2}=1\right)=p_{1} p_{2}
$$

故 $p^{2}=p_{1} p_{2}$ 仿上推理,有

$$
\begin{aligned}
& p^{2}=p_{1} p_{2},(1-p)^{2}=\left(1-p_{1}\right)\left(1-p_{2}\right) \\
& 2 p(1-p)=p_{1}\left(1-p_{2}\right)+\left(1-p_{1}\right) p_{2}
\end{aligned}
$$

由此三式, 不难解出 $p_{1}=p_{2}=p$.

10. (a) 设 $\lambda_{1}<\lambda_{2}, X_{1}, X_{2}$ 独立, 分别服从波哇松分布 $P\left(\lambda_{1}\right)$ 和 $P\left(\lambda_{2}-\lambda_{1}\right)$, 则 $X_{1}+X_{2}$ 服从波哇松分布 $P\left(\lambda_{2}\right)$. 再由 $P\left(X_{1} \leqslant\right.$ $k) \geqslant P\left(X_{1}+X_{2} \leqslant k\right)$ 即推出所要的结果. (b) 写出 $P(X \leqslant k)=$ $\sum_{i=0}^{k} \mathrm{e}^{-\lambda} \lambda^{i} / i !$, 证明其导数等于 $-\mathrm{e}^{-\lambda} \lambda^{k} / k !$. 故 $\frac{1}{k !} \int_{\lambda}^{\infty} t^{k} \mathrm{e}^{-t} \mathrm{~d} t-$ $\sum_{i=0}^{k} \mathrm{e}^{-\lambda} \lambda^{i} / i$ ! 为一常数 $C$ (与 $\lambda$ 无关). 但当 $\lambda \rightarrow 0$ 时, 它趋于 0 , 故 $C=0$.
11. 与第 5 题相似, 考察比 $p_{\lambda}(k) / p_{\lambda}(k+1)$.
12. 直接计算: $P\left(E_{1}\right)=b\left(n ; N, p^{\prime}\right)\left(p^{\prime}=p_{1}\left(1-p_{2}\right)+(1-\right.$ $\left.\left.p_{1}\right) p_{2}\right), P\left(E_{1} E_{2}\right)=\frac{N !}{k !(n-k) !(N-n) !}\left(p_{1}\left(1-p_{2}\right)\right)^{k}((1-$ $\left.\left.p_{1}\right) p_{2}\right)^{n-k}\left(p^{\prime \prime}\right)^{N-n}\left(p^{\prime \prime}=p_{1} p_{2}+\left(1-p_{1}\right)\left(1-p_{2}\right)\right.$, 是 $(A, B)+$ $(\bar{A}, \bar{B})$ 发生的概率), 再算出 $P\left(E_{2} \mid E_{1}\right)=P\left(E_{1} E_{2}\right) / P\left(E_{1}\right)$ 即 得 (注意 $p^{\prime}+p^{\prime \prime}=1$ ). 直接方法: 注意 $P((A, \bar{B}) \mid(A, \bar{B})+(\bar{A}$, $B))=p$. 故在 $E_{1}$ 发生的条件下, $(A, \bar{B})$ 出现的次数 $X$ 的条件分 布, 就是 $B(n, p)$.
13. 把负二项概率 (1.11) 记为 $d(i ; r, p)$. 所要证的结果当 $r$ $=1$ 时对. 设当 $r=k-1$ 时对, 则 $X_{1}+\cdots+X_{k-1}$ 服从分布 $b\langle i$; $k-1, p)$ 把 $X_{1}+\cdots+X_{k}$ 表为 $Y+X_{k}, Y=X_{1}+\cdots+X_{k-1}$. 按上 述归纳假设,及 $Y$ 与 $X_{k}$ 独立, 有

$$
\begin{aligned}
P\left(X_{1}+\cdots+X_{k}=i\right) & =\sum_{j=0}^{i} P(Y=j) P\left(X_{k}=i-j\right) \\
& =\sum_{j=0}^{i} d(j ; k-1, p) p(1-p)^{i-j}
\end{aligned}
$$

为要证此式为 $d(i, k, p)$, 只须证组合等式

$$
\sum_{j=0}^{i}\left(\begin{array}{c}
j+r-2 \\
r-2
\end{array}\right)=\left(\begin{array}{c}
i+r-1 \\
r-1
\end{array}\right)
$$

但此式已在第一章例 2.4 中证过,那里写为形式

$$
\sum_{r=0}^{m}\left(\begin{array}{c}
n-1+r \\
r
\end{array}\right)=\left(\begin{array}{c}
n+m \\
n
\end{array}\right)
$$

令 $n-1=r-2, r=j, m=i$, 并注意 $\left(\begin{array}{c}n-1+r \\ r\end{array}\right)=\left(\begin{array}{c}n-1+r \\ n-1\end{array}\right)$.

一直观上很容易解释, 以 $r=2$ 为

![](https://cdn.mathpix.com/cropped/2023_07_12_b9718b333d6146acf545g-5.jpg?height=109&width=551&top_left_y=959&top_left_x=296)

图 2

例,如图 2, ・表示 $A$ 不发生而 $\times$ 表示 $A$ 发生. 在 $A$ 发生第 2 次时, ·的个数 为 $X_{1}+X_{2}$. 由于各次试验独立, $X_{1}$, $X_{2}$ 必独立且都服从几何分布.

14. $p_{1}=\left(\begin{array}{c}i+r \\ r\end{array}\right) p^{r}(1-p)^{i}, p_{2}=\left(\begin{array}{c}i+r-1 \\ r-1\end{array}\right) p^{r}(1-p)^{i}$. 因为 有 $\left(\begin{array}{c}i+r \\ r\end{array}\right)>\left(\begin{array}{c}i+r-1 \\ r-1\end{array}\right)$ (除非 $\left.i=0\right)$, 故总有 $p_{1}>p_{2}$. 理由很简 单: 计算 $p_{2}$ 时多了一个限制: 最后一次试验 $A$ 必出现, 而算 $p_{1}$ 时, 并无这个限制。
15. 用全概率公式易得

$$
\begin{aligned}
P(Y=k) & =\sum_{n=k}^{\infty} P(X=n) b(k ; n, p) \\
& =\sum_{n=k}^{\infty}\left(\mathrm{e}^{-\lambda} \lambda^{n} / n !\right)\left(\begin{array}{l}
n \\
k
\end{array}\right) p^{k}(1-p)^{n-k} \\
& =\frac{(\lambda p)^{k} \mathrm{e}^{-\lambda}}{k !} \sum_{n=k}^{\infty} \frac{[\lambda(1-p)]^{n-k}}{(n-k) !}
\end{aligned}
$$

而式中的和等于 $\mathrm{e}^{\lambda(1-p)}$.

16. 计算 $P(X+Y \leqslant u)$. 用全概率公式, 并以 $F$ 记 $X$ 的分布 函数, 有

$$
P(X+Y \leqslant u)=P\left(Y=a_{1}\right) P\left(X+a_{1} \leqslant u\right)
$$

$$
\begin{aligned}
& +P\left(Y=a_{2}\right) \cdot P\left(X+a_{2} \leqslant u\right) \\
= & p_{1} F\left(u-a_{1}\right)+p_{2} F\left(u-a_{2}\right)
\end{aligned}
$$

对 $u$ 求导数即得,推广到多于两个值的情况显然.

17. 结果为 $\int_{0}^{\infty} f(w, z / w) w^{-1} \mathrm{~d} w$.
18. 当 $a_{i}$ 中有为 0 的时, 不妨设 $a_{1}=0$. 这时

$$
P(X Y=0) \geqslant P(Y=0)=p_{1}>0
$$

故 $X Y$ 不能有密度函数 (否则应. 用 $P(X Y=0)=0$ ). 如 $a_{i}$ 都不为 0 , 则仿 16 题做, 只须注意

$$
P\left(a_{i} X \leqslant u\right)=\left\{\begin{array}{l}
F\left(u / a_{i}\right), a_{i}>0 \\
1-F\left(u / a_{i}\right), a_{i}<0
\end{array}\right.
$$

$F$ 为 $X$ 的分布函数,二考对 $\dot{u}$ 的导数都是 $\frac{1}{\left|a_{i}\right|} f\left(\frac{u}{a_{i}}\right)$.

19. 记 $F(x)=P(Y \leqslant x)$. 当 $x \leqslant 0$ 时, $F(x)=0$. 若 $x>0$, 则 注意

$$
\begin{aligned}
\{Y \leqslant x\} & =\{\log Y \leqslant \log x\} \\
& =\{(\log Y-a) / \sigma \leqslant(\log x-a) / \sigma
\end{aligned}
$$

故 $F(x)=\Phi((\log x-a) / \sigma)$. 对 $x$ 求导得 $f(x)$.

21. 记 $F(x)=P(Y \leqslant x)$, 则 $F(x)=0$ 当 $x \leqslant-1$, = 1 当 $x \geqslant 1$. 若 $|x|<1$, 则在基本周期 $[0.2 \pi)$ 内, 事件 $\{Y \leqslant x\}$ 等于 $\{$ arc$\cos x \leqslant X \leqslant 2 \pi-\arccos x\}$, 其中 $\arccos x$ 在 $(0, \pi)$ 内, 故

$$
\{Y \leqslant x\}=\sum_{i=-\infty}^{\infty}[2 \pi i+\arccos x \leqslant X \leqslant 2 \pi(i+1)-\arccos x]
$$

于是

$$
\left.F(x)=\sum_{i=-\infty}^{\infty} \Phi(2 \pi(i+1)+\arccos x)-\Phi(2 \pi i-\arccos x)\right]
$$

逐项对 $x$ 求导, 即得 $f(x)$.

22. 注意 $\{Y \leqslant x\}=\prod_{i=1}^{n}\left\{X_{i} \leqslant x\right\}$. 于是得 $Y$ 的分布函数为 $F^{n}(x)$. 对 $Z$, 注意 $\{Z \geqslant x\}=\prod_{i=1}^{n}\left\{X_{i} \geqslant x\right\}$. 于是 $P(Z \leqslant x)=$ $1-P(Z \geqslant x)=1-(1-F(x))^{n}$. 对 $x$ 求导得密度函数.
23. 直接证明, 只须注意本题 $F(x)=x / \theta(0 \leqslant x \leqslant \theta)$, 而 $f(x)=1 / \theta(0 \leqslant x \leqslant \theta)$, 其外为 0$)$. 直观看法: $\theta-\max \left(X_{1}, \cdots\right.$, $\left.X_{n}\right)$ 为 $X_{1}, \cdots, X_{n}$ 的最右点与边界 $\theta$ 的距离. 而 $\min \left(X_{1}, \cdots, X_{n}\right)$ 是 $X_{1}, \cdots, X_{n}$ 的最左点与边界 0 的距离.二者性质一样只是看的

![](https://cdn.mathpix.com/cropped/2023_07_12_b9718b333d6146acf545g-7.jpg?height=454&width=440&top_left_y=670&top_left_x=337)

图 3 方向不同. 由于均匀分布对区间内各处 一视同仁, 这两个距离的概率分布应当 一样。

24. 考察事件 $\left\{Y_{1} \leqslant u, Y_{2} \leqslant v\right\}$. 看 图 3,OA 为第一象限分角线, $A$ 点的坐 标为 $(u, u), O B$ 和 $O E$ 之长都为 $v$, 而 $O B C A$ 和 $O E D A$ 都是平行四边形, 稍加 思考即不难发现。

$\left\{Y_{1} \leqslant u, Y_{2} \leqslant v\right\}=\left\{\left(X_{1}, X_{2}\right)\right.$ 落在上述两个平行四边形内 $\}$. 故

$$
\begin{aligned}
P\left\{Y_{1} \leqslant u, Y_{2} \leqslant v\right\}= & \int_{O B S A}^{n} \mathrm{e}^{-x_{1}-x_{2}} \mathrm{~d} x_{1} \mathrm{~d} x_{2} \\
& +\iint_{O E D A} \mathrm{e}^{-x_{1}-x_{2}} \mathrm{~d} x_{1} \mathrm{~d} x_{2}
\end{aligned}
$$

由对称性, 这两积分之值同, 用累积分法算第一个积分 (先固定 $x_{1}$ 对 $x_{2}$ 积), 不难得出上述两积分之和为 $\left(1-\mathrm{e}^{-2 u}\right)\left(1-\mathrm{e}^{-z^{\prime}}\right)$. 由此 证明了题中的所有结论.

25. 用归纳法, 先肯定: 当 $n=0$ 时, 不论 $T>0$ 取什么值, $P(X=0)=\mathrm{e}^{-\lambda T}$ 成立. 这很明显, 因为 $X=0$ 意味着最初那个元件 的寿命 $\geqslant T$, 其概率 $\int_{T}^{\infty} \lambda \mathrm{e}^{-\lambda t} \mathrm{~d} t=\mathrm{e}^{-\lambda T}$.

现假定公式 $P(X=n)=\mathrm{e}^{-\lambda T}(\lambda T)^{n} / n !$ 对 $n=k-1$ 成立, 而计算 $P(X=k)$. 以 $x_{1}$ 记第一次替换发生的时刻, 则在给定 $X_{1}$ 的条件下, 在时段 $\left(X_{1}, T\right)$ 内要发生 $k-1$ 替换. 这时段之长为 $T-x_{1}$. 按归纳假设,在这段时间内恰好替换 $k-1$ 次的概率, 为 $\mathrm{e}^{-\lambda\left(T-x_{1}\right)}\left(\lambda\left(T-x_{1}\right)\right)^{k-1} /(k-1)$ ! 由于 $X_{1}$ 只能在 $(0, T)$ 内且 其概率密度为 $\lambda \mathrm{e}^{-\lambda x_{1}}$, 故

$$
P(X=k)=\int_{0}^{T} \lambda \mathrm{e}^{-\lambda x_{1}} \mathrm{e}^{-\lambda\left(T-x_{1}\right)}\left(\lambda\left(T-x_{1}\right)\right)^{k-1} \mathrm{~d} x_{1} /(k-1) !
$$

易见此积分为 $\mathrm{e}^{-\lambda T}(\lambda T)^{k} / k$ !, 于是证明了公式当 $n=k$ 时成立, 而完成了归纳证明.

27. 用公式 (4.10) 算出 $(X+b Y, X-b Y)$ 的联合密度 $g(u$, $v)$. 再决定 $b$, 使这联合密度可拆成两个函数 $g_{1}(u)$ 和 $g_{2}(v)$ 之 积,答案: $b=\sigma_{1} / \sigma_{2}$. 此题有其他简单方法, 见第三章习题.
28. 设 $X_{1}, \cdots, X_{k}, Y_{1}, \cdots, Y_{n}$ 独立同分布, 各服从标准正态 分布 $N(0,1)$. 记

$$
\begin{aligned}
& Z_{1}=\frac{1}{k} \sum_{i=1}^{k} X_{i}^{2} / \frac{1}{n} \sum_{i=1}^{n} Y_{i}^{2}, \quad Z_{2}=\sum_{i=1}^{k} X_{i}^{2} / \frac{1}{n} \sum_{i=1}^{n} Y_{i}^{2} \\
& Z_{3}=X_{1}^{2} / \frac{1}{n} \sum_{i=1}^{n} Y_{i}^{2}
\end{aligned}
$$

则 $Z_{1} \sim F_{k, n}, Z_{3} \sim F_{1, n}, Z_{2} \geqslant Z_{3}$. 今有

$$
P\left(Z_{1} \geqslant F_{k, n}(\alpha)\right)=\alpha
$$

故有: $P\left(Z_{2} \geqslant k F_{k, n}(\alpha)\right)=\alpha$,另一方面, 又有

$$
P\left(Z_{1} \geqslant F_{1, n}(\alpha)\right)=\alpha
$$

由这两式,及 $Z_{2} \geqslant Z_{1}$, 即得 $k F_{k, n}(\alpha) \geqslant F_{1, n}(\alpha)$.

30. 易见 $\iint_{x^{2}+y^{2} \leqslant 1} x y \mathrm{~d} x \mathrm{~d} y=0$. 故为证明 $g$ 是密度函数, 只 须证明它非负. 但 $|x y|$ 在 $x^{2}+y^{2} \leqslant 1$ 内的最大值小于 1 , 而 $f(x$, $y$ ) 在 $x^{2}+y^{2} \leqslant 1$ 内的最小值为 $\mathrm{e}^{-1 / 2} / 2 \pi>1 / 100$. 故知 $g$ 非负. 后一结论易证，因为对任何 $a>0$ 有 $\int_{-a}^{a} x \mathrm{~d} x=0$.
