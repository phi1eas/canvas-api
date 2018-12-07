<p>One convenient way to guarantee that a code is unique decodable is to require it to be prefix-free:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Prefix-free code</strong></h4>
A binary symbol code \(C : {\cal X} \to \{0,1\}^*\) is prefix-free (or: <span style="color: #bc0031;"><strong>instantaneous</strong></span>) if for all \(x, x' \in \cal X\) with \(x \neq x'\), \(C(x)\) is <i>not</i> a <a href="https://en.wikipedia.org/wiki/Substring#Prefix">prefix</a> of \(C(x')\).</div>
<p>With a prefix-free encoding, the elements \(x_1, \ldots, x_m\) can be uniquely recovered from \(C(x_1)|\cdots |C(x_m)\), simply by reading the encoding from left to right one bit at a time: by prefix-freeness it will remain unambiguous as reading continues when the current word terminates and the next begins. This is a loose argument for the following proposition:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
If a code \(\cal C\) is prefix-free and \({\cal C} \neq {\bot}\) then \(\cal C\) is uniquely decodable.</div>
<p>The other direction does not hold: uniquely decodable codes need not be prefix-free. A prefix-free code is appealing from an efficiency point of view, as it allows to decode "on the fly". For a general uniquely decodable code one may possibly have to inspect all bits in the entire string before being able to even recover the first word.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
The following are all codes for the source \(P_X\), with \({\cal X} = \{\texttt{a},\texttt{b},\texttt{c},\texttt{d}\}\):
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
These codes can be visualised a as binary trees, with marked codewords, as follows:
<table style="width: 100%;">
<tbody>
<tr>
<td style="width: 25%; text-align: center;"><img src="/img/129820?verifier=u0q3wDA9EBKQipPVX2RfCNNAY9uXgtbLBbw9kjbl" alt="tree for code 1" width="71" height="114" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/129820" data-api-returntype="File"></td>
<td style="width: 25%;"><img src="/img/129819?verifier=hywuHJIM5BhDInZ0ZztlqWVvVKtGFZBENfMa3QMX" alt="tree for code 2" width="105" height="81" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/129819" data-api-returntype="File"></td>
<td style="width: 25%;"><img src="/img/129818?verifier=7WC9yv0PjxBja7ShtYC9xGxzhKKKOUri6P43j4WJ" alt="tree for code 3" width="105" height="116" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/129818" data-api-returntype="File"></td>
<td style="width: 25%;"><img src="/img/129817?verifier=KD29Pa5lzef9mbgK6nxm3XPFyeQ1po5DQXZ5vFeP" alt="tree for code 4" width="105" height="132" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/129817" data-api-returntype="File"></td>
</tr>
<tr>
<td style="width: 25%; text-align: center;">\(C_1\)</td>
<td style="width: 25%; text-align: center;">\(C_2\)</td>
<td style="width: 25%; text-align: center;">\(C_3\)</td>
<td style="width: 25%; text-align: center;">\(C_4\)</td>
</tr>
</tbody>
</table>
Which of these codes are uniquely decodable? Which are prefix-free?
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group2" style="">
<div class="content-box">\(C_1\) and \(C_2\) are prefix-free, and therefore also uniquely decodable. \(C_3\) is not uniquely decodable, as \(C_3(ad) = C_3(b)\). \(C_4\) is not prefix-free, but it is uniquely decodable, since it can be decoded from right to left (it is ``<a href="https://en.wikipedia.org/wiki/Substring#Suffix">suffix</a>-free"). Note that the binary trees for the prefix-free codes \(C_1, C_2\) only have codewords at the leaves.</div>
</div>
</div>