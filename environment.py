from pages.forgot_password_page import Forgot_password_page
from pages.sign_in_page import Sign_in_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.forgot_pass_page = Forgot_password_page()
    context.signin_page = Sign_in_page()

def after_all(context):
    context.browser.close()

    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # before all = BDD
    # after all = BDD
    # de fiecare data cand adaugam o pagina noua in proiect o vom adauga in context/un obiect de tipul paginii noi