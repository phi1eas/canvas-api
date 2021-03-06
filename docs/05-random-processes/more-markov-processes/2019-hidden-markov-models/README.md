# 2019: Hidden Markov Models

<p>\[\begin{align}

\sum_{k=(n+1)/2}{n} \binom{n}{k} 0.1^k 0.9^{n-k} &amp;\approx \binom{n}{(n+1)/2} 0.1^{(n+1)/2} 0.9^{(n-1)/2}\\

&amp;= \binom{n}{(n+1)/2} 0.1 \cdot 0.09^{(n-1)/2}\\

&amp;\approx 2^{n \cdot h(1/2)} \cdot 0.1 \cdot 0.09 \cdot {(n-1)/2}\\

&amp;= 2^{n} \cdot 0.1 \cdot 0.09 \cdot {(n-1)/2}\\

\end{align}\]

</p>
<p> </p>
<p>Intuitively, some of the stochastic processes we have seen in the previous sections are more predictable than others. The periodic Markov process from <a title="Markov Process: Irreducibility, Periodicity, Convergence" href="https://canvas.uva.nl/courses/10933/pages/markov-process-irreducibility-periodicity-convergence#example3" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/markov-process-irreducibility-periodicity-convergence%23example3" data-api-returntype="Page">Example 3</a> is not so surprising anymore as soon as the first \(\texttt{b}\) is observed. In this section, we will study a measure for the unpredictability of a stochastic process: the entropy rate.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Entropy rate</strong></h4>
The entropy rate \(H(\{X_i\})\) of a stochastic process \(\{X_i\}\) is \[ H(\{X_i\}) := \lim_{n \to \infty} \frac{1}{n} H(X_1, \dots, X_n), \] if the limit exists, and undefined otherwise.</div>
<p>In the literature, the entropy rate is often denoted \(H(\mathcal{X})\), referring to the common support of the variables in the stochastic process. The notation \(H(X)\) is also sometimes used, but this can be ambiguous and confusing. The entropy rate reflects the way in which the entropy of the sequence (observed so far) grows as \(n\) grows large.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Consider a process \(\{X_i\}\) where the \(X_i\) are i.i.d. sampled from \(P_X\). Then \begin{align*} H(\{X_i\}) &amp;= \lim_{n \to \infty} \frac{1}{n} H(X_1, \dots X_n)\\ &amp;= \lim_{n \to \infty} \frac{1}{n} \left( H(X_1) + H(X_2) + \ldots + H(X_n) \right)\\ &amp;= \lim_{n \to \infty} \frac{n}{n} H(X)\\ &amp;= H(X). \end{align*} So, every new coin toss increases the entropy of the entire observed sequence by \(H(X)\).
<p><span class="element_toggler" role="button" aria-controls="group15" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group15" style="">
<div class="content-box">decide whether this button is necessary, and whether the title of this block should be question instead of example</div>
</div>
</div>
<p>We can also define an alternative measure of the unpredictability of a stochastic process, where we focus not on the amount of entropy in the entire sequence observed so far, but on the amount of entropy present in the current random variable, given the past sequence.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Entropy rate given the past</strong></h4>
The entropy rate given the past \(H'(\{X_i\})\) of a stochastic process \(\{X_i\}\) is \[ H'(\{X_i\}) := \lim_{n \to \infty} H(X_n | X_1, \dots, X_{n-1}), \] if the limit exists, and undefined otherwise.</div>
<p>For all stationary processes, this alternative definition turns out to coincide with the original definition of entropy rate. In order to show this, we need an analytic statement about the convergence of sums.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Cesàro mean</strong></h4>
If \(\lim\limits_{n \to \infty} a_n = a\) and \(b_n = \frac{1}{n} \sum_{i=1}^n a_i\), then \(\lim\limits_{n \to \infty} b_n = a\).
<p><span class="element_toggler" role="button" aria-controls="group16" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group16" style="">
<div class="content-box"><a id="media_comment_maybe" class="instructure_file_link instructure_video_link" title="05 Cesàro mean.mp4" href="https://canvas.uva.nl/courses/10933/files/1322409/download?verifier=mSSjraPk649WGEVPcF6grqw4FBo01lldX2ViURhC&amp;wrap=1" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322409" data-api-returntype="File">05 Cesàro mean.mp4</a></div>
</div>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem</strong></h4>
For a stationary process \(\{X_i\}\), it holds that \(H(\{X_i\}) = H'(\{X_i\})\) (and both limits exist).
<p><span class="element_toggler" role="button" aria-controls="group17" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group17" style="">
<div class="content-box">We first show that \(H(X_n \mid X_1, \dots, X_{n-1})\) is a non-increasing function of \(n\): \begin{align} H(X_{n}|X_1, \dots, X_{n-1}) &amp;= H(X_{n+1}|X_2, \dots, X_{n}) &amp;\text{(stationary)}\\ &amp;\geq H(X_{n+1}|X_1, X_2, \ldots, X_{n}) &amp;(\href{$WIKI_REFERENCE$/pages/bounds-on-the-conditional-entropy}{\text{Bounds on the Conditional Entropy}}). \end{align} Combined with the fact that \(H(X_n \mid X_1, \dots, X_{n-1})\) is lower bounded by 0, this implies that the limit \(\lim_{n \to \infty} H(X_n \mid X_1, \dots, X_{n-1})\) must exist. It is \(H'(\{X_i\})\). It remains to show that \(H(\{X_i\}) = H'(\{X_i\})\): \begin{align} H(\{X_i\}) &amp;= \lim_{n \to \infty} \frac{1}{n} H(X_1, \dots, X_n)\\ &amp;= \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n H(X_i \mid X_1, \dots, X_{i-1})\\ &amp;= H'(\{X_i\}). \end{align} The final equality follows from the Cesaro mean.</div>
</div>
</div>