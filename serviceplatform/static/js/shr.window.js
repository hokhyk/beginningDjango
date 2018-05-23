if (typeof shr == 'undefined') {
	var shr = $;
}

shr.extend({
	
	custom_chrome: 'C:\\ChromePortable\\ChromePortable.exe',
	reg_chrome: 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe\\',
	help_page: 'browser.jsp',
	//hr_server: 'http://172.19.76.43:6888/easweb',
	
	openWindow: function(url) {
		if("userNameIsNull" == url){
			alert('此用户没有权限登录s-HR,请检查s-HR用户信息！');
			//window.close();
			return ;
		}
		if (!url || url == 'null') {
			alert('url为空');
			return;
		}
		
		if ($.browser.msie && $.browser.version < 9) {
			var shell = shr.getShell();
			if (!shell) {
				return;
			}
			
			// 先使用系统安装的chrome打开
			var chromePath;
			try {
				// 读注册表
				chromePath = shell.regRead(this.reg_chrome);
			} catch (ex) {
			}
			if (typeof(chromePath) != 'undefined') {
				chromePath = '"' + chromePath.replace(/\\/g, '\\\\') + '"';
				var result = this.execChrome(shell, chromePath, url);
				if (result && result.ExitCode == 0) {
					shr.closeWindow();
					return;
				}			
			}
			
			// 如果使用系统chrome没有打开，则再判断C盘是否有chromePortable
			var fileexists = shr.reportFileStatus(this.custom_chrome);
			if (fileexists == "false") {
				document.location.href = this.help_page;
			} else if (fileexists == "true") {
				var command = 'cmd /c start ' + this.custom_chrome;
				var result = this.execChrome(shell, command, url)
				if (result) {
					if (result.ExitCode == 0) {
						shr.closeWindow();
						return;
					} else if (result.ExitCode == 1) {
						alert('请确认是否安装了chrome');
					}
				}
			}
			
		} else {
			document.location.href = url;
		}
	},
	
	loginHR: function(tokenUrl, redirectTo) {
		$.ajax({
			url: tokenUrl, //tokenUrl = '<%=request.getContextPath()%>/shr/sso2hrUrl.jsp';
			// data: {
			// 	redirectTo: redirectTo
			// },
			type: 'POST',
			dataType: 'text',
			success: function(response) {
				alert(response);

				shr.openWindow($.trim(response));
			},
			error: function(xhr, textStatus, errorThrown) {
				alert('生成token失败，请联系系统管理员');
			}
		});
	},
	
	getRedirectTo: function() {
		var url = location.href,
			newUrl,
			flag = 'redirectTo=',
			index = url.indexOf(flag);
		if (index > 0) {
			var endIndex = url.indexOf('&', index);
			if (endIndex != -1) {
				newUrl = url.substring(index + flag.length, endIndex);
			} else {
				newUrl = url.substring(index + flag.length);
			}
			newUrl = decodeURIComponent(newUrl);
		} else {
			newUrl = '/main.do';
		}
		//alert(newUrl);
		return newUrl;
	},

	closeWindow: function() {
		// 去掉提示关闭窗口的信息
		window.open('','_self');
		window.opener = null;
		window.close();
	},
	
	showActivexMessage: function() {
		$('#main').show();
		//alert('请确认是否将站点设置为信任站点，并在安全设置里允许ActiveX插件运行!');
	},
	
	getShell: function() {
		try {
			return new ActiveXObject("WScript.Shell");
		} catch (ex) {
			shr.showActivexMessage();
		}
	},
	
	reportFileStatus: function (filespec) {
		try{
			var fso = new ActiveXObject("Scripting.FileSystemObject");
			if (fso.FileExists(filespec)) {
				return "true";
			} else {
				return "false";
			}
		}catch(ex){
			shr.showActivexMessage();
		}
	},
	
	execChrome: function(shell, chromePath, url) {
		//alert(chromePath);
		var command = chromePath +  ' "' + url + '"';
		return shell.Exec(command);
	}
	
});