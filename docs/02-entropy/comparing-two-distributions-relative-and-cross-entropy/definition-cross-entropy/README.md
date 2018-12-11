# Definition: Cross Entropy

<p>Suppose you draw samples from a set \(\mathcal{X}\), according do a distribution \(P\), while <i>thinking</i> you are drawing those samples according to a distribution \(Q\). How surprised do you expect to be? This surprisal value is expressed by the <span style="color: #bc0031;"><strong>cross entropy</strong></span>, a quantity that is very closely related to the relative entropy.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Cross Entropy</strong></h4>
The cross entropy of two probability distributions \(P\) and \(Q\) over the same \(\mathcal{X}\) is defined by \[ H_C(P,Q) := - \sum_{\substack{x \in \mathcal{X}, P(x) &gt; 0}} P(x) \log Q(x). \]</div>
<p>There are a few things to note about this definition:</p>
<ul>
<li>Note that if \(Q(x) = 0\) for some \(x\) with \(P(x) &gt; 0\), then \(H_C(P,Q) = \infty\).</li>
<li>Also note that \(H_C\) is a function of the <i>distributions</i> \(P\) and \(Q\). With regular Shannon entropy, we can be sloppy with the notation, and write \(H(X)\) instead of the more correct \(H(P)\). Here, that sloppy notation would lead to ambiguous expressions.</li>
<li>In the literature, the notation \(H(P,Q)\) is often used to denote the cross entropy. This notation can potentially be confused with the notation for joint entropy, so we use the subscript \(C\) to make the distinction explicit.</li>
</ul>
<p>The cross entropy often pops up in topics related to machine learning: a system usually learns from a set of <i>training data</i>, from which it hypothesizes a certain distribution \(Q\) (on letter frequencies, cluster sizes, or whatever the system is learning about). When the system is released into the real world, it encounters a (possibly) different distribution \(P\). The cross entropy \(H_C(P,Q)\) quantifies how well the system performs in the real world when it was trained on the training set.</p>