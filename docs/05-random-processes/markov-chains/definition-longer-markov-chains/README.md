# Definition: Longer Markov Chains

<p>We can extend the definition of Markov chains to more than three variables:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Markov chain (of length \(n\))</strong></h4>
The random variables \(X_1, X_2, \dots, X_n\) form a Markov chain (notation: \(X_1 \to X_2 \to \cdots \to X_n\)) if for all \(3 \leq i \leq n\), \[ P_{X_i|X_1 \cdots X_{i-1}} = P_{X_i|X_{i-1}}\, . \]</div>
<p>Markov chains of length \(n\) exhibit similar properties to the properties we have seen for Markov chains of length 3. In particular, the reverse chain is also a Markov chain (\(X_n \to \cdots \to X_2 \to X_1\)), and a more general form of the data-processing inequality holds in the sense that the further apart two variables are in the chain, the less correlated they are.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
<p>If \(X_1 \to X_2 \to X_3 \to X_4\) is a Markov chain, the following are Markov chains as well:</p>
<ol type="a">
<li>\(X_1 \to X_2 \to X_3\)</li>
<li>\( X_2 \to X_3 \to X_4 \)</li>
<li>\(X_1 \to X_2X_3 \to X_4 \)</li>
<li>\( X_4 \to X_3 \to X_2 \to X_1\)</li>
</ol>
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">left as exercise</div>
</div>
</div>
<p>In the exercises, we will prove that if \(X_1, X_2, \ldots, X_n\) forms a Markov chain, then for all \(1 \leq i \leq j \leq k \leq n\): \(I(X_i, X_j) \geq I(X_i,X_k)\). This is a generalized form of the <a title="Data-Processing Inequality" href="https://canvas.uva.nl/courses/10933/pages/data-processing-inequality" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/data-processing-inequality" data-api-returntype="Page">data-processing inequality</a>.</p>