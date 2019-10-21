# Introduction to Module 07

<p>Previous modules:</p>
<ul>
<li>01: Preliminaries (probability theory)</li>
<li>02: Building blocks (entropy, conditional entropy, mututal information, and relative entropy)</li>
<li>03/04: <em>compressing </em>information: encoding sources symbol-by-symbol (Huffman codes, arithmetic codes, Shannon's source coding theorem about the average codeword length of optimal codes), and encoding sources in blocks (typical sets).</li>
<li>04: <em>hiding</em> information: perfectly secure encryption (one-time pad).</li>
<li>05: generalization to stochastic processes (entropy rate)</li>
<li>06: <em>protecting</em> information: error-correcting codes and zero-error coding</li>
</ul>
<p>In this final module, we will try to find the optimal balance between compressing information on the one hand (so that we may send messages as efficiently as possible), and protecting it from noise on the other hand.</p>
<p>The channel capacity plays an important role in this balance. As stated, the channel capacity reflects the maximum amount of information that could <i>in principle</i> be sent over a noisy channel per use of that channel. The question remains whether this capacity is actually <span style="color: #bc0031;"><strong>achievable</strong></span>.</p>
<p>We will prove <span style="color: #bc0031;"><strong>Shannon's noisy-channel coding theorem</strong></span>, which states that any rate \(R\) that is strictly below the capacity \(C\) is achievable, and conversely, that any rate strictly above is not achievable. In the proof of Shannon's noisy-channel coding theory, the concept of typicality (and a variant of the AEP) will play an important role.</p>
<p>We end the module with a final theorem, the <span style="color: #bc0031;"><strong>source-channel separation theorem</strong></span>, which states that a good method (as in: efficient and protecting against errors) to encode a source to send it over a channel is to <em>first</em> compress it down, and <em>then</em> apply an error-correcting code that is appropriate for the channel.</p>
<p>As an additional resource, you may find <a href="https://www.youtube.com/playlist?list=PLwTkuB98zDQc39GNhoNYmJhzGiwPciWaI">these screen recordings</a> useful. However, please remember that the course content is defined by the material available on Canvas, so you may not get all the content by only watching the lecture recordings.</p>