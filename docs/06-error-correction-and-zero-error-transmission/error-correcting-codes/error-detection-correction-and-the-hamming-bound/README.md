# Error Detection/Correction and the Hamming Bound

<p>In general, a code with minimal distance \(d\) can <em><strong>detect</strong></em> up to \(d-1\) bit flip errors: in \(d-1\) bit flip 'steps', those bit flips can never result in another valid codeword. The code can accurately <strong><em>correct</em></strong> up to \(\frac{d-1}{2}\) bit flip errors. Look at the diagram below to understand why: if two codewords \(c_1\) and \(c_2\) are guaranteed to be at least \(d\) bit flips apart, then the set of strings that result from \(\frac{d-1}{2}\) bit flips on \(c_1\) (the orange circle on the left) never overlaps with the set of strings that result from \(\frac{d-1}{2}\) bit flips on \(c_2\) (the orange circle on the right).</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/2205/files/247009/preview?verifier=jcuwCEA36Lg3o9hyQGJS1pgQQL6C08K3PvDsV9NL" alt="The effect of the distance d on the error correction and detection capabilities of a code" width="437" height="317" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/247009" data-api-returntype="File"></p>
<p>Because every codeword is guaranteed to have this neighborhood around it that it does not share with any other codeword, we can upper bound the total number of codewords in terms of the distance.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition: Hamming bound</strong></h4>
If \(C\) is a <i>binary</i> code of block length \(n\) and minimum distance 3, then \(|C| \leq \frac{2^n}{n+1}\).
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">For each \(c \in C\), define the neighborhood of \(c\) to be \(N(c) := \{y \in \{0,1\}^n \mid d(x,y) \leq 1\}\). Every such neighborhood contains exactly \(n+1\) elements. Since \(d = 3\), \(N(c) \cap N(c') = \emptyset\) whenever \(c \neq c'\). Hence, \begin{align} 2^n \geq |\bigcup_{c \in C} N(c)| = \sum_{c \in C} |N(c)| = |C| \cdot (n+1), \end{align} and the result follows.</div>
</div>
</div>
<p>The \([7,4]\) Hamming code is optimal in the sense that it achieves this Hamming bound: it is a code with block length 7 and minimal distance 3, so an upper bound to the codebook size is \(\frac{2^7}{7+1} = 2^4\). The Hamming code achieves exactly this codebook size.</p>