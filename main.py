import tkinter as tk

def runapp():
        ans= 0

        window = tk.Tk()
        window.geometry("900x600")


        window.title("Welcome to application")
        # add labels before input fields
        welcomelabel =tk.Label(window)
        welcomelabel.config(text="Welcome! please enter the various fields and press calculate")


        citylabel = tk.Label(window)
        citylabel.config(text="enter city: ")


        geographylabel = tk.Label(window)
        geographylabel.config(text="enter how fun beautiful the surrounding geography is:  ")
        slider2 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        costlabel = tk.Label(window)
        costlabel.config(text="enter cheapness: ")
        slider3 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        educationlabel = tk.Label(window)
        educationlabel.config(text="enter education quality: ")
        slider4 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        sociallabel = tk.Label(window) # night life, clubs, nature of people,activites
        sociallabel.config(text="enter social life: ")
        slider5 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        joblabel = tk.Label(window)#
        joblabel.config(text="enter ease of working part time job: ")
        slider6 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        transitionlabel = tk.Label(window)#
        transitionlabel.config(text="enter ease of transition: ")
        slider7 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        housabilitylabel = tk.Label(window)
        housabilitylabel.config(text="enter the housing ability of the place: ")
        slider8 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        travabilitylabel = tk.Label(window)
        travabilitylabel.config(text="enter how easy it is to travel from this location:  ")
        slider9 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        safetylabel = tk.Label(window)
        safetylabel.config(text="how good is the geography here:   ")
        slider10 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        climatelabel = tk.Label(window)
        climatelabel.config(text="enter the quality of the climate:  ")
        slider11 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        distlabel = tk.Label(window)
        distlabel.config(text="Enter how close from home this place is")
        slider12 = tk.Scale(window, from_=2, to=8,orient=tk.HORIZONTAL)

        answerlabel = tk.Label(window)
        answerlabel.config(text="data pending ",font=46)
       #develop the textboxes respective to the labels

        citylabel = tk.Label(window)
        citylabel.config(text="enter city: ")



        costf = tk.Entry(window)
        educationf = tk.Entry(window)
        socialf = tk.Entry(window)
        jobf = tk.Entry(window)
        transitionf = tk.Entry(window)
        housabilityf = tk.Entry(window)
        travabilityf = tk.Entry(window)
        safetyf = tk.Entry(window)
        climatef = tk.Entry(window)
        distf =tk.Entry(window)
        cityf = tk.Entry(window)


        #place some of the widgets

        welcomelabel.grid(row=0,column =1)
        costf.          grid(row=1,column =1)
        educationf.     grid(row=2,column =1)
        socialf.        grid(row=3,column =1)
        jobf.           grid(row=4,column =1)
        transitionf.    grid(row=5,column =1)
        housabilityf.   grid(row=6,column =1)
        travabilityf.   grid(row=7,column =1)
        safetyf.        grid(row=8,column =1)
        climatef.       grid(row=9,column =1)
        distf.          grid(row=10,column =1)
        cityf.grid(row=4, column=3)



        welcomelabel.    grid(row=0, column=0)
        costlabel.       grid(row=1, column=0)
        educationlabel.  grid(row=2, column=0)
        sociallabel.     grid(row=3, column=0)
        joblabel.        grid(row=4, column=0)
        transitionlabel. grid(row=5, column=0)
        housabilitylabel.grid(row=6, column=0)
        travabilitylabel.grid(row=7, column=0)
        safetylabel.     grid(row=8, column=0)
        climatelabel.    grid(row=9, column=0)
        citylabel.      grid(row=3,column=3)


        distlabel.grid(row=10,column =0 )
        answerlabel.grid(row=11, column=0)

        slider2.grid(row=1,column=2)
        slider3.grid(row=2, column=2)
        slider4.grid(row=3, column=2)
        slider5.grid(row=4, column=2)
        slider6.grid(row=5, column=2)
        slider7.grid(row=6, column=2)
        slider8.grid(row=7, column=2)
        slider9.grid(row=8, column=2)
        slider10.grid(row=9, column=2)
        slider11.grid(row=10, column=2)

        def calculater():
                slidersum = 0
                slidersum+=slider2.get()
                slidersum+=slider3.get()
                slidersum+=slider4.get()
                slidersum+=slider5.get()
                slidersum+=slider6.get()
                slidersum+=slider7.get()
                slidersum+=slider8.get()
                slidersum+=slider9.get()
                slidersum+=slider10.get()
                slidersum+=slider11.get()
                print(slidersum)


                value = 1
                value *=     (int(costf.get()) **int(slider2.get()))
                value *= (int(educationf.get()) **int(slider3.get()))
                value *= (int(socialf.get())**int(slider4.get()))
                value *= (int(jobf.get())**int(slider5.get()))
                value *=       (int(transitionf.get())**int(slider6.get()))
                value *= (int(housabilityf.get())**int(slider7.get()))
                value *=       (int(travabilityf.get())**int(slider8.get()))
                value *=        (int(safetyf.get())**int(slider9.get()))
                value *=       (int(climatef.get())**int(slider10.get()))
                value *=        (int(distf.get())**int(slider11.get()))

                value= value**(1/slidersum)
                answerlabel.config(text=str(value))
                with open("calculations.txt","a") as f:
                        f.write("city: "+cityf.get()+"| score: "+str(value)+"\n")






        calculate = tk.Button(window, command=calculater)
        calculate.config(text="calculate")
        calculate.grid(row=11, column=1)

        window.mainloop()


if __name__ == '__main__':
        runapp()
       
