---
comments: true
tags:
  - 校订中……
---
# 3.3 协方差与相关系数

<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/3/3.3.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/3/3.3.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/3/3.3.pdf">下载 PDF</a>.</p>
    </embed>
</object>
现在我们来考虑多维随机向量的数字特征, 以二维的情况为 例. 设 $(X, Y)$ 为二维随机向量, $X, Y$ 本身都是一维随机变量, 可 以定义其均值方差, 在本节中我们记

$$
E(X)=m_{1}, E(Y)=m_{2}, \operatorname{Var}(X)=\sigma_{1}^{2}, \operatorname{Var}(Y)=\sigma_{2}^{2}
$$

这些都在上两节中已讨论过了, 没有什么新东西. 在多维随机向量 中, 最有兴趣的数字特征是反映分量之间的关系的那种量, 其中最 重要的,是本节要讨论的协方差和相关系数.

定义 3.1 称 $E\left[\left(X-m_{1}\right)\left(Y-m_{2}\right)\right]$ 为 $X, Y$ 的协方差, 并 记为 $\operatorname{Cov}(X, Y)$.

“协”即“协同”的意思. $X$ 的方差是 $\left(X-m_{1}\right)$ 与 $\left(X-m_{1}\right)$ 的 乘积的期望, 如今把一个 $X-m_{1}$ 换为 $Y-m_{2}$, 其形式接近方差, 又有 $X, Y$ 二者的参与, 由此得出协方差的名称. 由定义看出: $\mathrm{Cov}$ $(X, Y)$ 与 $X, Y$ 的次序无关: $\operatorname{Cov}(X, Y)=\operatorname{Cov}(Y, X)$. 直接由定 义得到协方差的一些简单性质. 例如, 若 $c_{1}, c_{2}, c_{3}, c_{4}$ 都是常数, 则

$$
\operatorname{Cov}\left(c_{1} X+c_{2}, c_{3} Y+c_{4}\right)=c_{1} c_{3} \operatorname{Cov}(X, Y)
$$

又易知

$$
\operatorname{Cov}(X, Y)=E(X Y)-m_{1} m_{2}
$$

这些简单性质的证明都留给读者.

下面的定理包含了协方差的重要性质.

定理 $3.11^{\circ}$ 若 $X, Y$ 独立, 则 $\operatorname{Cov}(X, Y)=0$.

$2^{\circ}[\operatorname{Cov}(X, Y)]^{2} \leqslant \sigma_{1}^{2} \sigma_{2}^{2}$. 等号当且仅当 $X, Y$ 之间有严格 线性关系 (即存在常数 $a, b$ 使 $Y=a+b X$ ) 时成立.

证 $1^{\circ}$ 的证明由定理 1.2 直接得出, 因据此定理,当 $X, Y$ 独 立时有 $E(X Y)=m_{1} m_{2}$. 为证明 $2^{\circ}$, 需要两点预备事实:

a. 若 $a, b, c$ 为常数, $a>0$, 而二次三项式 $a t^{2}+2 b t+c$ 对 $t$ 的任何实值都非负, 则必有 $a c \geqslant b^{2}$.

b. 若随机变量 $Z$ 只能够取非负值, 而 $E(Z)=0$, 则 $Z=0$.

为了不打断此处的讨论,我们将这两点事实的证明放到后面, 现考虑

$$
E\left[t\left(X-m_{1}\right)+\left(Y-m_{2}\right)\right]^{2}=\sigma_{1}^{2} t^{2}+2 \operatorname{Cov}(X, Y) t+\sigma_{2}^{2}
$$

* $\operatorname{Cov}$ 是胁方差 Covariance 的维写. 由于此式左边是一个非负随机变量的均值, 故它对任何 $t$ 非负. 按 预备事实 $\mathrm{a}$, 有

$$
\sigma_{1}^{2} \sigma_{2}^{2} \geqslant[\operatorname{Cov}(X, Y)]^{2}
$$

进一步, 如果 (3.4)成立等号, 则 (3.3) 右边等于 $\left(\sigma_{1} t \pm \sigma_{2}\right)^{2} . \pm$ 号 视 $\operatorname{Cov}(X, Y)>0$ 或 $<0$ 而定, 为确定计, 暂设 $\operatorname{Cov}(X, Y)>0$, 则 (3.3) 右边为 $\left(\sigma_{1} t+\sigma_{2}\right)^{2}$. 此式在 $t=t_{0}=-\sigma_{2} / \sigma_{1}$ 时为 0 . 以 $t=t_{0}$ 代人(3.3), 有

