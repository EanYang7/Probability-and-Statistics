---
comments: true
tags:
  - 校订中……
---
# 练习
<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/2/exercises.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/2/exercises.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/2/exercises.pdf">下载 PDF</a>.</p>
    </embed>
</object>
1. 某事件 $A$ 在一次试验中发生的概率为 $1 / 2$. 将试验独立地重复 $n$ 次. 证明: “ $A$ 发生偶数次” 的概率为 $1 / 2$, 不论 $n$ 如何 ( 0 算偶数).

- 104 . 2. 在上题中,若 $A$ 在一次试验中发生的概率为 $p$, 则 “ $A$ 发生偶数次” 的 概率为 $p_{n}=\frac{1}{2}\left[1+(1-2 p)^{n}\right]$. 用归纳法.

3. 两人分别各拿一个均匀铜板投搓 $n$ 次 (每次搓出正、反面的概率都是 1/2). 问: “两个郑出的正面数相同” 这事件的概率是多少?
4. 甲、乙二人赌博. 每局甲胜的概率为 $p$, 乙胜的概率为 $q=1-p$. 约 定: 赌到有人胜满 $a$ 局为止, 到这时即算他获胜. (a) 求甲胜的概率. (b) 若 $p$ $=1 / 2$, 用 (a) 的结果以及用直接推理, 证明甲胜的概率为 $1 / 2$.
5. 以 $b(k ; n, p)$ 记二项分布概率 $\left(\begin{array}{l}n \\ k\end{array}\right) p^{k}(1-p)^{n-k}$. 证明: (a) 若 $p \leqslant 1$ $(n+1)$, 则当 $k$ 增加时 $b(k ; n, p)$ 非增. (b) 若 $p \geqslant 1-1 /(n+1)$, 则当 $k$ 增加 时 $b(k ; n, p)$ 非降. (c) 若 $1 /(n+1)<p<1-1 /(n+1)$, 则当 $k$ 增加时, $b(k ; n, p)$ 先增后降. 求使 $b(k ; n, p)$ 达到最大的 $k$.

6.10 个球随机地放进 12 个盒子中, 问: “空盒 (不含球的盒) 数目为 10 ” 这事件的概率是多少?

7. 设随机变量 $X$ 服从二项分布 $B(n, p), k$ 为小于 $n$ 的非负整数, 记 $f$ $(p)=P(X \leqslant k)$.

(a) 用直观说理的方法指明: $f(p)$ 随 $p$ 增加而下降.

(b) 用概率方法证明 (a) 中的结果.

(c) 建立恒等式

$$
f(p)=\frac{n !}{k !(n-k-1) !} \int_{0}^{1-p} t^{k}(1-t)^{n-k-1} \mathrm{~d} t
$$

从湍用分析方法证明了 (a)中之结论.

8. 设随机变量 $X_{1}, X_{2}$ 独立同分布,而 $X_{1}+X_{2}$ 服从二项分布 $B(2, p)$. 则 $X_{1}, X_{2}$ 都服从二项分布 $B(1, p)$ (即 $P\left(X_{1}=1\right)=p, p\left(X_{1}=0\right)=1-p$ ), 若只假定 $X_{1}, X_{2}$ 独立且都只取 0,1 为值,这结论也对.
9. 在超几何分布 (1.10) 中固定 $n, m$, 令 $N \rightarrow \infty, M \rightarrow \infty$ 但 $M / N \rightarrow p, 0$ $\leqslant p \leqslant 1$. 证明: $(1.10)$ 以 $b(m ; n, p)$ 为极限.
10. 设随机变量 $X$ 服从波哇松分布 $P(\lambda) . k$ 为正整数.

(a) 用概率方法证明: $P(X \leqslant k)$ 随 $\lambda$ 增加而下降.

(b) 建立恒等式

$$
P(X \leqslant k)=\frac{1}{k !} \int_{\lambda}^{\infty} t^{k} \mathrm{e}^{-t} \mathrm{~d} t
$$

从而用分析方法证明 (a) 中之结论. 11. 记 $p_{\lambda}(k)=\mathrm{e}^{-\lambda} \lambda^{k} / k$ ! 证明 : (a) 若 $\lambda \leqslant 1$, 则 $p_{\lambda}(k)$ 随 $k$ 增加而非增. (b) 若 $\lambda>1$, 则 $p_{\lambda}(k)$ 先增后降，找出使 $p_{\lambda}(k)$ 达到最大的 $k$.

