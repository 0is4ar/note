# Flask

<!-- vim-markdown-toc GFM -->

* [Form相关](#form相关)
* [SQL相关](#sql相关)
* [Views](#views)
    * [render_template](#render_template)
* [关键字笔记](#关键字笔记)
    * [current_user](#current_user)
* [功能模块笔记](#功能模块笔记)
    * [显示博文功能views,form,templete的功能划分](#显示博文功能viewsformtemplete的功能划分)

<!-- vim-markdown-toc -->

## Form相关

* 在一个表单的class中，如果有方法validate_\<name>，其中name是这个表单的一个字段（class的一个属性，那么提交时会自动调用这个方法来检验这个字段
* 基础字段
    * TextAreaField(输入提示文字)
    * SubmitField(按钮文字)


## SQL相关

### 在Views中的使用
* `user.posts.order_by(Post.timestamp.desc()).all()`   
user.posts 返回的是一个query对象，就像User.query一样

* 如下代码中，
    1.Post.author_id引用user.id作为外键
    2.User.posts接受
    3.且返回一个author作为回引，post.author就直接访问这个User对象

```
class User():
    posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post():
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
```


  * order_by是个过滤器返回的依旧是对象的list, timestamp是集成的db.DateTime 所以有这个过滤器方法也不奇怪
  


## Views

* 使用分页导航

```python
pagination = query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
        
posts = pagination.items

```


- 可以使用flask中的request对象来得到请求的信息，比如说`request.args.get('page', 1, type=int)`(第二个参数指如果没有这个arg的话默认参数)

### render_template

- 可以返回的字段是一个user对象，这样在html中同样可以引用这个user对象

## 关键字笔记
### current_user
* current_user 由 Flask-Login 提供，和所有上下文变量一样，也是通过线程内的代理对象实现。这个对象的表现类似用户对象，但实际上却是一个轻度包装，包含真正的用户对象。 数据库需要真正的用户对象，因此要调用 _get_current_object() 方法。


## 功能模块笔记

### 显示博文功能views,form,templete的功能划分
* forms 简单规定了一个form的字段
* views 来实现将从表单中获取博文，生成Post对象，将对象写入数据库
* templete 控制了不同用户写权限是否要加载表单


## ckeditor配置
* 在app/__init加入 `ckeditor = CKEditor()`
    create_app函数加入`ckeditor.init(app)`
    
* PostForm中
   `body = CKEditorField('Content', validators=[DataRequired()])`
   
* config.py



```python
CKEDITOR_SERVE_LOCAL = True
CKEDITOR_HEIGHT = 400
CKEDITOR_FILE_UPLOADER = 'main.upload'
UPLOADED_PATH = basedir + '/upload'
```


* views

```python
@main.route('/upload', methods=['POST'])
@ckeditor.uploader
def upload():
       f = request.files.get('upload')
       f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
       url = url_for('main.files', filename=f.filename)
       return url

@main.route('/files/<filename>')
def files(filename):
       path = current_app.config['UPLOADED_PATH']
       return send_from_directory(path, filename)
```

* template

`{{ ckeditor.load() }}` 在body里

