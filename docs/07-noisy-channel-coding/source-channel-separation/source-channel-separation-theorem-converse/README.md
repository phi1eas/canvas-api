# Source-Channel Separation Theorem: Converse

<p>Conversely, if a source \(V\) has entropy \(H(V)\) that exceeds the channel capacity \(C\), then it is impossible to transmit the source over the channel with arbitrarily small error.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Source-channel separation theorem (converse)</strong></h4>
Let \(V_1, V_2, ..., V_n\) be i.i.d. random variables (the source) distributed according to some \(P_V\). Let \((\mathcal{X}, P_{Y|X},\mathcal{Y})\) be a discrete memoryless channel with capacity \(C\). If \(H(V) &gt; C\), then any source-channel code has an error probability that is bounded away from zero.
<p><span class="element_toggler" role="button" aria-controls="group7" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group7" style="">
<div class="content-box">Assume the error probability \(p_e := P[\hat{V}^n \neq V^n]\) <i>does</i> converge to zero as \(n\) goes to infinity. We show that \(H(V) \leq C\), in order to prove the theorem by contraposition. \begin{align} H(V) &amp;= \frac{H(V^n)}{n} &amp;\text{(since the source is i.i.d.)}\\ &amp;= \frac{1}{n} (H(V^n|\hat{V}^n) + I(V^n;\hat{V}^n)) &amp;\text{(by entropy diagrams)}\\ &amp;\leq \frac{1}{n} (1 + p_e \log(|\mathcal{V}|^n) + I(V^n;\hat{V}^n)) &amp;\text{(by Fano's inequality)}\\ &amp;=\frac{1}{n} + p_e \log(|\mathcal{V}|) + \frac{1}{n}I(V^n;\hat{V}^n)\\ &amp;\leq \frac{1}{n} + p_e \log(|\mathcal{V}|) + \frac{1}{n}I(X^n;Y^n) &amp;\text{(by the data-processing inequality)}\\ &amp;\leq \frac{1}{n} + p_e \log(|\mathcal{V}|) + C &amp;\text{(by the lemma (1) on multiple channel uses)}\\ &amp;\to 0 + 0 + C = C, \end{align} as \(n\) goes to infinity.
<p>
(1) See <a title="Definition: Channel Capacity" href="https://canvas.uva.nl/courses/10933/pages/definition-channel-capacity" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/definition-channel-capacity" data-api-returntype="Page">here</a>.
</p>
</div>
</div>
</div>
<p>We have shown the source-channel separation theorem (the forward direction and its converse) for discrete, memoryless channels, and i.i.d. sources. It also holds for channels with feedback, and any sources that satisfy the asymptotic equipartition property.</p>