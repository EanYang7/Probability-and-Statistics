---
comments: true
tags:
  - 校订中……
---
# 练习
<object data="https://eanyang7.github.io/Probability-and-Statistics/assets/3/exercises.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://eanyang7.github.io/Probability-and-Statistics/assets/3/exercises.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://eanyang7.github.io/Probability-and-Statistics/assets/3/exercises.pdf">下载 PDF</a>.</p>
    </embed>
</object>
1. 计算对数正态分布的均值和方差 (对数正态分布见第二章习题 19).
2. 计算均匀分布 $R(a, b)$ 的峰度系数.
3. 计算超几何分布的均值和方差.
4. 一人有 $N$ 把钥匙, 每次开门时, 他随机地拿出一把 (只有一把钥题能 打开这道门), 直到门打开为止. 以 $X$ 记到此时为止用的钥题数 (包括最后拿 对的那一把). 按以下两种情况分别计算 $E(X):(a)$ 试过不行的不再放回去. (b) 试过不行的仍放回去.

*一般 $\Phi(x)$ 的表上只列出当 $\Phi(x) \geqslant 1 / 2$ 时, $x$ 之值. 若 $\Phi(x)<1 / 2$, 则须先由公 式 $\Phi(-x)=1-\Phi(x)(>1 / 2)$ 查出 $-x$ 再得出 $x$. 有的表列出的是由 $2(1-\Phi(x))$ 之 值求 $x(x>0)$. 这时对本例而言. 应先由 $2(1-\Phi(y))=0.2$, 定出 $y$, 再取 $x=-y$ 即 得。 5. 某县有 $N$ 农户, 其年收人分别为 $a_{1}, \cdots, a_{N}$. 为估计平均收人 $a=\left(a_{1}\right.$ $\left.+\cdots+a_{N}\right) / N$, 随机不放回地抽出 $n$ 农户 $(1 \leqslant n \leqslant N)$, 以 $X_{1}, \cdots, X_{n}$ 记所抽 出的 $n$ 农户的年收人, 而以 $X=\left(X_{1}+\cdots+X_{n}\right) / n$ 去估计 $a$. 计算 $E(\bar{X})$ 和 $\operatorname{Var}(\bar{X})$.

6. 一盒中有 $n$ 个不同的球, 其上分别写数字 $1,2, \cdots, n$. 每次随机抽出 1 个, 登记其号码, 放回去, 再抽, 一直抽到登记有 $r$ 个不同的数字为止. 以 $X$ 记到这时为止的抽球次数,计算 $E(X)$.
7. 把 $r$ 个球随机地放入 $n$ 个盒子中, 以 $X$ 记空盒个数, 计算 $E(X)$. 此 题如直接从计算 $P(X=k)$ 出发很难, 但用下述步骤可以解决.

(a) 以 $p_{k}(r, n)$ 记 $r$ 个球随机放人 $n$ 盒恰有 $k$ 个空盒的概率, 用全概率 公式证明:

$$
p_{k}(r+1, n)=p_{k}(r, n) \frac{n-k}{n}+p_{k+1}(r, n) \frac{k+1}{n}
$$

(b) 以 $m_{r}$ 记题中要计算的均值 $E(X)$. 由 (a) 中得出的公式 (1) 两边乘 $k$ 对 $k$ 求和, 证明

$$
m_{r+1}=\left(1-\frac{1}{n}\right) m_{r}, \quad r=0,1,2, \cdots
$$

再由 $m_{0}=n$ 即得 $m_{r}=n\left(1-\frac{1}{n}\right)^{r}$.