$$
E\left[t_{0}\left(X-m_{1}\right)+\left(Y-m_{2}\right)\right]^{2}=0
$$

再按预备事实 $\mathrm{b}$, 即知 $t_{0}\left(X-m_{1}\right)+\left(Y-m_{2}\right)=0$, 因而 $X, Y$ 之 间有严格线性关系.

反之, 若 $X, Y$ 之间有严格线性关系 $Y=a X+b$, 则 $\sigma_{2}^{2}=$ Var $(Y)=\operatorname{Var}(a X+b)=\operatorname{Var}(a X)=a^{2} \operatorname{Var}(X)=a^{2} \sigma_{1}^{2}$. 又因 $m_{2}=E$ $(Y)=a E(X)+b=a m_{1}+b$, 有 $Y-m_{2}=(a X+b)-\left(a m_{1}+b\right)$ $=a\left(X-m_{1}\right)$. 于是

$$
\begin{aligned}
\operatorname{Cov}(X, Y) & =E\left[\left(X-m_{1}\right) a\left(X-m_{1}\right)\right]=a\left[E\left(X-m_{1}\right)^{2}\right] \\
& =a \sigma_{1}^{2}
\end{aligned}
$$

因此

$$
[\operatorname{Cov}(X, Y)]^{2}=a^{2} \sigma_{1}^{4}=\sigma_{1}^{2}\left(a^{2} \sigma_{1}^{2}\right)=\sigma_{1}^{2} \sigma_{2}^{2}
$$

即(3.4)成立等号, 这就证明了 $2^{\circ}$ 全部结论.

现证明用到的两个预备事实. 对 $\mathrm{a}$, 注意到若 $a c<b^{2}$, 则 $a t^{2}+$ $2 b t+c=0$ 有两个不同的实根 $t_{1}<t_{2}$, 而 $a t^{2}+2 b t+c=a\left(t-t_{1}\right)$ $\left(t-t_{2}\right)$. 取 $t_{0}$ 使 $t_{1}<t_{0}<t_{2}$, 则将有 $a t_{0}^{2}+2 b t_{0}+c=a\left(t_{0}-t_{1}\right)$ $\left(t_{0}-t_{2}\right)<0$, 与 $a t^{2}+2 b t+c$ 对任何 $t$ 非负矛盾, 这证明了 a. b 的 证明很简单: 若 $Z \neq 0$, 则因 $Z$ 只能取非负值, 它必以一定的大于 0 的概率取大于 0 的值, 这将导致 $E(Z)>0$, 与 $E(Z)=0$ 的假定不 合.

定理 3.1 给“相关系数”的定义打下了基础. 定义 3.2 称 $\operatorname{Cov}(X, Y) /\left(\sigma_{1} \sigma_{2}\right)$ 为 $X, Y$ 的相关系数, 并记 为 ${ }^{*} \operatorname{Corr}(X, Y)$.

形式上可以把相关系数视为“标准尺度下的协方差”. 协方差 作为 $\left(X-m_{1}\right)\left(Y-m_{2}\right)$ 的均值, 依赖于 $X, Y$ 的度量单位, 选择 适当单位使 $X, Y$ 的方差都为 1 , 则协方差就是相关系数. 这样就 能更好地反映 $X, Y$ 之间的关系,不受所用单位的影响.

由定理 3.1 立即得到:

定理 $3.21^{\circ}$ 若 $X, Y$ 独立, 则 $\operatorname{Corr}(X, Y)=0 . \quad 2^{\circ}-1$ $\leqslant \operatorname{Corr}(X, Y) \leqslant 1$, 或 $|\operatorname{Corr}(X, Y)| \leqslant 1$, 等号当且仅当 $X$ 和 $Y$ 有 严格线性关系时达到.

对这个定理我们要加以几条重要的解释.

1. 当 $\operatorname{Corr}(X, Y)=0$ (或 $\operatorname{Cov}(X, Y)=0$, 一样), 称 $X, Y$ “不 相关”. 本定理的 $1^{\circ}$ 说明由 $X, Y$ 独立推出它们不相关. 但反过来 一般不成立: 由 $\operatorname{Corr}(X, Y)=0$ 不一定有 $X, Y$ 独立.下面是一个 简单的例子.

例 3.1 设 $(X, Y)$ 服从单位圆内的均匀分布, 即其密度函数 为

