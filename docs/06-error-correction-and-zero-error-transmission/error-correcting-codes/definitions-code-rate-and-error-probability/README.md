<p>In order to get as much information through a channel as possible, we can encode messages before sending them through the channel.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Code</strong></h4>
Let \(M, n \in \mathbb{N}\). An \((M,n)\)-code for the channel \((\mathcal{X},P_{Y|X},\mathcal{Y})\) consists of
<ul>
<li>An index set \([M] = \{1, \ldots, M\}\) representing the set of possible messages.</li>
<li>A (possibly probabilistic) encoding function \(\mathtt{enc} :[M] \to \mathcal{X}^n\). This encoding function should be injective. \(n\) represents the number of channel uses we need to send a single message.</li>
<li>A deterministic decoding function \(\mathtt{dec} : \mathcal{Y}^n \to [M]\). The set of all codewords, \(\{\mathtt{enc}(1), \ldots, \mathtt{enc}(M)\}\) is called the <span style="color: #bc0031;"><strong>codebook</strong></span>.</li>
</ul>
</div>
<p>An alternative notation for codes is <span style="color: #bc0031;"><strong>\([n,k]\) code</strong></span>, using box brackets instead of round brackets: such a code encodes a \(k\)-bit message into \(n\) bits. In the notation of the above definition, an \([n,k]\) code would be an \((2^k,n)\) code.</p>
<p>The number of bits of information that are transmitted per channel use is captured by the following notion:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Rate</strong></h4>
The rate of an \((M,n)\)-code is defined as \[ R := \frac{\log M}{n}. \]</div>
<p>Given a code for a specific channel, we can study the probability that an error occurs while transmitting a message.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Probability of error</strong></h4>
Given an \((M,n)\) code for a channel \((\mathcal{X},P_{Y|X},\mathcal{Y})\), the probability of error \(\lambda_m\) is the probability that the decoded output is not equal to the input message \(m\). More formally, \[ \lambda_m^{(n)} := P[\mathtt{dec}(Y^n) \neq m \mid X^n = \mathtt{enc}(m)]. \] Given this quantity, the <span style="color: #bc0031;"><strong>maximal probability of error</strong></span> is defined as \[\lambda^{(n)} := \max_{m \in [M]} \lambda_m^{(n)}.\] Similarly, the <span style="color: #bc0031;"><strong>average probability of error</strong></span> is defined as \[ p_e^{(n)} := \frac{1}{M} \sum_{m=1}^M \lambda_m^{(n)}. \]</div>