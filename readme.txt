===============================V1.0:add by kongsh
基于关键字驱动的测试框架，整体的结构说明如下：
Action
            __init__.py
	 SendResultAction.py#发送邮件
           TestCaseFileParser.py#解析测试excel，包括清除测试结果，获取待执行的sheet名称
           WebElementAction.py#所有的映射函数
Config
            __init__.py
            Logger.conf#日志的配置文件
            ProjVar.py#工程根目录、所有目录文件路径、浏览器驱动路径，excel文件操作的行号
        Report# 测试结果
            CapturePics
                Fail# 存放用例执行失败时的截图
                Pass# 存放用例执行成功时的截图
            Log# 存放用例执行过程中的log信息
            TestReport# 存放测试报告
        Scripts
             __init__.py
             Test.py#单元测试脚本，继承unittest.Testcase
        TestData
             MailReceiver.ini#邮件相关配置信息
             ObjectDeposit.ini# 所有的页面元素定位表达式相关配置信息
             测试用例.xlsx# 测试用例信息
        Utils
            BrowserUtils# 存放浏览器相关的公共方法
                __init__.py
                ClipboardUtil.py# 剪贴板操作方法
                KeyboardUtil.py# 键盘操作方法
                ObjectMap.py# 对象映射，根据定位方法和定位表达式活动页面元素对象
                WaitUtil.py#显示等待工操作方法
            FileUtils# 存放文件操作相关的公共方法
                __init__.py
                Capture.py#截图操作方法
                ConfigParser.py#ini文件操作方法
                Dir.py#目录操作方法
                Excel.py#excel操作方法
                GenTestReport.py#生成测试报告
                Log.py#日志
 	  OtherUtils# 其它常用的公共方法
                __init__.py
               GenTime.py#日期和时间操作方法
               SendMail.py#发送邮件的基础函数
        main.py# 程序入口函数          