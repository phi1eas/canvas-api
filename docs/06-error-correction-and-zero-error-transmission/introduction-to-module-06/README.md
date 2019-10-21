# Introduction to Module 06

<p>Previous modules:</p>
<ul>
<li>01: Preliminaries (probability theory)</li>
<li>02: Building blocks (entropy, conditional entropy, mututal information, and relative entropy)</li>
<li>03/04: <em>compressing </em>information: encoding sources symbol-by-symbol (Huffman codes, arithmetic codes, Shannon's source coding theorem about the average codeword length of optimal codes), and encoding sources in blocks (typical sets).</li>
<li>04: <em>hiding</em> information: perfectly secure encryption (one-time pad).</li>
<li>05: generalization to stochastic processes (entropy rate)</li>
</ul>
<p>In Module 03, we saw how to encode information from a source to compress it, so that it can be stored or sent as efficiently as possible. While compression is great for efficiency, there is also a danger to it: because the information is so optimally compressed, if there is just a little bit of noise in the storage device or communication channel, some information is necessarily lost.</p>
<p>In this module, we consider the opposite setting, where we try to protect our messages from <span style="color: #bc0031;"><strong>noise </strong></span>on a communication channel. The noise may convert the channel input \(x\) to some potentially different value \(y\):</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322439/preview?verifier=RfJUX3b5qTSjRfSZwzBXaW0Bpk0K1ex6AmwP8kXF" alt="An encoding function, a channel, and a decoding function" width="706" height="115" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322439" data-api-returntype="File"></p>
<p>The goal is to design encoding and decoding functions that can resist this noise, so that the recovered message \(\tilde{W}\) is as close as possible to the original message \(w\). To do so, the encoding \(x\) must contain some redundancy, i.e., become slightly longer (whereas for compression we wanted \(x\) to become shorter than \(w\)).</p>
<p>In this module, we will formally define (communication) channels, and see several examples of codes that can protect against noise (<span style="color: #bc0031;"><strong>error-correcting codes</strong></span>). We will explore which properties an error-correcting code should satisfy in order to decode to the correct message with high probability.</p>
<p>In the second part of the module, we will explore an even harder requirement on error-correcting codes: what if we want to decode to the correct message with <em>certainty</em>? This is known as the <span style="color: #bc0031;"><strong>zero-error</strong></span> setting. It really depends on the structure of the noise in the channel whether that is even possible. We will learn tools to study the noise structure of a channel.</p>
<p> </p>
<p>As an additional resource, you may find <a href="https://www.youtube.com/playlist?list=PLij6EOUQRtG9VOAsI11Wh2gDv4h5G2oPy">these student-recorded lectures</a> or <a href="https://www.youtube.com/playlist?list=PLwTkuB98zDQc39GNhoNYmJhzGiwPciWaI">these screen recordings</a> useful. However, please remember that the course content is defined by the material available on Canvas, so you may not get all the content by only watching the lecture recordings.</p>