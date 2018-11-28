<p>Let \(X\) be a random variable and \(\cal A\) an event. Applying <a title="Definition: Shannon Entropy" href="https://canvas.uva.nl/courses/2205/pages/definition-shannon-entropy" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/definition-shannon-entropy" data-api-returntype="Page">the definition of entropy</a> to the conditional probability distribution \(P_{X|\cal A}\) allows us to naturally define the entropy of \(X\) conditioned on the event \(\cal A\):</p>
<p>\[ H(X|{\cal A}) := \sum_{x\in {\cal X}} P_{X|{\cal A}}(x)\cdot \log \frac{1}{P_{X|{\cal A}}(x)}. \]</p>
<p>This leads to the following notion:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Conditional entropy</strong></h4>
Let \(X\) and \(Y\) be random variables, with respective images \({\cal X}\) and \({\cal Y}\). The conditional entropy \(H(X|Y)\) of \(X\) given \(Y\) is defined as \[ H(X|Y) := \sum_{y\in {\cal Y}} P_Y(y)\cdot H(X|Y\!=\!y) \, , \] with the convention that the corresponding argument in the summation is \(0\) for \(y \in \cal Y\) with \(P_Y(y)=0\).</div>
<p>Note that the conditional entropy \(H(X|Y)\) is not the entropy of a probability distribution but an expectation: the average uncertainty about \(X\) when given \(Y\).</p>
<p> </p>