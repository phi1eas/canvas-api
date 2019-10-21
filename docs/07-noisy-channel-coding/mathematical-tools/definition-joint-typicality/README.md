# Definition: Joint Typicality

<p>Very roughly, the forward direction of Shannon's noisy-channel coding theorem follows from the <a title="The Asymptotic Equipartition Property" href="https://canvas.uva.nl/courses/10933/pages/the-asymptotic-equipartition-property" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/the-asymptotic-equipartition-property" data-api-returntype="Page">asymptotic equipartition property (AEP)</a>. Increasing \(n\) (the size of the input blocks) results in output blocks that are more likely to be typical. But can we be sure that no two typical input sequences result in the same typical output sequence? Such a collision would make it impossible to decode correctly. To show that this does not form a problem, we need stronger mathematical tools.</p>
<p>Before you start on this section, it is a good idea to refresh your understanding of <a title="Definition: Typical Set" href="https://canvas.uva.nl/courses/10933/pages/definition-typical-set" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/definition-typical-set" data-api-returntype="Page">typical sets</a> and the <a title="The Asymptotic Equipartition Property (AEP)" href="https://canvas.uva.nl/courses/10933/pages/the-asymptotic-equipartition-property-aep" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/pages/the-asymptotic-equipartition-property-aep" data-api-returntype="Page">asymptotic equipartition property</a>.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Joint typicality</strong></h4>
For a joint distribution \(P_{XY}\), the jointly typical set \(A_{\epsilon}^{(n)}\) is defined as \begin{align*} A_{\epsilon}^{(n)} := \{(x^n,y^n) \in \mathcal{X}^n \times \mathcal{Y}^n \mid \quad &amp;\left| - \frac{1}{n} \log P_{X^n}(x^n) - H(X)\right| &lt; \epsilon, \\ &amp;\left| - \frac{1}{n} \log P_{Y^n}(y^n) - H(Y)\right| &lt; \epsilon, \\ &amp;\left| - \frac{1}{n} \log P_{X^nY^n}(x^n,y^n) - H(XY)\right| &lt; \epsilon\}. \end{align*} Here, \(P_{X^nY^n} := \prod_{i=1}^nP_{XY}(x_iy_i)\).</div>
<p>A jointly typical set is a set where both elements of the pair are typical individually under the marginal distributions, and their combination is typical under the joint distribution. To get some intuition for what a typical set looks like, we give two examples: one where \(X\) and \(Y\) are very correlated, and one where they are independent.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
<p>Consider the almost fully correlated random variables \(X\) and \(Y\) with the following distribution:</p>
<div style="text-align: center;">
<table style="height: 72px; width: 210px;" border="1">
<tbody>
<tr style="height: 24px;">
<td style="height: 24px; width: 70px; text-align: center;"></td>
<td style="height: 24px; width: 70px;">\(X=0\)</td>
<td style="height: 24px; width: 70px; text-align: center;">\(X=1\)</td>
</tr>
<tr style="height: 24px;">
<td style="height: 24px; width: 70px;">\(Y=0\)</td>
<td style="height: 24px; width: 70px;">0.45</td>
<td style="height: 24px; width: 70px;">0.05</td>
</tr>
<tr style="height: 24px;">
<td style="height: 24px; width: 55px;">\(Y=1\)</td>
<td style="height: 24px; width: 56px;">0.05</td>
<td style="height: 24px; width: 56px;">0.45</td>
</tr>
</tbody>
</table>
</div>
<p>Note that the marginal distributions of \(X\) and \(Y\) are uniform, and so for all \(n\) and all \(x^n \in \{0,1\}^n\), \[-\frac{1}{n} \log P_{X^n}(x^n) - H(X) = -\frac{1}{n} \log \frac{1}{2^n} - \log 2 = 0,\] and a similar statement holds for \(Y\). Hence, the first and second inequalities in the definition of joint typicality are always satisfied for any \(\epsilon &gt; 0\).</p>
<p>What about the third inequality? The table below visualizes the probabilities of every pair for \(n = 3\) and \(\epsilon = 0.35\): every square represents a pair of elements from \(\mathcal{X}^3\) and \(\mathcal{Y}^3\). Bigger squares represent higher probabilities. The typical pairs are marked in orange.</p>
<p style="text-align: center;"><img src="https://canvas.uva.nl/courses/10933/files/1322455/preview?verifier=qmlEAcklWHrgAMzECx7U3GDOF7y9lnFai4conpUk" alt="The jointly typical set for n = 3 and epsilon = 0.35" width="197" height="196" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322455" data-api-returntype="File"></p>
<p>As you might expect, pairs \((x^3,y^3)\) with a higher overlap in bits have a higher probability of occurring. The jointly typical set has a very clear structure: only those pairs with \(x^3 = y^3\) are included. Increasing \(\epsilon\) would result in a bigger typical set. For example, for \(\epsilon = 0.8\), all pairs that differ in at most one position (e.g., \(\texttt{000},\texttt{001}\)) are part of the jointly typical set. Increasing \(n\) would have the same effect: for example, for \(n = 10\) and \(\epsilon = 0.35\), all pairs of sequences that differ at 0, 1, or 2 positions are part of the jointly typical set.</p>
<p>Similarly to what we saw earlier in the course, in this example, for big \(n\) and small \(\epsilon\), the jointly typical set contains only those pairs of sequences that differ in roughly 10 percent of the positions. The highest-probability pairs are excluded from the typical set. This might match your expectation, since the probability of sampling a non-matching pair of bits ((0,1) or (1,0)) is 10 percent: pairs with that percentage of non-matching bits are 'typical'. These jointly typical pairs together make up almost all of the probability mass, even though individually they are not the highest-probability pairs under \(P_{XY}\).</p>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Consider the following distribution on \(X\) and \(Y\):
<div style="text-align: center;">
<table style="height: 72px; width: 210px;" border="1">
<tbody>
<tr style="height: 24px;">
<td style="height: 24px; width: 70px; text-align: center;"></td>
<td style="height: 24px; width: 70px;">\(X=0\)</td>
<td style="height: 24px; width: 70px; text-align: center;">\(X=1\)</td>
</tr>
<tr style="height: 24px;">
<td style="height: 24px; width: 70px;">\(Y=0\)</td>
<td style="height: 24px; width: 70px;">1/8</td>
<td style="height: 24px; width: 70px;">1/8</td>
</tr>
<tr style="height: 24px;">
<td style="height: 24px; width: 55px;">\(Y=1\)</td>
<td style="height: 24px; width: 56px;">3/8</td>
<td style="height: 24px; width: 56px;">3/8</td>
</tr>
</tbody>
</table>
</div>
<p>Note that \(X\) is uniform, and that \(X\) and \(Y\) are independent. Just like in the previous example, since \(X\) is uniform, the first inequality in the definition of joint typicality is always satisfied for any \(\epsilon &gt; 0\). Furthermore, since \(X\) and \(Y\) are independent, the third inequality is satisfied whenever the second inequality is, because \begin{align*} -\frac{1}{n}\log P_{X^nY^n}(x^n,y^n) - H(XY) &amp;= -\frac{1}{n}\log P_{X^n}(x^n) - \frac{1}{n}\log P_{Y^n}(y^n) - H(X) - H(Y) \\ &amp;= -\frac{1}{n}\log P_{Y^n}(y^n) - H(Y). \end{align*} Hence, for this distribution, any pair where the second element is typical for \(Y\) is also jointly typical.</p>
<p>More concretely, consider \(n = 3\) and \(\epsilon = 0.35\). For these values, the sequences \(\texttt{011}, \texttt{101}\), and \(\texttt{110}\) are typical for \(Y\). This results in the following jointly typical set (again, bigger squares represent bigger probabilities, and orange squares indicate elements of the typical set, <strong>typo: the label of the axes label be switched around!</strong>):</p>
<p style="text-align: center;"><img src="https://canvas.uva.nl/courses/10933/files/1322454/preview?verifier=eQSVgXeM2RWAvNtdMtfzbuPXxouVMKm56ylSM7Er" alt="The jointly typical set for n = 3 and epsilon = 0.35" width="197" height="196" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322454" data-api-returntype="File"></p>
<p>Note that \(P_Y(\texttt{111}) \approx 0.422\), which is higher than \(P_Y(\texttt{011}) \approx 0.141\). However, \(\texttt{111}\) is not typical for \(Y\) while \(\texttt{011}\) is. \(\texttt{111}\)'s probability deviates too far from the 'benchmark' set by \(2^{-3H(Y)} \approx 0.185\). Together, the sequences in the typical set have a probability of about 0.422 of occurring. As \(n\) increases, this probability will grow, and the total probability of the elements that fall outside of the typical set (such as the all-\(\texttt{1}\) string) will diminish.</p>
</div>