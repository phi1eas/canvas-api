# Source-Coding Theorem for Stationary Stochastic Processes

<p>Recall <a title="Theorem: Shannon's Source-Coding Theorem (Optimal Codes)" href="https://canvas.uva.nl/courses/10933/pages/theorem-shannons-source-coding-theorem-optimal-codes" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/theorem-shannons-source-coding-theorem-optimal-codes" data-api-returntype="Page">Shannon's Source-Coding Theorem</a>: it states that an optimal code (for an i.i.d. source \(X\)) has expected codeword length approximately \(H(X)\).</p>
<p>We can state a similar result for stochastic processes:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Source-coding theorem (for stochastic processes)</strong></h4>
Let \(\{X_i\} = X_1, X_2, X_3, ...\) be a stationary stochastic source. Let \(\ell_{\text{min}}(n)\) be the expected minimal codeword length <i>per symbol</i> when encoding blocks of \(n\) source symbols, that is, \(\ell_{\text{min}}(n) := \ell_{\text{min}}(P_{X_1\cdots X_n})/n\). Then \[ \lim_{n \to \infty} \ell_{\text{min}}(n) = H(\{X_i\}). \]
<p><span class="element_toggler" role="button" aria-controls="group7" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group7" style="">
<div class="content-box">By Shannon's souce-coding theorem, we have that for every \(n\), \[ H(X_1X_2\cdots X_n) \leq \ell_{\text{min}}(P_{X_1X_2\cdots X_n}) \leq H(X_1X_2\cdots X_n) + 1. \] Dividing all sides by \(n\), and recalling that for stationary processes, \(H(X_1X_2\cdots X_n)/n\) converges to the entropy rate \(H(\{X_i\})\), the result follows.</div>
</div>
</div>
<p>In the limit, we can compress a stationary stochastic source down to its entropy rate.</p>