$$
f(x, y)= \begin{cases}\pi^{-1}, & \text { 当 } x^{2}+y^{2}<1 \\ 0, & \text { 当 } x^{2}+y^{2} \geqslant 1\end{cases}
$$

用第二章公式 (2.9), (2.10), 容易得出 $X, Y$ 有同样的边缘密度 函数 $g$ :

$$
g(x)=\left\{\begin{array}{cl}
2 x^{-2} \sqrt{1-x^{2}}, & \text { 当 }|x|<1 \\
0, & \text { 当 }|x| \geqslant 1
\end{array}\right.
$$

这个函数关于 0 对称, 因此其均值为 0 . 故 $E(X)=E(Y)=0$, 而

$$
\operatorname{Cov}(X, Y)=E(X Y)=\frac{1}{\pi} \iint_{x^{2}+y^{2}<1} x y \mathrm{~d} x \mathrm{~d} y=0
$$

故 $\operatorname{Corr}(X, Y)=0$. 但 $X, Y$ 不独立, 因为其联合密度 $f(x, y)$ 不 等于其边缘密度之积 $g(x) g(y)$.

* Corr 是相关 Correlation 的缩写.
- 136 · 2. 相关系数也常称为 “线性相关系数”. 这是因为, 实际上相 关系数并不是刻画了 $X, Y$ 之间 “一般”关系的程度,而只是 “线 性”关系的程度. 这种说法的根据之一就在于, 当且仅当 $X, Y$ 有 严格的线性关系时, 才有 $|\operatorname{Corr}(X, Y)|$ 达到最大值 1. 可以容易举 出例子说明: 即使 $X$ 与 $Y$ 有某种严格的函数关系但非线性关系, $|\operatorname{Corr}(X, Y)|$ 不仅不必为 1 , 还可以为 0 .

例 3.2 设 $X \sim R(-1 / 2,1 / 2)$ ，即区间 $[-1 / 2,1 / 2]$ 内的均 匀分布, 而 $Y=\cos X, Y$ 与 $X$ 有严格函数关系. 但因 $E(X)=0$, 由 (3.2)有

$$
\operatorname{Cov}(X, Y)=E(X Y)=E(X \cos X)=\int_{-1 / 2}^{1 / 2} x \cos x \mathrm{~d} x=0
$$

故 $\operatorname{Corr}(X, Y)=0$. 你看, $X, Y$ 说是“不相关”, 它们之间却有着严 格的关系 $Y=\cos X$. 足见这样的相关只能指线性而言, 一超出这 个范围, 这个概念就失去了意义。

3. 如果 $0<|\operatorname{Corr}(X, Y)|<1$, 则解释为: $X, Y$ 之间有“一定 程度的”线性关系而非严格的线性关系.何谓“一定程度”的线性关 系? 我们可以用图 3.6 所示的情况来说明. 在这三个图中,我们都 假定 $(X, Y)$ 服从所画出的区域 $A$ 内的均匀分布 (即其联合密度 $f(x, y)$ 在 $A$ 内为 $|A|^{-1}$, 在 $A$ 外为 $0,|A|$ 为区域 $A$ 的面积). 在这三个图中, $X, Y$ 都无严格的线性关系, 因为由 $X$ 之值并不能 决定 $Y$ 之值. 可是由这几个图我们都能“感觉” 出, $X, Y$ 之间存在

![](https://cdn.mathpix.com/cropped/2023_07_12_81839149c1329c8fde02g-5.jpg?height=379&width=397&top_left_y=1992&top_left_x=338)

(a)

![](https://cdn.mathpix.com/cropped/2023_07_12_81839149c1329c8fde02g-5.jpg?height=394&width=354&top_left_y=2005&top_left_x=794)

(b)

![](https://cdn.mathpix.com/cropped/2023_07_12_81839149c1329c8fde02g-5.jpg?height=368&width=396&top_left_y=2052&top_left_x=1204)

(c)

图 3.6 着一种线性的“趋势”. 这种趋势, 在 (a) 已较显著且是正向的 ( $X$ 增 加时 $Y$ 倾向于增加), 这相应于 $\operatorname{Corr}(X, Y)$ 比较显著地大于 0 . 在 (b), 这种线性趋势比 (a) 更明显, 程度更大, 反映 $|\operatorname{Corr}(X, Y)|$ 比 (a) 的情况更大, 但为负向的. 至于 (c), 则多少有一点儿线性倾向, 但已甚微弱: $\operatorname{Corr}(X, Y)$ 虽仍大于 0 但已接近 0 .

4. 上面谈到的 “线性相关” 的意义, 还可以从最小二乘法的角 度去解释: 设有两个随机变量 $X, Y$, 现在想用 $X$ 的某一线性函数 $a+b X$ 来逼近 $Y$, 问要选择怎样的常数 $a, b$, 才能使逼近的程度最 高? 这逼近程度, 我们就用 “最小二乘” 的观点来衡量, 即要使 $E\left[(Y-a-b X)^{2}\right]$ 达到最小.

仍以 $m_{1}, m_{2}$ 记 $E(X), E(Y), \sigma_{1}^{2}$ 和 $\sigma_{2}^{2}$ 记 $\operatorname{Var}(X), \operatorname{Var}(Y)$. 引进常数

$$
c=a-\left(m_{2}-b m_{1}\right)
$$

则

$$
\begin{aligned}
E\left[(Y-a-b X)^{2}\right] & =E\left[\left(Y-m_{2}\right)-b\left(X-m_{1}\right)-c\right]^{2} \\
& =\sigma_{2}^{2}+b^{2} \sigma_{1}^{2}-2 b \operatorname{Cov}(X, Y)+c^{2},
\end{aligned}
$$

为使此式达到最小, 必须取 $c=0, b=\operatorname{Cov}(X, Y) / \sigma_{1}^{2}=\sigma_{1} \sigma_{2}$ Corr $(X, Y) / \sigma_{1}^{2}=\sigma_{1}^{-1} \sigma_{2} \operatorname{Corr}(X, Y)$. 这样求出最佳线性逼近为 (记 $\rho=\operatorname{Corr}(X, Y))$

$$
L(X)=m_{2}-\sigma_{1}^{-1} \sigma_{2} \rho m_{1}+\sigma_{1}^{-1} \sigma_{2} \rho X
$$

这一逼近的剩余是

$$
\begin{aligned}
E\left[(Y-L(X))^{2}\right] & =\sigma_{2}^{2}+b^{2} \sigma_{1}^{2}-2 b \operatorname{Cov}(X, Y) \\
& =\sigma_{2}^{2}+\left(\sigma_{1}^{-1} \sigma_{2} \rho\right)^{2} \sigma_{1}^{2}-2\left(\sigma_{1}^{-1} \sigma_{2} \rho\right) \sigma_{1} \sigma_{2} \rho \\
& =\sigma_{2}^{2}\left(1-\rho^{2}\right)
\end{aligned}
$$

如果 $\rho= \pm 1$, 则 $E[(Y-L(X))]^{2}=0$ 而 $Y=L(X)$. 这时 $Y$ 与 $X$ 有严格线性关系, 已于前述. 若 $0<|\rho|<1$, 则 $|\rho|$ 愈接近 1 , 剩 余愈小, 说明 $L(X)$ 与 $Y$ 的接近程度愈大, 即 $X, Y$ 之间线性关系 的“程度”愈大. 反之, $|\rho|$ 愈小, 则二者的线性关系程度愈小, 当 $\rho=0$ 时, 剩余为 $\sigma_{2}^{2}$. 这时 $X$ 的线性作用已毫不存在. 因为, 仅取一 个与 $X$ 无关的常数 $m_{2}$, 已可把 $Y$ 逼近到 $\sigma_{2}^{2}$ 的剩余, 因 $E(Y-$ $\left.m_{2}\right)^{2}=\sigma_{2}^{2} . \rho$ 的符号的意义也由 (3.5) 得到解释: 当 $\rho>0$ 时, $L(X)$ 中 $X$ 的系数大于 0 , 即 $Y$ 的最佳逼近 $a+b X$ 随 $X$ 增加而增 加. 这就是正向相关.反之, $\rho<0$ 表示负向相关.

由于相关系数只能刻画线性关系的程度，而不能刻画一般的 函数相依关系的程度, 在概率论中还引进了另一些相关性指标, 以 补救这个缺点. 但是, 这些指标都末能在应用中推开. 究其原因, 除 了这些指标在性质上比较复杂外, 还有一个重要原因: 在统计学应 用上,最重要的二维分布是二维正态分布. 而对二维正态分布而 言, 相关系数是 $X, Y$ 的相关性的一个完美的刻画, 没有上面指出 的缺点. 其根据有两条:

1. 若 $(X, Y)$ 为二维正态, 则即使允许你用任何函数 $M(X)$ 去逼近 $Y$ (仍以 $E\left[(Y-M(X))^{2}\right]$ 最小为准则, 那你所得到的最 佳逼近, 仍是由 (3.5)式决定的 $L(X)$. 故在这个场合, 只须考虑线 性逼近已足,而这种逼近的程度完全由相关系数决定。
2. 当 $(X, Y)$ 为二维正态时, 由 $\operatorname{Corr}(X, Y)=0$ 能推出 $X, Y$ 独立. 即在这一特定场合, 独立与不相关是一回事. 我们前已指出, 这在一般情况并不成立.

第一点的证明超出本书范围.第二点则不难证明. 事实上我们 将验证: 若 $(X, Y)$ 有二维正态分布 $N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho\right)$, 则 Corr $(X, Y)=\rho$. 而当 $\rho=0$ 时, 按第二章 $(2.7)$ 式易知, $(X, Y)$ 的联合 密度可表为 $X, Y$ 各自的密度 $f_{1}(x)$ 和 $f_{2}(y)$ 之积, 因而 $X, Y$ 是 独立的.

为证明此事, 注意到 $E(X)=a, E(Y)=b$. 利用第二章 (2.7) 式的 $N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho\right)$ 的密度函数的形式. 有

$$
\begin{aligned}
& \operatorname{Cov}(X, Y)=E[(X-a)(Y-b)] \\
= & \left(2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}\right)^{-1} \iint_{-\infty}^{\infty}(x-a)(y-b) \exp \left[-\frac{1}{2\left(1-\rho^{2}\right)}\right. \\
& \left.\cdot\left(\frac{(x-a)^{2}}{\sigma_{1}^{2}}-\frac{2 \rho(x-a)(y-b)}{\sigma_{1} \sigma_{2}}+\frac{(y-b)^{2}}{\sigma_{2}^{2}}\right)\right] \mathrm{d} x \mathrm{~d} y .
\end{aligned}
$$

注意到

$$
\begin{aligned}
& \frac{(x-a)^{2}}{\sigma_{1}^{2}}-\frac{2 \rho(x-a)(y-b)}{\sigma_{1} \sigma_{2}}+\frac{(y-b)^{2}}{\sigma_{2}^{2}} \\
= & \left(\frac{x-a}{\sigma_{1}}-\frac{\rho(y-b)}{\sigma_{2}}\right)^{2}+\left(\sqrt{1-\rho^{2}} \frac{y-b}{\sigma_{2}}\right)^{2}
\end{aligned}
$$

作变数代换

$$
u=\frac{1}{\sqrt{1-\rho^{2}}}\left(\frac{x-a}{\sigma_{1}}-\frac{\rho(y-b)}{\sigma_{2}}\right), v=\frac{y-b}{\sigma^{2}}
$$

可将上面的重积分化为

$$
\begin{aligned}
\operatorname{Cov}(X, Y)= & (2 \pi)^{-1} \iint_{-\infty}^{\infty}\left[\sqrt{1-\rho^{2}} \sigma_{1} u+\sigma_{1} \rho v\right] \\
& \cdot \sigma_{2} v \exp \left[-\frac{u^{2}+v^{2}}{2}\right] \mathrm{d} u \mathrm{~d} v
\end{aligned}
$$

因为

$$
\begin{aligned}
& \iint_{-\infty}^{\infty} u v \exp \left(-\frac{u^{2}+v^{2}}{2}\right) \mathrm{d} u \mathrm{~d} v=\int_{-\infty}^{\infty} u \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u \int_{-\infty}^{\infty} u \mathrm{e}^{-v^{2} / 2} \mathrm{~d} v=0 \\
& \int_{-\infty}^{\infty} v^{2} \exp \left(-\frac{u^{2}+v^{2}}{2}\right) \mathrm{d} u \mathrm{~d} v=\int_{-\infty}^{\infty} \mathrm{e}^{-u^{2} / 2} \mathrm{~d} u \int_{-\infty}^{\infty} v^{2} \mathrm{e}^{-v^{2} / 2} \mathrm{~d} v=2 \pi
\end{aligned}
$$

得到 $\operatorname{Cov}(X, Y)=\rho \sigma_{1} \sigma_{2}$. 又 $\operatorname{Var}(X)=\sigma_{1}^{2}, \operatorname{Var}(Y)=\sigma_{2}^{2}$. 于是

$$
\operatorname{Corr}(X, Y)=\operatorname{Cov}(X, Y) /\left(\sigma_{1} \sigma_{2}\right)=\rho
$$

