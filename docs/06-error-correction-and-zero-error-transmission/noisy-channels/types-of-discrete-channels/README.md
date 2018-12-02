<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Deterministic channel</strong></h4>
A channel is deterministic if \(H(Y|X) = 0\). In other words, \[ \forall x \in \mathcal{X}\ \exists y \in \mathcal{Y}: P_{Y|X}(y|x) = 1. \]</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Lossless channel</strong></h4>
A channel is lossless (or <span style="color: #bc0031;"><strong>ideal</strong></span>) if \(H(X|Y) = 0\). In other words, \[ \forall y \in \mathcal{Y}\ \exists! x \in \mathcal{X}: P_{Y|X}(y|x) &gt; 0. \] (the notation \(\exists!x\) means that there exists <i>exactly</i> one such \(x\).)</div>
<p>In a deterministic channel, the output is completely determined by the input, whereas in a lossless channel, the input is completely determined by the output. A <span style="color: #bc0031;"><strong>noiseless</strong></span> channel is a channel that is both deterministic and lossless.</p>