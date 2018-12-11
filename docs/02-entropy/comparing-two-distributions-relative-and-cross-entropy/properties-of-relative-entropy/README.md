# Properties of Relative Entropy

<p>Even though relative entropy is always nonnegative (see the theorem below), it is not a proper distance measure, because it is not symmetric and does not satisfy the triangle inequality.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Lemma: Alternative Definition of Mutual Information<br></strong></h4>
The mutual information between \(X\) and \(Y\) can be expressed in terms of the relative entropy of their distributions as follows: \[ I(X;Y) = D(P_{XY} || P_X \cdot P_Y) \]
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">The statement follows by writing out the definitions of mutual information and relative entropy, and rearranging terms. \begin{align} I(X;Y) &amp;= H(X) - H(X|Y)\\ &amp;= - \sum_{x \in \mathcal{X}} P_X(x) \log P_X(x) + \sum_{y \in \mathcal{Y}} P_Y(y) \sum_{x \in \mathcal{X}} P_{X|Y}(x|y) \log P_{X|Y}(x|y)\\ &amp;= - \sum_{x \in \mathcal{X}, y \in \mathcal{Y}} P_{XY}(x,y) \log P_X(x)+ \sum_{x \in \mathcal{X}, y \in \mathcal{Y}} P_{XY}(x,y) \log P_{X|Y}(x|y)\\ &amp;= - \sum_{x \in \mathcal{X}, y \in \mathcal{Y}: P_{XY}(x,y) &gt; 0} P_{XY}(x,y) \log P_X(x)+ \sum_{x \in \mathcal{X}, y \in \mathcal{Y} : P_{XY}(x,y) &gt; 0} P_{XY}(x,y) \log P_{X|Y}(x|y)\\ &amp;= \sum_{x \in \mathcal{X}, y \in \mathcal{Y}: P_{XY}(x,y) &gt; 0} P_{XY}(x,y) (-\log P_X(x)+\log P_{X|Y}(x|y))\\ &amp;= \sum_{x \in \mathcal{X}, y \in \mathcal{Y}: P_{XY}(x,y) &gt; 0} P_{XY}(x,y) \log \frac{P_{X|Y}(x|y)}{P_X(x)}\\ &amp;= \sum_{x \in \mathcal{X}, y \in \mathcal{Y}: P_{XY}(x,y) &gt; 0} P_{XY}(x,y) \log \frac{P_{XY}(x,y)}{P_X(x)P_Y(y)}\\ &amp;= D(P_{XY}||P_XP_Y) \end{align}</div>
</div>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Information Inequality</strong></h4>
For any two probability distributions \(P\) and \(Q\) defined on the same \(\mathcal{X}\), \[ D(P||Q) \geq 0. \] Equality holds if and only if \(P = Q\).
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group2" style="">
<div class="content-box">Left as an exercise. Hint: use Jensen's inequality.</div>
</div>
</div>
<p>The above lemma and theorem together show that the mutual information is a measure of 'how independent' the variables \(X\) and \(Y\) are: if \(P_{XY} = P_X \cdot P_Y\), the variables are independent and their mutual information is zero.</p>