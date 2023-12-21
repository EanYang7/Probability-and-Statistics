---
comments: true
tags:
  - 校订中……
---
# 答案
<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/6/answers.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/6/answers.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/6/answers.pdf">下载 PDF</a>.</p>
    </embed>
</object>
# 第六章 

1. 记 $S^{2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}, S_{1}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}$

$$
\begin{aligned}
\sum_{i=1}^{n} & \left(Y_{i}-\alpha_{0}-\alpha_{1}\left(X_{i}-\bar{X}\right)\right)^{2} \\
& =S^{2} \alpha_{1}^{2}-2 S^{1} \alpha_{1}+n \alpha_{0}^{2}-2 n \bar{Y} \alpha_{0}+\sum_{i=1}^{n} Y_{i}^{2} \\
& =\left(S \alpha_{1}-S_{1} / S\right)^{2}+n\left(\alpha_{0}-\bar{Y}\right)^{2}
\end{aligned}
$$

$$
+\sum_{i=1}^{n} Y_{i}^{2}-n \bar{Y}^{2}-S_{1}^{2} / S^{2}
$$

由此立即看出此平方和之最小值在 $\alpha_{0}=\bar{Y}=\hat{\beta}_{0}$ 和 $\alpha_{1}=S_{1} / S^{2}=$ $\hat{\beta}^{1}$ 处达到, 且最小值为

$$
\begin{aligned}
\sum_{i=1}^{n} \delta_{i}^{2} & =\sum_{i=1}^{n} Y_{i}^{2}-n \bar{Y}^{2}-S_{1}^{2} / S^{2} \\
& =\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}-S_{1}^{2} / S^{2} \\
& =\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}-\hat{\beta}_{1} S_{1}
\end{aligned}
$$

即(2.23) 式, 这个证明不仅简单, 还有一个好处, 即它确实肯定了 达到最小值. 用偏导数方法, 理论上还有一个验证方程组 (2.10), (2.11) 的解确实是最小值点的问题.

2. (a)利用 $\hat{\beta}_{0}, \hat{\beta}_{1}$ 的无偏性, 因为

$$
\begin{aligned}
\delta_{i} & =Y_{i}-\hat{Y}_{i}=\beta_{0}+\beta_{1}\left(X_{i}-\bar{X}\right)+e_{i}-\left(\hat{\beta}_{0}+\hat{\beta}_{1}\left(X_{i}-\bar{X}\right)\right) \\
& =\left(\beta_{0}-\hat{\beta}_{0}\right)+\left(\beta_{1}-\hat{\beta}_{1}\right)\left(X_{i}-\bar{X}\right)+e_{i}
\end{aligned}
$$

且 $E\left(e_{i}\right)=0$, 即得 $E\left(\delta_{i}\right)=0$.

(b) 这是因为, 在 $(2.10)$ 式中把 $a_{0}, a_{1}$ 分别换成其解 $\hat{\beta}_{0}, \hat{\beta}_{1}$, 得到 $\delta_{1}+\cdots+\delta_{n}=0, \delta_{1}+\cdots+\delta_{n}$ 之间既然有这样一个函数关系, 它不可能是相互独立的.

(c) 在证明 $(2.21)$ 式的过程中已得出

$$
\delta_{i}=e_{i}-\bar{e}-t_{i} \sum_{j=1}^{n} t_{j} e_{j} / S^{2} \quad\left(t_{j}=X_{j}-\bar{X}, \bar{e}=\sum_{j=1}^{n} e_{j} / n\right)
$$

又由 (a) 有 $E\left(\delta_{i}\right)=0\left(E\left(\delta_{i}\right)=0\right.$ 也直接由上式得出 $)$, 故

$$
\operatorname{Var}\left(\delta_{i}\right)=E\left(\delta_{i}^{2}\right)=E\left(e_{i}-\bar{e}\right)^{2}+t_{i}^{2} S^{-4} E\left(\sum_{j=1}^{n} t_{j} e_{j}\right)^{2}
$$

