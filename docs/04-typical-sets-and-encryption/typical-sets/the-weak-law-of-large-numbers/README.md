# The Weak Law of Large Numbers

<p>Recall the weak law of large numbers from the first homework set. We rephrase it here in terms of converging random variables. It states that if we sample several times from the same distribution, the average converges (in probability) to the expected value of the distribution.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Weak Law of Large Numbers</strong></h4>
Let \(X_1, X_2, \ldots\) be real i.i.d. random variables with mean \(\mu = \mathbb{E}[X_i]\) and variance \(\sigma^2 = \mathbb{E}[(X_i - \mu)^2] &lt; \infty\). Define the random variables \[ S_n := \frac{1}{n} \sum_{i=1}^n X_i. \] Then \(S_n \xrightarrow{p} \mu\), where we interpret \(\mu\) as the constant random variable that is \(\mu\) with probability 1.</div>