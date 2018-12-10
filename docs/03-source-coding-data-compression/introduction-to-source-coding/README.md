<p>Suppose we sample $x$ from a distribution $P_X$ with image $\cal X$. In the context of data compression, $P_X$ is typically called a <span style="color: #bc0031;"><strong>source</strong></span> that emits value $x \in {\cal X}$ with probability $P_X(x)$. We want to compress (or encode) symbols $x$ sampled from $P_X$ in such a way that we can later decompress (or decode) it reliably, without losing any information about the value $x$.</p>
<p>![An image](./public/assets/img/129715)<img style="display: block; margin-left: auto; margin-right: auto;" src="129715" alt="Encoding and decoding of a source" width="521" height="76" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/129715" data-api-returntype="File"></p>
<p>A counting argument shows that it is possible to encode the elements of ${\cal X}$ by bit strings of length $n$, where $n=\lceil \log (|{\cal X}|) \rceil $: we simply list all elements of ${\cal X}$, and use the (binary) index of $x$ in the list as its encoding. Thus, to store or to transmit an element $x\in {\cal X}$, $n$ bits of information always suffice. However, if not all $x \in \cal X$ are equally likely according to $P_X$, one should be able to exploit this to achieve codes with shorter <i>average</i> length. The idea is to use encodings of varying lengths, assigning shorter codewords to the elements in ${\cal X}$ that have higher probabilities, and vice versa.</p>
<div style="width: 100%; float: left; text-align: center;">
<iframe src="https://www.youtube.com/embed/musBo7Kafic" width="640" height="360" allowfullscreen="allowfullscreen"></iframe>
<p style="text-align: center;"><span style="color: #999999;">Video by Khan Academy is licensed under <a style="color: #999999;" href="https://creativecommons.org/licenses/by-nc-sa/3.0/us/">CC BY-NC-SA 3.0 US.</a></span></p>
</div>
<p>In the video, Alice and Bob communicate by encoding their messages (dice rolls) from $\mathcal{X} = \{2,3,...,12\}$ into a unitary alphabet $\{1\}$, where each 1 stands for a pluck of the wire. For example, the roll 8 is encoded as <span>111</span>, or three plucks.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4>Exercise</h4>
<p>At the end of the video, Bob gets a better idea. He notices that they can pluck the wire in two different ways that are easy to distinguish: long or short. Can you design a code using this binary alphabet of plucks? How long are your codewords on average?</p>
<p><span class="element_toggler" role="button" aria-controls="group_1" aria-label="Toggler" aria-expanded="false"> <span class="Button">Show solution</span></span></p>
<div id="group_1" style="">
<div class="content-box">
<div class="grid-row middle-xs">
<div class="col-xs-12 col-md-6">
<div class="styleguide-section__grid-demo-element">The code on the right is an example of a code that Alice and Bob may use: 0 stands for a short pluck, 1 stands for a long one. Each die roll has a different codeword, and short codewords are assigned to the most likely outcomes. The expected codeword length is \[ \frac{1}{36} \cdot 3 + \frac{2}{36} \cdot 3 + \frac{3}{36} \cdot 2 + ... + \frac{1}{36} \cdot 3 = \frac{35}{18} \approx 1.944. \] So on average, Alice and Bob expect to pluck the wire a little less than two times per die roll they want to communicate. However, if they want to communicate a list of die roll outcomes, they run into a problem: if Alice receives 011, how can she tell whether Bob sent the list [7,4], or [5,6], or even [2]?</div>
</div>
<div class="col-xs-12 col-md-6">
<div class="styleguide-section__grid-demo-element">
<table class="ic-Table">
<thead>
<tr>
<th>Die roll</th>
<th>Codeword</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>011</td>
</tr>
<tr>
<td>3</td>
<td>001</td>
</tr>
<tr>
<td>4</td>
<td>11</td>
</tr>
<tr>
<td>5</td>
<td>01</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>0</td>
</tr>
<tr>
<td>8</td>
<td>00</td>
</tr>
<tr>
<td>9</td>
<td>10</td>
</tr>
<tr>
<td>10</td>
<td>000</td>
</tr>
<tr>
<td>11</td>
<td>010</td>
</tr>
<tr>
<td>12</td>
<td>100</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div class="content-box">
<div class="grid-row middle-xs">
<div class="col-xs-12 col-md-6">
<div class="styleguide-section__grid-demo-element">This problem is resolved in the code on the right: confusions do not arise even when variable-length lists of messages are sent. The average codeword length is longer, however: roughly 3.306 plucks on average. In this module, you will encounter several algorithms for constructing such codes yourself for any given probability distribution.</div>
</div>
<div class="col-xs-12 col-md-6">
<div class="styleguide-section__grid-demo-element">
<table class="ic-Table">
<thead>
<tr>
<th>Die roll</th>
<th>Codeword</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>11110</td>
</tr>
<tr>
<td>3</td>
<td>0010</td>
</tr>
<tr>
<td>4</td>
<td>0011</td>
</tr>
<tr>
<td>5</td>
<td>100</td>
</tr>
<tr>
<td>6</td>
<td>000</td>
</tr>
<tr>
<td>7</td>
<td>010</td>
</tr>
<tr>
<td>8</td>
<td>011</td>
</tr>
<tr>
<td>9</td>
<td>101</td>
</tr>
<tr>
<td>10</td>
<td>110</td>
</tr>
<tr>
<td>11</td>
<td>1110</td>
</tr>
<tr>
<td>12</td>
<td>11111</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<p>The question we will answer in this module is: how short can codes be in general (on average over repeated samples $x$ from $P_X$)? We explore both <span style="color: #bc0031;"><strong>lossless</strong></span> codes (where we want to recover the original data with certainty) and <span style="color: #bc0031;"><strong>lossy</strong></span> codes (where with small probability, the data is lost).</p>
<p> </p>