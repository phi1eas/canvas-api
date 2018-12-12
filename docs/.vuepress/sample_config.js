module.exports = {
	title: 'Information Theory',
	description: 'UvA course',
	themeConfig: {
		sidebar: SIDEBAR,
		editLinks: false,
		displayAllHeaders: true
	},
	head: [
		[
			'script',
			{ 
				type: 'text/x-mathjax-config'
			},
			"MathJax.Hub.Config({tex2jax: {inlineMath: [ ['$','$'], ['\\\\(','\\\\)'] ],processEscapes: true}});"
		],
		[ 'script',
			{ src: '/assets/js/MathJax.js?config=TeX-AMS_HTML'}
		],
		[
			'script',
			{ 
				type: 'application/javascript'
			},
			"function timeout() {setTimeout(function() {MathJax.Hub.Queue([\"Typeset\", MathJax.Hub]);timeout();}, 1000)};MathJax.Hub.Queue([\"Typeset\", MathJax.Hub]);timeout();"
		]
	]
}