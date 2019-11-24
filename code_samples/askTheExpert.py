import tkinter
import tkinter.simpledialog
import tkinter.messagebox

print("Ask the expert - Capital cities of the world")

the_world = {}


def read_from_file():
    with open('countries.txt', 'r') as text_file:
        for line in text_file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city


def write_to_file(country_name, city_name):
    with open('countries.txt', 'a') as text_file:
        text_file.write("\n" + country_name + '/' + city_name)


root = tkinter.Tk()
root.withdraw()
read_from_file()

while True:
    query_country = tkinter.simpledialog.askstring("Country", "Type the name: ")
    if query_country in the_world:
        result = the_world[query_country]
        tkinter.messagebox.showinfo("Answer", "The capital city of " + query_country + " is " + result + "!")
    elif not query_country:
        break
    else:
        new_city = tkinter.simpledialog.askstring("Teach Me", "I do not know, what is the capital of " + query_country + "?")
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()