# Definition: Strong Graph Product

<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Strong graph product</strong></h4>
Let \(G, H\) be two graphs. We define the strong graph product \(G \boxtimes H\) as follows. The set of vertices is \[ V(G \boxtimes H) := V(G) \times V(H). \] The set of edges is \[ \begin{split} E(G \boxtimes H) := \big\{\{(x,y),(x',y')\} \mid (x,y) \neq (x',y') &amp;\text{ and } \left(x = x' \text{ or } \{x,x'\} \in E(G) \right) &amp;\text{ and } \left(y=y' \text{ or } \{y,y'\} \in E(H) \right) \big\}, \end{split} \] i.e., there is an edge between \((x,y)\) and \((x',y')\) if and only if the vertices of \(G\) are confusable (or equal) <i>and</i> the vertices of \(H\) are confusable (or equal).</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Consider the graph \(G\):
<p style="text-align: center;"><img src="https://canvas.uva.nl/courses/10933/files/1322446/download?verifier=7JXNP8LGp4O1VMQQdn36YY5mVjw0NY1qWEpG0z6y" alt="A graph with three vertices" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322446" data-api-returntype="File"></p>
and the graph \(H\):
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322444/download?verifier=LCjaZqG0AXEFfvDKuqGFXbh3q7YQB8PLkRqc6GYa" alt="A graph with two vertices" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322444" data-api-returntype="File"></p>
The strong graph product of \(G \boxtimes H \) is
<p style="text-align: center;"><img src="https://canvas.uva.nl/courses/10933/files/1322452/download?verifier=yH31xhcvXW8heK5on26NH2So41NP3q1pvMq3mV1V" alt="Strong graph produt of G and H" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322452" data-api-returntype="File"></p>
The independence number of this graph is 2. The strong product \( G \boxtimes G \) of \(G\) with itself is
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://canvas.uva.nl/courses/10933/files/1322447/download?verifier=MY3G0KocQB4fbqjHqAKDHglo78fOyyd0pSJiBqiz" alt="ZE9-1.svg" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/10933/files/1322447" data-api-returntype="File"></p>
The independence number of this graph is 4. As the graphs get bigger, the independence number is increasingly hard to compute.</div>
<p>For our application, we will often be interested in the strong graph product of a graph \(G\) with itself, possibly many times. Therefore it is useful to work out the definition of \(G^{\boxtimes n}\), based on the above definition: \begin{align*} V(G^{\boxtimes n}) &amp;= V(G) \times \cdots \times V(G)\\ E(G^{\boxtimes n})&amp;= \big\{ \{(x_1, \ldots, x_n),(v_1, \ldots, v_n)\} \mid (x_1, \ldots, x_n) \neq (v_1, \ldots, v_n) \text{ and } \forall i : x_i = v_i \vee \{x_i,v_i\} \in E(G)\} \end{align*}</p>