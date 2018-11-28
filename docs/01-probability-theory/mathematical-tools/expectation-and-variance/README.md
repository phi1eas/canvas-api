<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Expectation</strong></h4>
The expectation of a <i>real</i> random variable \(X\) is defined as \[ \mathbb{E}[X] := \sum_{x \in \mathcal{X}} P_X(x) \cdot x. \]</div>
<p>Note that if \(X\) is not real, then we can still consider the expectation of some function \(f : \mathcal{X} \to \mathbb{R}\), where \[ \mathbb{E}[f(X)] = \sum_{x \in \mathcal{X}} P_X(x) \cdot f(X). \]</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Variance</strong></h4>
The variance of a <i>real</i> random variable \(X\) is defined as \[ \text{Var}[X] := \mathbb{E}[(X - \mathbb{E}[X])^2]. \]</div>
<p>The variation is a measure for the deviation of the mean. Hoeffding's inequality (here stated for binary random variables) states that for a list of i.i.d. random variables, the average of the random variables is close to the expectation, except with very small probability. We state it here without proof.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Hoeffding's inequality</strong></h4>
Let \(X_1, \ldots, X_n\) be independent and identically distributed binary random variables with \(P_{X_i}(0) = 1 - \mu\) and \(P_{X_i}(1) = \mu\), and thus \(\mathbb{E}[X_i] = \mu\). Then, for any \(\delta &gt; 0\) \[ P\left[\sum_i X_i &gt; (\mu + \delta) \cdot n\right] \leq \exp(-2\delta^2n). \]
</div>