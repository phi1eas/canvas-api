# Theorem: Shannon's Source-Coding Theorem (Optimal Codes)

<p>We now know that prefix-free codes can achieve the same minimal code lengths for a source \(P_X\) as the more general class of uniquely decodable codes. How small is this minimal code length in general? In this section we explore the following relation between the minimal code length and the entropy of the source:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Shannon's source-coding theorem (for symbol codes)</strong></h4>
For any source \(P_X\), we have the following bounds: \[ H(X) \leq \ell_{\min}(P_X) \leq H(X) + 1. \]
<p><span class="element_toggler" role="button" aria-controls="group7" aria-label="Toggler" aria-expanded="false"><span class="Button">\(H(X) \leq \ell_{\min}(P_X)\)</span></span></p>
<div id="group7" style="">
<div class="content-box">The proof relies on Kraft's inequality. Let \(C\) be a (uniquely decodable) code, and write \(\ell_x\) for \(\ell(C(x))\) as a notational convenience. For the lower bound, we have that \begin{align} H(X) - \ell_C(P_X) &amp;= - \sum_{x \in {\cal X}} P_X(x) \log(P_X(x)) - \sum_{x \in X} P_X(x) \ell_x\\ &amp;= \sum_{x \in {\cal X}} P_X(x) \left(-\log(P_X(x)) - \log\left(2^{\ell_x}\right)\right)\\ &amp;= \sum_{x \in {\cal X}} P_X(x) \log \left(\frac{1}{P_X(x)\cdot 2^{\ell_x}}\right)\\ &amp;\leq \log\left(\sum_{x \in {\cal X}} \frac{1}{2^{\ell_x}}\right) &amp;&amp;\mbox{(by Jensen's inequality)}\\ &amp;\leq \log(1) = 0&amp;&amp;\mbox{(by Kraft's inequality)} \end{align}</div>
</div>
<p><span class="element_toggler" role="button" aria-controls="group8" aria-label="Toggler" aria-expanded="false"><span class="Button">\(\ell_{\min}(P_X) \leq H(X) + 1\)</span></span></p>
<div id="group8" style="">
<div class="content-box">For the upper bound, let us denote by \(\ell_x\) the surprisal value in bits rounded up to the next integer, i.e. for any \(x \in {\cal X}\), \begin{align} \ell_x := \left\lceil\log\frac{1}{P_X(x)}\right\rceil, \end{align} and note that \begin{align} \sum_{x \in {\cal X}} 2^{-\ell_x} \leq \sum_{x \in {\cal X}} 2^{-\log\frac{1}{P_X(x)}} = \sum_{x \in {\cal X}} P_X(x) = 1. \end{align} Therefore, by Kraft's inequality, there exists a prefix-free code \(C\) such that \(\ell(C(x)) = \ell_x\) for all \(x \in {\cal X}\). This code satisfies \begin{align} \ell_C(P_X) &amp;= \sum_{x \in {\cal X}} P_X(x) \ell_x \\ &amp;\leq \sum_{x \in {\cal X}} P_X(x) \left(\log \frac{1}{P_X(x)} + 1 \right)\\ &amp;= -\sum_{x \in {\cal X}} P_X(x)\log P_X(x) + \sum_{x \in {\cal X}} P_X(x) \\ &amp;= H(X) + 1. \end{align} We have thus constructed a code \(C\) with \(\ell_C(P_X) \leq H(X) + 1\), so \(\ell_{\min}(P_X) \leq H(X) + 1\).</div>
</div>
</div>