# java/spring

bean, pojo, maven, hibernate, pom, application.properties

### handler 

A handler is a function annotated by `@RequestMapping("/somedirectory")`

* parameters

there're a lot of parameters handler can receive from "dispatcher"\(or other term\).  

{% embed url="https://docs.spring.io/spring/docs/current/spring-framework-reference/web.html\#mvc-ann-arguments" %}

* return value

if return a string, like 

`return "success";`

the app will find "success.jsp" in template directory\( if configure so\). Which is configured in application.properties

`spring.mvc.view.prefix=/WEB-INF/templates/ spring.mvc.view.suffix=.jsp` 

### Model

`Model` in Spring is a interface, is not a class. Which is **VERY VERY** different from Flask.

Model is kinda like a dictionary, so attribute is like element of it.

#### ModelAttribute

use `@ModelAttribute` to access an attribute from the model.

example:

```java
@PostMapping("/owners/{ownerId}/pets/{petId}/edit")
public String processSubmit(@ModelAttribute Pet pet) { }
```

`@ModelAttribute` can be used with or without parameter. When used without parameter. It will try to "guess" something. 

There are three kinds of `@ModelAttribute` usages. Below are two main usages. 

* on a method argument in `@RequestMapping`
* before definition of method in `@Controller` 

> A controller can have any number of `@ModelAttribute` methods. All such methods are invoked before `@RequestMapping` methods in the same controller.

{% embed url="https://blog.csdn.net/abc997995674/article/details/80464023" %}

When a model is defined by a `@ModelAttribute` method associate with a real model in other class file\(`import ru.volgactf.shop.models.User;`\), and as parameter of `@RequestMapping` method, the request parameter\(form\) will be used to populate the  model.



### Array and ArrayList

* Array is fixed length

```text
int arr[] = new int[10]
```

* Array list is dynamic sized

```
ArrayList<Type> arrL = new ArrayList<Type>();
```

