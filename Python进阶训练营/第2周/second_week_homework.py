# 1-（需提交代码作业）不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。
# 2-（需提交代码作业）使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
# 3-通过课程代码，熟练掌握 HTTP 协议头、返回码、HTML 等知识点，这些在后面开发 Web 服务端程序时会频繁使用到。

> 助教的答复: 如果游客的方式可以抓取 ，就用游客身份抓取就可以。如果需要登录，就需要分析登录后的一些请求接口了，模拟请求时附带上登陆后的 cookie 来验证

> 老师的答复: ②要解决的是cookie问题，而知乎post用户密码是加密的可以采用调用知乎的js加密密码提交，也可以采用selenium模拟浏览器登陆成功一次拿到cookie再继续用requests做自动化操作，其他大家可以讨论

#  https://www.zhihu.com/tardis/sogou/art/32898234?ab_signature=CiRBUEJneXFtV3ZROUxCZThtLXZ2M2VmcV9YZ0k3Znczclcwaz0SIDU1MWQ0YzllY2JjNDE3ZmMxYWJmMDk5NzU5NmE4ZWZiGhAIARIGNi42OS4xGgQzNDYw

