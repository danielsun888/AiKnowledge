import datetime
from haystack import indexes
from .models import Articles


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索ArticlePost，所以创建ArticlePostIndex类
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段
    # author = indexes.CharField(model_attr='author')  # 创建一个author字段,model_attr='author'代表对应数据模型ArticlePost中的author字段，可以删
    # title = indexes.CharField(model_attr='title')  # 创建一个title字段
    # body = indexes.CharField(model_attr='body')

    # 对那张表进行查询
    def get_model(self):  # 重载get_model方法，必须要有！
        # 返回这个model
        return Articles

    # 针对哪些数据进行查询
    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(updated__lte=datetime.datetime.now())
        return self.get_model().objects.all()


# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     author = indexes.CharField(model_attr='user')
#     pub_date = indexes.DateTimeField(model_attr='pub_date')

#     def get_model(self):
#         return Note

#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())