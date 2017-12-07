

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9451269
#    Student name: Oswald Doring
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser

from HTMLParser import *



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#


##### DEVELOP YOUR SOLUTION HERE #####


from sqlite3 import *

def iTunes_page():

    #Create a page to hold the iTunes list and change some of its properties

    first_window = Toplevel()

    first_window.title('Top 10 Songs!')

    first_window.configure(background = 'light grey')

    #Open, read the iTunes HTML code, then close the webpage

    iTunes_page = urlopen('http://www.apple.com/au/itunes/charts/songs/')

    iTunes_html_content = iTunes_page.read()

    iTunes_page.close()


    #Enter regex to find the songs in the webpage

    iTunes = findall('alt=(.+?)><\/a>', iTunes_html_content)


    #Display image from web on page


    iTunes_logo = image_to_PhotoImage(urlopen('http://www.gen-y-telugus.com/wp-content/uploads/2016/05/Top10-music.png').read())
    iTunes_label = Label(first_window, image = iTunes_logo)
    iTunes_label.pack()


    #Display the first 10 results from the regex
    
    Label1 = Label(first_window, text = '1.' + ' ' + iTunes[0], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'blue')
    Label1.pack()

    Label2 = Label(first_window, text = '2.' + ' ' + iTunes[1], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'dark blue')
    Label2.pack()

    Label3 = Label(first_window, text = '3.' + ' ' + iTunes[2], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'violet')
    Label3.pack()

    Label4 = Label(first_window, text = '4.' + ' ' + iTunes[3], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'blue')
    Label4.pack()

    Label5 = Label(first_window, text = '5.' + ' ' + iTunes[4], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'dark blue')
    Label5.pack()

    Label6 = Label(first_window, text = '6.' + ' ' + iTunes[5], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'violet')
    Label6.pack()

    Label7 = Label(first_window, text = '7.' + ' ' + iTunes[6], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'blue')
    Label7.pack()

    Label8 = Label(first_window, text = '8.' + ' ' + iTunes[7], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'dark blue')
    Label8.pack()

    Label9 = Label(first_window, text = '9.' + ' ' + iTunes[8], font = ("Comic Sans MS", 12),
                   bg = 'light grey', fg = 'violet')
    Label9.pack()

    Label10 = Label(first_window, text = '10.' + ' ' + iTunes[9], font = ("Comic Sans MS", 12),
                    bg = 'light grey', fg = 'blue')
    Label10.pack()

    def save_iTunes():

        connection = connect(database = 'top_ten.db')
        list_db = connection.cursor()

        command_delete = "DELETE FROM top_ten"

        list_db.execute(command_delete)

        iTunes_list1 = iTunes[0]
        iTunes_list2 = iTunes[1]
        iTunes_list3 = iTunes[2]
        iTunes_list4 = iTunes[3]
        iTunes_list4a = iTunes_list4.replace("'", "")   #For some reason I am unable to print apostrophies with my string into SQL, so I have had to remove them
        iTunes_list5 = iTunes[4]
        iTunes_list6 = iTunes[5]
        iTunes_list6a = iTunes_list6.replace ("'", "")   #For some reason I am unable to print apostrophies with my string into SQL, so I have had to remove them
        iTunes_list7 = iTunes[6]
        iTunes_list8 = iTunes[7]
        iTunes_list9 = iTunes[8]
        iTunes_list10 = iTunes[9]

        iTunes_one = "INSERT INTO top_ten VALUES (1, 'test1')"

        iTunes_entry_one = iTunes_one.replace('test1', iTunes_list1)

        iTunes_two = "INSERT INTO top_ten VALUES (2, 'test2')"

        iTunes_entry_two = iTunes_two.replace('test2', iTunes_list2)


        iTunes_three = "INSERT INTO top_ten VALUES (3, 'test3')"

        iTunes_entry_three = iTunes_three.replace('test3', iTunes_list3)


        iTunes_four = "INSERT INTO top_ten VALUES (4, 'test4')"

        iTunes_entry_four = iTunes_four.replace('test4', iTunes_list4a)


        iTunes_five = "INSERT INTO top_ten VALUES (5, 'test5')"

        iTunes_entry_five = iTunes_five.replace('test5', iTunes_list5)


        iTunes_six = "INSERT INTO top_ten VALUES (6, 'test6')"

        iTunes_entry_six = iTunes_six.replace('test6', iTunes_list6a)


        iTunes_seven = "INSERT INTO top_ten VALUES (7, 'test7')"

        iTunes_entry_seven = iTunes_seven.replace('test7', iTunes_list7)


        iTunes_eight = "INSERT INTO top_ten VALUES (8, 'test8')"

        iTunes_entry_eight = iTunes_eight.replace('test8', iTunes_list8)


        iTunes_nine = "INSERT INTO top_ten VALUES (9, 'test9')"

        iTunes_entry_nine = iTunes_nine.replace('test9', iTunes_list9)


        iTunes_ten = "INSERT INTO top_ten VALUES (10, 'test0')"

        iTunes_entry_ten = iTunes_ten.replace('test0', iTunes_list10)

        list_db.execute(iTunes_entry_one)
        list_db.execute(iTunes_entry_two)
        list_db.execute(iTunes_entry_three)
        list_db.execute(iTunes_entry_four)
        list_db.execute(iTunes_entry_five)
        list_db.execute(iTunes_entry_six)
        list_db.execute(iTunes_entry_seven)
        list_db.execute(iTunes_entry_eight)
        list_db.execute(iTunes_entry_nine)
        list_db.execute(iTunes_entry_ten)

        connection.commit()

        list_db.close()
        connection.close()

    Save_iTunes_button = Button(first_window, text = 'Save this list!', command = save_iTunes)

    Save_iTunes_button.pack()

    first_window.mainloop()


