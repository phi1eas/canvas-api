# Definition: Binary Entropy

<p>For a <a title="A binary random variable is a random variable that can take on two values." data-tooltip='{"tooltipClass":"popover popover-padded", "position":"right"}'>binary random variable</a> \(X\) with image \({\cal X} = \{x_0,x_1\}\) and probabilities \(P_X(x_0) = p\) and \(P_X(x_1) = 1-p\), we can write \(H(X) = h(p)\), where \(h\) denotes the binary entropy function:</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Binary entropy function \(h\)</strong></h4>
<p>The binary entropy function is defined for \(0 &lt; p &lt; 1\) as \[ h(p) := p \log\frac{1}{p} + (1-p)\log\frac{1}{1-p}, \] and is defined as \(h(p) = 0\) for \(p=0\) or \(p=1\).</p>
</div>
<p>The <a href="https://www.wolframalpha.com/input/?i=Plot%5B-p*log2(p)-(1-p)*log2(1-p),+p%3D0..1%5D">graph of \(h\) </a>on the interval \([0,1]\), as a function of \(p\), looks as follows:</p>
<p style="text-align: center;"><a class="instructure_file_link" title="fig-binary-entropy-1.svg" href="https://canvas.uva.nl/courses/2205/files/46125/download?verifier=S390kKrlAnalczK4QkRCvq5f1CJ7JectfRO2Yjy1&amp;wrap=1" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/46125" data-api-returntype="File"><img style="border: 0px solid #000000; padding: 2px;" src="https://canvas.uva.nl/courses/2205/files/46125/preview?verifier=S390kKrlAnalczK4QkRCvq5f1CJ7JectfRO2Yjy1" alt="plot of binary entropy" width="318" height="254" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/46125" data-api-returntype="File"></a></p>
<p style="text-align: left;">If we think of \(X\) as the random variable describing the outcome of a coin flip, we see that a relatively fair coin (\(p \approx \frac{1}{2}\)) yields a higher expected surprisal value than a very biased coin (where \(p\) is closer to 0 or 1). If the coin is completely fair (\(p = \frac{1}{2}\)), the entropy is exactly 1 bit.</p>
<p> </p>