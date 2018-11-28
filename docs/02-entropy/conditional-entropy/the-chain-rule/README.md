<p>The chain rule expresses the relation between the conditional entropy and the joint/maringal entropies of the variables involved. We first state and prove the chain rule for two random variables, and then generalize it to \(n\) variables.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition: Chain Rule</strong></h4>
Let \(X\) and \(Y\) be random variables. Then \[ H(XY)= H(X) + H(Y|X) \, . \]
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof hint</span></span></p>
<div id="group2" style="display: none;">
<div class="content-box">We encourage you to try to prove this for yourself. As a starting point, write out the definition of \(H(XY)\), and rewrite the terms \(P_{XY}(x,y)\) into a conditional form in order to relate it to \(H(Y|X)\).
<p><span class="element_toggler" role="button" aria-controls="group2sub" aria-label="Toggler" aria-expanded="false"><span class="Button">Show full proof</span></span></p>
<div id="group2sub" style="display: none;">
<div class="content-box">The chain rule is a matter of rewriting: \begin{align} H(XY) &amp;= -\sum_{x,y} P_{XY}(x,y)\log P_{XY}(x,y) \\ &amp;= -\sum_{x,y} P_{XY}(x,y)\log\bigl(P_X(x)P_{Y|X}(y|x)\bigr) \\ &amp;= -\sum_{x,y} P_{XY}(x,y) \log P_X(x) -\sum_{x,y} P_{XY}(x,y) \log P_{Y|X}(y|x) \\ &amp;= -\sum_{x}P_X(x)\log P_X(x) -\sum_{x,y} P_{XY}(x,y) \log P_{Y|X}(y|x) \\ &amp;= -\sum_{x}P_X(x)\log P_X(x) - \sum_{x} P_X(x)\sum_{y} P_{Y|X}(y|x) \log P_{Y|X}(y|x) \\ &amp;= H(X) + H(Y|X) \, . \end{align} This was to be shown.</div>
</div>
</div>
</div>
</div>
<p>The chain rule immediately results in the so-called 'independence bound':</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Corollary: Subadditivity (independence bound)</strong></h4>
\[ H(XY)\leq H(X)+H(Y) \, . \] Equality holds iff \(X\) and \(Y\) are independent.
<p><span class="element_toggler" role="button" aria-controls="group3" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group3" style="display: none;">
<div class="content-box">\[H(XY) = H(X) + H(Y|X) \leq H(X) + H(Y),\] where the equality is due to the chain rule and the inequality is due to <a href="https://canvas.uva.nl/courses/2205/pages/bounds-on-the-conditional-entropy#condEntropyBounds%20target=">the upper bound on the conditional entropy</a> that \(H(Y|X) \leq H(Y)\) (and equal iff \(X\) and \(Y\) are independent).</div>
</div>
</div>
<p>We can naturally generalize the definition of conditional entropy by applying it to the conditional distribution \(P_{XY|\cal A}\); this results in \(H(X|Y,{\cal A})\), the entropy of \(X\) given \(Y\) and conditioned on the event \(\cal A\). Since the entropy is a function of the <i>distribution</i> of a random variable, the chain rule also holds when conditioning on an event \({\cal A}\). Furthermore, it holds that \[ H(X|YZ) = \sum_z P_Z(z) H(X|Y,Z\!=\!z) \, , \] which is straightforward to verify. With this observation, we see that the chain rule generalizes as follows.</p>
<div id="corGeneralizedChainRule" class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Corollary: generalized chain rule</strong></h4>
Let \(X\), \(Y\) and \(Z\) be random variables. Then \[ H(XY|Z) = H(X|Z) + H(Y|XZ) \, . \]</div>
<p>Inductively applying the (generalized) chain rule implies that for any sequence \(X_1,\ldots,X_n\) of random variables: \[ H(X_1\cdots X_n)= H(X_1) + H(X_2|X_1) + \cdots + H(X_n|X_{n-1}\cdots X_1) \, . \] Combining this with the upper bound on the conditional entropy, we see that subadditivity generalizes to \[H(X_1\cdots X_n)\leq \sum_{i=1}^n H(X_i). \]</p>