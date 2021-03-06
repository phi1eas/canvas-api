# Definition: Linear Code

<p>In this section, we study a class of error-correcting codes called linear codes. This type of code has a nice structure and can be encoded/decoded efficiently.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Linear code</strong></h4>
A code \(C\) is linear if any linear combination of codewords is also a codeword.</div>
<p>For the definition of linearity to make sense, addition and multiplication by constants needs to be defined on \(\mathcal{X}^n\) (formally, \(\mathcal{X}^n\) needs to be a <a href="https://en.wikipedia.org/wiki/Vector_space">vector space</a>). Then \(C\) is linear if it is a <a href="https://en.wikipedia.org/wiki/Linear_subspace">linear subspace</a> of \(\mathcal{X}^n\). In the following, we will assume that \(\mathcal{X} = \{0,1\}\): in that case, we are talking about <span style="color: #bc0031;"><strong>binary codes</strong></span> and addition is simply bitwise addition modulo 2 (which is the exclusive OR function). Note that for binary codes, addition and subtraction are the same operation, as \(-1 = +1\) modulo \(2\).</p>