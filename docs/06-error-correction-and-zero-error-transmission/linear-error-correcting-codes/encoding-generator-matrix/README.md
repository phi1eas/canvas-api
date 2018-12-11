# Encoding: Generator Matrix

<p>The encoding procedure of a linear code is nicely captured by the generator matrix:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Generator matrix</strong></h4>
Given a \([n,k,d]\) linear code, the generator matrix \(G^T\) is an \(n \times k\) matrix such that the columns \(c_1, \ldots, c_k\) form a basis for \(C\). The generator matrix can always be transformed into <span style="color: #bc0031;"><strong>systematic form</strong></span>: \[ G^T = \left( \begin{array}{c} \mathbb{I}_k \\ \hline P \end{array} \right), \] where \(P\) is some \((n-k) \times k\) matrix representing the parity bits of the code.</div>
<p>The generator matrix is used in the encoding function as follows: \[ \mathtt{enc}(m) = G^T \cdot m. \] The codebook \(C\) is the set \(\{G^T \cdot m \mid m \in \mathcal{X}^k\}\).</p>
<p>The reason for the transposition in \(G^T\) is that historically, coding theorists prefer to use row vectors and matrix multiplication from the right instead of column vectors and multiplication from the left, which is more standard in other areas. Notice that for row vectors \(c = m \cdot G\), we equivalently have column vectors \(c^T = (m \cdot G)^T = G^T \cdot m^T\).</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Generator matrix of the \([7,4]\) Hamming code</strong></h4>
The following \(7 \times 4\) matrix generates the \([7,4]\) Hamming code: \[ G^T = \left( \begin{array}{c c c c} 1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 1 \\ \hline 1 &amp; 1 &amp; 1 &amp; 0 \\ 0 &amp; 1 &amp; 1 &amp; 1 \\ 1 &amp; 0 &amp; 1 &amp; 1 \end{array} \right). \] The generator matrix is given in systematic form. Encode the message 1010.
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group1" style="">
<div class="content-box">To encode the message 1010, we compute \[ G^T \left(\begin{array}{c} 1 \\ 0 \\ 1 \\ 0 \end{array}\right) = \left(\begin{array}{c} 1 \\ 0 \\ 1 \\ 0 \\ 0 \\ 1 \\ 0 \end{array}\right). \] Note that due to the systematic form, the first \( k \) bits of the codeword is the actual message, whereas the rest are the parity-check bits.</div>
</div>
</div>