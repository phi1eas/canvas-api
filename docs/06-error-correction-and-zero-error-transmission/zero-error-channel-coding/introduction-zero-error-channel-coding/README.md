# Introduction: Zero-Error Channel Coding

<p>We consider the problem of using a noisy channel to transmit a message perfectly, i.e., with maximal probability of error equal to zero. For some channels, for example the non-trivial binary symmetric channel with \(f \not\in \{0,1\}\), it is not possible to send multiple different messages over the channel in this way. For other channels, an interesting question is: how many messages (or how much information) can be sent over this channel in an error-free way?</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Consider the following channel:
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322448/preview?verifier=luqcct2ZmIuBWslBVKBW33QBbtismJpEVcLg8g08" alt="A channel with two inputs and three outputs" width="108" height="102" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322448" data-api-returntype="File"></p>
We can send two messages, \(m_1\) and \(m_2\), over the channel by defining \(\mathtt{enc}(m_1) = a\) and \(\mathtt{enc}(m_2) = b\). The decoding is defined as \(\mathtt{dec}(1) = m_1\), and \(\mathtt{dec}(2) = \mathtt{dec}(3) = m_2\).</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 id="noisy" style="color: #2d3b45;"><strong>Example: Noisy typewriter</strong></h4>
The noisy typewriter channel sends the letters a through e, but with some nonzero probability, it sends the adjacent letter instead. It is defined as follows:
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322449/preview?verifier=0lYQZSKmqYnEMrQmPIzi35wyqsizrwm6K32vro1i" alt="The noisy typewriter" width="147" height="121" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322449" data-api-returntype="File"></p>
How many messages can you send error-free over this channel?
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Show solution</span></span></p>
<div id="group2" style="">
<div class="content-box">
<p>There is a way to send two messages \(m_1\) and \(m_2\) error-free over this channel by defining \(\mathtt{enc}(m_1) = a\) and \(\mathtt{enc}(m_2) = c\). The decoding function is defined as \(\mathtt{dec}(a) = \mathtt{dec}(b) = m_1\), and \(\mathtt{dec}(c) = \mathtt{dec}(d) = m_2\) (note that the definition of \(\mathtt{dec}(e)\) is irrelevant, as this output symbol will never be observed).</p>
<p>Is there a way to encode three different messages in an error-free way? Upon inspection, we see that any encoding function \(\mathtt{enc}(\cdot)\) on three messages will map at least two messages to channel inputs that are <span style="color: #bc0031;"><strong>confusable</strong></span> (i.e., are possibly mapped to the same channel output).</p>
</div>
</div>
</div>
<p>In general, it is not easy to tell directly from the channel how many messages can be perfectly transmitted. We will invoke some graph theory to help us with the analysis.</p>