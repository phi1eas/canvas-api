<p>So far in this course we have mostly seen independent random variables. In source coding, we designed our codes according to a single distribution \(P_X\), and assumed that if we encoded a sequence of source symbols, the symbols in the sequence would be drawn independently according to \(P_X\). In the real world, however, subsequent events are often dependent on each other. For example, in an English text, after observing a letter \( \texttt{q} \), the next letter is much more likely to be \( \texttt{u} \) than it is to be \( \texttt{r} \), even though in general the letter \( \texttt{r} \) is more prevalent in English text. The event of observing the letter \(\texttt{q}\) changes the probability distribution of the next letter. We start by studying a restricted form of dependence between variables: Markov chains. Random variables form a Markov chain if the distribution of each random variable depends only on the outcome of the random variable that directly precedes it.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Markov chain (of length 3)</strong></h4>
The random variables \(X, Y,\) and \(Z\) form a Markov chain (notation: \(X \to Y \to Z\)) if and only if \[ P_{Z|XY} = P_{Z|Y}. \]</div>
<p>In this chapter, we regularly use the shortcut \(P_{Z|XY} = P_{Z|Y}\) to denote that this equality should hold for all possible input values, i.e. \begin{align} P_{Z|XY} = P_{Z|Y} \qquad \Leftrightarrow \qquad \forall x \in \mathcal{X}, y \in \mathcal{Y}, z \in \mathcal{Z}: P_{Z|XY}(z|x,y) = P_{Z|Y}(z|y) \, . \end{align}</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
For all random variables \(X,Y,Z\), the following statements are equivalent:
<ol type="a">
<li>\(X \to Y \to Z\),</li>
<li>\(Z \to Y \to X\),</li>
<li>\(P_{XZ|Y} = P_{X|Y} \cdot P_{Z|Y}\) (that is, \(I(X;Z|Y) = 0\)). </li>
</ol>
<p><span class="element_toggler" role="button" aria-controls="group1" aria-label="Toggler" aria-expanded="false"><span class="Button">Proof</span></span></p>
<div id="group1" style="">
<div class="content-box">We prove that (a) \(\Rightarrow\) (b), that (b) \(\Rightarrow\) (c), and that (c) \(\Rightarrow\) (a). All other directions follow from (combinations of) these three implications.</div>
<ul>
<li>[(a) \(\Rightarrow\) (b):] Suppose \(X \to Y \to Z\). Then \begin{align} P_{X|YZ} &amp;= \frac{P_{XYZ}}{P_{YZ}} = \frac{P_{XY} \cdot P_{Z|XY}}{P_{YZ}} = \frac{P_{XY} \cdot P_{Z|XY}}{P_Y \cdot P_{Z|Y}}\\ &amp;= \frac{P_{XY} \cdot P_{Z|Y}}{P_Y \cdot P_{Z|Y}} = \frac{P_{XY}}{P_Y} = P_{X|Y}, \end{align} where we go from the top to the bottom line using the assumption that \(X \to Y \to Z\).</li>
<li>[(b) \(\Rightarrow\) (c):] Suppose \(Z \to Y \to X\). Then \begin{align} P_{XZ|Y} &amp;= \frac{P_{XYZ}}{P_Y} = \frac{P_{X|YZ} \cdot P_{YZ}}{P_Y}\\ &amp;= \frac{P_{X|Y} \cdot P_{YZ}}{P_Y} = P_{X|Y} \cdot \frac{P_{YZ}}{P_Y} = P_{X|Y} \cdot P_{Z|Y}, \end{align} where we go from the top to the bottom line using the assumption that \(Z \to Y \to X\).</li>
<li>[(c) \(\Rightarrow\) (a):] For the final implication, suppose that \(P_{XZ|Y} = P_{X|Y} \cdot P_{Z|Y}\). Then \begin{align} P_{Z|YX} &amp;= \frac{P_{XYZ}}{P_{XY}} = \frac{P_{XZ|Y} \cdot P_Y}{P_{XY}}\\ &amp;= \frac{P_{X|Y} \cdot P_{Z|Y} \cdot P_Y}{P_{XY}} = \frac{P_{XY} \cdot P_{Z|Y}}{P_{XY}} = P_{Z|Y}, \end{align} and therefore \(X \to Y \to Z\).</li>
</ul>
</div>
</div>
<p>Because of the equivalence of items (a) and (b), we often write \(X \leftrightarrow Y \leftrightarrow Z\) to denote a Markov chain.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Whispering game</strong></h4>
Alice, Bob and Charlie play a game: Alice comes up with a message, and whispers it into Bob's ear. Bob then proceeds to whisper the message into Charlie's ear, who says it out loud. Of course, Bob and Charlie may not hear the message correctly: there is some noise in the communication. Let \(A\) be the random variable that contains the message that Alice picks. For simplicity, let's say she picks a uniformly random bit. Let \(B\) be the message that Bob heard: it is also a bit, but with probability 0.1, it is not the same as \(A\). More formally, \begin{align*} P_{B|A}(0|0) = P_{B|A}(1|1) &amp;= 0.9,\\ P_{B|A}(1|0) = P_{B|A}(0|1) &amp;= 0.1.\\ \end{align*} Finally, let \(C\) be the message that Charlie heard: again, let us suppose that it is unequal to the whispered message \(B\) with probability 0.1. For the conditional distribution of \(C\), we see that \(P_{C|AB}(0|00) = 0.9 = P_{C|B}(0|0)\), and similarly for all other possible values of \(A\), \(B\), and \(C\). Thus, these random variables form a Markov chain: \(A \to B \to C\). The proposition above tells us that we can also look at this game in the converse direction: if we are curious about Alice's original message \(A\), we only have to look at Bob's interpretation \(B\) of the message. Additionally knowing Charlie's interpretation \(C\) does not change the distribution of \(A\).</div>