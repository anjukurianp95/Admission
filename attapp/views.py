from django.shortcuts import render
from attapp.models import sign,faculty,student,admin,mark,fleave,sleave,stud_att,timetable
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def display(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
    a=sign(name=name,email=email,mobile=mobile,password=password)
    a.save()

def signupfac(request):
    if request.method=="POST":
        facid=request.POST.get('facid')
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        batchincharge=request.POST.get('batchincharge')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
    a=faculty(facid=facid,name=name,address=address,dob=dob,gender=gender,qualification=qualification,mobile=mobile,batchincharge=batchincharge,email=email,password=password)
    a.save()
    return render(request,'faculty_signup.html')

def signupstudent(request):
    if request.method=="POST":
        stid=request.POST.get('stid')
        name=request.POST.get('name')
        admissionno=request.POST.get('admissionno')
        admissiondate=request.POST.get('admissiondate')            
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        guardian=request.POST.get('guardian')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        b=student(stid=stid,name=name,admissionno=admissionno,admissiondate=admissiondate,address=address,dob=dob,gender=gender,guardian=guardian,batch=batch,mobile=mobile,email=email,password=password)
        b.save()
    return render(request,'student_signup.html')
def addmarks(request):
    if request.method=="POST":
        stid=request.POST.get('stid')
        assno=request.POST.get('assno')
        sub1=request.POST.get('sub1')
        sub2=request.POST.get('sub2')
        sub3=request.POST.get('sub3')
        per=request.POST.get('percentage')
        d=mark(stid_id=stid,assno=assno,sub1=sub1,sub2=sub2,sub3=sub3,percentage=per)
        d.save()
    return render(request,'view_stud_marks.html')

def addattendance(request):
    if request.method=="POST":
        stid=request.POST.get('stid')
        date=request.POST.get('date')
        h1=request.POST.get('h1')
        h2=request.POST.get('h2')
        h4=request.POST.get('h4')
        h3=request.POST.get('h3')
        d=stud_att(stid=stid,date=date,status_h1=h1,status_h2=h2,status_h3=h3,status_h4=h4)
        d.save()
    return redirect('view_stud_attendance')

'''def addattn(request):
    if request.method=="POST":
        date=request.POST.get('date')
        hour=request.POST.get('hour')
        
        aid=[]
        aid=(request.POST.get('stid')).split(',')
        for i in aid:
            rid=stud_att.objects.filter(date=date,stid=i)
            if(rid.count()==1):
                if(hour==1):
                   # aid=[]
                    #aid=(request.POST.get('stid')).split(',')
                    
                    d=stud_att.objects.filter(stid=i).update(date=date,status_h1='absent')
                if(hour==2):
                  #  aid=[]
                   # aid=(request.POST.get('stid')).split(',')
                    #for i in aid:
                    d=stud_att.objects.filter(stid=i).update(date=date,status_h2='absent')
                if(hour==3):
                    #aid=[]
                    #aid=(request.POST.get('stid')).split(',')
                    #for i in aid:
                    d=stud_att.objects.filter(stid=i).update(date=date,status_h3='absent')
                if(hour==4):
                    #aid=[]
                    #aid=(request.POST.get('stid')).split(',')
                    #for i in aid:
                    d=stud_att.objects.filter(stid=i).update(date=date,status_h4='absent')
           # else:
                #if(hour==1):



    return redirect('view_stud_attendance')'''


def statbyfac(request):
    qqs=stud_att.objects.all().filter()
    return render(request,'view_stud_attendance.html',{'rs':qqs})

def viewmarkbyfac(request):
    qs=mark.objects.all().filter()
    return render(request,'view_stud_marks.html',{'r':qs})

def viewmarkbyadmin(request):
    qs=mark.objects.all().filter()
    return render(request,'stud_mark.html',{'r':qs})

def approvestud(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        sleave.objects.filter(sid=sid).update(status='Approved')
    return render(request,'viewleavestud.html')

def approvefac(request):
    if request.method=="POST":
        fid=request.POST.get('fsid')
        fleave.objects.filter(fsid=fid).update(status='Approved')
    return render(request,'viewleavefac.html')

def authenticate(request):  
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=admin.objects.filter(username=username)
        p=admin.objects.filter(password=password)
        c=0
        if u.count()==1 and p.count()==1:
            c+=1
        if c==1:
            return render(request,'adminhome.html')
        else:
            uf=faculty.objects.filter(name=username,password=password)
           # pf=faculty.objects.filter(password=password)
            c1=0
            if uf.count()==1:
                c1+=1
            if c1==1:
                request.session['user']=username
                q=faculty.objects.all().filter(name=username)[0]
                request.session['id']=q.facid
                #queryset1=faculty.objects.all().filter(name=username)
                return render(request,'faculty_home.html')
            else:
                us=student.objects.filter(name=username , password=password)
                #ps=student.objects.filter(password=password)
                c2=0
                if us.count()==1 :
                    c2+=1
                if c2==1:
                    request.session['user']=username
                    q=student.objects.all().filter(name=username)[0]
                    request.session['id']=q.stid
                    request.session['batch']=q.batch
                    return render(request,'student_home.html')
                else:
                    return HttpResponse('username or password incorrect')
def viewfac(request):
    queryset1=faculty.objects.all().filter(name=request.session['user'])
    return render(request,'fac_profile.html',{'authors1':queryset1})
def viewatt(request):
    queryset2=stud_att.objects.all().filter(batch='jsd2')
    return render(request,'jsd2attendance.html',{'author':queryset2})
def viewstud(request):
    queryset=student.objects.all().filter()
    return render(request,'stud_details.html',{'authors':queryset})
def facdet(request):
    queryset=faculty.objects.all().filter()
    return render(request,'fac_details.html',{'authors':queryset})
def view_stud(request):                                                                                                                                                                                                                                                         
    queryset=student.objects.all().filter()
    return render(request,'view_stud_details.html',{'authors':queryset})
def stuprof(request):
    queryset=student.objects.all().filter(name=request.session['user'])
    return render(request,'view_student_details.html',{'author':queryset})

def leaveapply(request):
    if request.method=="POST":
        fsid=request.POST.get('fsid')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        l=fleave(fsid=fsid,fromdate=fromdate,todate=todate,reason=reason,status=status)
        l.save()
    return render(request,'fac_applyleave.html')

def stuapplyleave(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        reason=request.POST.get('reason')
        status=request.POST.get('status')
        ls=sleave(sid=sid,fromdate=fromdate,todate=todate,reason=reason,status=status)
        ls.save()
    return render(request,'student_applyleave.html')
def viewleavef(request):
    queryset=fleave.objects.all().filter()
    print(queryset)
    return render(request,'viewleavefac.html',{'result':queryset})

def facultyviewleave(request):
    q=fleave.objects.all().filter(fsid=request.session['id'])
    return render(request,'fac_applyleave.html',{'r':q})

def stuviewleave(request):
    q=sleave.objects.all().filter(sid=request.session['id'])
    return render(request,'student_applyleave.html',{'r':q})
def viewleavest(request):
    qs=sleave.objects.all().filter()
    return render(request,'viewleavestud.html',{'r':qs})

def attbyadmin(request):
    qset=stud_att.objects.all().filter()
    return render(request,'stud_attendance.html',{'r':qset})

def mymark(request):
    qr=mark.objects.filter(stid_id=request.session['id'])
    return render(request,'view_student_marks.html',{'rs':qr})

def myattendance(request):
    qr=stud_att.objects.all().filter(stid=request.session['id'])
    return render(request,'view_student_attendance.html',{'rs':qr})

def timeadmin(request):
    qr=timetable.objects.all().filter()
    return render(request,'timetable.html',{'rs':qr})

def timefac(request):
    qr=timetable.objects.all().filter()
    return render(request,'timetable_fac.html',{'rs':qr})

def timestudent(request):
    qr=timetable.objects.all().filter(batch=request.session['batch'])
    return render(request,'timetablestudent.html',{'rs':qr})

def logout_view(request):
    logout(request)
    return redirect('login')

def save_fac(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        mobile=request.POST.get('mobile')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        faculty.objects.filter(facid=request.session['id']).update(name=name,address=address,gender=gender,qualification=qualification,batchincharge=batch,mobile=mobile,email=email,password=password)
    return redirect('fac_profile')

def edit_fac(request):
    q=faculty.objects.all().filter(facid=request.session['id'])
    return render(request,'save_facd.html',{'r':q})

def savestud(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('stid')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        adno=request.POST.get('adno')
        addate=request.POST.get('addate')
        guardian=request.POST.get('guardian')
        mobile=request.POST.get('mobile')
        batch=request.POST.get('batch')
        email=request.POST.get('email')
        password=request.POST.get('password')
        student.objects.filter(stid=request.session['id']).update(name=name,address=address,admissionno=adno,gender=gender,guardian=guardian,batch=batch,mobile=mobile,email=email,password=password)
    return redirect('view_student_details')

def edit_stud(request):
    qr=student.objects.all().filter(stid=request.session['id'])
    return render(request,'save_studd.html',{'r':qr})
