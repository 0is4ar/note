# java/spring

## Java

bean, pojo, maven, hibernate, pom, application.properties

- pojo stands for **Plain** Old Java Object. No extend, inplement, annotations
- bean: a serializable pojo
    - All properties private(use getters/setters)
    - A public no-argument constructor
    - Implements Serializable
- maven is like cargo to Rust

### Bean

a property of a bean means a private variable that use setter/getter to interact with.

And the setter and getter have to follow name convention by default.

```java
private String name

public void setName(String name) {this.name = name}
public String getName() {return this.name;}

```

### import package

/haha.java
    `import test.Product`
/test/Product.java
    `package test`

And Product.java has to be compiled to `Product.class` before run haha.java, by `javac Product.java`

#### default path to find class dependency

### Some specification

- A class file only have `one` **public** class, with the same class name as filename.

- every class could have a main, which main to be invoked depends on which class is run.

### Array and ArrayList

* Array is fixed length

```text
int arr[] = new int[10]
```

* Array list is dynamic sized

```
ArrayList<Type> arrL = new ArrayList<Type>();
```

### decompile/compile 

extract a jar and assemble it again can lead to a lot of troubles.
A convenient way is to update it using `jar -uf warfile updatedfile`

## Spring

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


- Example(`@ModelAttribute` method without annotation param)


```java
@ModelAttribute 
public Account addAccount(@RequestParam String number) { 
    return accountManager.findAccount(number); 
} 
```
In this case, because there's no spcification like `@ModelAttribute('attrname')`, the framework use the return object's class name --- 'Account', and use lowercase, so the attribute name is `account`


##### Example(`ModelAttribute` as parameter)

I think this should be classified to two scenarios:

- `@ModelAttribute` annotates param in method B, but also annotated method A.

    Because method A is also annotated and will be invoked earlier, let's say `@ModelAttribute('user')`, B will retrieved the object in model attribute return by A, knowing it's a `User` object by the parameter, and replace the fields User object has according to request parameter.

- `@ModelAttribute` only annottates param in method B. 

  `@ModelAttribute(value="message") String message`

  the Spring can't find the attribute in the model. so according to `String`, it initialize a String object. And try to find request parameter `message`


There's a minor imsymmatrical of these two examples. 

because for the first example, I won't pass parameter like `?user=`, instead, because User object has `name` field, I pass `?name=`

for the second example, I pass `?message=`
