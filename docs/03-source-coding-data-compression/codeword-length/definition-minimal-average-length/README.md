<p>For efficiency reasons, we are often interested in the average (expected) length of a code \(C\):</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Average length</strong></h4>
Let \(\ell(s)\) denote the length of a string \(s \in \{0,1\}^*\). The (average) length of a code \(C\) for a source \(P_X\) is defined as \[ \ell_C(P_X) := \mathbb{E}[\ell(C(X))] = \sum_{x \in \cal X} P_X(x) \ell(C(x)) \, . \]</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
<p>The following are all codes for the source \(P_X\), with \({\cal X} = \{\texttt{a},\texttt{b},\texttt{c},\texttt{d}\}\):</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 16.6667%;">\(x\)</td>
<td style="width: 16.6667%;">\(P_X(x)\)</td>
<td style="width: 16.6667%;">\(C_1(x)\)</td>
<td style="width: 16.6667%;">\(C_2(x)\)</td>
<td style="width: 16.6667%;">\(C_3(x)\)</td>
<td style="width: 16.6667%;">\(C_4(x)\)</td>
</tr>
<tr>
<td style="width: 16.6667%;">\(\texttt{a}\)</td>
<td style="width: 16.6667%;">0.5</td>
<td style="width: 16.6667%;">00</td>
<td style="width: 16.6667%;">0</td>
<td style="width: 16.6667%;">0</td>
<td style="width: 16.6667%;">0</td>
</tr>
<tr>
<td style="width: 16.6667%;">\(\texttt{b}\)</td>
<td style="width: 16.6667%;">0.25</td>
<td style="width: 16.6667%;">01</td>
<td style="width: 16.6667%;">10</td>
<td style="width: 16.6667%;">010</td>
<td style="width: 16.6667%;">01</td>
</tr>
<tr>
<td style="width: 16.6667%;">\(\texttt{c}\)</td>
<td style="width: 16.6667%;">0.125</td>
<td style="width: 16.6667%;">10</td>
<td style="width: 16.6667%;">110</td>
<td style="width: 16.6667%;">01</td>
<td style="width: 16.6667%;">011</td>
</tr>
<tr>
<td style="width: 16.6667%;">\(\texttt{d}\)</td>
<td style="width: 16.6667%;">0.125</td>
<td style="width: 16.6667%;">11</td>
<td style="width: 16.6667%;">111</td>
<td style="width: 16.6667%;">10</td>
<td style="width: 16.6667%;">111</td>
</tr>
</tbody>
</table>
For the codes above, we obtain the following average codeword lengths: \( \ell_{C_1}(P_X) = 2, \ell_{C_2}(P_X)=\ell_{C_4}(P_X)=\frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 2 + \frac{1}{8} \cdot 3 + \frac{1}{8} \cdot 3 = \frac{7}{4} = 1.75 \) and \( \ell_{C_3}(P_X) = \frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 3 + \frac{1}{8} \cdot 2 + \frac{1}{8} \cdot 2 = \frac{7}{4} = 1.75. \)  We see that the codes \(C_2,C_3,C_4\) have a smaller average codeword length, but \(C_2\) and \(C_4\) are preferred over \(C_3\) because their unique decodability. Notice that the individual codeword lengths of codes \(C_2\) and \(C_4\) correspond exactly to the surprisal values of \(P_X\) in bits, e.g. \(\ell(C_2(b)) = \ell(C_4(b)) = 2 = -\log P_X(b)\). Therefore, the computations of the entropy \(H(X)\) and of the average code length \(\ell_{C_2}(P_X)\) are exactly the same, and we have that \(H(X) = \ell_{C_2}(P_X) = \ell_{C_4}(P_X)\). We will see later that this property characterizes optimal codes.
<p> </p>
<div id="group3" style="">
<div class="content-box">decide whether this button is necessary, and whether the title of this block should be question instead of example</div>
</div>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Minimal code length</strong></h4>
The minimal code length of a source \(P_X\) is defined as \[ \ell_{\min}(P_X) := \min_{C \in \frak{C}} \ell_C(P_X) \] where \(\frak{C}\) is some class of codes, for example the set of all prefix-free codes (resulting in \(\ell_{\min}^{\text{p.f.}}\)), or the set of all uniquely decodable codes (resulting in \(\ell_{\min}^{\text{u.d.}}\)).</div>
<p> </p>