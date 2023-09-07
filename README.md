ISOTOP 面试问题【后端java】   
我们在区块链（mumbai）上存放了一个NFT包含一张动态图片，每秒改变一次，以base64方式编码的SVG格式存放。请以java语言编写一个后台服务器，可以尽量多得接受前端GET并发请求，返回这张图片。

【更多信息】：   
参考仓库：isotop-interview   
可以添加你的branch提交代码   
Mumbai链的信息：   
80001	Polygon Mumbai   
合约地址：0x0314502e8F38be59221B95c60eEFeB39FE3b5a78   
合约ABI：abi.json   
需要调用的方法取得metadata：tokenURI(0) 其中0为NFT的编号   

【提示】：   
tokenURI 返回的结果为base64编码的JSON metadata，可以直接在浏览器打开查看。其中的image字段就是我们要的图片。图片本身也是用base64编码的，可以直接拷贝其内容到浏览器查看。解码后保持到本地缓存。该图片每秒钟变化一次。   

可以自备服务器，或者我们可提供阿里云服务器部署。测试使用并发压力测试，获取服务器缓存的图片。可以使用任何后台并发技术或数据库技术。   

尽情展示你的才能，加入探宝游戏！
