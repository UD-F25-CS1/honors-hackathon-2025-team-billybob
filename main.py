from bakery import assert_equal
from drafter import *
from dataclasses import dataclass
#hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


set_website_framed(False)
set_website_title("Free Time Calculator")
#"TabithaZ@udel.edu and nkapadia@udel.edu",
   
hide_debug_information()
set_website_style("none")

add_website_css('''
body{
    background-color:lightblue;
    font-size:25px;
    }
    ''')
@dataclass
class Class_info:
    Class_nam1: str 
    Class_len1: int
    Class_nam2: str 
    Class_len2: int 
    Class_nam3: str 
    Class_len3: int 
    Class_nam4: str 
    Class_len4: int 
    Class_nam5: str 
    Class_len5: int 
    Class_nam6: str 
    Class_len6: int 
    Class_nam7: str 
    Class_len7: int 
    Class_nam8: str 
    Class_len8: int 

@dataclass
class Sleep_info:
    Sleep_night: int 
    Sleep_day: int 

@dataclass
class Transit_info:
    Transport_len: int 
    
@dataclass
class Cleaning_info:
    Showering_time: int
    Brushing_time: int 
    Dressing_time: int 
    
@dataclass
class Additional_info:
    Task_nam1: str 
    Task_len1: int 
    Task_nam2: str 
    Task_len2: int 
    Task_nam3: str 
    Task_len3: int 
    Task_nam4: str 
    Task_len4: int 
    Task_nam5: str 
    Task_len5: int 
    Task_nam6: str 
    Task_len6: int 
    Task_nam7: str 
    Task_len7: int 
    Task_nam8: str 
    Task_len8: int 
    
@dataclass
class State:
    time_remaining: int 
    classes: Class_info 
    class_total: int 
    sleeps: Sleep_info 
    sleep_total: int 
    transits: Transit_info 
    transit_total: int 
    cleanings: Cleaning_info 
    cleanings_total: int 
    additionals: Additional_info 
    additional_total: int 

def minutes_to_hours(minutes: int) -> str:
    hours = minutes // 60
    leftover = minutes % 60
    return str(hours) + " hours and " + str(leftover) + " minutes"

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("Welcome to the Free Time Calculator!"),
        Row("Input your daily obligations"),
        Row("Please put in your information in before hitting 'Calculate Free Time'"),
        Button("Classes", "Class_time"),
        Button("Sleep", "Sleep_time"),
        Button("Transportation", "Transit_time"),
        Button("Hygiene/Getting Ready", "Clean_time"),
        Button("Additional", "Additional_time"),
        Button("Calculate Free Time", "Calced_Free_Time")
        ])

@route
def Class_time(state:State) -> Page:
    return Page(state, [
    Text("Input how long each class is"),
    Row("Class 1:", TextBox("Class1_nam", ""),  "Length(minutes)", TextBox("Class1_len", "0")),
    Row("Class 2:", TextBox("Class2_nam", ""), "Length(minutes)", TextBox("Class2_len", "0")),
    Row("Class 3:", TextBox("Class3_nam", ""),  "Length(minutes)", TextBox("Class3_len", "0")),
    Row("Class 4:", TextBox("Class4_nam", ""),   "Length(minutes)", TextBox("Class4_len", "0")),
    Row("Class 5:", TextBox("Class5_nam", ""),   "Length(minutes)", TextBox("Class5_len", "0")),
    Row("Class 6:", TextBox("Class6_nam", ""),   "Length(minutes)", TextBox("Class6_len", "0")),
    Row("Class 7:", TextBox("Class7_nam", ""),   "Length(minutes)", TextBox("Class7_len", "0")),
    Row("Class 8:", TextBox("Class8_nam", ""),   "Length(minutes)", TextBox("Class8_len", "0")),
    Button("Calculate_total", "Calced_class")
    ])

