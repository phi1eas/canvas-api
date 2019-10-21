# The Chain Rule for Mutual Information

<p>Similarly to the <a title="The Chain Rule" href="https://canvas.uva.nl/courses/10933/pages/the-chain-rule" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/the-chain-rule" data-api-returntype="Page">chain rule for entropy</a>, we can prove a chain rule for mutual information:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Corollary: Chain rule for mutual information</strong></h4>
Let \(W,X,Y\) and \(Z\) be random variables. Then \[ I(WX;Y|Z) = I(X;Y|Z)+ I(W;Y|ZX) \, . \]
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof hint</span></span></p>
<div id="group2" style="">
<div class="content-box">Apply the <a title="Conditional Entropy" href="https://canvas.uva.nl/courses/10933/pages/the-chain-rule#corGeneralizedChainRule" data-api-returntype="Page" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/the-chain-rule%23corGeneralizedChainRule">generalized chain rule</a>.
<p><span class="element_toggler" role="button" aria-controls="group2sub" aria-label="Toggler" aria-expanded="false"><span class="Button">Show full proof</span></span></p>
<div id="group2sub" style="">
<div class="content-box">\begin{align} I(WX;Y|Z) &amp;= H(WX|Z) - H(WX|YZ) \\ &amp;= (H(X|Z) + H(W | XZ)) - (H(X|YZ) + H(W|XYZ)) \\ &amp;= H(X|Z) - H(X|YZ) + H(W|XZ) - H(W|XYZ) \\ &amp;= I(X;Y|Z) + I(W;Y|XZ).\end{align}</div>
</div>
</div>
</div>
</div>
<p><span style="color: #ff00ff;"> </span></p>