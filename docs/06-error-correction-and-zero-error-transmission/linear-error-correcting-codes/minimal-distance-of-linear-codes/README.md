<p>Apart from the trivial way to determine the minimal distance of a code (which is listing the entire codebook and comparing all the codeword pairs), there is a much faster way if the code is linear. It turns out that it already suffices to consider just the Hamming weights of the (nonzero) codewords:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
For a linear code \(C\), the minimal distance is equal to the minimal weight of the nonzero codewords.
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">The following derivation proves the claim: \begin{align} d_{\min} &amp;= \min_{\stackrel{x,y \in C}{x \neq y}} d(x,y) = \min_{\stackrel{x,y \in C}{x \neq y}} \sum_{i=1}^n |x_i - y_i| = \min_{\stackrel{x,y \in C}{x \neq y}} d(x-y,0) = \min_{\stackrel{z \in C}{z \neq 0}} d(z,0) = \min_{\stackrel{z \in C}{z \neq 0}} |z| \, , \end{align}
where |z| denotes the <a href="https://en.wikipedia.org/wiki/Hamming_weight">Hamming weight </a> of a string z.
</div>
</div>
</div>
<p>An equivalent way to determine the minimal distance of a linear code is possible if the parity check matrix is known.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
For a linear code \(C\) with parity check matrix \(H\), the minimal distance \(d_{\min}\) equals the minimum number of columns of \(H\) that are <a href="https://en.wikipedia.org/wiki/Linear_independence">linearly dependent</a>.
<p><span class="element_toggler" role="button" aria-controls="group6" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group6" style="">
<div class="content-box">Left as an exercise.</div>
</div>
</div>