@route
def Calced_class(state:State, Class1_len: str, Class2_len: str, Class3_len: str, Class4_len: str, Class5_len: str, Class6_len: str, Class7_len: str, Class8_len: str, Class1_nam: str, Class2_nam: str, Class3_nam: str, Class4_nam: str, Class5_nam: str, Class6_nam: str, Class7_nam: str, Class8_nam: str):
    state.classes.Class_nam1 = Class1_nam
    state.classes.Class_len1 = int(Class1_len)
    state.classes.Class_nam2 = Class2_nam
    state.classes.Class_len2 = int(Class2_len)
    state.classes.Class_nam3 = Class3_nam
    state.classes.Class_len3 = int(Class3_len)
    state.classes.Class_nam4 = Class4_nam
    state.classes.Class_len4 = int(Class4_len)
    state.classes.Class_nam5 = Class5_nam
    state.classes.Class_len5 = int(Class5_len)
    state.classes.Class_nam6 = Class6_nam
    state.classes.Class_len6 = int(Class6_len)
    state.classes.Class_nam7 = Class7_nam
    state.classes.Class_len7 = int(Class7_len)
    state.classes.Class_nam8 = Class8_nam
    state.classes.Class_len8 = int(Class8_len)
    class_time_sum = int(Class1_len) + int(Class2_len) + int(Class3_len) + int(Class4_len) + int(Class5_len) + int(Class6_len) + int(Class7_len) + int(Class8_len) 
    state.class_total = class_time_sum
    return index(state)
    
    
                   
@route
def Sleep_time(state: State) -> Page:
    return Page(state, [
        "Input how long you intend to sleep:",
        Row("Sleeping at night:", TextBox("NightSleep", "0")),
        Row("Napping:", TextBox("NapSleep", "0")),
        Button("Calculate Sleep", "Calced_sleep"),
        ])
@route
def Calced_sleep(state:State, NightSleep:str, NapSleep:str)-> Page:
    sleep_time_sum = int(NightSleep)+int(NapSleep)
    state.sleeps.Sleep_night = int(NightSleep)
    state.sleeps.Sleep_day = int(NapSleep)
    state.sleep_total = sleep_time_sum
    return index(state)

@route
def Transit_time(state: State) -> Page:
    return Page(state, [
        "Input an estimate as to the amount of time you spend getting around",
        TextBox("Transit", "0"),
        Button("Submit Time", "Calced_transit"),
        ])

@route
def Calced_transit(state: State, Transit: str) -> Page:
    state.transits.Transport_len = int(Transit)
    state.transit_total = int(Transit)
    return index(state)
    

@route
def Clean_time(state: State) -> Page:
    return Page(state, [
        "Input how long you take to complete the fields below:",
        Row("Showering", TextBox("Shower_Time", "0")),
        Row("Brushing Teeth", TextBox("Brushing_Time", "0")),
        Row("Getting Dressed", TextBox("Dressing_Time", "0")),
        Button("Calculate cleaning", "Calced_cleaning"),
        ])
@route
def Calced_cleaning(state:State, Shower_Time:str, Brushing_Time:str, Dressing_Time:str):
    state.cleanings.Showering_time = Shower_Time
    state.cleanings.Brushing_time = Brushing_Time
    state.cleanings.Dressing_time = Dressing_Time
    state.cleanings_total = int(Shower_Time) + int(Brushing_Time) + int(Dressing_Time)
    return index(state)
    

@route
def Additional_time(state: State) -> Page:
    return Page(state, [Text("Input each additional yask for today and an estimate o how long it wil take"),
    Row("Task 1:", TextBox("Task1_nam", ""),  "Length(minutes)", TextBox("Task1_len", "0")),
    Row("Task 2:", TextBox("Task2_nam", ""), "Length(minutes)", TextBox("Task2_len", "0")),
    Row("Task 3:", TextBox("Task3_nam", ""),  "Length(minutes)", TextBox("Task3_len", "0")),
    Row("Task 4:", TextBox("Task4_nam", ""),   "Length(minutes)", TextBox("Task4_len", "0")),
    Row("Task 5:", TextBox("Task5_nam", ""),   "Length(minutes)", TextBox("Task5_len", "0")),
    Row("Task 6:", TextBox("Task6_nam", ""),   "Length(minutes)", TextBox("Task6_len", "0")),
    Row("Task 7:", TextBox("Task7_nam", ""),   "Length(minutes)", TextBox("Task7_len", "0")),
    Row("Task 8:", TextBox("Task8_nam", ""),   "Length(minutes)", TextBox("Task8_len", "0")),
    Button("Calculate Additional", "Calced_additional")
    ])

