# DNSPOD_Domain_Log

HTTP请求方式：
POST
请求参数：
参数名	是否必须	参数描述
公共参数	是	详见：公共参数
domain_id 或 domain	是	分别对应域名ID和域名, 提交其中一个即可
offset	否	记录开始的偏移，第一条记录为 0，依次类推，默认为0
length	否	共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条

响应代码：
共通返回
-7 企业账号的域名需要升级才能设置
-8 代理名下用户的域名需要升级才能设置
6 域名ID错误
8 非域名所有者


![images](https://github.com/hanyan007/DNSPOD_Domain_Log/blob/master/dns.png)
