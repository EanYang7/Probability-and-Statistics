# 附 录 

## 1. A. 若干检验的一致最优性

在本章定义 1.3 中已给出了一个检验问题 $H_{0}: H_{1}$ 的水平 $\alpha$ 一致最优检验的定义. 它是一切水平 $\alpha$ 检验中其功效在对立假设 $H_{1}$ 上处处达到最大的检验. 如已说明的, 这种检验的存在是稀有 的例外, 但在一些重要的单参数分布族的单侧检验问题中, 以及在 个别多参数检验中, 它确实存在. 5.2 节中许多例子属于这种情 况。这里我们来作一些讨论.

## 2. 1. 简单假设下的奈曼一皮尔逊基本引理

考虑一个最简单的情况：原假设 $H_{0}$ 和对立假设 $H_{1}$ 中, 都只 包含一分布. 为确定计, 设分布都有密度, 离散型的情况完全类似, 只须把积分变成求和即可. 因此, 有

## 3. $H_{0}$ : 总体有密度 $f_{0}(x)$ 
 $H_{1}$ : 总体有密度 $f_{1}(x)$

设 $X_{1}, \cdots, X_{n}$ 为样本, 则 $\left(X_{1}, \cdots, X_{n}\right)$ 的密度, 在 $H_{0}$ 和 $H_{1}$ 之下, 分别为 $g_{0}(y)=f_{0}\left(x_{1}\right) \cdots f_{0}\left(x_{n}\right)$ 和 $g_{1}(y)=f_{1}\left(x_{1}\right) \cdots f_{1}\left(x_{n}\right)$. 这 里已简记 $y=\left(x_{1}, \cdots, x_{n}\right)$. 求这个问题的水平 $\alpha$ 的检验, 转化为 下述数学问题: 找 $y$ 空间之一区域 $Q$, 作为检验的否定域 (当 $\left(X_{1}\right.$, $\left.\cdots, X_{n}\right)$ 落在 $Q$ 内时否定 $H_{0}$, 不然就接受 $\left.H_{0}\right)$. 为使 $Q$ 达到最优, 就必须在条件

$$
\int_{Q} g_{0}(y) \mathrm{d} y \leqslant \alpha
$$

之下, 使 $\int_{Q} g_{1}(y) \mathrm{d} y$ 达到最大. 很容易看出: 为达到这一点, $Q$ 必 须这样取: 把比值 $g_{1}(y) / g_{0}(y)$ 大的那些 $y$ 收进来. 这就是奈一皮 基本引理:

奈-皮基本引理 水平 $\alpha$ 的一致最优检验 $\varphi$ 的否定域 $Q$ 应如 下取:找常数 $C$, 使

$$
Q=\left\{y: g_{1}(y) / g_{0}(y)>C\right\}
$$

而满足

$$
\int_{Q} g_{0}(y) \mathrm{d} y=\alpha
$$

证 (2) 式保证了检验 $\varphi$ 的水平为 $\alpha$, 现设 $\varphi^{\prime}$ 为另一水平 $\alpha$ 检 验, 其否定域为 $Q^{\prime}$. 记 $Q$ 与 $Q^{\prime}$ 的公共部分为 $R . Q_{1}$ 记 $Q$ 中去掉 $R$ 的剩余部分, $Q^{\prime}{ }_{1}$ 记 $Q^{\prime}$ 中去掉 $R$ 的剩余部分 (图 5.5), 则易见

$$
\int_{Q^{\prime}} g_{1}(y) \mathrm{d} y-\int_{Q^{\prime}} g_{1}(y) \mathrm{d} y=\int_{Q_{1}} g_{1}(y) \mathrm{d} y-\int_{Q_{1}^{\prime}} g_{1}(y) \mathrm{d} y
$$

由于 $\varphi^{\prime}$ 有水平 $\alpha$, 有

$$
\int_{Q^{\prime}} g_{0}(y) \mathrm{d} y \leqslant \alpha
$$

再由 (2) 式, 知

$$
\int_{Q_{1}} g_{0}(y) \mathrm{d} y \geqslant \int_{Q_{1}^{\prime}} g_{0}(y) \mathrm{d} y
$$

因为 $Q_{1}^{\prime}$ 在 $Q$ 之外,按 (1) 式, 当 $y$ 属于 $Q_{1}^{\prime}$ 时,有 $g_{1}(y) \leqslant C g_{0}(y)$. 而当 $y$ 属于 $Q_{1}$ 时有

