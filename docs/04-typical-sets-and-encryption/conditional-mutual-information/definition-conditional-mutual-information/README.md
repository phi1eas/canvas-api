# Definition: Conditional Mutual Information

<p>Applying the <a title="Definition: Mutual Information" href="https://canvas.uva.nl/courses/2205/pages/definition-mutual-information" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/definition-mutual-information" data-api-returntype="Page">definition of mutual information</a> to the conditional distribution \(P_{XY|\cal A}\) naturally defines \(I(X;Y|{\cal A})\), the mutual information of \(X\) and \(Y\) conditioned on the event \(\cal A\):</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Conditional mutual information</strong></h4>
Let \(X,Y,Z\) be random variables. Then the conditional mutual information of \(X\) and \(Y\) given \(Z\) is defined as \[ I(X;Y| Z) = \sum_z P_Z(z) I(X;Y|Z\!=\!z) \, , \] with the convention that the corresponding argument in the summation is \(0\) for \(z\) with \(P_Z(z)=0\).</div>
<p>Conditional mutual information has properties similar to the ones we saw for mutual information: \begin{align} I(X;Y|Z) &amp;= I(Y;X|Z) \\ I(X;Y|Z) &amp;\geq 0 \\ I(X;Y|Z) &amp;= 0 \text{ iff \(X\) and \(Y\) are independent given \(Z\)}. \end{align} Furthermore, the previous bounds \(H(X) \geq 0\), \(H(X|Y) \geq 0\), and \(I(X;Y) \geq 0\), can all be seen as special cases of \(I(X;Y| Z) \geq 0\). These bounds, and any bound they imply, are called <span style="color: #bc0031;"><strong>Shannon inequalities</strong></span>. It is important to realize that \(I(X;Y| Z)\) may be larger or smaller than (or equal to) \(I(X;Y)\).</p>
<p>The following is sometimes used as definition of \(I(X;Y| Z)\): verify it for yourself using the definition above.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Alternative definition</strong></h4>
Let \(X,Y,Z\) be random variables. Then \[ I(X;Y| Z)= H(X|Z)- H(X|YZ) \, . \]
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">\begin{align} I(X;Y|Z) &amp;= \sum_{z \in \mathcal{Z}} P_Z(z) I(X;Y|Z=z) &amp;\text{(by definition)} \\ &amp;= \sum_{z \in \mathcal{Z}} P_Z(z) (H(X|Z=z) - H(X|Y,Z=z)) &amp;\text{(definition of mutual information)} \\ &amp;= \sum_{z \in \mathcal{Z}} P_Z(z) H(X|Z=z) - \sum_{z \in \mathcal{Z}} P_Z(z) H(X|Y,Z=z) \\ &amp;= H(X|Z) - H(X|YZ). \end{align}</div>
</div>
</div>