def IMDb_page():

    second_window = Toplevel()

    second_window.title('Top 10 Movies!')

    second_window.geometry('1100x709')

    second_window.configure(background = 'gold')

    IMDb_page = urlopen('http://www.imdb.com/chart/top')

    IMDb_html_content = IMDb_page.read()

    IMDb_page.close()

    IMDb = findall('title=.*>(.+)</a>', IMDb_html_content)

    IMDb_logo = image_to_PhotoImage(urlopen('http://4.bp.blogspot.com/-76yIbHJaOxk/TuDz0YQ-w6I/AAAAAAAAGfA/b8z9aPn2bF8/s1600/IMDB+Top+250.png%22,tid:%22OIP.M7837ddf7a26272ef4b394bc4bc6d6268o0').read())
    IMDb_label = Label(second_window, image = IMDb_logo)
    IMDb_label.pack()
    IMDb_label.place(x = 0, y = 0)

    Label1 = Label(second_window, text = '1.' + ' ' + IMDb[1], font = ("Courier 12 bold"), bg = 'gold')
    Label1.pack()
    Label1.place(x = 550, y = 50)

    Label2 = Label(second_window, text = '2.' + ' ' + IMDb[2], font = ("Courier 12 bold"), bg = 'gold')
    Label2.pack()
    Label2.place(x = 550, y = 110)

    Label3 = Label(second_window, text = '3.' + ' ' + IMDb[3], font = ("Courier 12 bold"), bg = 'gold')
    Label3.pack()
    Label3.place(x = 550, y = 170)

    Label4 = Label(second_window, text = '4.' + ' ' + IMDb[4], font = ("Courier 12 bold"), bg = 'gold')
    Label4.pack()
    Label4.place(x = 550, y = 230)

    Label5 = Label(second_window, text = '5.' + ' ' + IMDb[5], font = ("Courier 12 bold"), bg = 'gold')
    Label5.pack()
    Label5.place(x = 550, y = 290)

    Label6 = Label(second_window, text = '6.' + ' ' + IMDb[6], font = ("Courier 12 bold"), bg = 'gold')
    Label6.pack()
    Label6.place(x = 550, y = 350)

    Label7 = Label(second_window, text = '7.' + ' ' + IMDb[7], font = ("Courier 12 bold"), bg = 'gold')
    Label7.pack()
    Label7.place(x = 550, y = 420)

    Label8 = Label(second_window, text = '8.' + ' ' + IMDb[8], font = ("Courier 12 bold"), bg = 'gold')
    Label8.pack()
    Label8.place(x = 550, y = 490)

    Label9 = Label(second_window, text = '9.' + ' ' + IMDb[9], font = ("Courier 12 bold"), bg = 'gold')
    Label9.pack()
    Label9.place(x = 550, y = 550)

    Label10 = Label(second_window, text = '10.' + ' ' + IMDb[10], font = ("Courier 12 bold"), bg = 'gold')
    Label10.pack()
    Label10.place(x = 550, y = 610)


    def save_IMDb():

        connection = connect(database = 'top_ten.db')
        list_db = connection.cursor()

        command_delete = "DELETE FROM top_ten"

        list_db.execute(command_delete)

        IMDb_list1 = IMDb[1]
        IMDb_list2 = IMDb[2]
        IMDb_list3 = IMDb[3]
        IMDb_list4 = IMDb[4]
        IMDb_list5 = IMDb[5]
        IMDb_list5a = IMDb_list5.replace("'", "") #For some reason I am unable to print apostrophys with my string into SQL, so I have had to remove them
        IMDb_list6 = IMDb[6]
        IMDb_list7 = IMDb[7]
        IMDb_list8 = IMDb[8]
        IMDb_list9 = IMDb[9]
        IMDb_list10 = IMDb[10]

        IMDb_one = "INSERT INTO top_ten VALUES (1, 'test1')"

        IMDb_entry_one = IMDb_one.replace('test1', IMDb_list1)


        IMDb_two = "INSERT INTO top_ten VALUES (2, 'test2')"

        IMDb_entry_two = IMDb_two.replace('test2', IMDb_list2)


        IMDb_three = "INSERT INTO top_ten VALUES (3, 'test3')"

        IMDb_entry_three = IMDb_three.replace('test3', IMDb_list3)


        IMDb_four = "INSERT INTO top_ten VALUES (4, 'test4')"

        IMDb_entry_four = IMDb_four.replace('test4', IMDb_list4)


        IMDb_five = "INSERT INTO top_ten VALUES (5, 'test5')"

        IMDb_entry_five = IMDb_five.replace('test5', IMDb_list5a)


        IMDb_six = "INSERT INTO top_ten VALUES (6, 'test6')"

        IMDb_entry_six = IMDb_six.replace('test6', IMDb_list6)


        IMDb_seven = "INSERT INTO top_ten VALUES (7, 'test7')"

        IMDb_entry_seven = IMDb_seven.replace('test7', IMDb_list7)


        IMDb_eight = "INSERT INTO top_ten VALUES (8, 'test8')"

        IMDb_entry_eight = IMDb_eight.replace('test8', IMDb_list8)


        IMDb_nine = "INSERT INTO top_ten VALUES (9, 'test9')"

        IMDb_entry_nine = IMDb_nine.replace('test9', IMDb_list9)


        IMDb_ten = "INSERT INTO top_ten VALUES (10, 'test0')"

        IMDb_entry_ten = IMDb_ten.replace('test0', IMDb_list10)
        
        list_db.execute(IMDb_entry_one)
        list_db.execute(IMDb_entry_two)
        list_db.execute(IMDb_entry_three)
        list_db.execute(IMDb_entry_four)
        list_db.execute(IMDb_entry_five)
        list_db.execute(IMDb_entry_six)
        list_db.execute(IMDb_entry_seven)
        list_db.execute(IMDb_entry_eight)
        list_db.execute(IMDb_entry_nine)
        list_db.execute(IMDb_entry_ten)

        connection.commit()

        list_db.close()
        connection.close()

    Save_IMDb_button = Button(second_window, text = 'Save this list!', command = save_IMDb)

    Save_IMDb_button.pack()

    second_window.mainloop()


