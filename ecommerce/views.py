from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  context = {
    "title":"Hello World!",
    "content": "welcome to the homepage!"
  }
  return render(request, "home_page.html", context)

def about_page(request):
  context = {
    "title":"About page!",
    "content": "welcome to the homepage!"
  }
  return render(request, "home_page.html", context)

def contact_page(request):
  context = {
    "title":"Contact page!",
    "content": "welcome to the homepage!"
  }
  if request.method == "POST":
    print(request.POST)
    print(request.POST.get('fullname'))
    print(request.POST.get('email'))
    print(request.POST.get('content'))
  return render(request, "contact/view.html", context)

def home_page_old(request):
  html_ = """
  <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class='text-center'>
    <h1>Hello, world!</h1>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
  """

  return HttpResponse(html_)