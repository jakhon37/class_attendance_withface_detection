############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import image_names, ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time


# from attend import assure_path_exists, check_haarcascadefile
import face_recognition
import cv2
import numpy as np
from send_mail import main_mail


############################################# FUNCTIONS ################################################


def assure_path_exists(path):
    dir = os.path.exists(path)
    print(dir)
    if not os.path.exists(dir):
        print('creating ', dir)
        os.makedirs(dir)

# dd


def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

###################################################################################


def contact():
    mess._show(title='Contact us',
               message="Please contact us on : 'mushtariy9800@gmail.com' ")

###################################################################################


def check_haarcascadefile():
    exists = os.path.isfile("utils/haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing',
                   message='Please contact us for help')
        window.destroy()

###################################################################################


def save_pass():
    assure_path_exists("TrainingImageLabel")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found',
                                'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered',
                       message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered',
                       message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel/psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password',
                   message='Please enter correct old password.')
        return
    mess._show(title='Password Changed',
               message='Password changed successfully!!')
    master.destroy()

###################################################################################


def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password',
                    bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid',
                   font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password',
                    bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid',
                   font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password',
                    bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',
                    font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red",
                       height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48",
                      height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################


def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found',
                                'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered',
                       message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered',
                       message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password',
                   message='You have entered wrong password')

######################################################################################


def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear3():
    txt3.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)
#######################################################################################


def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '', 'E-MAIL']
    assure_path_exists("StudentDetails")
    assure_path_exists("TrainingImage")
    serial = 0
    exists = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists:
        with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
                print(l)
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    e_mail = (txt3.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "utils/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            # im_g = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # im_g = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            faces = detector.detectMultiScale(img, 1.3, 5)
            for (x, y, w, h) in faces:
                scale = 1.5
                img_name = name.split(" ")[-1]
                # w, h = w * scale, h * scale
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                if sampleNum == 10:
                    cv2.imwrite(f"faces/{img_name}.jpg",
                                img[y:y + int(h*scale), x:x + int(w*scale)])
                # display the frame
                    cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 10:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name, '', e_mail]
        serial = serial + 1

        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)


######################################## USED STUFFS ############################################
# from attend import assure_path_exists, check_haarcascadefile


def TrackImages():
    # pip install opencv-python
    # pip install face_recognition

    # ----------------------------
    #  attendance info register

    # check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    # ----------------------------

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    path = "faces"

    # ----------------------------
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails/StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails/StudentDetails.csv",
                         on_bad_lines='skip')
    else:
        mess._show(title='Details Missing',
                   message='Students details are missing, please check!')
        video_capture.release()
        cv2.destroyAllWindows()
        window.destroy()
    # ----------------------------

    # REGISTER FACCES

    face_list = []
    known_face_encodings = []
    known_face_names = []
    for i in df["NAME"]:
        # print(i)
        if str(i) == "nan":
            print('no value ')
            continue
        else:
            face_list.append(i)
            try:
                f_image = face_recognition.load_image_file(
                    f"{path}/{str(i).split(' ')[-1]}.jpg")
                img_face_encoding = face_recognition.face_encodings(f_image)[0]
                known_face_encodings.append(img_face_encoding)
                known_face_names.append(i)
            except:
                print("No image available for given student info")
                pass

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    detected_names = []
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding, tolerance=0.35)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

    # ----------------------------

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            timeStamp = datetime.datetime.fromtimestamp(
                ts).strftime('%H:%M:%S')

            aa = df.loc[df['NAME'] == name]['SERIAL NO.'].values
            ID = df.loc[df['NAME'] == name]['ID'].values
            student_mail = df.loc[df['NAME'] == name]['E-MAIL'].values
            ID = str(ID).split(".")[0]
            ID = ID[1:-1]
            attendance = [str(ID), '', name, '', str(date),
                          '', str(timeStamp)]

    # ----------------------------

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)
            # print('name detected ', name)
        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # ----------------------------
        exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")
        # exists1 = os.path.isfile("Attendance/Attendance_17-10-2022.csv")
        if exists:
            dff = pd.read_csv("Attendance/Attendance_" +
                              date + ".csv", on_bad_lines='skip')
        # elif name == "Unknown":
        #     continue
        else:

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                # writer.writerow(attendance)
            csvFile1.close()

        try:

            name_list = []
            for i in dff["Name"]:
                name_list.append(i)
            if name in name_list:
                continue
            elif name == "Unknown":
                continue
            else:
                detected_names.append(name)
                yes = 0
               # print(detected_names)
                try:
                    if name == detected_names[-5]:
                        for idx, i in enumerate(detected_names):
                            if i != detected_names[idx-1]:
                                detected_names.clear()
                            if i == name:
                                yes += 1
                except:
                    pass

                if yes == 15:
                    detected_names.clear()
                    # ------------------------------------------------------------------------
                    print('name  ', yes, name)
                    atn_info = f' Student ID: {attendance[0]}\n Name: {attendance[2]}\n Date: {attendance[4]}\n Time: {attendance[6]}'
                    m_mail, m_password, mail_to_send, attn_info = 'dil1977@gachon.ac.kr', 'gulim1997!', student_mail, atn_info
                    main_mail(m_mail, m_password, mail_to_send, attn_info)
                    print('email sending is done...')
                    # ------------------------------------------------------------------------

                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(
                        ts).strftime('%d-%m-%Y')
                    exists = os.path.isfile(
                        "Attendance/Attendance_" + date + ".csv")
                    if exists:
                        with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                            writer = csv.writer(csvFile1)
                            writer.writerow(attendance)
                        csvFile1.close()
                    # else:
                    #     with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                    #         writer = csv.writer(csvFile1)
                    #         writer.writerow(col_names)
                    #         writer.writerow(attendance)
                    #     csvFile1.close()
                    with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
                        reader1 = csv.reader(csvFile1)
                        for lines in reader1:
                            i = i + 1
                            if (i > 1):
                                if (i % 2 != 0):
                                    iidd = str(lines[0]) + '   '
                                    tv.insert('', 0, text=iidd, values=(
                                        str(lines[2]), str(lines[4]), str(lines[6])))
        except:
            continue
     # ----------------------------

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