12. 有一个大试验由两个独立的小试验构成. 在第一个小试验中, 观察 某事件 $A$ 是否发生, $A$ 发生的概率为 $p_{1}$; 在第二个小试验中, 观察某事件 $B$ 是否发生, $B$ 发生的概率为 $p_{2}$. 故这个大试验有 4 个可能结果: $(A, B)$, $(\bar{A}, \bar{B}),(A, \bar{B}),(\bar{A}, B)$. 把这大试验重复 $N$ 次.记

$$
\begin{aligned}
& E_{1}=\{(A, \bar{B}),(\bar{A}, B) \text { 总共发生 } n \text { 次 }\} \\
& E_{2}=\{((A, \bar{B}) \text { 发生 } k \text { 次 }\}
\end{aligned}
$$

计算条件概率 $P\left(E_{2} \mid E_{1}\right)$, 证明它等于 $b(k ; n, p)$, 其中 $p=p_{1}\left(1-p_{2}\right) /\left[p_{1}\right.$ $\left.\left(1-p_{2}\right)+\left(1-p_{1}\right) p_{2}\right]$, 并用直接方法 (不通过按条件概率公式计算) 证明这 个结果.

13. 设 $X_{1}, \cdots, X_{r}$ 独立同分布, 其公共分布为几何分布 (1.12). 用归纳法 证明: $X_{1}+\cdots+X_{r}$ 服从负二项分布 (1.11). 又: 对这个结果作一直观上的解 释, 因而得出一简单证法.
14. 在一串独立试验中观察某事件 $A$ 是否发生, 每次 $A$ 发生的概率都 是 $p$. 有以下两个概率: (1) $p_{1}=$ 做 $i+r$ 次试验, $A$ 出现 $r$ 次的概率. (2) $p_{2}=$ 做试验直到 $A$ 出现 $r$ 次为止, 到此时 $A$ 有 $i$ 次不出现的概率.二者都是做 $i$ $+r$ 次而 $A$ 出现 $r$ 次, 但总有 $p_{1}>p_{2}$. 证明这一事实并给一解释.
15. 先观察一个服从波哇松分布 $P(\lambda)$ 的随机变量之值 $X$, 然后做 $X$ 次 独立试验, 在每次试验中某事件 $A$ 发生的概率为 $p$. 以 $Y$ 记在这 $X$ 次试验中 $A$ 发生的次数,证明: $Y$ 服从波哇松分布 $P(\lambda p)$.
16. 设随机变量 $X, Y$ 独立, $X$ 有概率密度 $f(x)$, 而 $Y$ 为离散型, 只取 两个值 $a_{1}$ 和 $a_{2}$, 概率分别为 $p_{1}$ 和 $p_{2}$. 证明: $X+Y$ 有概率密度 $h(x)$ :

$$
h(x)=p_{1} f\left(x-a_{1}\right)+p_{2} f\left(x-a_{2}\right)
$$

把这个结果推广到 $Y$ 取任意有限个值以至无限个值 (但仍为离散型) 的情 况。

17. 设 $X, Y$ 独立, 各有概率密度函数 $f(x)$ 和 $g(y)$, 且 $X$ 只取大于 0 的值. 用以下两种方法计算 $Z=X Y$ 的概率密度, 并证明结果一致:

(a) 利用变换 $Z=X Y, W=X$.

(b) 把 $X Y$ 表为 $Y / X^{-1}$. 先算出 $X^{-1}$ 的密度, 再用商的密度公式 $(4.29)$.

18. 设 $X, Y$ 独立, $X$ 有概率密度 $f(x), Y$ 为离散型, 其分布为.

$$
P\left(X=a_{i}\right)=p_{i}, i=1,2, \cdots, p_{i}>0, i=1,2, \cdots
$$

证明: 若 $a_{1}, a_{2}, \cdots$ 都不为 0 , 则 $X Y$ 有密度函数

$$
h(x)=\sum_{i=1}^{\infty} p_{i}\left|a_{i}\right|^{-1} f\left(x / a_{i}\right)
$$

若 $a_{1}, a_{2}, \cdots$ 中有为 0 的, 则 $X Y$ 没有概率密度函数.

19. 设 $Y$ 为只取正值的随机变量, 且 $\log Y$ 服从正态分布 $N\left(a, \sigma^{2}\right)$. 求 $Y$ 的密度函数 ( $Y$ 的分布称为对数正态分布).

20 . 设 $X$ 服从自由度为 $n$ 的 $t$ 分布, 而 $Y=X / \sqrt{a+X^{2}}$, 其中 $a>0$ 为 常数, 试求 $Y$ 的密度函数.

21. 设 $X \sim N(0,1), Y=\cos X$, 求 $Y$ 的密度函数.
22. 设 $X_{1}, \cdots, X_{n}$ 独立同分布, $X_{1}$ 有分布函数 $F(x)$ 和密度函数 $f(x)$. 记

$$
Y=\max \left(X_{1}, \cdots, X_{n}\right), Z=\min \left(X_{1}, \cdots, X_{n}\right)
$$

证明: $Y, Z$ 分别有概率密度函数 $n F^{n-1}(x) f(x)$ 和 $n[1-F(x)]^{n-1} \cdot f(x)$.

23. 续上题, 若 $F(X)$ 为 $[0, \theta]$ 上的均匀分布 ( $\theta>0$ 为常数). 用上题结果 证明: $\theta-\max \left(X_{1}, \cdots, X_{n}\right)$ 与 $\min \left(X_{1}, \cdots, X_{n}\right)$ 的分布相同, 并从对称的观点 对这个结果作一直观的解释.
24. 设 $X_{1}, X_{2}$ 独立同分布, 其公共密度为

$$
f(x)= \begin{cases}\mathrm{e}^{-x}, & x>0 \\ 0, & x \leqslant 0\end{cases}
$$

记 $Y_{1}=\min \left(X_{1}, X_{2}\right), Y_{1}=\max \left(X_{1}, X_{2}\right)-\min \left(X_{1}, X_{2}\right)$. 证明: $Y_{1}$ 与 $Y_{2}$ 独 立, $Y_{1}$ 的分布与 $X_{1} / 2$ 的分布同, $Y_{2}$ 的分布与 $X_{1}$ 同 (直接计算概率 $P\left(Y_{1}\right.$ $\left.\left.\leqslant u, Y_{2} \leqslant u\right)\right)$.

25. 一大批元件其寿命服从指数分布 (1.21). 固定一个时间 $T>0$. 让一 个元件从时刻 0 开始工作. 每当这元件坏了马上用一个新的替换之. 以 $X$ 记 到时刻 $T$ 为止的替换次数. 证明: $X$ 服从波哇松分布 $P(\lambda T)$, 即 $P(X=n)=$ $\mathrm{e}^{-\lambda T n} / n$ ! (用归纳法, 详见提示).
26. 证明 $F_{m, n}(a)=F_{n, m}(1-a), 0<a<1$.
27. 设 $(X, Y)$ 服从二维正态分布 $N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho\right)$. 证明: 必存在常数 $b$, 使 $X+b Y$ 与 $X-b Y$ 独立.
28. 设 $(X, Y)$ 有密度函数