8. 设 $n$ 为自然数, $f(x)=C /\left(1+x^{2}\right)^{n}$, 找常数 $C$, 使 $f(x)$ 为概率密度 函数, 并计算其均值方差.
9. 设 $X_{1}, X_{2}$ 独立, 都服从标准正态分布 $N(0,1)$. 记 $Y_{1}=\max \left(X_{1}\right.$, $\left.X_{2}\right), Y_{2}=\min \left(X_{1}, X_{2}\right)$. 计算 $E\left(Y_{1}\right), E\left(Y_{2}\right)$.
10. 设 $X_{1}, X_{2}$ 独立,都服从卡方分布,而常数 $b$ 非 0 非 1 , 则 $X_{1}+b X_{2}$ 决不服从卡方分布。
11. 设 $X, Y$ 独立, 都服从标准正态分布, 而 $Z=\left(a X^{2}+b Y^{2}\right) /\left(X^{2}+\right.$ $\left.Y^{2}\right)$, 其中 $a, b$ 为常数. 计算 $E(Z)$ 和 $\operatorname{Var}(Z)$.
12. 设随机变量 $X$ 只取非负值, 其分布函数为 $F(x)$, 证明: 在以下两种 情况都有

$$
E(X)=\int_{0}^{\infty}[1-F(x)] \mathrm{d} x
$$

(a) $X$ 有概率密度函数 $f(x)$.

(b) $X$ 为离散型, 有分布 $P(X=k)=p_{k}, k=0,1,2, \cdots$

注: 公式 (2)对任何非负随机变量都对,并不限于 (a),(b)两种情况 . 但证 明超出初等方法之外

13. 设 $X_{1}, X_{2}$ 独立同分布,都只取正值,则必有 $E\left(X_{1} / X_{2}\right) \geqslant 1$, 等号当 且仅当 $X_{1}, X_{2}$ 只取一个值时成立.

注: 按此题结论, 也有 $E\left(X_{2} / X_{1}\right) \geqslant 1\left(X_{1}, X_{2}\right.$ 地位平等 $)$, 故 $E\left(X_{1} / X_{2}\right)$ $E\left(X_{2} / X_{1}\right) \geqslant 1$, 但 $\left(X_{1} / X_{2}\right)\left(X_{2} / X_{1}\right) \equiv 1$.

14. 设 $X_{1}, \cdots, X_{n}$ 独立同分布,都只取正值. 证明:

$$
E\left(\frac{X_{1}}{X_{1}+\cdots+X_{n}}\right)=\frac{1}{n}
$$

15. 设 $p_{1}, \cdots, p_{n}$ 都界于 0,1 之间,记 $p$ 为它们的算术平均. 作两串独立 试验, 每串各 $n$ 次, 在第一串中, 事件 $A$ 在各次试验中发生的概率, 依次为 $p_{1}, \cdots, p_{n}$. 在第二串中, 事件 $A$ 在各次试验中发生的概率始终保持为 $p$. 以 $Y_{1}$ 和 $Y_{2}$ 分别记在第一串和第二串试验中事件 $A$ 发生的总次数. 证明 $Y_{1}$, $Y_{2}$ 有相同均值, 而 $\operatorname{Var}\left(Y_{1}\right) \geqslant \operatorname{Var}\left(Y_{2}\right)$, 等号当且仅当 $p_{1}=\cdots=p_{n}=p$ 时成 立. 试给这后一结论以一直观的解释.
16. 设随机变量 $X$ 只取 $[0,1]$ 上的值. 证明 $\operatorname{Var}(x) \leqslant 1 / 4$. 指出等号达到 的情况，把这结果推广到 $X$ 只取 $[a, b]$ 上的值的情况.
17. 在第一章例 1.2 中, 若先到的人必等到后到的人来了为止, 问先到 的人平均要等多久?
18. 设 $X$ 服从指数分布, 试计算其中位数 $m$ 以及 $E|X-m|$.
19. 设 $X$ 有概率密度函数 $f(x)$. 令 $h(a)=E|X-a|$. 证明: 当 $a$ 等于 $X$ 的中位数 $m$ 时, $h(a)$ 达到最小 (这是中位数一个重要性质).
20. 解第二章 27 题, 用如下的方法: 找 $b$, 使 $X+b Y$ 和 $X-b Y$ 的相关系 数为 0 . 这比用第二章的方法简单得多.
21. 设 $X_{1}, X_{2}$ 独立, 分别有概率密度函数 $f\left(x_{1}\right)$ 和 $g\left(x_{2}\right)$. 试求 $Y=$ $X_{1} X_{2}$ 的密度函数,并用所得结果证明

$$
E(Y)=E\left(X_{1}\right) E\left(X_{2}\right)
$$

