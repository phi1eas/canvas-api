<p>The weak law of large numbers has an entropy variant, which follows almost directly:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Asymptotic Equipartition Property (AEP)</strong></h4>
Let \(X_1, X_2, X_3, \ldots\) be i.i.d. random variables with distribution \(P_X\). Then \[ -\frac{1}{n} \log P_{X_1 \cdots X_n}(X_1, \ldots, X_n) \xrightarrow{p} H(X). \] (Note that \(P_{X_1 \cdots X_n}(X_1, \ldots, X_n)\) is itself a random variable, and \(H(X)\) can be regarded as a constant random variable.)
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group1" style="display: none;">
<div class="content-box">Since the variables \(X_i\) are independent, so are the random variables \(\log P_X(X_i)\). Then \begin{align} -\frac{1}{n} \log P_{X_1\cdots X_n}(X_1, \ldots, X_n) &amp;= -\frac{1}{n} \sum_{i=1}^n \log P_X(X_i)\\ &amp;\xrightarrow{p} - \mathbb{E}[\log P_X(X_i)] = H(X) \end{align} by the weak law of large numbers.</div>
</div>
</div>
<p>In terms of surprisal values, the AEP states that your surprisal value, averaged over all samples, will eventually approach the entropy \(H(X)\) of a single sample.</p>