case文件夹：
    1.主要是存放的用例（例：Test_a_Login.py）
    2.base.py是把每次unittest请求相同的初始化、垃圾回收提取，以及log的打印的工作，通过继承的方式解决test每次的初始化工作和后续需要打印log的地方的调用
    3.如果下一个请求需要使用上一个请求返回的数据（如：token）可以通过调用上一个请求，获取返回数据，然后当作参数传入下一个请求的参数中
    4.往excel指定单元格写入数据

common文件夹：
    1.主要是存放一些常用的工具类
    2.CommonMethod.py：存储的都是请求参数的获取
    3.MysqlTest.py:连接数据库执行增删改查
    4.HTMLTestRunner.py:用于测试报告的生成，不需要修改
    5.RequestsMethod.py：用于对请求方法的封装，通过判断传入的请求方法名，来判断使用什么请求方法

config文件夹：
    1.config.ini：配置文件，用于存储一些基本配置，如：ip、路径、端口、请求方法等。因为不需要参数化，所以存在配置文件中
    2.read_excel.py：用于读取excel，来获取参数化的内容
    3.ReadWriteConfig.py：用于读写配置文件中的内容
    4.write_excel.py:用于向excel中写入响应得数据
    5.id_rsa:为git密钥
    6.get_parameters.py:为指定参数化testdata.xlsx的路径、sheet获取

log文件夹;
    1.logger.txt用于存储生成的日志文件（目前为追加模式）
    2.log.py：日志打印功能，用于打印输出在控制台和写入文件中
    3.logger1.py：可以控制日志文件写入大小，从而生成第二个、第三个、、、、、、、日志文件（目前没使用）

report文件夹：
    1.用于生成html测试报告的存储

run_allcase_report:
    1.用于批量执行测试用例，把测试报告写成html格式，对于生成的测试报告发送邮件

testdata.xlsx：
    1.测试用例（参数化的存储地方）


具体封装之间通过以下之间互调
    1.因为unittest通过test关键字来运行测试用例，所以Test_*.py通过继承base.py来实现初始化、垃圾回收、以及日志的打印
    2.那么base.py就需要继承unittest.TestCase和logger（是log.py的方法）
    3.既然base.py来处理初始化工作，那么test需要的参数也就可以在这里面来获取了，因此通过调用CommonMethod方法来获取需要的参数
    4.CommonMethod通过传递的参数来调用config，读取ini文件中的数据，通过获取的数据作为参数，这样也就可以获取请求方法，来判断是什么方法来调用什么使用什么方法请求了

目前遗留问题：
    1.如果要结合jenkins使用接口自动化执行，那么需要自己在Jenkins上写一段运行.py文件的代码（例如cd E：  python D:\xxx\xxx\xxx.py）
    2.对于需要使用代理、认证、cookie、session、重定向等没有加入例子，个别的没有找到比较合适的例子



