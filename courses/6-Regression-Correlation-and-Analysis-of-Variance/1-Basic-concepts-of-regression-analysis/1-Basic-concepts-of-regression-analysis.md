---
comments: true
tags:
  - 校订中……
---
# 6.1 回归分析基本概念

<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/6/6.1.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/6/6.1.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/6/6.1.pdf">下载 PDF</a>.</p>
    </embed>
</object>
# 第六章 回归、相关与方差分析 

## 1. 1 回归分析基本概念

本章所要讨论的题目都是在数理统计学中应用很广泛的分 支. 它们有一个共同点, 即都是研究变量之间的关系. 这些变量可 以是随机的, 也可以是非随机 (可以理解为能由人所控制) 的, 但不 能全部为非随机的. 它们的不同之处在于: 回归分析着重在寻求变 量之间近似的函数关系, 相关分析则不着重这种关系, 而致力于寻 求一些数量性的指标, 以刻画有关变量之间关系深浅的程度. 第三 章中讨论过的相关系数, 就是这样的一个指标. 方差分析着重考虑 一个或一些变量对一特定变量的影响有无及大小, 由于其方法是 基于样本方差的分解, 故得名. 以上只是一个很一般的描述, 在以 后的叙述中将加以充实和确切化.

我们先来谈回归分析. “回归”一词的来由将在后面加以解释. 在现实世界中存在着大量这样的情况: 两个或多个变量之间有一 些联系, 但没有确切到可以严格决定的程度. 例如, 人的身高 $X$ 和 体重 $Y$ 有联系,一般表现为 $X$ 大时， $Y$ 也倾向于大, 但由 $X$ 并不 能严格地决定 $Y$. 一种农作物的亩产量 $Y$ 与其播种量 $X_{1}$, 施肥量 $X_{2}$ 有联系,但 $X_{1}, X_{2}$ 不能严格决定 $Y$.工业产品的质量指标 $Y$ 与工艺参数和配方等有联系,但后者也不能严格决定 $Y$.

在以上诸例及类似的例子中, $Y$ 通常称为因变量或预报量, $X, X_{1}, X_{2}$ 等则称为自变量或预报因子. 因变量自变量的称呼借 用自函数关系, 它不十分妥贴, 因为, 有时变量间并无明显的因果 关系存在. 例如, 不好说一个人的身高是因体重是果, 因为你也可 以反过来说, 该人身高是因其体重大. 预报量与预报因子的名称来 源于实际. 因为在应用中,多是借助于一些变量之值去预测另一些 变量之值. 比如说, 用播种量和施肥量去预测产量. 这名称也非十 分完善, 因为在回归分析的某些应用中, 并无预报的含义. 迄今为 止, 对 $X\left(\right.$ 或 $\left.\left(X_{1}, X_{2} \cdots\right)\right)$ 和 $Y$ 并无一种一致采用或公认为妥贴的 称呼, 为简单计, 今后我们将固定使用自变量和因变量这一对名 词.

为什么由 $X_{1}, X_{2}$ 等不能严格决定 $Y$ ? 理由很清楚. 拿农作 物那个例子来说, 影响产量 $Y$ 的因素(变量)很多, 远不止播种量 $X_{1}$ 和施肥量 $X_{2}$ 二者, 其他如灌溉情况, 气温变化情况, 灾害 (病 虫害、风灾之类), 都影响到 $Y$. 这些因素中, 有可以人为控制的 (如已考虑的 $X_{1}, X_{2}$ ), 有原则上可控但因技术、经济力量不及, 或 研究工作目标有限末予控制的, 还有一大批难于控制的随机因素. 因此,已考虑的因素 $X_{1}, X_{2}$ 只能在一定程度上决定产量 $Y$, 其余 则委之于随机误差. 因此, 在回归分析中, 因变量总是看作为随机 变量. 至于自变量则情况较复杂: 有随机的, 如人的身高体重那个 例子, 不是给定身高去测体重, 而是随机地抽出一个人, 同时测其 身高体重,故二者都是随机变量.也有非随机的,农作物例中的播 种量和施肥量即是, 它们的取值可以由人控制. 从数理统计学的理 论上说这二者有差别. 但从实用上说, 人们往往把随机自变量当作 非随机去处理, 但对结果的解释要小心, 以后再谈. 在本章 6.2 和 6.3 这两节中, 除有特别声明, 我们将一律把自变量视为非随机 的.

