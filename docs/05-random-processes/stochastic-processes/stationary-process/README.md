# Stationary Process

<p>Often, we will be interested in stochastic processes with specific properties, such as processes where all \(X_i\) are independent, or processes with a Markov-like property. We review several such properties.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Stationary process</strong></h4>
A stochastic process is stationary if for all \(n,k \in \mathbb{N}_+\), \[ P_{X_1 \cdots X_n} = P_{X_{1+k} \cdots X_{n+k}}. \]</div>
<p>Stationary processes are invariant under time shifts: when observing a subsequence of length \(n\), it does not matter where in the process you look exactly.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: i.i.d. process</strong></h4>
Let \(X\) be a random variable. Consider a stochastic process \(\{X_i\}\) where \(P_{X_i} = P_X\) for all \(i\). That is, the random variables in the sequence are all independent and identically distributed. This process is stationary, since for any \(n,k\), it holds that \[ P_{X_1\cdots X_n} = \prod_{i=1}^n P_{X_i} = \prod_{i=1+k}^{n+k} P_{X_i} = P_{X_{1+k} \cdots X_{n+k}}. \]</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Ten fair coins</strong></h4>
The following is another example of a stationary process. Throw a fair coin 10 times: this can be described by the finite sample space \(\{\texttt{H},\texttt{T}\}^{10}\). Define the stochastic process \(\{X_i\}_{i \in \mathbb{N}_0}\) by setting \[ X_i = \left\{ \begin{array}{l l} 1 &amp; \text{ if the [\(i\) mod 10]th coin lands on heads}\\ 0 &amp; \text{otherwise.} \end{array} \right. \] Here, \([k\) mod \(N]\) is defined to be an element of \(\{0,1,2,\ldots,N-1\}\). If we want the first variable in the process to be \(X_1\) instead of \(X_0\), we can determine the value of \(X_i\) based on the \([((i-1)\) mod \(10)+1]\)th coin. 
<p>As an exercise, show that this process is indeed stationary.
</p>
<p><span class="element_toggler" role="button" aria-controls="group7" aria-label="Toggler" aria-expanded="false"><span class="Button">Hint</span></span></p>
<div id="group7" style="">
<div class="content-box">Observe that for all \(i\), \(X_i = X_{i+10} = X_{i+20} = ...\)</div>
</div>
</div>