
i


$(
	function(){
		var qiyeweixin ='<img src="{% static 'img/img_3.png'%}">'
		var jishuwenxi ='<img src="{% static 'img/img_3.png'%}">'
		var xiaoshouweixin ='<img src="{% static 'img/img_3.png'%}">'
		$('#right_weixin_qiye').popover({
			html:true,
			content:qiyeweixin,
		});
		$('#right_qq').popover({
			html:true,

		});
		$('#right_weixin_xiaoshou').popover({
			html:true,
			content:xiaoshouweixin,
		});
		$('#right_weixin_jishu').popover({
			html:true,
			content:jishuwenxi,
		});
	  }
    )


function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