![](https://cdn.mathpix.com/cropped/2023_07_12_4f97b95423ff4c23ad17g-2.jpg?height=395&width=417&top_left_y=939&top_left_x=1325)
$g_{1}(y)>\operatorname{Cg}_{0}(y)$. 故

$$
\int_{Q_{1}} g_{1}(y) \mathrm{d} y \geqslant C \int_{Q_{1}} g_{0}(y) \mathrm{d} y, \int_{Q_{1}^{\prime}} g_{1}(y) \mathrm{d} y \leqslant C \int_{Q_{1}^{\prime}} g_{0}(y) \mathrm{d} y
$$

由此及 $(3),(4)$, 即知

$$
\int_{Q} g_{1}(y) \mathrm{d} y \geqslant \int_{Q_{1}^{\prime}} g_{1}(y) \mathrm{d} y
$$

即检验 $\varphi$ 的功效总不小于 $\varphi^{\prime}$ 的功效, 由于 $\varphi^{\prime}$ 是任取的水平 $\alpha$ 检 验,证明了 $\varphi$ 是水平 $\alpha$ 的一致最优检验.

2. 复合假设检验的情况

现考虑一般的复合假设检验问题 $H_{0}: H_{1}$. 关于其水平 $\alpha$ 一致 最优检验的存在, 有如下的简单结果:

定理 在 $H_{0}$ 中取定一值 $\theta_{0}$, 对 $H_{1}$ 中的值 $\theta_{1}$ 建立假设检验 问题:

$$
H_{0}^{\prime}: \theta_{0} ; H_{1}^{\prime}: \theta_{1}
$$

按奈一皮引理,求出其水平 $\alpha$ 一致最优检验 $\varphi$. 如果 $\varphi$ 符合以下两 个条件,则它必须是原问题 $H_{0}: H_{1}$ 的一个水平 $\alpha$ 一致最优检验:

$1^{\circ}$ 检验 $\varphi$ 也是 $H_{0}: H_{1}$ 的水平 $\alpha$ 检验.

$2^{\circ}$ 检验 $\varphi$ 不依赖于 $\theta_{1}$ 值.

证 设 $\varphi^{\prime}$ 为 $H_{0}$ : $H_{1}$ 之任一水平 $\alpha$ 检验, 则它必是 (5) 的一个 水平 $\alpha$ 检验. 这很显然: 以 $\beta_{\varphi^{\prime}}(\theta)$ 记 $\varphi^{\prime}$ 的功效函数. $\varphi^{\prime}$ 为 $H_{0}: H_{1}$ 的水平 $\alpha$ 检验, 意味着 $\beta_{\varphi^{\prime}}(\theta)$ 在 $H_{0}$ 上处处不超过 $\alpha$, 因而特别在 $\theta_{0}$ 点不超过 $\alpha$. 这样, $\varphi$ 和 $\varphi^{\prime}$ 都是 (5) 的水平 $\alpha$ 检验而 $\varphi$ 是 (5) 的 水平 $\alpha$ 一致最优检验，故 $\beta_{\varphi}\left(\theta_{1}\right) \geqslant \beta_{\varphi^{\prime}}\left(\theta_{1}\right)$. 因为这个事实对 $H_{1}$ 中任一个 $\theta_{1}$ 都成立, 即知 $\varphi$ 为 $H_{0}: H_{1}$ 的水平 $\alpha$ 一致最优检验.

在本定理中, $\theta_{0}$ 值如何取? 对形如 $\theta \leqslant a$ 或 $\theta \geqslant a$ 这样的单侧 原假设, $\theta_{0}$ 总是取为 $a$.

例 $1 X_{1}, \cdots, X_{n}$ 为抽自正态总体 $N\left(\theta, \sigma^{2}\right)$ 的样本, $\sigma^{2}$ 已知， 考虑检验问题

$$
H_{0}: \theta \leqslant a ; H_{1}: \theta>a
$$

$a$ 为给定常数.

按本定理,取 $\theta_{0}=a$, 任取 $\theta_{1}>a$. 作检验问题

$$
H_{0}^{\prime}: \theta=a ; H_{1}^{\prime}: \theta=\theta_{1}
$$

按奈一皮基本引理, (7) 的水平 $\alpha$ 一致最优检验 $\varphi$ 有否定域:

$$
\begin{gathered}
\left\{\left(x_{1}, \cdots, x_{n}\right):\left(\frac{1}{\sqrt{2 \pi} \sigma}\right)^{n} \exp \left[-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\theta_{1}\right)^{2}\right]\right. \\
\left.\mid\left(\frac{1}{\sqrt{2 \pi} \sigma}\right)^{n} \exp \left[-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-a\right)^{2}\right]>C\right\}
\end{gathered}
$$