$$
-2 t S^{-2} E\left(\sum_{j=1}^{n} t_{j} e_{i} e_{j}\right)-2 t_{i} S^{-2} E\left(\sum_{j=1}^{n} t_{j} \bar{e} e_{j}\right)
$$

注意到 $E\left(e_{i}-\bar{e}\right)^{2}=E\left(e_{i}^{2}\right)+E\left(\bar{e}^{2}\right)-2 E\left(e_{i} \bar{e}\right)=\sigma^{2}+\sigma^{2} / n-$ $2 \sigma^{2} / n=\sigma^{2}-\sigma^{2} / n=(1-1 / n) \sigma^{2}$, 以及

$$
\begin{aligned}
& E\left(\sum_{j=1}^{n} t_{j} e_{j}\right)^{2}=\sigma^{2} \sum_{j=1}^{n} t_{j}^{2}=\sigma^{2} S^{2}, E\left(\sum_{j=1}^{n} t_{j} e_{i} e_{j}\right)=t_{i} \sigma^{2}, \\
& E\left(\sum_{j=1}^{n} t_{j} \bar{e} e_{j}\right)=\sum_{j=1}^{n} t_{j} \sigma^{2} / n=0
\end{aligned}
$$

代人(2) 式即得所要证的结果.

注: 由这个结果, 得

$$
\begin{aligned}
E\left(\sum_{i=1}^{n} \delta_{i}^{2}\right)=\sum_{i=1}^{n} E\left(\delta_{i}^{2}\right) & =\sum_{i=1}^{n}\left[1-\frac{1}{n}-\left(X_{i}-\bar{X}\right)^{2} / S^{2}\right] \sigma^{2} \\
& =(n-2) \sigma^{2}
\end{aligned}
$$

因而得到 $\sum_{i=1}^{n} \delta_{i}^{2} /(n-2)$ 为 $\sigma^{2}$ 的无偏估计的另一证明.

(d) 与 (1) 式类似写出 $\delta_{j}$ 的表达式, 注意 $\operatorname{Cov}\left(\delta_{i}, \delta_{j}\right)=E$ $\left(\delta_{i} \delta_{j}\right)$, 把两式相乘逐项求均值, 与 $(c)$ 完全类似地得到所要的结 果.

3. 考虑线性回归模型

$$
Y=\alpha_{0}+\alpha_{1} x+e, \alpha_{0}=a, \alpha_{1}=b-a
$$

其中 $e-N\left(0, \sigma^{2}\right)$. 在 $X=0$ 点重复观察 $n$ 次, 其 $Y$ 值记为 $X_{1}$, $\cdots, X_{n}$; 在 $X=1$ 点重复观察 $m$ 次, 其 $Y$ 值记为 $Y_{1}, \cdots, Y_{m}$. 这样 按模型 $(3), X_{1}, \cdots, X_{n} \sim N\left(a, \sigma^{2}\right), Y_{1}, \cdots, Y_{m} \sim N\left(b, \sigma^{2}\right)$, 如题 中所设者. 然自模型 (3) 观之, 估计 $b-a$ 相当于估计回归系数 $a_{1}$, 检验亦然. 而此处的平方和 (2.9) 为 $\sum_{i=1}^{n}\left(X_{i}-a_{0}\right)^{2}+\sum_{j=1}^{m}\left(Y_{j}-a_{0}\right.$ $\left.-a_{1}\right)^{2}$, 直接得出 $a_{0}, a_{1}$ 的最小二乘估计为 $\bar{X}$ 和 $\bar{Y}-\bar{X}$. 后者即 $b-a$ 的估计. 残差平方和为 $\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}+\sum_{j=1}^{m}\left(Y_{j}-\bar{Y}\right)$. 自由 度 $m+n-2$. 又此处之 $S^{2}\left(S^{2}\right.$ 即 (2.16) 式中的 $\left.S_{x}^{2}\right)$ 为 (注意自变 量值中 $n$ 个 0 和 $m$ 个 1 , 其平均为 $m /(n+m))$