现设在一个问题中有因变量 $Y$, 及自变量 $X_{1}, \cdots, X_{p}$. 可以设 想 $Y$ 的值由两部分构成: 一部分由 $X_{1}, \cdots, X_{p}$ 的影响所致, 这一 部分表为 $X_{1}, \cdots, X_{p}$ 的函数形式 $f\left(X_{1}, \cdots, X_{p}\right)$. 另一部分则由其 他众多末加考虑的因素, 包括随机因素的影响所致, 它可视为一种 随机误差, 记为 $e$. 于是得到模型:

$$
Y=f\left(X_{1}, \cdots, X_{p}\right)+e
$$

$e$ 作为随机误差, 我们要求其均值为 0 :

$$
E(e)=0
$$

于是得到: $f\left(X_{1}, \cdots, X_{p}\right)$ 就是在给定了自变量 $X_{1}, \cdots, X_{p}$ 之值的 条件下,因变量 $Y$ 的条件期望值. 可写为 *

$$
f\left(X_{1}, \cdots, X_{p}\right)=E\left(Y \mid X_{1}, \cdots, X_{p}\right)
$$

函数 $f\left(x_{1}, \cdots, x_{p}\right)$ 称为 $Y$ 对 $X_{1}, \cdots, X_{p}$ 的 “回归函数”, 而方程

$$
y=f\left(x_{1}, \cdots, x_{p}\right)
$$

则称为 $Y$ 对 $X_{1}, \cdots, X_{p}$ 的 “回归方程”. 有时在回归函数和回归方 程之前加上“理论”二字, 以表明它是直接来自模型, 也可以说是模 型的一个组成部分, 而非由数据估计所得. 后者称为 “经验回归函 数”和“经验回归方程”.

设 $\xi$ 为一随机变量, 则 $E(\xi-c)^{2}$ 作为 $c$ 的函数, 在 $c=E(\xi)$ 处达到最小. 由这个性质, 可以对理论回归函数 $f\left(x_{1}, \cdots, x_{p}\right)$ 作下 面的解释: 如果我们只掌握了因素 $X_{1}, \cdots, X_{p}$, 而希望利用它们的 值以尽可能好地逼近 $Y$ 的值, 则在均方误差最小的意义下, 以使 用理论回归函数为最好.

但在实际问题中,理论回归函数一般总是末知的,统计回归分 析的任务, 就在于根据 $X_{1}, \cdots, X_{p}$ 和 $Y$ 的观察值, 去估计这个函 数, 及讨论与此有关的种种统计推断问题,如假设检验问题和区间 估计问题. 所用的方法, 在相当大的程度上取决于模型中的假定, 也就是对回归函数 $f$ 及随机误差 $e$ 所作的假定. 先说回归函数 $f$. 一种情况是对 $f$ 的数学形式并无特殊的假定, 这种情况称为 “非 参数回归”. 另一种情况, 即目前在应用上最多见的情况, 是假定 $f$ 的数学形式已知, 只其中若干个参数末知. 例如, $p=2$, 而已知 $f\left(x_{1}, x_{2}\right)$ 形如

$$
f\left(x_{1}, x_{2}\right)=c_{1}+c_{2} \mathrm{e}^{c_{3} x_{1}}+c_{4} \log x_{2}
$$

其中 $c_{1}, \cdots, c_{4}$ 是末知参数, 要通过观察值去估计. 这种情况称为 “参数回归”. 其中在应用上最重要且在理论上发展得最完善的特

* 以往我们定义条件期望时, 是假定所有的变量都为随机的. 如今自变量 $X_{1}, \cdots$, $X_{p}$ 并非随机, 故记号 $E\left(Y \mid X_{1}, \cdots, X_{p}\right)$ 只是一种借用. 可以简单地理解为: $Y$ 的分布 依赖于参数 $X_{1}, \cdots, X_{p}$, 故其期望值也应与 $X_{1}, \cdots, X_{p}$ 有关. 例, 是 $f$ 为线性函数的情形:

