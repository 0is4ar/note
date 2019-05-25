# jsonp

## background

the very basical idea is `<script src=a.com/jsonp.php?id=9">` in client front end page

a.com/jsonp.php could easily return different java script code as per `id`. This could wrap data.

After front end got the code return from server, because it's actually a standalone external javascript, it will naturely run it as javascript code.


## example

### front end

```javascript

function showData (result) {
    var data = JSON.stringify(result); //json对象转成字符串
    $("#text").val(data);
}

$(document).ready(function () {

    $("#btn").click(function () {
        $("head").append("<script src='http://localhost:9090/student?id=3&callback=showData'><\/script>");
    });

});

```

As code, define function `showData`, and tell server the name of function by GET parameter, server return a javascript calling the function with **data stored in server**

### server side

in nodejs
```javascript

protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    response.setCharacterEncoding("UTF-8");
    response.setContentType("text/html;charset=UTF-8");

    List<Student> studentList = getStudentList();

    student_id = getParameter("id");
    JSONArray jsonArray = JSONArray.fromObject(student_id);
    //construct json as per student id sent from client
    String result = jsonArray.toString();

    String callback_name = request.getParameter("callback");
    result = callback_name + "(" + result + ")";

    response.getWriter().write(result);
}
```
