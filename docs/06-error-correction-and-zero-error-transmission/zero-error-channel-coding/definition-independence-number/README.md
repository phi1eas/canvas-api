<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Undirected Graph</strong></h4>
A undirected simple graph \(G\) consists of a set \(V(G)\) of <span style="color: #bc0031;"><strong>vertices</strong></span> and a set \(E(G)\) of <span style="color: #bc0031;"><strong>edges</strong></span>. The edges are unordered pairs of vertices: each edge connects two different vertices of the graph.</div>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Independence number</strong></h4>
The independence number \(\alpha(G)\) of a graph \(G\) is the size of the largest <span style="color: #bc0031;"><strong>independent set</strong></span> of \(G\), where an independent set of \(G\) is a set \(S \subseteq V(G)\) such that \[ \forall x, x' \in S: (x,x') \not\in E(G). \] That is, an independent set \(S\) in \(G\) is a set of vertices such that there is no edge between any of the vertices.</div>
<p>Finding the independence number of a graph is an NP-hard problem, meaning there is no known efficient method for finding the independence number of an arbitrary graph.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #2d3b45;"><strong>Example</strong></h4>
Consider the following graph with \(V(G) = \{1,2,3,4,5,6\}\) and \(E(G) = \{\{1,2\}, \{2,3\}, \{2,4\}, \{3,4\}, \{4,5\}, \{4,6\}, \{5,6\}\}\):
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="/img/329558?verifier=wkoBJ5kHXla1669RTG9fzb3q18VILJNrUQU8MDE2" alt="A graph" width="137" height="111" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/329558" data-api-returntype="File"></p>
A maximal independent set \(\{1,3,6\}\) is marked in the graph. As there is no independent set of size 4 (can you prove that?), the independence number of this graph is 3.</div>