$$
\begin{aligned}
S^{2} & =n(0-m /(n+m))^{2}+m(1-m /(n+m))^{2} \\
& =n m /(n+m)
\end{aligned}
$$

由此,按 (2.26) 式求 $\alpha_{1}=b-a$ 的区间估计, 所得结果与两样本 $t$ 区间估计一致。

4. 将平方和 $\sum_{i=1}^{n}\left(Y_{i}-b X_{i}\right)^{2}$ 按第 1 题的方式处理: $\sum_{i=1}^{n}\left(Y_{i}-\right.$ $\left.b X_{i}\right)^{2}=S_{0}^{2} b^{2}-2 S_{01} b+\sum_{i=1}^{n} Y_{i}^{2}=\left(S_{0} b-S_{01} / S_{0}\right)^{2}+\sum_{i=1}^{n} Y_{i}^{2}-$ $S_{01}^{2} / S_{0}^{2}$, 此处 $S_{0}^{2}=\sum_{i=1}^{n} X_{i}^{2}, S_{01}=\sum_{i=1}^{n} X_{i} Y_{i}$. 由此式立即得出 $b$ 的最 小二乘估计 为

$$
\hat{b}=S_{01} / S_{0}^{2}=\sum_{i=1}^{n} X_{i} Y_{i} / \sum_{i=1}^{n} X_{i}^{2}
$$

而残差平方和为 $\sum_{i=1}^{n} Y_{i}^{2}-S_{01}^{2} / S_{0}^{2}$, 暂记为 $R$. 由于

$$
\begin{aligned}
E\left(Y_{i}^{2}\right) & =\left(E Y_{i}\right)^{2}+\operatorname{Var}\left(Y_{i}\right)=b^{2} X_{i}^{2}+\sigma^{2} \\
E\left(S_{01}^{2}\right) & =\left(E S_{01}\right)^{2}+\operatorname{Var}\left(S_{01}\right) \\
& =\left(\sum_{i=1}^{n} b X_{i}^{2}\right)^{2}+\sum_{i=1}^{n} X_{i}^{2} \sigma^{2}=b^{2} S_{0}^{4}+\sigma^{2} S_{0}^{2}
\end{aligned}
$$

得到

$$
\begin{aligned}
E(R) & =\sum_{i=1}^{n}\left(b^{2} X_{i}^{2}+\sigma^{2}\right)-\left(b^{2} S_{0}^{4}+\sigma^{2} S_{0}^{2}\right) / S_{0}^{2} \\
& =n \sigma^{2}+b^{2} S_{0}^{2}-b^{2} S_{0}^{2}-\sigma^{2}=(n-1) \sigma^{2}
\end{aligned}
$$

因而证明了 $R /(n-1)$ 是 $\sigma^{2}$ 的无偏估计.

(c) 只须作一个正交变换

$$
\left(\begin{array}{c}
Z_{1} \\
\vdots \\
Z_{n}
\end{array}\right)=A\left(\begin{array}{c}
Y_{1} \\
\vdots \\
Y_{n}
\end{array}\right)
$$

其中 $A$ 为正交方阵, 第一行是 $\left(X_{1} / S_{0}, \cdots, X_{n} / S_{0}\right)$. 则 $R=Z_{2}^{2}+$ $\cdots+Z_{n}^{2}$, 其中 $Z_{2}, \cdots, Z_{n}$ 独立同分布且有公共分布 $N\left(0, \sigma^{2}\right)$.

