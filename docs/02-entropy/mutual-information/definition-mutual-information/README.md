# Definition: Mutual Information

<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Mutual information</strong></h4>
Let \(X\) and \(Y\) be random variables. The mutual information \(I(X;Y)\) of \(X\) and \(Y\) is defined as \[ I(X;Y)= H(X) - H(X|Y). \]</div>
<p>Thus, in a sense, mutual information reflects the reduction in uncertainty about \(X\) when we learn \(Y\). Verify the following properties of the mutual information: \begin{align} I(X;Y) &amp;= H(X) + H(Y) - H(XY)\\ I(X;Y) &amp;= I(Y;X) &amp;(``\text{symmetry}") \\ I(X;Y) &amp;\geq 0 &amp;(``\text{positivity}") \\ I(X;Y) &amp;= 0 \text{ iff \(X\) and \(Y\) are independent} \\ I(X;X) &amp;= H(X) &amp;(``\text{self-information}") \end{align}</p>