from django.http import HttpResponse


# # Pycharm不认识咱们的项目结构，标准结构是子应用创建在根目录下面。所以可以把app设置为根目录就可以
# # 但是也不影响 留着后面看看写博客留着水文章
from TestModel.models import Test

from django.shortcuts import render

def testdb(request):
    test1 = Test(name='LXH')
    test1.save()
    return HttpResponse('<p>数据{}添加成功</p>'.format(test1))