from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from testproject.models import Student
from forms import RegisterstForm

from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
import pickle
from .models import Student

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def home_page(request):
    # if request.method == "POST":
    #     gender = request.POST['gender']
    #     packages = request.POST['packages']
    #
    #     try:
    #         user = User.objects
    #         user.gender = gender
    #         user.packages = packages
    #         user.save()
    #
    #     except:
    #         return render(request, "index.html", {
    #             "message": "Please select from the provided options"
    #         })
    #     return HttpResponseRedirect(reverse("home_page"))
    # else:
    #     return render(request, "index.html")
    return render(request,"index.html")
########################################################



def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home_page"))

        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home_page'))
        else:
            return render(request, "login.html")
    #return render(request,"login.html")
###################################################

def register_page(request):
    if request.method == "POST":
        form = RegisterstForm(request.POST)
        # confirmation = request.POST["confirmation"]
        # if password != confirmation:
        #     return render(request, "reg.html", {
        #         "message": "Passwords must match."
        #     })

        # Attempt to create new user
        if form.is_valid():
            try:
                form.save()
                return redirect('/payment_page')

            except Exception as e:
                
                print(request.POST)
            
        else:
            
            print(f"Form is not valid. Errors: {form.errors}")
            
    
        #return render(request,"reg.html")
    
    return render(request, 'index.html', {'form': form})
    
def registrationnew(request):
    if request.method=="POST":
        
        form = StudentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/report')
            except:
                pass
        else:
            form = StudentForm()
           
    return render(request, 'registrationnew.html', {'form': form})

def payment_page(request):
    return render(request,"pay.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_page"))



class Ticket:
    pass


def packages(request):
    if request.user.is_authenticated:
        packs = Ticket.objects.filter(user=request.user)
        return render(request, 'packages.html', {
            'page': 'packages',
            'packs': packs
        })
    else:
        return HttpResponseRedirect(reverse('login'))
###################################################

def student_info_form(request):
    return render(request,"form_student_info.html" )

####################################################


##### use function called   get_student_info_from_form  #################################

###### Use form - method=get retrieve all form values and display them on the same page

# def get_student_info_from_form (request):
#     try:
#         student_info = ""
#         firstname = str(request.GET.get("first_name"))
#         if firstname != "":
#             student_info += " First Name:   " + firstname + "</br>"
#         else:
#             student_info += " First Name:   " + "Not Entered" + "</br>"

#         lastname = str(request.GET.get("last_name"))
#         if lastname != "":
#             student_info += " Last Name:   " + lastname + "</br>"
#         else:
#             student_info += " Last Name:   " + "Not Entered" + "</br>"

#         program_enrolled = str(request.GET.get("program"))
#         if program_enrolled != "":
#             student_info += " Program Enrolled:   " + program_enrolled + "</br>"
#         else:
#             student_info += " Program Enrolled:   " + "Not Enrolled Yet!" + "</br>"

#         student_number = str(request.GET.get("student_number"))
#         if student_number != "":
#             student_info += " Student Number entered:   " + student_number + "</br>"
#         else:
#             student_info += " Student Number entered:   " + "Not Entered Yet!" + "</br>"

#         my_enrollment_status = str(request.GET.get("my_status"))

#         if my_enrollment_status != "":
#             student_info += " Enrollment status: " + my_enrollment_status + "</br>"
#         else:
#             student_info += " My Enrollment status is NOT selected!  </br>"

#         year_enrolled = ""
#         first_year = str(request.GET.get("year1"))
#         second_year = str(request.GET.get("year2"))
#         third_year = str(request.GET.get("year3"))
#         fourth_year = str(request.GET.get("year4"))
#         if first_year == "" and second_year == "" and third_year == "" and fourth_year == "":
#             year_enrolled += " Not currently enrolled in the program yet! </br>"
#         if first_year == "year1":
#             year_enrolled += " Enrolled in First Year courses </br>"
#         if second_year == "year2":
#             year_enrolled += " Enrolled in Second Year courses  </br>"
#         if third_year == "year3":
#             year_enrolled += " Enrolled in Third Year courses  </br>"
#         if fourth_year == "year4":
#             year_enrolled += " Enrolled in Fourth Year courses  </br>"

#         student_info += "</br></br>"
#         student_info += year_enrolled

#         student_data_display = {}
#         student_data_display['output_info'] = student_info
#         print(student_data_display)

#     except:
#         pass

#     return HttpResponse(student_info)
# ###############################################################################################


# ##############################################################################################

# ######################## Get method to save information in file #########################

# #############################And Also display Information from the file as well ############

# ######################################################################################

# ####################### file_save_student_info.html  ####################################

# def save_student_info(request):
#     return render(request, "file_save_student_info.html")


# #######################################################################################
# def process_data_file(request):
#     try:
#         if request.method == "GET":
#             if request.GET.get('save_data') == "save":
#                 student_data = {}
#                 student_data['first_name'] = request.GET.get('first_name')
#                 student_data['last_name'] = request.GET.get('last_name')
#                 student_data['student_number'] = request.GET.get('student_number')
#                 student_data['program'] = request.GET.get('program')
#                 student_data['my_status'] = request.GET.get('my_status')

