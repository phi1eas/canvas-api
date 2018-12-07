<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Standard binary representation</strong></h4>
The standard binary representation of a real number \(r \in [0,1)\) is a (possibly infinite) string of bits \(c_1c_2\cdots\) such that \[ r = \sum_i c_i \cdot 2^{-i}, \] where by convention, 0 is represented by the string 0.</div>
<p>Not all reals in \([0,1)\) have a finite representation, but any interval \([a,b)\) with \(0 \leq a &lt; b \leq 1\) contains at least one number with a finite binary representation.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
The following table lists some numbers \(r \in [0,1)\) and their standard binary representation. \[ \begin{array}{c | c} r &amp; \mbox{binary representation of } r\\\hline 1/2 &amp; 1\\ 1/3 &amp; 01010101\cdots\\ 1/4 &amp; 01\\ 3/4 &amp; 11\\ 13/16 &amp; 1101\\ 13/32 &amp; 01101\\ \end{array} \] Note that 1101 is also the binary form of the natural number 13. Adding a 0 on the left divides the represented value by 2.</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Binary interval</strong></h4>
A binary interval is an interval of the form \[ \left[\frac{s}{2^{\ell}}, \frac{s+1}{2^{\ell}}\right) \] with \(s, \ell \in \mathbb{N}\) and \(0 \leq s &lt; 2^{\ell}\).
<div class="content-box pad-box-mini "><img style="display: block; margin-left: auto; margin-right: auto;" src="/img/181506/download?verifier=zlrZwoMycdQRpsvdOuXwm3mmGAdTtD9wPE5CSRw6&amp;wrap=1" alt="Binary intervals" width="279" height="252" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/181506" data-api-returntype="File"></div>
The <span style="color: #bc0031;"><strong>name</strong></span> of the interval is the binary representation of \(s\) (as a natural number) padded with zeroes on the left to reach length \(\ell\). The name can also be interpreted as the path to follow from the root in order to reach the interval as follows:
<p><img style="font-size: 1rem; display: block; margin-left: auto; margin-right: auto;" src="/img/181508/download?verifier=G7GBlnzt72BeQKw6w3DKg9RLz3l1Z5qkyyoW8cl1" alt="BinaryIntervalsHaveNames.png" width="275" height="183" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/181508" data-api-returntype="File"></p>
<p>[Images by <a href="https://www.linkedin.com/in/mathias-madsen-aa87333/">Mathias Madsen</a>, thanks a lot!]</p>
</div>