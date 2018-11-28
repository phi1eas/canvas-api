<p>In the coin-flipping example on the previous page, the typical set eventually contained almost all of the probability. The following proposition states that this is a general property of typical sets. The proposition also bounds the size of the typical set.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
A typical set \(A_{\epsilon}^{(n)}\) satisfies the following:
<ol>
<li>For all \((x_1, \ldots, x_n) \in A_{\epsilon}^{(n)}\), \[H(X) - \epsilon \leq - \frac{1}{n} \log P_{X^n}(x_1, \ldots, x_n) \leq H(X) + \epsilon.\]</li>
<li>\(P[A_{\epsilon}^{(n)}] &gt; 1 - \epsilon\) (for large enough \(n\)).</li>
<li>\(|A_{\epsilon}^{(n)}| \leq 2^{n(H(X) + \epsilon)} \,\).</li>
<li>\(|A_{\epsilon}^{(n)}| \geq (1-\epsilon) 2^{n(H(X) - \epsilon)}\) (for large enough \(n\)).</li>
</ol>
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group1" style="display: none;">
<div class="content-box">
<ol>
<li>This is immediate from the definition (take the logarithm and divide by \(-n\), thereby reversing the inequalities).</li>
<li>This follows from the Asymptotic Equipartition Property: for all \(\epsilon &gt; 0\), \begin{align}P[|-\frac{1}{n} \log P_{X^n}(X_1, \ldots, X_n) - H(X)| &gt; \epsilon] \xrightarrow{n \to \infty} 0,\end{align} that is, \begin{align}\forall (\epsilon &gt; 0) \ \forall (\delta &gt; 0) \ \exists n_0 \ \forall (n \geq n_0) \ P[|-\frac{1}{n} \log P_{X^n}(X_1, \ldots, X_n) - H(X)| \leq \epsilon] &gt; 1 - \delta. \end{align} By choosing \(\delta := \epsilon\), the result follows from the first property.</li>
<li>First, observe that \begin{align} 1 = \sum_{\vec{x} \in \mathcal{X}^n} P_{X^n}(\vec{x}) \geq \sum_{\vec{x} \in A_{\epsilon}^{(n)}} P_{X^n}(\vec{x}) \geq |A_{\epsilon}^{(n)}| \cdot 2^{-n(H(X) + \epsilon}, \end{align} where the last inequality follows by the definition of typicality. The claim follows by multiplying both sides of the equation by \(2^{n(H(X) + \epsilon)}\).</li>
<li>By Property 2, we can choose an \(n\) large enough so that \begin{align} 1 - \epsilon &lt; P[A_{\epsilon}^{(n)}] = \sum_{\vec{x} \in A_{\epsilon}^{(n)}} P_{X^n}(\vec{x}) \leq |A_{\epsilon}^{(n)}| \cdot 2^{-n(H(X)-\epsilon)}, \end{align} where again, the last inequality follows by the definition of typicality.</li>
</ol>
</div>
</div>
</div>