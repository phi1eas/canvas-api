# Definition: Relative Entropy

<p>We can compare two distributions on the same set \(\mathcal{X}\) by considering their relative entropy: this measure reflects how different two distributions are.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Relative entropy</strong></h4>
The relative entropy (or: <a href="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"><span style="color: #bc0031;"><strong>Kullback-Leibler divergence</strong></span></a>) of two probability distributions \(P\) and \(Q\) over the same \(\mathcal{X}\) is defined by \[ D(P||Q) := \sum_{\substack{x \in \mathcal{X} P(x) &gt; 0}} P(x) \log \frac{P(x)}{Q(x)}, \] where by convention, \(\log\frac{p}{0} = \infty\) for all \(p\).</div>
<p>Note that if \(Q(x) = 0\) for some \(x\) with \(P(x) &gt; 0\), then \(D(P||Q) = \infty\).</p>