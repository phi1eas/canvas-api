# Definition: Channel Capacity

<p>We just discovered that for some noisy channels, zero-error communication is very hard, or even impossible. For example, if Alice and Bob have to communicate over a <a title="Definition: Discrete Channel" href="https://canvas.uva.nl/courses/2205/pages/definition-discrete-channel" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/definition-discrete-channel" data-api-returntype="Page">binary symmetric channel (BSC)</a> that has non-zero bit-flip probability, they cannot hope to do any zero-error communication, because the Shannon capacity of the BSC's confusability graph is zero.</p>
<p>We also saw that error-correcting codes can help deal with such inherently noisy channels. Even though the communication error may not become zero, an error-correcting code can increase the probability of receiving the correct message. It does come at a cost, however, because the codewords are longer than the original messages, and so the amount of information that is transmitted <i>per channel use</i> does not necessarily increase.</p>
<p>In this final part of the module, we explore the limits of how much information can be sent over a channel if a small error is allowed. Central to our study will be the concept of channel capacity. It reflects the maximum amount of information that could <i>in principle</i> be communicated with a single use of a channel. In the next module, we will see how well that theoretical limit can be approached with actual error-correcting codes.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Channel capacity</strong></h4>
The channel capacity \(C\) of a discrete, memoryless channel \((\mathcal{X}, P_{Y|X}, \mathcal{Y})\) is given by \[ C:= \max_{P_X} I(X;Y). \]</div>
<p>Remember that using a certain input distribution \(P_X \) for a channel \( P_{Y|X} \) yields a joint input-output distribution \(P_{XY}\) which determines the real quantity \(I(X;Y) \) we can optimize over. One can <a title="The set of joint distributions { P_{XY} } is compact, and the mutual information is a continuous function from that set to the real numbers. It follows from the extreme-value theorem that the maximum is attained. " data-tooltip='{"tooltipClass":"popover popover-padded", "position":"right"}'>argue</a> that the maximum is attained and therefore the channel capacity is a well-defined quantity.</p>
<p>Important: the channel capacity is often called the Shannon capacity (of a channel). You should not confuse it with the <a title="Shannon Capacity of a Graph" href="https://canvas.uva.nl/courses/2205/pages/shannon-capacity-of-a-graph" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/shannon-capacity-of-a-graph" data-api-returntype="Page">Shannon Capacity of a Graph</a>. Generally, the Shannon capacity of a channel is not equal to the Shannon capacity of its confusability graph.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Capacity of a BSC</strong></h4>
What is the capacity (in terms of \(f\)) of a binary symmetric channel with parameter \(f \in [0,1/2]\)?
<p><span class="element_toggler" role="button" aria-controls="group1a" aria-label="Toggler" aria-expanded="false"><span class="Button">Show hint</span></span></p>
<div id="group1a" style="">
<div class="content-box">Rewrite \(I(X;Y)\) as \(H(Y) - H(Y|X)\) and note that you can compute \(H(Y|X)\) without fixing \(P_X\). Then think about how to maximize \(H(Y)\).
<p><span class="element_toggler" role="button" aria-controls="group1b" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group1b" style="">
<div class="content-box">The channel capacity is \begin{align} \max_{P_X} I(X;Y) &amp;= \max_{P_X} \left( H(Y) - H(Y|X)\right)\\ &amp;= \max_{P_X} \left( H(Y) - \sum_{x \in \mathcal{X}} P_X(x) \cdot H(Y|X=x)\right) \\ &amp;= \max_{P_X} \left( H(Y) - \sum_{x \in \mathcal{X}} P_X(X) \cdot h(f)\right) \\ &amp;= \max_{P_X} \left( H(Y) - h(f)\right) \\ &amp;= 1- h(f). \end{align} The last step follows because \(H(Y)\) is maximized if \(Y\) is uniform, which is achievable by choosing \(X\) to be uniform.</div>
</div>
</div>
</div>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Capacity of a BEC</strong></h4>
<p>Consider the binary erasure channel (BEC) with \(\mathcal{X} = \{0,1\}\) and \(\mathcal{Y} = \{0,1,\bot\}\), where \(\bot\) is the <span style="color: #bc0031;"><strong>erasure symbol</strong></span>, and \(\epsilon \in [0,1]\) is the <span style="color: #bc0031;"><strong>erasure probability</strong></span>:</p>
<p style="text-align: center;"><img src="https://canvas.uva.nl/courses/2205/files/388658/preview?verifier=E9ranqn35eYPibIXdJ5XcEG1CWqNXu5KVumwLJUd" alt="A binary erasure channel" width="240" height="140" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/388658" data-api-returntype="File"></p>
<p>What is the channel capacity of the BEC, as a function of \(\epsilon\)?</p>
<p><span class="element_toggler" role="button" aria-controls="group2a" aria-label="Toggler" aria-expanded="false"><span class="Button">Show hint</span></span></p>
<div id="group2a" style="">
<div class="content-box">Contrary to the previous example, break \(I(X;Y)\) up as \(H(X) - H(X|Y)\), using symmetry of the mutual information. Consider the three possible outputs separately: how much uncertainty is left if you receive output 0? What about output 1? And output \(\bot\)?
<p><span class="element_toggler" role="button" aria-controls="group2b" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group2b" style="">
<div class="content-box">Write \(p\) for \(P_X(0)\). \begin{align*} \max_{P_X} I(X;Y) &amp;= \max_{P_X} \left( H(X) - H(X|Y)\right) \\ &amp;= \max_{p} \left( h(p) - \sum_{y \in \mathcal{Y}} P_Y(y) \cdot H(X|Y=y)\right) \\ &amp;= \max_{p} \left( h(p) - P_Y(\bot) \cdot h(p)\right) \\ &amp;= \max_{p} \left( h(p) (1-\epsilon)\right) \\ &amp;= 1 - \epsilon \, . \end{align*} Again, the last step follows because \(H(X)=h(p)\) is maximized if \(X\) is uniform, hence \(p=\frac12\).</div>
</div>
</div>
</div>
</div>
<p>If a channel is memoryless, then using it more than once does not increase the capacity <i>per transmission</i>. Note that this is different from the zero-error setting, where multiple channel uses can in fact increase the efficiency of getting information across! This is formally captured in the following lemma, which we state without proof:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;" id="lemma"><strong>Lemma: Multiple Channel Uses</strong></h4>
Let \(X_1, ..., X_n =: X^n\) be \(n\) random variables. Let \(Y^n\) be the result of passing \(X^n\) through a discrete memoryless channel of capacity \(C\). Then for any joint distribution \(P_{X^n}\), \[ I(X^n,Y^n) \leq n \cdot C. \]</div>