取对数,易知此集合为

$$
\left\{\left(x_{1}, \cdots, x_{n}\right): \sigma^{-2}\left(\theta_{1}-a\right) \sum_{i=1}^{n} x_{i}>C_{1}\right\}
$$

对某个常数 $C_{1}$. 因 $\theta_{1}-a>0, \sigma^{2}>0$, 此集合化为

$$
\left\{\left(x_{1}, \cdots, x_{n}\right): \sum_{i=1}^{n} x_{i}>C_{2}\right\}
$$

的形状. $C_{2}$ 为另一常数, 要使此检验有水平 $a$, 应取 $C_{2}=n a+$ $\sqrt{n} \sigma u_{\alpha}$. 此值与 $\theta_{1}$ 无关, 因而定理的条件 $2^{\circ}$ 满足. 另外, 这个检验 的功效函数是 $1-\Phi\left(u_{\alpha}-\frac{\theta-a}{\sigma}\right)$, 是 $\theta$ 的上升函数. 所以, 这个检 验也是 (6) 的水平 $\alpha$ 检验. 这样, 条件 $1^{\circ}$ 也适合. 据定理, 这检验就 是 (6) 的水平 $\alpha$ 的一致最优检验.

指数分布, 二项分布和波哇松分布参数的单侧假设检验问题, 也可以用与本例相同的方法证明其一致最优检验存在. 留给读者 作为习题.

若在本例中考察双侧假设 $H_{0}: \theta=a, H_{1}: \theta \neq a$, 则一致最优 检验不存在, 其理由现在也不难看出, 因现在 $\theta_{1}$ 可以大于 $a$ 也可 以小于 $a$. 当 $\theta_{1}>a$ 时, 检验问题 (7) 的一致最优检验的形式如 (8). 若 $\theta_{1}<a$, 则一致最优检验的否定域形如

$$
\left\{\left(x_{1}, \cdots, x_{n}\right): \sum_{i=1}^{n} x_{i}<C_{3}\right\}
$$

与(8)不同. 因此,定理的条件 $2^{\circ}$ 不满足.

## 4. B. 非中心 $t$ 分布与 $t$ 检验

设 $X$ 与 $Y$ 独立, $X \sim N(0,1), Y \sim \chi_{n}^{2}$, 又设 $\delta$ 为常数, 则随机 变量 $Z=(X+\delta) / \sqrt{\frac{1}{n} Y}$ 的分布称为自由度 $n$ 、非中心参数 $\delta$ 的 非中心 $t$ 分布, 记为 $Z \sim t_{n, \delta} . t_{n, \delta}$ 的分布函数将记为 $F_{n, \delta}(x)$. 当 $\delta=0$ 时, 就得到在第二章例 4.10 中介绍过的自由度 $n$ 的 $t$ 分布 (有时称中心 $t$ 分布).

非中心 $t$ 分布也是数理统计应用上的重要分布, 但其分布函 数 $F_{n, \delta}(x)$ 的形式很复杂, 此处不去介绍. 只提到一点对下文有用 的性质: 若 $\delta_{2}>\delta_{1}$, 则 $F_{n, \delta_{2}}(x) \leqslant F_{n, \delta_{1}}(x)$. 事实上, 记

$$
Z_{i}=\left(X+\delta_{i}\right) / \sqrt{\frac{1}{n} Y}, i=1,2
$$

$X, Y$ 如上文所述, 则有 $Z_{1}<Z_{2}$, 故对任何 $x$ 有 $P\left(Z_{1} \leqslant x\right) \geqslant$ $P\left(Z_{2} \leqslant x\right)$, 即 $F_{n, \delta_{1}}(x) \geqslant F_{n, \delta_{2}}(x)$.

有了这些准备, 我们可以解决 5.2 节中遗留下来的有关 $t$ 检 验的问题.