def Amazon_page():

    third_window = Toplevel()

    third_window.title('Top 10 E-Books!')

    third_window.configure(background = 'white')


    Amazon_page = urlopen('https://www.amazon.com.au/gp/bestsellers/digital-text/2496751051/ref=zg_bs_fvp_f_p_2496751051')

    Amazon_html_content = Amazon_page.read()

    Amazon_page.close()#For some reason I am unable to print apostrophys with my string into SQL, so I have had to remove them

    Amazon = findall('alt="(.+)" title', Amazon_html_content)



    Label1 = Label(third_window, text = '1.' + ' ' + Amazon[0], font = ("Arial", 12), bg = 'white')
    Label1.pack()

    Label2 = Label(third_window, text = '2.' + ' ' + Amazon[1], font = ("Arial", 12), bg = 'white')
    Label2.pack()

    Label3 = Label(third_window, text = '3.' + ' ' + Amazon[2], font = ("Arial", 12), bg = 'white')
    Label3.pack()

    Label4 = Label(third_window, text = '4.' + ' ' + Amazon[3], font = ("Arial", 12), bg = 'white')
    Label4.pack()

    Label5 = Label(third_window, text = '5.' + ' ' + Amazon[4], font = ("Arial", 12), bg = 'white')
    Label5.pack()

    Label6 = Label(third_window, text = '6.' + ' ' + Amazon[5], font = ("Arial", 12), bg = 'white')
    Label6.pack()

    Label7 = Label(third_window, text = '7.' + ' ' + Amazon[6], font = ("Arial", 12), bg = 'white')
    Label7.pack()

    Label8 = Label(third_window, text = '8.' + ' ' + Amazon[7], font = ("Arial", 12), bg = 'white')
    Label8.pack()

    Label9 = Label(third_window, text = '9.' + ' ' + Amazon[8], font = ("Arial", 12), bg = 'white')
    Label9.pack()

    Label10 = Label(third_window, text = '10.' + ' ' + Amazon[9], font = ("Arial", 12), bg = 'white')
    Label10.pack()

    Amazon_logo = image_to_PhotoImage(urlopen('http://4.bp.blogspot.com/-V03MPJUuljo/T9nLPPnU64I/AAAAAAAADVg/w2MLatUEeHE/s1600/Top10.png').read())
    Amazon_label = Label(third_window, image = Amazon_logo)
    Amazon_label.pack()


    def save_Amazon():

        connection = connect(database = 'top_ten.db')
        list_db = connection.cursor()

        command_delete = "DELETE FROM top_ten"

        list_db.execute(command_delete)

        Amazon_list1 = Amazon[0]
        Amazon_list2 = Amazon[1]
        Amazon_list2a = Amazon_list2.replace("'", "") #For some reason I am unable to print apostrophys with my string into SQL, so I have had to remove them
        Amazon_list3 = Amazon[2]
        Amazon_list4 = Amazon[3]
        Amazon_list5 = Amazon[4]
        Amazon_list6 = Amazon[5]
        Amazon_list7 = Amazon[6]
        Amazon_list8 = Amazon[7]
        Amazon_list9 = Amazon[8]
        Amazon_list10 = Amazon[9]

        Amazon_one = "INSERT INTO top_ten VALUES (1, 'test1')"

        Amazon_entry_one = Amazon_one.replace('test1', Amazon_list1)


        Amazon_two = "INSERT INTO top_ten VALUES (2, 'test2')"

        Amazon_entry_two = Amazon_two.replace('test2', Amazon_list2a)

        list_db.execute(Amazon_entry_two)


        Amazon_three = "INSERT INTO top_ten VALUES (3, 'test3')"

        Amazon_entry_three = Amazon_three.replace('test3', Amazon_list3)


        Amazon_four = "INSERT INTO top_ten VALUES (4, 'test4')"

        Amazon_entry_four = Amazon_four.replace('test4', Amazon_list4)


        Amazon_five = "INSERT INTO top_ten VALUES (5, 'test5')"

        Amazon_entry_five = Amazon_five.replace('test5', Amazon_list5)


        Amazon_six = "INSERT INTO top_ten VALUES (6, 'test6')"

        Amazon_entry_six = Amazon_six.replace('test6', Amazon_list6)


        Amazon_seven = "INSERT INTO top_ten VALUES (7, 'test7')"

        Amazon_entry_seven = Amazon_seven.replace('test7', Amazon_list7)


        Amazon_eight = "INSERT INTO top_ten VALUES (8, 'test8')"

        Amazon_entry_eight = Amazon_eight.replace('test8', Amazon_list8)


        Amazon_nine = "INSERT INTO top_ten VALUES (9, 'test9')"

        Amazon_entry_nine = Amazon_nine.replace('test9', Amazon_list9)


        Amazon_ten = "INSERT INTO top_ten VALUES (10, 'test0')"

        Amazon_entry_ten = Amazon_ten.replace('test0', Amazon_list10)

        list_db.execute(Amazon_entry_one)
        list_db.execute(Amazon_entry_three)
        list_db.execute(Amazon_entry_four)
        list_db.execute(Amazon_entry_five)
        list_db.execute(Amazon_entry_six)
        list_db.execute(Amazon_entry_seven)
        list_db.execute(Amazon_entry_eight)
        list_db.execute(Amazon_entry_nine)
        list_db.execute(Amazon_entry_ten)
       
        connection.commit()

        list_db.close()
        connection.close()

    Save_Amazon_button = Button(third_window, text = 'Save this list!', command = save_Amazon)

    Save_Amazon_button.pack()

    third_window.mainloop()


#splash screen
root_window = Tk()

root_window.title('Top 10 lists!')


top_list_logo = image_to_PhotoImage(urlopen('http://www.hsstrengthcoach.com/wp-content/uploads/2015/07/top_10.png').read())
top_list_label = Label(root_window, image = top_list_logo)
top_list_label.pack()


iTunes_button = Button(root_window, text = "Press for Top 10 Songs!",
                       command = iTunes_page)
iTunes_button.pack()


IMDb_button = Button(root_window, text = "Press for Top 10 Movies!",
                     command = IMDb_page)
IMDb_button.pack()


Amazon_button = Button(root_window, text = "Press for Top 10 E-Books!",
                       command = Amazon_page)
Amazon_button.pack()
                 

root_window.mainloop()