@route
def Calced_additional(state:State, Task1_len: str, Task2_len: str, Task3_len: str, Task4_len: str, Task5_len: str, Task6_len: str, Task7_len: str, Task8_len: str, Task1_nam: str, Task2_nam: str, Task3_nam: str, Task4_nam: str, Task5_nam: str, Task6_nam: str, Task7_nam: str, Task8_nam: str) -> Page:
    state.additionals.Task_len1 = Task1_len
    state.additionals.Task_nam1 = Task1_nam
    state.additionals.Task_nam2 = Task2_nam
    state.additionals.Task_len2 = Task2_len
    state.additionals.Task_nam3 = Task3_nam
    state.additionals.Task_len3 = Task3_len
    state.additionals.Task_nam4 = Task4_nam
    state.additionals.Task_len4 = Task4_len
    state.additionals.Task_nam5 = Task5_nam
    state.additionals.Task_len5 = Task5_len
    state.additionals.Task_nam6 = Task6_nam
    state.additionals.Task_len6 = Task6_len
    state.additionals.Task_nam7 = Task7_nam
    state.additionals.Task_len7 = Task7_len
    state.additionals.Task_nam8 = Task8_nam
    state.additionals.Task_len8 = Task8_len
    additional_time_sum = int(Task1_len) + int(Task2_len) + int(Task3_len) + int(Task4_len) + int(Task5_len) + int(Task6_len) + int(Task7_len) + int(Task8_len) 
    state.additional_total = additional_time_sum
    return index(state)

@route
def Calced_Free_Time(state:State) -> Page:
    Total_time = int(state.class_total) + int(state.sleep_total) +int(state.transit_total) + int(state.cleanings_total) + int(state.additional_total)
    Total_free_time = 1440-Total_time
    Free_time_hours = minutes_to_hours(Total_free_time)
    return Page(state, [
        Header("Here are your results!"),
        Row("You have " + str(Free_time_hours) + " free time on this day"),
        Button("Reset", "Reset"), Button("Home", "index")
        ])
@route
def Reset(state:State):
    state.classes.Class_nam1 = ''
    state.classes.Class_len1 = 0
    state.classes.Class_nam2 = ''
    state.classes.Class_len2 = 0
    state.classes.Class_nam3 = ''
    state.classes.Class_len3 = 0
    state.classes.Class_nam4 = ''
    state.classes.Class_len4 = 0
    state.classes.Class_nam5 = ''
    state.classes.Class_len5 = 0
    state.classes.Class_nam6 = ''
    state.classes.Class_len6 = 0
    state.classes.Class_nam7 = ''
    state.classes.Class_len7 = 0
    state.classes.Class_nam8 = ''
    state.classes.Class_len8 = 0
    state.class_total = 0
    state.sleeps.Sleep_night = 0
    state.sleeps.Sleep_day = 0
    state.sleep_total = 0
    state.transits.Transport_len = 0
    state.transit_total = 0
    state.cleanings.Showering_time = 0
    state.cleanings.Brushing_time = 0
    state.cleanings.Dressing_time = 0
    state.cleanings_total = 0
    state.additionals.Task_nam1 = ''
    state.additionals.Task_len1 = 0
    state.additionals.Task_nam2 = ''
    state.additionals.Task_len2 = 0
    state.additionals.Task_nam3 = ''
    state.additionals.Task_len3 = 0
    state.additionals.Task_nam4 = ''
    state.additionals.Task_len4 = 0
    state.additionals.Task_nam5 = ''
    state.additionals.Task_len5 = 0
    state.additionals.Task_nam6 = ''
    state.additionals.Task_len6 = 0
    state.additionals.Task_nam7 = ''
    state.additionals.Task_len7 = 0
    state.additionals.Task_nam8 = ''
    state.additionals.Task_len8 = 0
    state.additional_total = 0
    return index(state)
    
start_server(State(0, Class_info(), 0,Sleep_info(),0,Transit_info(),0,Cleaning_info(),0,Additional_info(),0))