$$
f(x, y)= \begin{cases}\frac{c}{1+x^{2}+y^{2}}, & \text { 当 } x^{2}+y^{2} \leqslant 1 \\ 0, & \text { 当 } x^{2}+y^{2}>1\end{cases}
$$

(a) 求出常数 $c$. (b)算出 $X, Y$ 的边缘分布密度,并证明 $X, Y$ 不独立.

29. 证明: 对任何自然数 $k, n$ 及 $0<a<1$, 有

$$
k F_{k, n}(a) \geqslant F_{1, n}(a)
$$

(实际成立严格不等号).

30. 设 $X, Y$ 独立,都服从标准正态分布 $N(0,1)$, 以 $f(x, y)$ 记 $(X, Y)$ 的联合密度函数。证明:函数

$$
g(x, y)= \begin{cases}f(x, y)+x y / 100, & \text { 当 } x^{2}+y^{2} \leqslant 1 \\ f(x, y), & \text { 当 } x^{2}+y^{2}>1\end{cases}
$$

是二维概率密度函数. 若随机向量 $(U, V)$ 有密度函数 $g(x, y)$, 证明: $U, V$ 都服从标准正态分布 $N(0,1)$, 但 $(U, V)$ 不服从二维正态分布:

本例说明: 由各分量为正态推不出联合分布为正态.