5. 若 $c_{1}=0$, 则因 $b$ 的区间估计问题已解决了, $c_{2} b$ 当然直接 由之得出. 若 $c_{1} \neq 0$, 把 $c_{1} a+c_{2} b$ 表为 $c_{1}(a+x b)\left(x=c_{2} / c_{1}\right)$, 即 $c_{1} m(x)$. 因 $m(x)$ 的区间估计已在 (2.27) 式的基础上求得,故问 题得到解决.
6. (a) 取 $i=1$ 来讨论, 因为把 $X_{1}, \cdots, X_{n}$ 作线性变换 $X_{i}^{\prime}=$ $a X_{i}+b(a \neq 0)$ 不影响 $\left(X_{1}-\bar{X}\right)^{2} / \sum_{j=1}^{n}\left(X_{j}-\bar{X}\right)^{2}$ 之值, 不妨设 $\bar{X}=0, X_{1}=1$. 这时, 为使上述比值最大, 应在 $X_{2}+\cdots+X_{n}=-1$ 的约束下, 使 $X_{2}^{2}+\cdots+X_{n}^{2}$ 达到最小. 但易知后者的最小值在 $X_{2}=\cdots=X_{n}=-\frac{1}{n-1}$ 时达到, 最小值为 $\frac{1}{n-1}$. 故所述比值不能 大于 $1 /\left(1+\frac{1}{n-1}\right)=1-\frac{1}{n}$, 等号当且仅当对某个 $i$, 有 $X_{1}=\cdots=$ $X_{i-1}=X_{i+1}=\cdots=X_{n} \neq X_{i}$.

(b) 分两种情况: 若 $\bar{X}_{n}$ 保持有界, 则因 $S_{n}^{2} \rightarrow \infty$, 就有 $(a-$ $\left.\bar{X}_{n}\right)^{2} / S_{n}^{2} \rightarrow 0$. 若 $\left|\bar{X}_{n}\right| \rightarrow \infty$, 则注意到

$$
\left(a-\bar{X}_{n}\right)^{2} / S_{n}^{2} \leqslant\left(a-\bar{X}_{n}\right)^{2} / \sum_{i=1}^{m}\left(X_{i}-\bar{X}_{n}\right)^{2}, m \leqslant n
$$

固定 $m$, 令 $n \rightarrow \infty$. 因为 $\left|\bar{X}_{n}\right| \rightarrow \infty$, 上式右端有极限 $1 / m$. 因 $m$ 可取得任意大, 知 $\left(a-\bar{X}_{n}\right)^{2} / S_{n}^{2}$ 的极限可任意小, 故只能为 0 (若 $\left|\bar{X}_{n}\right|$ 既不有界也不随 $n \rightarrow \infty$ 而趋于无穷, 则通过抽取子序列的方 法去讨论).