设 $X_{1}, \cdots, X_{n}$ 为抽自 $N\left(\theta, \sigma^{2}\right)$ 中的样本, $\theta, \sigma^{2}$ 都末知, 对假 设检验问题

$$
H_{0}: \theta \geqslant \theta_{0}, H_{1}: \theta<\theta_{0}
$$

我们引进了 $t$ 检验 $\psi$, 由 (2.14) 给出. 其功效函数为 (2.15). 现易 知, $(2.15)$ 的 $\beta_{\psi}(\theta, \sigma)$ 为

$$
\beta_{\psi}(\theta, \sigma)=F_{n-1, \sqrt{n}\left(\theta-\theta_{0}\right) / \sigma}\left(-t_{n-1}(\alpha)\right)
$$

事实上,有

$$
\sqrt{n}\left(\bar{X}-\theta_{0}\right) / S=\left(\frac{\sqrt{n}(\bar{X}-\theta)}{\sigma}+\frac{\sqrt{n}\left(\theta-\theta_{0}\right)}{\sigma}\right) \sqrt{\frac{1}{\sigma^{2}} S^{2}}
$$

当参数值为 $(\theta, \sigma)$ 时, $\sqrt{n}(\bar{X}-\theta) / \sigma \sim N(0,1),(n-1) S^{2} / \sigma^{2} \sim$ $\chi_{n}^{2}-1$, 且二者独立. 故按非中心 $t$ 分布的定义及 $(2.15)$ 式, 即得 (9).

由 (9) 式可知, $\beta_{\psi}(\theta, \sigma)$ 为 $\theta$ 的下降函数. 因当 $\theta$ 增加时, $\sqrt{n}\left(\theta-\theta_{0}\right) / \sigma$ 增加. 按前面证明的性质, 即知(9)式右边下降, 因 为 $\beta\left(\theta_{0}, \sigma\right)=\alpha$, 知当 $\theta \geqslant \theta_{0}$ 时有 $\beta_{\psi}(\theta, \sigma) \leqslant \alpha$. 这证明了: $t$ 检验 (2.14) 有水平 $\alpha$.

其次, 功效函数 (9) 的形式也说明: 给定 $\theta_{1}<\theta_{0}$ 及 $\beta<\alpha$, 不论 你取样本大小 $n$ 多大, 也无法保证对一切 $\sigma>0$ 有 $\beta_{\psi}\left(\theta_{1}, \sigma\right) \geqslant \beta$, 事实上,固定 $n$, 当 $\sigma \rightarrow \infty$ 时有

$$
\begin{aligned}
\lim _{\sigma \rightarrow \infty} \beta_{\psi}\left(\theta_{1}, \sigma\right) & =\lim _{\sigma \rightarrow \infty} F_{n-1, \sqrt{n}\left(\theta-\theta_{0}\right) / \sigma}\left(-t_{n-1}(\alpha)\right) \\
& =F_{n-1,0}\left(-t_{n-1}(\alpha)\right)=\alpha
\end{aligned}
$$

这样, 不论你固定 $n$ 多大, 只要 $\alpha$ 充分大, 就可以使 $\beta_{\varphi}\left(\theta_{1}, \sigma\right)<$ $\beta$.

如果以 $\sigma$ 为单位来衡量 $\theta_{1}$ 与 $\theta_{0}$ 的差距, 即要求当 $\left(\theta_{1}-\theta_{0}\right) / \sigma$ 固定为某个指定的 $\delta_{0}<0$ 时有 $\beta_{\psi}\left(\theta_{1}, \sigma\right) \geqslant \beta(\beta$ 为指定 的小于 1 的数), 则这可以做到: 只须取 $n$ 充分大, 使 $F_{n-1, \sqrt{n} \delta_{0}}$ $\left(-t_{n-1}(\alpha)\right) \geqslant \beta$. 这可以通过查非中心 $t$ 分布表求得. 这个在实用上看也是合理的. 在方差末知时, 均值距离的实际 意义如何, 往往要看方差大小而定. 方差愈大, 一定的均值距离意 义就愈小.好比秤的误差愈大, 两件东西的重量就必须有更大的差 别, 才能较有把握地在这把秤上显示出来. (9) 式中的功效函数, 通 过 $\left(\theta-\theta_{0}\right) / \sigma$ 而依赖于 $(\theta, \sigma)$, 反映了这一点.

类似的结论对两样本 $t$ 检验当然也成立,我们把细节留给读 者去完成.

