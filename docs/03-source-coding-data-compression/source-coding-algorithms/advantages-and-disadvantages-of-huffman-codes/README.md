<p>It turns out that Huffman codes indeed have optimal code length.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Theorem: Optimality of Huffman codes</strong></h4>
Let \(P_X\) be a source, and let \(C^*\) be the associated Huffman code. For any other uniquely decodable code \(C'\) with the same alphabet, \[ \ell_{C^*}(P_X) \leq \ell_{C'}(P_X). \]
<p><span class="element_toggler" role="button" aria-controls="group10" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group10" style="display: none;">
<div class="content-box">see <a href="http://onlinelibrary.wiley.com/book/10.1002/0471200611" target="_blank">Cover/Thomas</a>, Section 5.8</div>
</div>
</div>
<p> </p>
<p><span style="font-size: 1rem;">As we have seen, the average codeword length of Huffman codes is theoretically optimal. However, Huffman codes (and symbol codes in general) still have a number of disadvantages:</span></p>
<ul>
<li>When compressing, for example, an English text symbol-by-symbol, the probability distribution for each position may depend on the string of text that precedes it: for example, the letter <strong><em>n</em></strong> is a lot more likely than the letter <strong><em>a </em></strong>if it comes after the string <strong><em>informatio </em></strong>. Given this change of distribution, the Huffman code may not produce the shortest possible code. This can be resolved by recomputing the Huffman code after every symbol, but this results in a lot of overhead.</li>
<li>The average codeword length is upper bounded by \(H(X) + 1\). This additive cost of 1 bit is fine when \(H(X)\) is very large, but can be a significant overhead when \(H(X)\) is small itself.</li>
</ul>