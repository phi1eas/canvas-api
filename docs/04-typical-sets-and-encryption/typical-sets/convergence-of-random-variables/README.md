<p>The following definition of converging random variables may remind you of a converging sequence of numbers. Recall that a sequence \(x_1, x_2, x_3, \ldots\) of numbers converges to \(x\) if \(\forall\epsilon &gt; 0 \ \exists n_0 \ \forall (n \geq n_0) : |x_n - x| &lt; \epsilon\). We denote this by writing \(x_n \xrightarrow{n \to \infty} x\).</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Converging random variables</strong></h4>
A sequence \(X_1, X_2, X_3, \ldots\) of real random variables converges to a random variable \(X\), if it satisfies one of the following definitions:
<table cellpadding="20">
<tbody>
<tr>
<td><span style="color: #bc0031;"><strong>in probability</strong></span></td>
<td>(notation \(X_n \xrightarrow{p} X\))</td>
<td>if \(\forall \epsilon &gt; 0\), \(P[|X_n - X| &gt; \epsilon] \xrightarrow{n \to \infty} 0\)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>"As \(n\) increases, the distribution of \(X_n\) gets closer and closer to that of \(X\)."</td>
</tr>
<tr>
<td><span style="color: #bc0031;"><strong>in mean square</strong></span></td>
<td>(notation \(X_n \xrightarrow{m.s.} X\))</td>
<td>if \(\mathbb{E}[(X_n - X)^2] \xrightarrow{n \to \infty} 0\)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>"As \(n\) increases, the expected (square of the) difference between \(X_n\) and \(X\) diminishes."</td>
</tr>
<tr>
<td><span style="color: #bc0031;"><strong>almost surely</strong></span></td>
<td>(notation \(X_n \xrightarrow{a.s.} X\))</td>
<td>if \(P[\lim_{n \to \infty} X_n = X] = 1\)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>"Any event \(\omega\) for which \(X_n\) does <i>not</i> approach the distribution \(X\) has zero probability."</td>
</tr>
</tbody>
</table>
The definition of \(X_n \xrightarrow{a.s.} X\) can be interpreted as \(P[\{\omega \in \Omega \mid X_n(\omega) \xrightarrow{n \to \infty} X(\omega)\}] = 1\).</div>
<p>In general, the following implications hold (although their converses do not): \begin{align} X_n \xrightarrow{m.s.} X \ \ \ &amp;\Rightarrow\ \ \ X_n \xrightarrow{p} X\\ X_n \xrightarrow{a.s.} X \ \ \ &amp;\Rightarrow\ \ \ X_n \xrightarrow{p} X \end{align}</p>