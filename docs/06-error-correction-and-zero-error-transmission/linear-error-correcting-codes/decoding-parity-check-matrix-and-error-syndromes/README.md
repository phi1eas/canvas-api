# Decoding: Parity-Check Matrix and Error Syndromes

<p>The decoding operation can be described by defining the parity-check matrix:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Parity-check matrix</strong></h4>
Let \(C\) be a code with generator matrix \[G^T = \left(\begin{array}{c} \mathbb{I}_k \\ \hline P \end{array}\right) \, .\] Then the parity check matrix for \(C\) is given by \[ H := \left( - P \mid \mathbb{I}_{n-k}\right). \] Note that if \(\mathcal{X}^n = \{0,1\}^n\), then \(P\) is a matrix with binary entries, and hence \(-P = P\).</div>
<p>The parity-check matrix shows whether or not an error has occurred, and if it did, what kind of error occurred. The information about the error is contained in the syndrome, which you get by applying the parity check to the received codeword.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Syndrome</strong></h4>
Let \(C\) be a code with parity-check matrix \(H\). The syndrome of a received codeword \(c \in \mathcal{Y}^n\) is \(Hc\).</div>
<p>For all \(c \in C\), the syndrome is the all-zero vector, since \(c = G^Tm\) for some \(m\), and \[ HG^Tm = \left(-P\mid \mathbb{I}_{n-k}\right)\left(\begin{array}{c} \mathbb{I}_{k} \\ \hline P \end{array}\right) m = 0^{n-k} \, , \] where we make use of <a href="https://en.wikipedia.org/wiki/Block_matrix">block matrix multiplication</a>. The syndrome gives a lot of valuable information about where an error occurred. Suppose a codeword \(c\) is sent over a channel, and a single bit of \(c\) is flipped, at the \(i\)th position. The output of the channel is thus \(c' = c + e_i\) (where \(e_i\) is the \(i\)th unit vector, which is 1 at position \(i\) and 0 elsewhere). The syndrome for this received output is \[ Hc' = H(c + e_i) = Hc + He_i = He_i, \] which is the \(i\)th column of \(H\). So by comparing the syndrome to the parity-check matrix \(H\), we can find out which bit was most likely flipped.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Parity-check matrix of the \([7,4]\) Hamming code</strong></h4> The following \(3 \times 7\) matrix is the parity-check matrix for the \([7,4]\) Hamming code: \[ H = \left(\begin{array}{c c c c c c c} 1 &amp; 1 &amp; 1 &amp; 0 &amp; 1 &amp; 0 &amp; 0 \\ 0 &amp; 1 &amp; 1 &amp; 1 &amp; 0 &amp; 1 &amp; 0 \\ 1 &amp; 0 &amp; 1 &amp; 1 &amp; 0 &amp; 0 &amp; 1 \end{array} \right). \] Suppose the codeword 1010100 is received. What is the syndrome? Which errors occurred, if any? And what is the correct decoding?
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group2" style="">
<div class="content-box">The syndrome is 110: the result of applying \(H\) to the received codeword. This syndrome matches \(He_2\) (the second column of \(H\)), and so it is most likely the second codeword bit that was flipped. The decoding is therefore 1110 (corrected from 1010).
<p>Notice that all columns of \(H\) are different, and that there are \(2^3 = 8\) possible syndromes we might observe. This aligns well with the fact that there are three parity bits that can all either be correct or incorrect.</p>
</div>
</div>
</div>