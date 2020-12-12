# Introduction to Module 05

<p>Previous modules:</p>
<ul>
<li>01: Preliminaries (probability theory)</li>
<li>02: Building blocks (entropy, conditional entropy, mututal information, and relative entropy)</li>
<li>03/04: <em>compressing </em>information: encoding sources symbol-by-symbol (Huffman codes, arithmetic codes, Shannon's source coding theorem about the average codeword length of optimal codes), and encoding sources in blocks (typical sets).</li>
<li>04: <em>hiding</em> information: perfectly secure encryption (one-time pad).</li>
</ul>
<p>So far in this course we have mostly seen independent random variables. In source coding, we designed our codes according to a single distribution \(P_X\), and assumed that if we encoded a sequence of source symbols, the symbols in the sequence would all be drawn independently according to \(P_X\). In the real world, however, subsequent events are often dependent on each other. For example, in an English text, after observing a letter \( \texttt{q} \), the next letter is much more likely to be \( \texttt{u} \) than it is to be \( \texttt{r} \), even though in general the letter \( \texttt{r} \) is more prevalent in English text. The event of observing the letter \(\texttt{q}\) changes the probability distribution of the next letter.</p>
<p>In this module, we study so-called <em>stochastic processes</em>, sequences of random variables which may depend on each other in various ways. We start by studying a restricted form of dependence between variables, Markov chains, and observe how information propagates through the sequence of random variables. We then move on to more general stochastic processes, and categorize them according to all kinds of properties they may have.</p>
<p>We end the module by quantifying how much information is contained in a random process. Because the samples in such a process are not necessarily independent, it does not make sense to measure their information content by the entropy of a single random variable. Instead, we define the entropy rate.</p>
<p>As an additional resource, you may find <a href="https://www.youtube.com/playlist?list=PLij6EOUQRtG9VOAsI11Wh2gDv4h5G2oPy">these student-recorded lectures</a> useful. However, please remember that the course content is defined by the material available on Canvas, so you may not get all the content by only watching the lecture recordings.</p>