(c) 先给出一个预备事实: 在 $[0,1]$ 上给出三个数 $x, c-x(0$ $\leqslant c \leqslant 1)$ 及 $a$, 记 $I=(x-a)^{2}+(c-x-a)^{2}$, 则总可以改变 $x$ 之 值以增大 $I$, 使 $x, c-x$ 都仍在 $[0,1]$ 上, 且 $x$ 及 $c-x$ 中至少有一 个为 0 或 1. 如 $x$ 和 $c-x$ 分处 $a$ 的两边, 这一点很清楚. 若同在一 边, 例如 $0<x \leqslant c-x \leqslant a$, 则 $\mathrm{d} I / \mathrm{d} x=4 x-2 c \leqslant 0$ (因 $x \leqslant c-x$, $2 x \leqslant c$ ). 故让 $x$ 下降能增大 $I$. 让 $x$ 降为 0 (这时 $c-x$ 升为 $c$, 仍 在 $[0,1]$ 上) 即可. 现证明本题,不失普遍性可设区间 $[A, B]$ 为 $[0,1]$. 证明分三 段: $1^{\circ}$ 为使 $S^{2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$ 最大, 诸 $X_{i}$ 中至多只能有一个非 0 非 1.,因为, 若有两个, 例如 $X_{1}, X_{2}$ ，非 0 非 1 . 则据上述预备知 识, 可以在不改变 $X_{3}, \cdots, X_{n}$ 和 $\bar{X}$ 的条件下, 使 $X_{1}, X_{2}$ 中至少有 一个为 0 或 1 , 而 $\left(X_{1}-\bar{X}\right)^{2}+\left(X_{2}-\bar{X}\right)^{2}$ 增大, 即 $S^{2}$ 增大. $2^{\circ}$ 现 设 $X_{1}, \cdots, X_{n}$ 中, 有 $n_{0}$ 个为 $0, n_{1}$ 个为 1 , 还有一个为 $a, 0 \leqslant a \leqslant$ 1 . 证明: 总可以把 $a$ 改为 0 或 1 以增大 $S^{2}$. 此时

$$
S^{2}=n_{0}\left(0-\frac{n_{1}+a}{n}\right)^{2}+n_{1}\left(1-\frac{n_{1}+a}{n}\right)^{2}+\left(a-\frac{n_{1}+a}{n}\right)^{2}
$$

注意到 $n_{0}+n_{1}=n-1$, 易算出

$$
\mathrm{d}\left(S^{2}\right) / \mathrm{d} a=2(n-1) n^{-1} a+D
$$

$D$ 与 $a$ 无关,若上式大于 0 , 则把 $a$ 增至 1 可增大 $S^{2}$; 若上式不大 于 0 , 则把 $a$ 域至 0 可以增大 $S^{2}$. 总之, $a$ 可改为 0 或 1 以增大 $S^{2} .3^{\circ}$ 以上两步证明了: 为使 $S^{2}$ 最大, 全部 $X_{i}$ 必须只取 0,1 这两 个值, 设有 $n_{0}$ 个 $0, n_{1}$ 个 1 . 则

$$
S^{2}=n_{0}\left(0-\frac{n_{1}}{n}\right)^{2}+n_{1}\left(1-\frac{n_{1}}{n}\right)=n_{0} n_{1} / n
$$

在 $n_{0}+n_{1}=n$ 的约束下, 要使 $S^{2}$ 最大, $n_{0}$ 和 $n_{1}$ 之差距应尽量 小, 如 $n=2 m$, 应取 $n_{0}=n_{1}=m$ : 若 $n=2 m+1$, 则 $n_{0}, n_{1}$ 中应有 一个为 $m$, 另一个为 $m+1$.

7. (a) 由 $\hat{\beta}_{0}=\bar{Y}$ 易得出 $E\left(\hat{\beta}_{0}\right)=\beta_{0}$, 为证 $E(\hat{\beta})=\beta$, 暂把 $p$ 行 $n$ 列方阵 $L{ }^{-1} X$ 记为

$$
L^{-1} X=\left(\begin{array}{llll}
l_{11} & l_{12} & \cdots & l_{1 n} \\
\cdots & \cdots & \cdots & \cdots \\
l_{p 1} & l_{p 2} & \cdots & l_{p n}
\end{array}\right)
$$

从 $X$ 的每行元素之和为 0 , 可推出此矩阵每行元素之和为 $0: l_{i 1}+$ $\cdots+l_{i n}=0, i=1, \cdots, p$. 现有

$$
E\left(\hat{\beta}_{j}\right)=E\left(\sum_{i=1}^{n} l_{j i} Y_{i}\right)=\sum_{i=1}^{n} l_{j i} \beta_{0}+\sum_{k-1}^{p} \beta_{k} \sum_{i=1}^{k} l_{j i} X_{k i}
$$

据上述, $\beta_{0}$ 之系数为 0 , 而 $\beta_{k}$ 之系数, 正是两矩阵 $L^{-1} X$ 和 $X^{\prime}$ 之 积的 $(j, k)$ 元, 因 $L^{-1} X X^{\prime}=L^{-1} L=$ 单位阵 $I$, 知只有当 $k=j$ 时 此系数为 $1, k$ 为其他值时为 0 . 故证明了 $E\left(\hat{\beta}_{j}\right)=\beta_{j}, j=1, \cdots, p$.

(b) 因为 $\hat{\beta}_{0}=\frac{1}{n}\left(Y_{1}+\cdots+Y_{n}\right), \hat{\beta}_{j}=l_{j 1} Y_{1}+\cdots+l_{j n} Y_{n}$. 由 $\left(Y_{1}, \cdots, Y_{n}\right)$ 独立且由等方差,易知

$$
\operatorname{Cov}\left(\hat{\beta}_{0}, \hat{\beta}_{j}\right)=\frac{1}{n} \sigma^{2}\left(l_{j 1}+\cdots+l_{j n}\right)=0, j=1, \cdots, p .
$$

(c) 与 (b) 相似, 由 $\hat{\beta}_{j}=l_{i 1} Y_{1}+\cdots+l_{i n} Y_{n}$ 及 $\hat{\beta}_{j}=l_{j 1} Y_{1}+\cdots+$ $l_{j n} Y_{n}$. 得知

$$
\operatorname{Cov}\left(\hat{\beta}_{i}, \hat{\beta}_{j}\right)=\sigma^{2}\left(l_{i 1} l_{j 1}+\cdots+l_{i n} l_{j n}\right)
$$

右边括号内之量是矩阵 $L^{-1} X$ 及其转置之积的 $(i, j)$ 元. 因 $L$ 为 对称方阵, 故 $L^{-1}$ 也是对称方阵, 即 $\left(L^{-1}\right)^{\prime}=L^{-1}$. 故 $\left(L^{-1} X\right)$ • $\left(L^{-1} X\right)^{\prime}=L^{-1} X X^{\prime} L^{-1}=L^{-1} L L^{-1}=L^{-1}$. 因此, $\operatorname{Cov}\left(\hat{\beta}_{i}, \hat{\beta}_{j}\right)=$ $\sigma^{2} \cdot L^{-1}$ 的 $(i, j)$ 元, 当 $i=j$ 时, 得到 $\hat{\beta}_{i}$ 的方差.

8 . 有关的理论考虑在题中已说了. 现在只须计算一下 $r \sqrt{n-2} / \sqrt{1-r^{2}}:$ 记 $S_{x}^{2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2}$ 并注意 $\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)$ $\cdot\left(Y_{i}-\bar{Y}\right)=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}$, 有

