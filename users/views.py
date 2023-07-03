import dotenv
dotenv.load_dotenv()
import os
API_KEY = os.environ.get('API_KEY')
token=os.environ.get('token')
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from users.models import data_collected
import time 
import datetime
from django.utils.timezone import make_aware
import requests
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
@csrf_exempt
def home(request):
  

    
        
    if request.user is not None :
            obj11=datetime.datetime.now()
            time_stamp=str(make_aware(obj11).hour)+"H"+str(make_aware(obj11).minute)+"M"
            date_stamp=str(make_aware(obj11).day)+"D"+str(make_aware(obj11).month)+"M"+str(make_aware(obj11).year)+"Y"
            print("asdasdasdasdsadasdsa",date_stamp)
            uid=str(request.user)+"UID"+time_stamp+"DD"+date_stamp
            
            total_start=time.time()
            #username start--------------------
            user_start=time.time()
            print("User: ", request.user)
            username=request.user
            # uid=username+"UID"+current_time

            # print("uidasdasdasdasdasd",uid)
            user_end=time.time()
            totaltime_user=user_end-user_start
    #username end-------------------------------------
            #lang----------------start-----------
            lang_start=time.time()
            lang=request.META['HTTP_ACCEPT_LANGUAGE']
            # print(lang)
            lang_end=time.time()
            lang_totaltime=lang_end-lang_start
             #-------------lang end---------------
             #getting date and time ----------------------
            naive_datetime = datetime.datetime.now()
            naive_datetime.tzinfo  # None

            # settings.TIME_ZONE  # 'UTC'
            aware_datetime = make_aware(naive_datetime)
            aware_datetime.tzinfo  # <UTC>

            print("the real ip of the user",request.client_ip)
            
            start_timezone = time.time()

            local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
            # print("Timezone of the user is --> ",local_timezone)
            # printing date and time 
            # print("Date Time: ",aware_datetime)
            # print('date time -----',naive_datetime.date())
            # print('date time -----',naive_datetime.time())
            time_collected=naive_datetime.time()   #time collected 
            end_timezone = time.time()
            final_timezone=end_timezone-start_timezone
            print(final_timezone)

            #timezone done------------------------


             # getting ip-----------------------------------
            start_ip = time.time()

            
        


          

            ip1 = requests.get("https://api64.ipify.org/?format=json").json().get('ip')
            ip2 = requests.get("https://api-bdc.net/data/client-ip").json().get('ipString')
            ip3 = requests.get('https://ipapi.co/ip/').text.strip()

            ip_address = max(ip1, ip2, ip3) if ip1 == ip2 == ip3 else "All three values are different" if len({ip1, ip2, ip3}) == 3 else ip1
       
           
