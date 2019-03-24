# Imports Needed Modules
from tkinter import * # GUI
from tkinter import messagebox # Error MSG
import math # GCF, SQRT
import cmath # Quadratic Formula
import time # time.sleep


# Defines a function, does all work, to be called on Button Press
def quadraticProgram(event):


  try:
    # Gets Input from Textbox
    quadratic = userInputEntry.get()


    # Letters that can be used as variables
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    # Cleans up Input

    for letter in alphabet:

      quadratic = quadratic.replace(letter," ")

    refinedQuadratic = quadratic.replace("^2", " ")
    refinedQuadratic = refinedQuadratic.replace("+", " ")

    # Splits Input into a list with the delimiter of " "
    refinedQuadratic = refinedQuadratic.split()

    # Changes Elements of List to Integers
    refinedQuadratic = list(map(int, refinedQuadratic))
    # Sets Coefficients of function
    a = refinedQuadratic[0]
    b = refinedQuadratic[1]
    c = refinedQuadratic[2]

    # Boolean Set to True to Initialize
    factorable = True

    # Makes Math More User Friendly -- Finds Discriminant
    discriminant = (b**2)-(4*a*c)

    # Finds Solutions -- Uses Discriminant Variable
    solution1 = ((-1*b)+cmath.sqrt(discriminant))/(2*a)
    solution2 = ((-1*b)-cmath.sqrt(discriminant))/(2*a)

    # Converts to String
    solution1 = str(solution1)
    solution2 = str(solution2)

    # Cleans up Solutions -- CMATH adds 0j if no imaginary numbers
    if "-0j" in solution1:
      solution1 = solution1.replace("-0j","")
    if "-0j" in solution2:
      solution2 = solution2.replace("-0j","")

    if "+0j" in solution1:
      solution1 = solution1.replace("+0j","")
    if "+0j" in solution2:
      solution2 = solution2.replace("+0j","")

    if "j" in solution1:
      solution1 = solution1.replace("j","i")
    if "j" in solution2:
      solution2 = solution2.replace("j","i")


    solution1 = solution1.replace("(","")
    solution1 = solution1.replace(")","")
    solution2 = solution2.replace("(","")
    solution2 = solution2.replace(")","")

    # Outputs Solutions -- With tkinter.Label
    output = Label(rootFrame, text = "\nThe solutions are: %s and %s"%(solution1,solution2), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
    output.pack()

    # Factors out GCF of the polynomial
    initialGCF = math.gcd(a,b)
    finalGCF = math.gcd(initialGCF,c)
    a //= finalGCF
    b //= finalGCF
    c //= finalGCF

    # Makes GCF Negative if a is negative
    if a < 0:
      finalGCF *= -1

    if discriminant < 0:
      discriminant = .5 # Arbitrary number to avoid sqrt(negative_number)

    # If the Discriminant is not a Perfect Square, The Quadratic cannot be factored
    sqrtDiscriminant = math.sqrt(discriminant)

    # If the discriminant is a perfect square,
    if float(sqrtDiscriminant).is_integer():
      pass

    # If not,
    else:

      # Cannot Factor
      factorable = False

      # Outputs with tkinter.label
      output = Label(rootFrame, text = "This quadratic function cannot be factored.", font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
      output.pack()

      # Converts back to original input
      if finalGCF == "":
        finalGCF = 1

      if finalGCF < 0:
        finalGCF *= -1

      a *= finalGCF
      b *= finalGCF
      c *= finalGCF

      if a == 1:
        a = ""
      if b == 1:
        b = ""

      if "-" not in str(b):
        b = "+"+str(b)
      if "-" not in str(c):
        c = "+"+str(c)

      # Final Output -- With tkinter.Label
      finalLabel = Label(rootFrame, text = "The quadratic that was entered: (%sx^2%sx%s)"%(a, b, c), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
      finalLabel.pack()

    # If the Quadratic can be Factored
    if factorable:

      # Case a = 1
      if a == 1:

        # Defines Variables
        coefficient1 = a
        coefficient2 = a

        # Converts to int
        solution1 = int(solution1)
        solution2 = int(solution2)

        # If a = 1, The factors will be -a
        factor1 = -1*solution1
        factor2 = -1*solution2

        # Adds + to factors if non-negative
        if "-" not in str(factor1):
          factor1 = "+"+str(factor1)
        if "-" not in str(factor2):
          factor2 = "+"+str(factor2)

      else:

        # Make the coefficients -a if a is negative
        if a < 0:
          coefficient1 = -1*a
          coefficient2 = -1*a
        else:
          coefficient1 = a
          coefficient2 = a

        # Convert to float
        solution1 = float(solution1)
        solution2 = float(solution2)

        # Find Initial Factors
        factor1 = -1*solution1
        factor2 = -1*solution2

        # Make factors negative if a is negative, also get rid of any decimals
        if a < 0:
          factor1 *= -1*a
          factor2 *= -1*a
        else:
          factor1 *= a
          factor2 *= a

        # Converts to Int
        factor1 = int(factor1)
        factor2 = int(factor2)

        # Factors Out GCFs within each factors
        factor1GCF = math.gcd(a, factor1)
        coefficient1 /= factor1GCF
        factor1 /= factor1GCF

        factor2GCF = math.gcd(a, factor2)
        coefficient2 /= factor2GCF
        factor2 /= factor2GCF

        # Adds + to factors if non-negative
        if "-" not in str(factor1):
          factor1 = "+"+str(int(factor1))
        else:
          factor1 = int(factor1)
        if "-" not in str(factor2):
          factor2 = "+"+str(int(factor2))
        else:
          factor2 = int(factor2)


      # Cleaning Up and Printing Output
      if coefficient1 == 1:
        coefficient1 = ""
      if coefficient2 == 1:
        coefficient2 = ""

      if finalGCF == 1:
        finalGCF = ""


      # Makes the output not print coefficients of 1 -- Outputs with tkinter.Label
      if a != 1:

        if coefficient1 == "" and coefficient2 != "":
          factorLabel = Label(rootFrame, text = "The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, coefficient1, factor1, int(coefficient2), factor2), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
          factorLabel.pack()
        elif coefficient2 == "" and coefficient1 != "":
          factorLabel = Label(rootFrame, text = "The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, int(coefficient1), factor1, coefficient2, factor2), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
          factorLabel.pack()
        else:
          factorLabel = Label(rootFrame, text = "The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, int(coefficient1), factor1, int(coefficient2), factor2), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
          factorLabel.pack()


      else: # If a is 1, output with tkinter.Label
        factorLabel = Label(rootFrame, text = "The factors are: %s(x%s)(x%s)"%(finalGCF, factor1, factor2), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
        factorLabel.pack()


      # More Cleanup -- Converts back to original input
      if finalGCF == "":
        finalGCF = 1

      if finalGCF < 0:
        finalGCF *= -1

      a *= finalGCF
      b *= finalGCF
      c *= finalGCF

      if a == 1:
        a = ""
      if b == 1:
        b = ""

      if "-" not in str(b):
        b = "+"+str(b)
      if "-" not in str(c):
        c = "+"+str(c)

      # Final Output -- With tkinter.Label
      finalLabel = Label(rootFrame, text = "The quadratic that was factored: (%sx^2%sx%s)"%(a, b, c), font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
      finalLabel.pack()

  except:
   messagebox.showerror("Error","An Error Has Occured -- The Program will Terminate")
   time.sleep(.5)
   root.destroy()

def quitProgram(event):
  root.destroy()

def clear(event):
  global rootFrame, root, welcome, inputLabel, userInputEntry, silverCreekLogo, logoLabel, calculateButton, clearButton
  rootFrame.destroy()
  rootFrame = Frame(root, bg = '#1d1f21')
  rootFrame.pack()
  # Welcome Label
  welcome = Label(rootFrame, text = "Welcome to the Quadratic Program:", font = ("Courier New Bold",36), bg = '#1d1f21', fg = "#ffffff")
  welcome.pack()

  # Input Label
  inputLabel = Label(rootFrame, text = "Enter a Quadratic Equation:", font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
  inputLabel.pack()

  # Getting Input
  userInputEntry = Entry(rootFrame)
  userInputEntry.pack()

  userInputEntry.delete(0, END) # Delete anything in there already
  userInputEntry.insert(0, "ax^2+bx+c") # Sample Input
  userInputEntry.focus() # Able to immediately start typing

  # Calculate Button -- Executes earlier function
  calculateButton = Button(rootFrame, text = "Calculate", fg = "#000000", highlightbackground = "#800080")
  calculateButton.bind("<Button-1>", quadraticProgram)
  calculateButton.pack()
  root.bind("<Return>", quadraticProgram)

  # Clear Button -- Executes earlier function
  clearButton = Button(rootFrame, text = "Clear", fg = "#000000", highlightbackground = "#800080")
  clearButton.bind("<Button-1>", clear)
  clearButton.pack()
  root.bind("<Control-BackSpace>", clear)
  root.bind("<Command-BackSpace>", clear)

  # Quit Button -- Executes Earlier function
  quitButton = Button(rootFrame, text = "Quit", fg = "#000000", highlightbackground = "#800080")
  quitButton.bind("<Button-1>", quitProgram)
  quitButton.pack()
  root.bind("<Control-q>", quitProgram)

# Initializes Blank Window
root = Tk()

# Sets Title
root.title("Quadratics")
# Sets Window Size
root.geometry('1920x1080')
# Sets Background Color
root.config(bg = '#1d1f21')

rootFrame = Frame(root, bg = '#1d1f21')
rootFrame.pack()

# Welcome Label
welcome = Label(rootFrame, text = "Welcome to the Quadratic Program:", font = ("Courier New Bold",36), bg = '#1d1f21', fg = "#ffffff")
welcome.pack()

# Input Label
inputLabel = Label(rootFrame, text = "Enter a Quadratic Function:", font = ("Courier New Bold", 24), bg = '#1d1f21', fg = "#ffffff")
inputLabel.pack()

# Getting Input
userInputEntry = Entry(rootFrame)
userInputEntry.pack()

userInputEntry.delete(0, END) # Delete anything in there already
userInputEntry.insert(0, "ax^2+bx+c") # Sample Input
userInputEntry.focus() # Able to immediately start typing

# Calculate Button -- Executes earlier function
calculateButton = Button(rootFrame, text = "Calculate", fg = "#000000", highlightbackground = "#800080")
calculateButton.bind("<Button-1>", quadraticProgram)
calculateButton.pack()
root.bind("<Return>", quadraticProgram)

# Clear Button -- Executes earlier function
clearButton = Button(rootFrame, text = "Clear", fg = "#000000", highlightbackground = "#800080")
clearButton.bind("<Button-1>", clear)
clearButton.pack()
root.bind("<Control-BackSpace>", clear)
root.bind("<Command-BackSpace>", clear)

# Quit Button -- Executes Earlier function
quitButton = Button(rootFrame, text = "Quit", fg = "#000000", highlightbackground = "#800080")
quitButton.bind("<Button-1>", quitProgram)
quitButton.pack()
root.bind("<Control-q>", quitProgram)

root.mainloop()
