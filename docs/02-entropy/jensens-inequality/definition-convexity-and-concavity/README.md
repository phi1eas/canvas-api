<p>In the following, let \(\mathcal{D}\) be an interval in \(\mathbb{R}\).</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Definition: Convex and concave functions</strong></h4>
The function \(f : \mathcal{D} \to \mathbb{R}\) is convex if for all \(x_1, x_2 \in \mathcal{D}\) and all \(\lambda \in [0,1] \subset \mathbb{R}\): \[ \lambda f(x_1) + (1-\lambda)f(x_2) \geq f(\lambda x_1 + (1-\lambda)x_2). \] The function \(f\) is <i>strictly</i> convex if equality only holds when \(\lambda \in \{0,1\}\) or when \(x_1 = x_2\). The function \(f\) is (strictly) concave if the function \(-f\) is (strictly) convex.</div>
<p>Intuitively, a function is convex if any straight line drawn between two points \(f(x_1)\) and \(f(x_2)\) lies above the graph of \(f\) entirely. For a concave function, such a line must lie entirely beneath the graph. Play around with the interactive figure below to understand the formulas above! Note that you can move the red slider for \(\lambda\), and you can also adjust \(x_0, x_1\) directly in the graph.</p>
<p> </p>
<p><iframe src="https://esc.fnwi.uva.nl/blend/information-theory/interactive-graphs/definition-of-convexity-concavity.htm" width="1010" height="850"></iframe></p>
<h3>Convex or concave? MacKay's Mnemonic</h3>
<p>David MacKay has a great way of remembering "which way" convex and concave functions go, namely by noticing the following. When pronouncing the word "convex", one could continue to say "smile", while pronouncing the word "concave", it could be followed by the word "frown".</p>
<p><a id="media_comment_maybe" class="instructure_file_link instructure_video_link" title="Video-2018-05-16-12-30-51_MacKays mnemonic.MP4" href="https://canvas.uva.nl/courses/2205/files/123923/download?verifier=AEFfJEKv3GeUfdocb3NI5vKenxMjeBPCTVdgzBPy&amp;wrap=1" data-api-endpoint="https://canvas.uva.nl/api/v1/courses/2205/files/123923" data-api-returntype="File">Video-2018-05-16-12-30-51_MacKays mnemonic.MP4</a></p>
<p>The following proposition establishes a formal method of proving the convexity of a function.</p>
<div class="content-box pad-box-mini border border-trbl border-round">
<h4 style="color: #bc0031;"><strong>Proposition</strong></h4>
Let \(f : \mathcal{D} \to \mathbb{R}\). If \(\mathcal{D}\) is open, and for all \(x \in \mathcal{D}\), the second-order derivative \(f''(x)\) exists and is non-negative (positive), then \(f\) is convex (strictly) convex.
<p><span class="element_toggler" role="button" aria-controls="group2" aria-label="Toggler" aria-expanded="false"><span class="Button">Show proof</span></span></p>
<div id="group2" style="display: none;">
<div class="content-box">
<p>We omit the proof, which can be found in, for example, <a href="http://homepages.cwi.nl/~schaffne/courses/inftheory/2016/notes/CramerFehr.pdf">[CF]</a> (Lemma 1).</p>
</div>
</div>
</div>