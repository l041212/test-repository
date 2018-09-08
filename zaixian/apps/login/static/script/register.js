$(function(){
	var error_code = false;
	var error_password = false;
	var error_check = false;


	$('#code').blur(function() {
		check_code();
	});

	$('#pwd').blur(function() {
		check_password();
	});




	function check_password(){
		var len = $('#password').val().length;
		if(len<8||len>20)
		{
			$('#password').next().html('密码最少8位，最长20位')
			$('#password').next().show();
			error_password = true;
		}
		else
		{
			$('#password').next().hide();
			error_password = false;
		}		
	}



	function check_code(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#code').val()))
		{
			$('#code').next().hide();
			error_code = false;
		}
		else
		{
			$('#code').next().html('你输入的邮箱格式不正确')
			$('#code').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {

		check_code();
		check_password();
        console.log
		if( error_password == false && error_code == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});
})
