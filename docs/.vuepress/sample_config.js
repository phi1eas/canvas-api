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
			"MathJax.Hub.Config({tex2jax: {inlineMath: [ ['$','$'], ['\(','\)'] ],processEscapes: true}});"
		],
		[ 'script',
			{ src: 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_HTML'}
		]
	],
	base: '/canvas-api/'
}