$$
f\left(x_{1}, \cdots, x_{p}\right)=b_{0}+b_{1} x_{1}+\cdots+b_{p} x_{p}
$$

这种情况叫做“线性回归”, 是我们今后讨论的主要对象. 线性回归 的限制看来较强. 不过, 如果自变量变化的范围不太大, 而曲面 $y$ $=f\left(x_{1}, \cdots, x_{p}\right)$ 弯曲的程度边不过分, 则在较小的范围内, 它可以 近似地用一个平面 (即线性函数) 去代替之, 而不致引起过大的误 差. 其次,有些形式上看是非线性的回归函数, 可能通过自变量的 代换转化为线性的, 见 6.3 节. 因此,线性回归模型有比较大的适 用面, 加之它处理上简便, 成为一个极其重要的模型.

对随机误差 $e$, 我们已假定其均值 $E(e)=0 . e$ 的方差 $\sigma^{2}$ 是回 归模型的一重要参数, 因为

$$
E\left[Y-f\left(X_{1}, \cdots, X_{p}\right)\right]^{2}=E\left(e^{2}\right)=\operatorname{Var}(e)=\sigma^{2}
$$

$\sigma^{2}$ 愈小, 用 $f\left(X_{1}, \cdots, X_{p}\right)$ 逼近 $Y$ 所导致的均方误差就愈小，回归 方程也就愈有用. $\sigma^{2}$ 的大小由什么决定呢? 这就在于以下两点:

1. 在选择自变量时, 是否把对因变量 $Y$ 有重要影响的那些 都收进来了. 如果是这样, 则末被考虑的即作为随机误差去处理的 那些因素, 总的起作用就较小, 因而 $\sigma^{2}$ 也就会较小.反之, 若遗漏 了或因条件关系,使某些对 $Y$ 有重要影响的因素末被考虑,则其 影响进人随机误差 $e$, 将导致 $\sigma^{2}$ 增大.
2. 回归函数的形状是否选得准. 比如, 理论回归函数 $f\left(x_{1}\right.$, $\left.\cdots, x_{p}\right)$ 本是 $\cdots$ 个非线性函数, 而你用一个线性函数 $g\left(x_{1}, \cdots\right.$, $\left.x_{p}\right)$, 则二者的差距 $f-g$ 就作为一种误差进入 $e$ 内, 而加大了它 的亦差.

因此在应用上, 通过观察数据对误差方差 $\sigma^{2}$ 作估计, 也是很 重要的. 如果估计值很大, 超过了该项应用所能承受的范围, 则估 计所得的回归方程意义就不大. 在这个时候, 就有必要再考虑一下 自变量的选择是否抓着了主要因素, 以及所用的回归方程的形式 是否太不符合实际.

如果要处理有关的检验和区间估计问题, 比方说, 取定了线性 回归函数 $b_{0}+b_{1} x_{1}+\cdots+b_{p} x_{p}$, 有对末知系数 $b_{i}$ 等作假设检验和 区间估计的问题, 则只有在假定随机误差 $e$ 服从正态分布 $N\left(0, \sigma^{2}\right)$ 时, 才有满意的小样本方法. 因此, 在实用回归分析中, 常 假定误差服从正态分布. 经验证明: 对多数应用问题来说,这个假 定是可以接受的, 如果没有这个假定, 那就需要使用大样本方法.

回归分析的应用, 可以归纳为以下几方面.

第一方面是纯描述性的. 为简单计, 以一个自变量 $X$ 的情况为例, 因变量总 记为 $Y$. 假定在工作中我们经常要记录 $X$ 和 $Y$ 之值(比如说, $X$ 代表月份, $Y$ 代 表该月的产值), 而积累了一批数据 $\left(X_{1}\right.$, $\left.Y_{1}\right),\left(X_{2}, Y_{2}\right), \cdots,\left(X_{n}, Y_{n}\right)$. 把它们标 在直角坐标系上, 称为散点图. 这往往是