$$
\begin{aligned}
\frac{r \sqrt{n-2}}{\sqrt{1-r^{2}}} & =\frac{\sqrt{n-2} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} /\left[S_{x} \sqrt{\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}}\right]}{\left(1-\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}\right)^{2} /\left(S_{x}^{2} \sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}\right)^{1 / 2}} \\
& =\frac{\sqrt{n-2} \sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} / S_{x}}{\left(\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}-\left(\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}\right)^{2} / S_{x}^{2}\right)^{1 / 2}}
\end{aligned}
$$

因为 $\hat{\sigma}=\left(\sum_{i=1}^{n}\left(Y_{i}-\bar{Y}\right)^{2}-\left(\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i}\right)^{2} / S_{x}^{2}\right)^{1 / 2} / \sqrt{n-2}$, 而 $\hat{\beta}_{1}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right) Y_{i} / S_{x}^{2}$, 又 $\beta_{1}=0$. 故即有

$$
\frac{r \sqrt{n-2}}{\sqrt{1-r^{2}}}=\left(\hat{\beta}_{1}-\beta_{1}\right) /\left(\hat{\sigma} S_{X}^{-1}\right)
$$

再用 $(2.26)$, 即证得所要的结果.

$$
\text { 9. (a) 令 } Z_{i}=Y_{i}-X_{i}, i=1, \cdots, n, Z_{1}, \cdots Z_{n} \text { 独立同分布, 公 }
$$

