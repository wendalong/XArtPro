from django.db import models

# Create your models here.
class Tag(models.Model):
    # name, describe, add_time
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='标题')
    describe = models.CharField(max_length=100,
                                verbose_name='描述')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:  # 元信息－描述模型类的信息(ORM)
        db_table = 't_tag'  # 类对应 数据库中表的名称
        verbose_name = '标签'  # 在后台显示模型类的名
        verbose_name_plural = verbose_name  # 后台复数的显示内容
        ordering = ['-add_time']


class Category(models.Model):
    title = models.CharField(max_length=20,
                             unique=True,
                             verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    # 父分类关系？
    # parentCate = models.ForeignKey(Category, )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name


class Art(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='标题')
    summary = models.CharField(max_length=100,
                               verbose_name='描述')
    content = models.TextField(verbose_name='详细说明')

    author = models.CharField(max_length=20,
                              verbose_name='作者')

    publish_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='发布时间')

    # 文章的封面图片 cover

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='分类名')

    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_art'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']