![](https://cdn.mathpix.com/cropped/2023_07_12_95110c656c320aa30a1ag-5.jpg?height=346&width=506&top_left_y=775&top_left_x=1209)

图 6.1 杂乱无章的, 但仍可能有某种趋势存在. 如图 6.1 中的点虽系杂乱 无章, 但大体呈现出一种直线走向的趋势. 用回归分析的方法可找 出一条较好地代表这些点的走向的直线 $l$. 在一定程度上, 这条直 线 $l$ 描述了所观察到的这批数据所遵从的规律, 虽不十分准确, 但 有时很有用.

这种应用之所以称为描述性的, 是因为它只是对数据的一种 “总结”, 它只涉及现有数据, 不超出其外, 用统计的语言说, 它并不 企图对数据 $\left(X_{1}, Y_{1}\right), \cdots,\left(X_{n}, Y_{n}\right)$ 所来自的总体作任何推断.

第二方面是估计回归函数 $f$. 仍拿人的身高 $X$ 和体重 $Y$ 这个 例子来说, 姑且把 $X$ 视为自变量而 $Y$ 为因变量. 若假定 $(X, Y)$ 服 从二维正态分布, 则如在第二章中已证明的, $Y$ 对 $X$ 的回归函数 $f(x)$, 即条件期望 $E(Y \mid X=x)$, 为 $x$ 的线性函数 $b_{0}+b_{1} x$. 如果 通过样本对 $b_{0}$ 和 $b_{1}$ 作出了估计 $\hat{b}_{0}$ 和 $\hat{b}_{1}$, 则用 $\hat{b}_{0}+\hat{b}_{1} x$ 去估计 $b_{0}+b_{1} x$. 在本例中, 后者就是在身高为 $x$ 的人群中的平均体重. 这在应用上很有意义,因为在不少问题中, 我们所关心的正是这个 平均值. 再拿亩产 $Y$ 与播种量 $X_{1}$ 与施肥量 $X_{2}$ 的关系这个例子 来说,也许我们所关心的正是在一定播种量 $x_{1}$ 和一定施肥量 $x_{2}$ 之下, 平均亩产能达到多少. 这就是 $Y$ 对 $X_{1}, X_{2}$ 的回归函数 $f\left(x_{1}, x_{2}\right)$.

第三方面是预测, 即在特定的自变量值 $\left(x_{10}, \cdots, x_{p 0}\right)$ 之下, 去 预测因变量 $Y$ 将取的值 $y_{0}$. 例如, 随意碰到一个人测出其身高为 $x_{0}$, 而没有秤其体重或秤了没有把结果告诉你, 让你去预测这人 体重有多少. 这与估计身高为 $x_{0}$ 的人群的平均体重 $f\left(x_{0}\right)=$ $E\left(Y \mid X=X_{0}\right)$ 不同. 后者并非特定的一个身高为 $x_{0}$ 的人的体重， 而是全体这样的人体重的平均值，而预测的对象则是这个特定的 人的体重. 从模型上可以这样看: 设在 $X=X_{0}$ 处进行观察, 随机 误差为 $e_{0}$, 而 $Y$ 之值为 $y_{0}$, 则 $y_{0}=f\left(x_{0}\right)+e_{0}$. 为了预测 $y_{0}$, 需要 对 $f\left(x_{0}\right)$ 进行估计, 同时也对随机误差值 $e_{0}$ 作估计, 把二者相加 得出 $y_{0}$. 随机误差 $e_{0}$ 之值凭机会而定, 没有什么好的估计方法, 只能根据其均值为 0 这一点, 将其值估计为 0 . 于是 $Y$ 的预测值就 取为回归函数 $f(x)$ 在这个点 $x_{0}$ 处的估计 $\hat{f}\left(x_{0}\right)$.

由这里得出两条结论: 一是预测问题与回归函数问题虽然在 实质上很不一样 (如前面所曾解释的), 但二者之解则一样. 因为这 一点, 有些著作没有强调这二者的区别所在.二是预测的精度要比 估计回归函数的精度差. 因为在预测中,除了估计回归函数有一个 误差外, 还要加上一个随机误差 $e_{0}$. 这一点在考虑区间估计时能 更清楚地看出来.

第四方面是控制. 在这类应用中, 不妨把自变量解释为输入 值, 因变量解释为输出值. 目标是要把输出值控制在给定的水平 $y_{0}$. 若通过数据估计出了经验回归方程 $y=\hat{f}\left(x_{1}, \cdots, x_{p}\right)$, 则根据 这方程可调整自变量 $X_{1}, \cdots, X_{p}$ 的取值, 以达到上述目的. 例如, 自变量 $X$ 是用药量, 而 $Y$ 是某种生理指标, 例如血压, 调整用药 量以使血压达到某种认为是正常的水平.

我们提一下 “回归设计”这个概念. 为了估计理论回归函数 $f\left(x_{1}, \cdots, x_{p}\right)$, 需要对自变量 $X_{1}, \cdots, X_{p}$ 和因变量 $Y$ 进行观测. 有 两种情况: 一是自变量也是随机的, 如人的身高体重那个例子, 这 时除了一般地保证抽样的随机性以外, 就没有多少可做的事情了. 例如在一大群人中抽取若干以量测其身高体重, 则只须尽力保证 人群中的每一个有同等的被抽出的机会.

另一种情况是自变量是非随机的, 其取值在一定限度内可由 人去控制, 这时, 为保证取得最大的效果,应对自变量在各次试验 中所取的值进行适当的规划. 例如, 若在将来的应用中自变量多取 某区域 $B$ 上之值,则在进行试验时就要让自变量多在这个范围内 取值. 也可以设想,试验点在空间的排列可能需要有某种对称性, 以便于统计分析. 这些问题的研究构成了回归分析的一个分支,叫 做回归设计, 它也可以看作是试验设计这个统计学分支的一个组 成部分,本章将不讨论这方面的问题.

最后我们来解释一下“回归”这名称的由来.这个术语是英国 生物学家兼统计学家 F. 高尔顿在 1886 年左右提出来的. 人们大 概都注意到, 子代的身高与其父母之身高有关. 高尔顿以父母之平 均身高 $X$ 作为自变量,某成年子女身高的平均 $Y$ 为因变量. 他观 察了 1074 对父母及某成年子女身高的平均, 将所得 $(X, Y)$ 值标 在直角坐标系上, 发现二者的关系近乎一条直线,有如图 6.1. 总 的趋势是 $X$ 增加时 $Y$ 倾向于增加一一这是意料中的结果. 有意思 的是, 高尔顿对所得数据作了深人一层的考察, 而发现了某种有趣 的现象.

高尔顿算出这 1074 个 $X$ 值的算术平均为 $\bar{X}=68$ 英寸 (1 英 寸为 2.54 厘米), 而 1074 个 $Y$ 值的算术平均为 $\bar{Y}=69$ 英寸, 子代 身高平均说增加了 1 英寸, 这个趋势现今人们也已注意到. 以此为 据, 人们可能会这样推想: 如果父母平均身高为 $a$ 英寸,则这些父 母的子代平均身高,应为 $a+1$ 英寸, 即比父代多 1 英寸. 但高尔 顿观察的结果与此不符: 他发现: 当父母平均身高为 72 英寸时, 他 们的子代身高平均只有 71 英寸, 不仅达不到预计的 $72+1=73$ 英 寸, 反而比父母平均身高小了.反之, 若父母平均身高为 64 英寸, 则观察数据显示子代平均身高为 67 英寸, 比预计的 $64+1=65$ 英 寸要多.

高尔顿对此的解释是: 大自然有一种约束机制, 使人类身高分 布保持某种稳定形态而不作两极分化. 这就是一种使身高“回归于 中心”的作用.例如, 父母身高平均为 72 英寸, 比他们这一代平均 身高 68 英寸高出许多, “回归于中心”的力量把他们子代的身高拉 回来一些: 其平均只有 71 英寸, 反比父母平均身高小, 但仍超过子 代全体平均 69 英寸.反之, 当父母平均身高只有 64 英寸一一远低 于他们这一代的平均值 68, 而“回归于中心”的力量将其子代身高 拉回去一些, 其平均值达到 67 , 增长了 3 英寸, 但仍低于子代全体 平均值 69 .

正是通过这个例子, 高尔顿引人了回归这个名词. 现在我们觉 得, 高尔顿的例子只反映了变量关系中的一种情况, 在其他涉及变 量关系的众多情况中,多不必如此,故拿这个名称作为变量关系统 计分析的称呼, 实不见得恰当. 但这个名词现今已沿用成习, 如硬 要改变, 反觉多此一举了.