共分布为 $N\left(b-a, 2 \sigma^{2}\right)$. 而 $H_{0}: b=a$ 成为一个检验正态分布 $N\left(\theta, \sigma_{1}^{2}\right)\left(\sigma_{1}^{2}=2 \sigma^{2}, \theta=b-a\right)$ 中均值 $\theta=0$ 的问题, 可用一样本 $t$ 检验: 当

$$
\sqrt{n}|\bar{Z}| /\left(\frac{1}{n-1} \sum_{i=1}^{n}\left(Z_{i}-\bar{Z}\right)^{2}\right)^{1 / 2}>t_{n-1}(\alpha / 2)
$$

时否定 $H_{0}$.

注: 这个模型叫做 “成对比较模型”, 意即 $X_{i}, Y_{i}$ 这一对可以 比较, 但当 $i \neq j$ 时, $X_{i}, Y_{j}$ 无法比较, 因为 $Y_{j}-X_{i} \sim N(b-a+$ $d_{j}-d_{i}, 2 \sigma^{2}$, 不只与 $b-a$ 有关而 $d_{j}-d_{i}$ 又不知道. 这与所谓“成 组比较" 不同: 在成组比较模型中是 $d_{1}=\cdots=d_{n}=0$. 这时任意的 $X_{i}, Y_{j}$ 都可比较, 而我们可使用两样本 $t$ 检验去检验 $H_{0}$, 它有 $2 n-2$ 个自由度.而检验 (4) 只有 $n-1$ 个自由度,所损失的自由 度, 就是因为有了赘余参数 $d_{1}, \cdots, d_{n}$.

(b) 可以把 $X_{1}, \cdots, X_{n}$ 和 $Y_{1}, \cdots, Y_{n}$ 分别视为一个两水平因 素在其水平 1 的 $n$ 个观察值和水平 2 的 $n$ 个观察值. $d_{i}$ 为区组效 应, $j=1, \cdots, n$, 而 $a, b$ 则分别是这两个水平的效应. 为把模型写 成 (5.13) 的形式, 可令 $Y_{1 j}=X_{j}, Y_{2 j}=Y_{j, j}=1, \cdots, n$; 而

$$
\begin{aligned}
& \mu=\bar{d}+(a+b) / 2 \quad\left(\bar{d}=\left(d_{1}+\cdots d_{n}\right) / n\right) \\
& a_{1}=a-(a+b) / 2, a_{2}=b-(a+b) / 2 \\
& b_{j}=d_{j}-\bar{d}, j=1, \cdots, n
\end{aligned}
$$

则有

$$
Y_{i j}=\mu+a_{i}+b_{j}+e_{i j}, i=1,2 ; j=1, \cdots, n
$$

这里 $e_{i j}, i=1,2 ; j=1, \cdots, n$ 全体独立同分布并有公共分布 $N(0$, $\left.\sigma^{2}\right)$. 模型 (5) 符合所要求的约束条件:

$$
\begin{aligned}
a_{1}+a_{2}= & a-(a+b) / 2+b-(a+b) / 2=0 \\
& \sum_{j=1}^{n} b_{j}=\sum_{j=1}^{n}\left(d_{j}-\bar{d}\right)=0
\end{aligned}
$$

原假设: $H_{0}: a=b$ 相应于检验(5) 中的因子效应为 0 , 即 $a_{1}=a_{2}=$ 0.

(c) 就模型 $(5)$ 按 $(5.23)$ 的分解式来计算 $S S_{A}$ 和 $S S_{e}$ :

$$
\begin{aligned}
\mathrm{SS}_{e}= & \sum_{i=1}^{2} \sum_{j=1}^{n}\left(Y_{i j}-Y_{i .}-Y_{j}+Y_{. .}\right)^{2} \\
= & \sum_{j=1}^{n}\left(X_{j}-\bar{X}-\left(X_{j}+Y_{j}\right) / 2+(\vec{X}+\bar{Y}) / 2\right)^{2} \\
& +\sum_{i=1}^{n}\left(Y_{j}-\bar{Y}-\left(X_{j}+Y_{j}\right) / 2+(\bar{X}+\bar{Y}) / 2\right)^{2} \\
= & \sum_{j=1}^{n}\left[\left(X_{j}-Y_{j}\right) / 2-(\bar{X}-\bar{Y}) / 2\right]^{2} \\
& +\sum_{j=1}^{n}\left[\left(Y_{j}-X_{j}\right) / 2-(\bar{Y}-\bar{X}) \% 2\right]^{2} \\
= & \frac{1}{2} \sum_{j=1}^{n}\left(Z_{j}-\bar{Z}\right)^{2} \quad\left(Z_{j}=Y_{j}-X_{j}\right)
\end{aligned}
$$

自由度为 $(2-1)(n-1)=n-1$. 而

$$
\begin{aligned}
S S_{A}= & n \sum_{i=1}^{2}\left(Y_{i .}-Y_{. .}\right)^{2}=n\left[(\bar{X}-(\bar{X}+\bar{Y}) / 2)^{2}\right. \\
& \left.+(\bar{Y}-(\bar{X}+\bar{Y}) / 2)^{2}\right] \\
= & \frac{n}{2}(\bar{X}-\bar{Y})^{2}=\frac{n}{2} \bar{Z}^{2}
\end{aligned}
$$

自由度为 $2-1=1$. 故 $H_{0}: a_{1}=a_{2}=0$, 即 $a=b$ 的 $F$ 检验为: 当

$$
\frac{n}{2} \bar{Z}^{2} /\left[\left(\frac{1}{2} \sum_{j=1}^{n}\left(Z_{i}-\bar{Z}\right)^{2} /(n-1)\right]>F_{1, n-1}(\alpha)\right.
$$

时否定 $H_{0}$ ，即当

$$
\sqrt{n}|\bar{Z}| /\left(\frac{1}{n-1} \sum_{i=1}^{n}\left(Z_{i}-\bar{Z}\right)^{2}\right)^{1 / 2}>\sqrt{F_{1, n-1}(\alpha)}
$$

时否定 $H_{0}$. 由于 $t_{n-1}^{2}(\alpha / 2)=F_{1, n-1}(\alpha)$ (这是因为, 按定义, 若 $X \sim t_{n-1}$, 则 $\left.X^{2} \sim F_{1, n-1}\right)$, 这个检验与 (a)中得到的一致.

10. 这张正交表叫 $L_{8}\left(2^{7}\right)$ 正交表. 它只能排 2 水平因子, 至多 7 个, 试验一定做 8 次, 不能多也不能少.

把因子 $A, B, C$ 分别排在第 $1,2,4$ 列头上, 区组也视为一个 因子 $D$, 排在第 5 列头上, 则得到如下的设计:

区组 1: $A_{1} B_{1} C_{1}, A_{1} B_{2} C_{1}, A_{2} B_{1} C_{2}, A_{2} B_{2} C_{2}$,

区组 2: $A_{1} B_{1} C_{2}, A_{1} B_{2} C_{2}, A_{2} B_{1} C_{1}, A_{2} B_{2} C_{1}$,

其中例如, $A_{1} B_{2} C_{1}$ 表示因子 $A$ 取水平 $1, B$ 取水平 $2, C$ 取 水平 1 ,余类推.

其所以舍掉第 3 列不用, 是为了避免某些组合做两次（如 $A_{1} B_{1} C_{1}$ 等 $)$, 而某些组合 ( $A_{1} B_{2} C_{1}$ 等) 则不出现, 按上述设计, 则 8 种可能的组合各出现了一次.

此设计 $A, B, C$ 及区组各占一自由度, 共 4 个自由度. 全部自 由度为 $8-1=7$, 故误差平方和 $S S_{e}$ 尚有三个自由度.

