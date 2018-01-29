import random
from Tkinter import *

total = 0
accepted = 0
denied = 0

app = Tk()

def generate_random():
  ran_num = random.uniform(-1, 1)
  return ran_num

def generate_pair():
  x = generate_random()
  y = generate_random()
  return (x, y)

def distance_from_center(x, y):
  distance = (x ** 2 + y ** 2) ** 0.5
  return distance

def plot():
  global total, accepted, denied, c, app
  if total < 10000:
    ran_x, ran_y = generate_pair()
    dist_center = distance_from_center(ran_x, ran_y)
    if dist_center <= 1:
      accepted += 1
      c.create_oval((150 + ran_x * 100 - 0.2), (150 + ran_y * 100 - 0.2), (150 + ran_x * 100 + 0.2), (150 + ran_y * 100 + 0.2), outline="green", fill="green")
    else:
      denied += 1
      c.create_oval((150 + ran_x * 100 - 0.2), (150 + ran_y * 100 - 0.2), (150 + ran_x * 100 + 0.2), (150 + ran_y * 100 + 0.2), outline="red", fill="red")
    total += 1
    app.after(1, plot)
  else:
    percentage_accepted = float(accepted) / total
    print("Accepted: %d, Percentage: %f") %(accepted, percentage_accepted)
    print("Denied: %d, Percentage: %f") %(denied, 1 - percentage_accepted)
    print("Area of circle: %f") %(percentage_accepted * 4)

def main():
  global app
  app.title("Monte Carlo Simulation")
  app.geometry("300x300")
  global c
  c = Canvas(app, width=300, height=300)
  c.pack()
  c.create_rectangle(50, 50, 250, 250, outline="black")
  c.create_oval(50, 50, 250, 250, outline="blue")
  plot()
  app.mainloop()

main()
