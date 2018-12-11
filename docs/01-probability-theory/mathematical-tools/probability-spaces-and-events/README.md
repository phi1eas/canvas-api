# Probability Spaces and Events

<p>For this course, we will only be concerned with discrete probabilities. This section formalizes some notions you should already be familiar with: probability spaces, events and probability distributions.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Probability space</strong></h4>
A (discrete) probability space \((\Omega, \mathcal{F}, P)\) consists of a discrete, non-empty <i>sample space</i> \(\Omega\), an <i>event space</i> \(\mathcal{F} \subseteq \mathcal{P}(\Omega)\) (where \(\mathcal{P}(\Omega)\) is the <a href="https://en.wikipedia.org/wiki/Power_set">powerset</a> of \(\Omega\)) and a <i>probability measure</i> \(P\) which is a function \(P : \Omega \to \mathbb{R}_{\geq 0}\) that satisfies \[ \sum_{\omega \in \Omega} P(\omega) = 1. \]</div>
<p>The event space \(\mathcal{F}\) is required to be non-empty and closed under intersection, union and complements. For convenience, we will most often assume that \(\mathcal{F}\) equals the powerset \(\mathcal{P}(\Omega)\) of \(\Omega\), i.e., it contains all possible subsets of events, and therefore fulfils the required properties.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Event</strong></h4>
An event \(\mathcal{A}\) is an element of the event space \(\mathcal{F} \subseteq \mathcal{P}(\Omega)\), i.e., a subset \(\mathcal{A}\) of the sample space \(\Omega\). Its probability is defined as \[ P[\mathcal{A}] := \sum_{\omega \in \mathcal{A}} P(\omega), \] where by convention \(P[\emptyset] = 0\).</div>
<p>As a notational convention, we write \(P[\mathcal{A},\mathcal{B}]\) for \(P[\mathcal{A} \cap \mathcal{B}]\), and \(P[\overline{\mathcal{A}}]\) for \(P[\Omega\backslash\mathcal{A}]\). The following identities hold for arbitrary events \(\mathcal{A}, \mathcal{B} \subseteq \Omega\) (try to prove them for yourself):</p>
<ul>
<li>\(P[\overline{\mathcal{A}}] = 1 - P[\mathcal{A}]\)</li>
<li>\(P[\mathcal{A} \cup \mathcal{B}] = P[\mathcal{A}] + P[\mathcal{B}] - P[\mathcal{A}, \mathcal{B}]\)</li>
<li>\(P[\mathcal{A}] = P[\mathcal{A}, \mathcal{B}] + P[\mathcal{A}, \overline{\mathcal{B}}].\)</li>
</ul>
<p>It is often useful to consider the probability of an event <i>given</i> that some other event happened:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Conditional probability</strong></h4>
For events \(\mathcal{A}\) and \(\mathcal{B}\) with \(P[\mathcal{A}] &gt; 0\), the conditional probability of \(\mathcal{B}\) given \(\mathcal{A}\) is defined as \[ P[\mathcal{B} | \mathcal{A}] := \frac{P[\mathcal{A},\mathcal{B}]}{P[\mathcal{A}]} \, . \]</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example: Fair die</strong></h4>
We throw a six-sided fair die once, and consider the number that comes up. The sample space for this experiment is \(\Omega = {1,2,3,4,5,6}\), with event space \(\mathcal{F} = \mathcal{P}(\Omega)\) and probability measure \(P[i] = \frac{1}{|\Omega|} = \frac{1}{6}\) for all \(i \in \Omega\) (this is a <span style="color: #bc0031;"><strong>uniform</strong></span> probability measure). Consider the events \(\mathcal{A} = {2,4,6}\) and \(\mathcal{B} = {3,6}\). Using the formulas in the definitions of events and conditional probabilities, we can compute the following probabilities: \begin{align*} P[\mathcal{A}] = \frac{1}{2} &amp;\text{(the outcome is even)}\\ P[\mathcal{B}] = \frac{1}{3}&amp;\text{(the outcome is a multiple of 3)} \\ P[\mathcal{A}, \mathcal{B}] = P[{6}] = \frac{1}{6} &amp;\text{(the roll is even and a multiple of 3)} \\ P[\mathcal{A} | \mathcal{B}] = \frac{1/6}{1/3} = \frac{1}{2} &amp;\text{(the roll is even, given that it is a multiple of 3)} \\ P[\mathcal{B} | \mathcal{A}] = \frac{1/6}{1/2} = \frac{1}{3}&amp;\text{(the roll is a multiple of 3, given that it is even)}\end{align*} This example shows that in general, \(P[\mathcal{A} | \mathcal{B}]\) is <i>not necessarily equal</i> to \(P[\mathcal{B} | \mathcal{A}]\). In fact, they are related through <a href="https://en.wikipedia.org/wiki/Bayes'_theorem">Bayes' rule</a>.
<div id="group1" style="">
<div class="content-box">decide whether this button is necessary, and whether the title of this block should be question instead of example</div>
</div>
</div>