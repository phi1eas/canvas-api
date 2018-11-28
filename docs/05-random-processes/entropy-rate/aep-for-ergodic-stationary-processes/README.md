<p>Under some natural assumptions, many statements and interpretations of the Shannon entropy we have seen in the context of the asymptotic equipartition property (AEP) can be generalized to the entropy rate \(H( \{ X_i \} ) \) of stochastic processes. </p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Ergodic Random Processes</strong></h4>
A stochastic process \(\{X_i\}\) is <strong>ergodic</strong> if <span>its statistical properties can be deduced from a single, sufficiently long, random sample of the process. </span>
</div>
<p>There are <a href="https://en.wikipedia.org/wiki/Ergodicity">many equivalent ways</a> of giving precise mathematical definitions of this notion, but this goes beyond the scope of this course. Instead, we consider the following examples.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Suppose we repeatedly pick a letter at random and print it three times: \( \texttt{LLL EEE HHH QQQ MMM QQQ OOO TTT EEE YYY XXX GGG} \ldots \)
<p>This random process is ergodic (as we see all letters eventually) but not stationary.</p>
<p>On the other hand, if we pick a letter at random and print it forever: \( \texttt{ GGGGGGGGGGGGGGGGGGGG} \ldots  \)</p>
<p>This process is stationary, but not ergodic (from one sample of the process, we can only see a single letter).</p>
</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Shannon–McMillan–Breiman theorem: AEP</strong></h4>
If \(H(\{X_i\}) \) is the entropy rate of a finite-valued stationary ergodic process \(\{X_i\}\), then \[-\frac{1}{n} \log P_{X_1, \ldots X_n}(X_1, \ldots X_n) \rightarrow H(\{X_i\}) \qquad \text{ with probability 1.} \]</div>
<p>In other words, the <a title="The Asymptotic Equipartition Property (AEP)" href="https://canvas.uva.nl/courses/2205/pages/the-asymptotic-equipartition-property-aep" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/the-asymptotic-equipartition-property-aep" data-api-returntype="Page">asymptotic equipartition property</a> holds for such processes: we can define <a title="Definition: Typical Set" href="https://canvas.uva.nl/courses/2205/pages/definition-typical-set" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/definition-typical-set" data-api-returntype="Page">typical sets</a> and all the <a title="Source Coding using Typical Sets" href="https://canvas.uva.nl/courses/2205/pages/source-coding-using-typical-sets" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/pages/source-coding-using-typical-sets" data-api-returntype="Page">results about data compression</a> we have seen in the previous module not only hold for iid processes, but more generally for stationary ergodic processes. The entropy rate \(H(\{X_i\}) \) measures how many bits on average are needed to optimally compress the stationary ergodic process \(\{X_i\}\).</p>