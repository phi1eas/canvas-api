# Definition: Confusability Graph

<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Confusability graph</strong></h4>
Let \((\mathcal{X},P_{Y|X},\mathcal{Y})\) be a channel. The confusability graph \(G\) for the channel consists of the set of input symbols of the channel: \[V(G) := \mathcal{X},\] and \[ E(G) := \{\{x,x'\} \subset \mathcal{X} \mid x \neq x' \text{ and } \exists y \in \mathcal{Y} \text{ s.t. } P_{Y|X}(y|x) \cdot P_{Y|X}(y|x') &gt; 0\} \] is the set of input pairs that are confusable (because they reach a shared output symbol \(y \in \mathcal{Y}\)).</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Confusability graph of the noisy typewriter</strong></h4>
Consider again the <a title="Introduction: Zero-Error Channel Coding" href="https://canvas.uva.nl/courses/2205/pages/introduction-zero-error-channel-coding#noisy" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/introduction-zero-error-channel-coding%23noisy" data-api-returntype="Page">noisy typewriter channel</a>. The confusability graph for that channel is:
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/2205/files/329559/preview?verifier=ovFz8cyJwFLqufGN4vmcxsk7N38aHuITUYKcaA64" alt="The confusability graph of the noisy typewriter" width="168" height="181" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/329559" data-api-returntype="File"></p>
This graph is also known as \(C_5\), the circle of size 5. Its independence number is \(\alpha(C_5) = 2\).</div>
<p>In the above example, the independence number of the confusability graph is exactly the number of messages that can be sent over the channel perfectly. This is no coincidence:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
Given a channel with confusability graph \(G\), the maximal message set \([M]\) that can be communicated perfectly in a single channel use is of size \(\alpha(G)\).
<p><span class="element_toggler" role="button" aria-controls="group5" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group5" style="">
<div class="content-box">
<p>Let \((x,x') \in E(G)\), i.e., \(x\) and \(x'\) are confusable. They cannot both be used to send different messages, for suppose there are messages \(m \neq m'\) such that \(\mathtt{enc}(m) = x\) and \(\mathtt{enc}(m') = x'\), then by definition of the confusability graph, there is a \(y \in \mathcal{Y}\) such that \(x\) and \(x'\) are both mapped to \(y\) with nonzero probability. In order to correctly decode in all cases, it must therefore be that \(\mathtt{dec}(y) = m\) and \(\mathtt{dec}(y) = m'\), contradicting the assumption that \(m \neq m'\). Therefore, the number of messages that can be sent over the channel cannot exceed the independence number \(\alpha(G)\).</p>
<p>For the other direction, it is easy to find an encoding and decoding function for \(\alpha(G)\) different messages. Let \(\{x_1, x_2, \ldots, x_{\alpha(G)}\}\) be a largest independent set of \(G\). Define \(\mathtt{enc}(m_i) = x_i\) for all \(i \in [\alpha(G)]\). Then for all \(y \in \mathcal{Y}\), by definition of the confusability graph and the independent set, there is exactly one \(i\) such that \(P_{Y|X}(y|x_i) &gt; 0\). Define \(\mathtt{dec}(y) = m_i\). This code can send \(\alpha(G)\) different messages over the channel without error.</p>
</div>
</div>
</div>