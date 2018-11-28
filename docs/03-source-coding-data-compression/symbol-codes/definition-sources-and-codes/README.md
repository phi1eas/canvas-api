<p>We start by investigating symbol codes: codes that encode a source \(P_X\), one symbol at a time. Later on, we will also see codes that group the source symbols together into blocks.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Symbol code</strong></h4>
<p>Let \(P_X\) be the distribution of a random variable \(X\) (with image \({\cal X}\)), and let \(\mathcal{A}\) be a finite set. A symbol code for the source \(P_X\) and with alphabet \(\mathcal{A}\) is an <a href="https://en.wikipedia.org/wiki/Injective_function">injective function</a> \(C : {\cal X} \to \mathcal{A}^*\).</p>
<p>Here, \({\cal A}^* = \bigcup_{n \in \mathbb{N}} {\cal A}^n \cup {\bot}\), and \(\bot\) is the empty string. That is, \(\mathcal{A}^*\) is the set of finite sequences of elements from \(\mathcal{A}\): this operation on sets is called the <a href="https://en.wikipedia.org/wiki/Kleene_star">Kleene star</a>.</p>
</div>
<p>We often refer to the set of codewords, \({\cal C} = \text{im}(C)\), as code and leave the actual encoding function \(C\) implicit.</p>
<p>In many instances, the alphabet \(\mathcal{A}\) is fixed to be the set \(\{0,1\}\) of size 2. In that case, we speak of a <span style="color: #bc0031;"><strong>binary symbol code</strong></span>. The codewords of a binary code are simply binary strings.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Codeword length</strong></h4>
Let \(C : \mathcal{X} \to \mathcal{A}^*\) be an encoding function. For any \(x \in \mathcal{X}\), the length \(\ell(C(x))\) of the codeword \(C(x)\) is the length of the sequence of symbols from \(\mathcal{A}\). That is, if \(C(x) \in \mathcal{A}^k\), then \(\ell(C(x)) = k\).</div>
<p>For practical applications, it is important that the codewords are (on average) short: that way, the transmission or storage of a message is as efficient as possible.</p>