#                 year_enrolled = ""
#                 first_year = str(request.GET.get("year1"))
#                 second_year = str(request.GET.get("year2"))
#                 third_year = str(request.GET.get("year3"))
#                 fourth_year = str(request.GET.get("year4"))
#                 if first_year == "" and second_year == "" and third_year == "" and fourth_year == "":
#                     year_enrolled += " Not currently enrolled in the program yet! </br>"
#                 year_enrolled += first_year + ';'
#                 year_enrolled += second_year + ';'
#                 year_enrolled += third_year + ';'
#                 year_enrolled += fourth_year + ';'

#                 student_data['enrollment_year'] = year_enrolled
#                 file_name = "student.dat"
#                 try:
#                     data_file = open(file_name, "ab")
#                     pickle.dump(student_data, data_file)
#                     data_file.close()
#                 except:
#                     print("Error opening file....")

#                 return render(request, "file_save_student_info.html")

#             elif request.GET.get('save_data') == 'display':
#                 display_table = "<body bgcolor='aqua'>"
#                 display_table += "<h2 align='right'> Muhammad Khan </h2>"
#                 display_table += "<h2 align='right' > Student Number: N012345 </h2>"
#                 display_table += """
#                                     <table>
#                                     <tr>
#                                     <th> First Name </th>
#                                     <th> Last Name </th>
#                                     <th> Student Number </th>
#                                     <th> Program Enrolled </th>
#                                     <th> Enrollment status </th>
#                                     <th> Courses from Years </th>

#                                     </tr>

#                 """
#                 file_name = "student.dat"
#                 try:
#                     data_file = open(file_name, "rb")
#                     data_from_file = {}
#                     while True:
#                         try:
#                             data_from_file = pickle.load(data_file)
#                             firstname = data_from_file['first_name']
#                             lastname = data_from_file['last_name']
#                             studentnumber = data_from_file['student_number']
#                             program_enrolled_in = data_from_file['program']
#                             my_enrollment_status = data_from_file['my_status']
#                             enrolled_years = data_from_file['enrollment_year']

#                             display_table += """
#                                                 <tr>
#                                                 <td align='center'> %s </td>
#                                                 <td align='center'> %s </td>
#                                                 <td align='center'> %s </td>
#                                                 <td align='center'> %s </td>
#                                                 <td align='center'> %s </td>
#                                                 <td align='center'> %s </td>
#                                                 </tr>

#                             """ % (firstname, lastname, studentnumber, program_enrolled_in, my_enrollment_status,
#                                    enrolled_years)
#                         except:
#                             data_file.close()
#                             display_table += "</table> </body>"
#                             break

#                 except:
#                     print("Error opening file to read .. File may not exist")

#     except:
#         pass

#     return HttpResponse(display_table)

# ########################################################################################################

# #####################################################################################################

# ##################################################################################################

# ############################ POST PROCESSING FORMS ##########################################


# ########################################################################################################

# ###################### POST method processing ###########################

# #######################################################################################################

# ######## display student information form --- POST

# def get_student_info_post_form(request):
#     return render(request, "form_student_info_post.html")



# #################################################################################

# def get_student_info_from_post_form(request):
#     if request.method == 'POST':
#         try:
#             student_info = ""
#             firstname = str(request.POST.get("first_name"))
#             if firstname != "":
#                 student_info += " First Name:   " + firstname + "</br>"
#             else:
#                 student_info += " First Name:   " + "Not Entered" + "</br>"

#             lastname = str(request.POST.get("last_name"))
#             if lastname != "":
#                 student_info += " Last Name:   " + lastname + "</br>"
#             else:
#                 student_info += " Last Name:   " + "Not Entered" + "</br>"

#             program_enrolled = str(request.POST.get("program"))
#             if program_enrolled != "":
#                 student_info += " Program Enrolled:   " + program_enrolled + "</br>"
#             else:
#                 student_info += " Program Enrolled:   " + "Not Enrolled Yet!" + "</br>"

#             student_number = str(request.POST.get("student_number"))
#             if student_number != "":
#                 student_info += " Student Number entered:   " + student_number + "</br>"
#             else:
#                 student_info += " Student Number entered:   " + "Not Entered Yet!" + "</br>"

#             my_enrollment_status = str(request.POST.get("my_status"))

#             if my_enrollment_status != "":
#                 student_info += " Enrollment status: " + my_enrollment_status + "</br>"
#             else:
#                 student_info += " My Enrollment status is NOT selected!  </br>"

#             year_enrolled = ""
#             first_year = str(request.POST.get("year1"))
#             second_year = str(request.POST.get("year2"))
#             third_year = str(request.POST.get("year3"))
#             fourth_year = str(request.POST.get("year4"))
#             if first_year == "" and second_year == "" and third_year == "" and fourth_year == "":
#                 year_enrolled += " Not currently enrolled in the program yet! </br>"
#             if first_year == "year1":
#                 year_enrolled += " Enrolled in First Year courses </br>"
#             if second_year == "year2":
#                 year_enrolled += " Enrolled in Second Year courses  </br>"
#             if third_year == "year3":
#                 year_enrolled += " Enrolled in Third Year courses  </br>"
#             if fourth_year == "year4":
#                 year_enrolled += " Enrolled in Fourth Year courses  </br>"

#             student_info += "</br></br>"
#             student_info += year_enrolled

#             student_data_display = {}
#             student_data_display['output_info'] = student_info
#             print(student_data_display)

#         except:
#             pass

#     return HttpResponse(student_info)


###################################################################################################

##############################################################################################

################################################################################################