######################################## USED STUFFS ############################################


global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Attendance Management System (itsourcecode.com)")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance Management System",
                    fg="white", bg="#262523", width=55, height=1, font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text=day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",
                 bg="#262523", width=55, height=1, font=('times', 22, ' bold '))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="orange", bg="#262523", width=55,
                 height=1, font=('times', 22, ' bold '))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ",
                 fg="black", bg="#03F2FD", font=('times', 17, ' bold '))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ",
                 fg="black", bg="#03F2FD", font=('times', 17, ' bold '))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter ID", width=20, height=1,
               fg="black", bg="#00aeff", font=('times', 17, ' bold '))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt.place(x=30, y=88)  # 88

lbl2 = tk.Label(frame2, text="Enter Name", width=20, fg="black",
                bg="#00aeff", font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt2.place(x=30, y=173)

lbl2_2 = tk.Label(frame2, text="Enter e-mail", width=20, fg="black",
                  bg="#00aeff", font=('times', 17, ' bold '))
lbl2_2.place(x=80, y=220)

txt3 = tk.Entry(frame2, width=32, fg="black", font=('times', 15, ' bold '))
txt3.place(x=30, y=253)

message1 = tk.Label(frame2, text="1)Take Image  >>>  2)Save Profile", bg="#00aeff",
                    fg="black", width=39, height=1, activebackground="yellow", font=('times', 15, ' bold '))
message1.place(x=7, y=360)

message = tk.Label(frame2, text="", bg="#00aeff", fg="black", width=39,
                   height=1, activebackground="yellow", font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="black",
                bg="#00aeff", height=1, font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res = 0
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
if exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Change Password', command=change_pass)
filemenu.add_command(label='Contact Us', command=contact)
filemenu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=82)
tv.column('name', width=130)
tv.column('date', width=133)
tv.column('time', width=133)
tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')


###################### SCROLLBAR ################################

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear, fg="black",
                        bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)

clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="black",
                         bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)

clearButton3 = tk.Button(frame2, text="Clear", command=clear3, fg="black",
                         bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold '))
clearButton3.place(x=335, y=255)

takeImg = tk.Button(frame2, text="Take Image", command=TakeImages, fg="black", bg="#F5FD03",
                    width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
takeImg.place(x=30, y=320)
trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="black", bg="#F5FD03",
                     width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
trainImg.place(x=30, y=400)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="black",
                     bg="#1AFD03", width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
trackImg.place(x=30, y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="black", bg="red",
                       width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
