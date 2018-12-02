<p>The whispering game in the example on the previous page exhibits an important property of Markov chains: you can only lose information down the line. Charlie's final message \(C\) does not contain any more information about Alice's original message \(A\) than what was already contained in Bob's message \(B\). This observation is formalized in the following theorem:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Data-processing inequality</strong></h4>
If \(X \to Y \to Z\), then \(I(X;Y) \geq I(X;Z)\). Equality holds if and only if \(I(X;Y|Z) = 0\).
<p><span class="element_toggler" role="button" aria-controls="group3" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group3" style="">
<div class="content-box">The following entropy diagram depicts the area \(I(X;YZ)\):<br><img src="/docs/public/img/275032?verifier=UvTfQBq2E5Wa9KcEMv81FSbjxo7gRKSWa2xQnM3E" alt="DataProcessingInequality.png" width="289" height="338" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/275032" data-api-returntype="File"><br>From the diagram, we can see that \begin{align} I(X;Z) + I(X;Y|Z) = I(X;YZ) = I(X;Y) + I(X;Z|Y). \end{align} Combining this with part (c) of the proposition on the last page, it follows that \begin{align} I(X;Z) + I(X;Y|Z) = I(X;Y). \end{align} Since \(I(X;Y|Z) \geq 0\), the result follows: \(I(X;Z) \leq I(X;Y)\), with equality iff \(I(X;Y|Z) = 0\).</div>
</div>
</div>
The following corollary formalizes the intuition that the mutual information between two random variables can only decrease by post-processing any of the two.
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Corollary</strong></h4>
\(I(X;Y) \geq I(X;g(Y))\) for any two random variables \(X\) and \(Y\), and any function \(g\) on the range of \(Y\).
<div id="group4" style="">
<div class="content-box">Paste proof here</div>
</div>
</div>