# Definition: Discrete Channel

<p>We now make the notion of 'channel' more precise.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Discrete channel</strong></h4>
A (discrete) channel is a tuple \((\mathcal{X}, P_{Y|X}, \mathcal{Y})\) such that \(\mathcal{X}\) and \(\mathcal{Y}\) are finite sets, and for any \( x \in \mathcal{X}\), the function \(P_{Y|X=x} : \mathcal{Y} \to [0,1]\) is a probability distribution. \(\mathcal{X}\) represents the set of possible inputs, \(\mathcal{Y}\) the set of possible outputs, and \(P_{Y|X}(y|x)\) is the probability of receiving output \(y\) given input \(x\).</div>
<p>Given a channel \((\mathcal{X}, P_{Y|X}, \mathcal{Y})\), fixing a distribution \(P_X\) for the set \(\mathcal{X}\), immediately determines a joint distribution \(P_{XY}\)  and therefore also a distribution \( P_Y \) for \(\mathcal{Y}\) by marginalization.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Binary symmetric channel (BSC)</strong></h4>
Define the binary symmetric channel with parameter \(f \in [0,1/2]\) by \(\mathcal{X} = \mathcal{Y} = \{0,1\}\) and \begin{align*} P_{Y|X}(0|0) &amp;= P_{Y|X}(1|1) = 1-f,\\ P_{Y|X}(0|1) &amp;= P_{Y|X}(1|0) = f.\\ \end{align*} With probability \(f\), the input is flipped, and with probability \(1-f\), it remains unaffected. This channel can be represented visually as:
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322432/preview?verifier=gzc6G8kmsIzQv7u0KXh3VrNNt6WpvSBq0sWaOzXv" alt="BSC-1.svg" width="506" height="140" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322432" data-api-returntype="File"></p>
</div>
<p>We are interested in <span style="color: #bc0031;"><strong>memoryless</strong></span> channels where the probability distribution of the output depends only on the current input. If the channel is used repeatedly, the channel distribution does not change depending on previous inputs and outputs. If we use a discrete memoryless channel \(n\) times, this can be regarded as the channel \((\mathcal{X}^n, P_{Y^n|X^n}, \mathcal{Y}^n)\) where \begin{align} P_{Y^n|X^n}(\vec{y}|\vec{x}) = \prod_{i=1}^n P_{Y|X}(y_i|x_i) \, , \end{align}</p>