#             ip_address=print(request.META['REMOTE_ADDR'])

            print('the ip address-------',ip_address)
            end_ip = time.time()
            final_ip = print(end_ip-start_ip)
            #final ip=----------------



            #location start ----------------------
            # getting location from the ip 

            
          
            # response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            


            #browser start----------------------------

            ua_starttime = time.time()

            browser_ua = request.user_agent.browser
            system_ua = request.user_agent.os
            ua_endtime = time.time()
            ua_totaltime = ua_endtime - ua_starttime

            # print("ua----------- ",ua_totaltime)
            #browser end----------------------
            #screen size ---------------------------
          
            #screen size end ---------------------------



            #system fonts start ---------------------
              
            import os  #for windows
        
            # systemfonts_start=time.time()
            # from sys import platform
            # sys_fonts=[]
            # if platform == "win32":
            #     sys_font=os.listdir((r'C:\Windows\fonts'))
            #     sys_fonts=list(set(sys_font))
            #     # print("system fonts are ",sys_fonts)
            # elif platform =="macOS":
            #     import pycocoa #for mac
            #     manager = pycocoa.NSFontManager.sharedFontManager()
            #     font_families = list(manager.availableFontFamilies())
            #     print(font_families)
            
            # else:
            #     print("system fonts are not available")

            # systemfonts_final=time.time()
            # fonts_totaltime=systemfonts_final-systemfonts_start

            #system fonts end ---------------------

            
            #browser fonts,canvas,webgl,plugins
            # import json
            # browser_fonts_start=time.time()
            # f=open(r"C:\Users\Srikant Shubham\Downloads\data.json")
            # plugins_start=time.time()
            # g=open(r"C:\Users\Srikant Shubham\Downloads\plugins.json")
            # h=open(r"C:\Users\Srikant Shubham\Downloads\canvas.json")
            # i=open(r"C:\Users\Srikant Shubham\Downloads\webgl.json")


            # browser_fonts = json.load(f)
            # browser_fonts_end=time.time()
            # browser_totaltime=browser_fonts_end-browser_fonts_start
            # plugins=json.load(g)
            # plugins_end=time.time()
            # plugins_totaltime=plugins_end-plugins_start
            # canvas_data=json.load(h)
            # canvas=canvas_data["canvas"]
            # canvas_totaltime=canvas_data["total_time"]
        
            
            # webgl_data=json.load(i)
            # webgl=webgl_data["webgl"]
            # webgl_totaltime=webgl_data["webgl_totaltime"]
            # print(plugins)
            # f.close()
            # g.close()
            # h.close()
            # i.close()
            # print(canvas,webgl)
            # os.remove(r'C:\Users\Srikant Shubham\Downloads\data.json')
            # os.remove(r'C:\Users\Srikant Shubham\Downloads\plugins.json')
            # os.remove(r"C:\Users\Srikant Shubham\Downloads\canvas.json")
            # os.remove(r"C:\Users\Srikant Shubham\Downloads\webgl.json")
            # geo_loc_time=time.time()
            # latitude = request.POST.get('latitude')
            # longitude = request.POST.get('longitude')
            # # data=request.POST.get('data')
            # # data = json.loads(request.body.decode('utf-8'))
            # # data_final = data.get("data")
            # # print('Data received from client:', data_final)
            # data=print(request.body)
            webgl = ''
            canvas_hash = ''
            browser_version = ''
            user_agent = ''
            OS = ''
            screen_res_height = ''
            screen_res_width = ''
            # latitude=''
            if request.method == 'POST':
                latitude=None
                longitude=None
                data = json.loads(request.body.decode('utf-8'))
                # print(type(data),data)
                webgl = data['data']['webgl']
                webgl_total_time = data['data']['webgl_total_time']
                canvas_hash = data['data']['canvas_hash']
                canvas_total_time = data['data']['canvas_total_time']
                plugins = data['data']['plugins']
                plugins_totaltime = data['data']['plugins_totaltime']
                browser_fonts = data['data']['browser_fonts']
                browser_fonts_totaltime = data['data']['browser_fonts_totaltime']
                browser_version = data['data']['browser_version']
                browser_version_total_time = data['data']['browser_version_total_time']
                user_agent = data['data']['userAgent']
                useragent_total_time = data['data']['useragent_total_time']
                OS = data['data']['OS']
                os_plat_total_time = data['data']['os_plat_total_time']
                screen_res_height = data['data']['screen_res_height']
                screen_res_width = data['data']['screen_res_width']
                screen_res_total_time = data['data']['screen_res_total_time']
                device_type_final = data['data']['device_type_final']
                latitude=data['data']['latitude']['latitude']
                longitude=data['data']['latitude']['longitude']
                # timezone=data['data']['timezone_offset']
                
                print("device_type_final",device_type_final)
                print('webgl:', webgl)
                print('webgl_total_time:', webgl_total_time)
                print('canvas_hash:', canvas_hash)
                print('canvas_total_time:', canvas_total_time)
                print('plugins:', plugins)
                print('plugins_totaltime:', plugins_totaltime)
                print('browser_fonts:', browser_fonts)
                print('browser_fonts_totaltime:', browser_fonts_totaltime)
                print('browser_version:', browser_version)
                print('browser_version_total_time:', browser_version_total_time)
                print('user_agent:', user_agent)
                print('useragent_total_time:', useragent_total_time)
                print('OS:', OS)
                print('os_plat_total_time:', os_plat_total_time)
                print('screen_res_height:', screen_res_height)
                print('screen_res_width:', screen_res_width)
                print('screen_res_total_time:', screen_res_total_time)
                print('latitude:', latitude)
                print('longitude:', longitude)

            
                time_zone=None
                if latitude is not None and longitude is not None:
                    location_start=time.time()

                    print("collected from getCurrentLocation",latitude,longitude)
                    url = "https://api.geoapify.com/v1/geocode/reverse?lat={0}&lon={1}&format=json&apiKey={2}".format(latitude,longitude,API_KEY)
                    res=requests.get(url).json()
                    print(url)
                    # print("using geolocay->",res)
                    city=res['results'][0]['city']
                    # print(city)
                    country=res['results'][0]['country']
                    region=res['results'][0]['state']
                    location_final = str(res['results'][0]['country'])+str(res['results'][0]['state'])+str(res['results'][0]['city'])
                    time_zone = res.get('results', [{}])[0].get('timezone', {}).get('name')
                    lat_long=str(latitude)+":"+str(longitude)
                    location_end=time.time()
                    location_totaltime=location_end-location_start
                # locay=str(city+region+country+"from geoapify"
                if latitude is  None and longitude is  None:
                    url="https://ipinfo.io/{0}?token={1}".format(request.client_ip,token) 
                    # url="https://ipinfo.io/{0}?token={1}".format("34.82.78.16",token) 
                    print(url)
                    res=requests.get(url).json()
                    print(res)
                    city = res['city']
                    region = res['region']
                    country = res['country']
                    lat_long = res['loc']
                    location_final=str(res['country'])+str(res['region'])+str(res['city'])
                    time_zone = res['timezone']
                    location_totaltime=0 
                    # "ip": ip_address,
                    # city= response.get("city")
                    
                    
                    # country= response.get("country_name")
                    # print(data)
                   
                else:
                    location_totaltime=0    
                    #location end-------------------------
                
                total_end=time.time()
                overall_totaltime=total_end-total_start
                # csrf_token = csrf.get_token(request)
                    # print(request.META)
                browser_final=str(browser_ua.family)+str(browser_ua.version_string)
                OS=str(system_ua.family)+str(system_ua.version_string)
                    # print(ip_address)
                data=data_collected(Uid=uid,Os=OS,system_type=device_type_final,userid=username,latlong=lat_long,browser=browser_final,location=location_final,latitude=latitude,longitude=longitude,webgl=webgl,canvas=canvas_hash,screen_res_height=screen_res_height,screen_res_width=screen_res_width,plugins=plugins,ip=request.client_ip,language=lang,date=naive_datetime.date(),time_collected=time_collected,city=city,region=region,country=country,browser_name=browser_ua.family,time_zone=time_zone, browser_version =browser_ua.version_string,os_family=system_ua.family,os_version=system_ua.version_string,rtt=overall_totaltime)
                data.save()
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)