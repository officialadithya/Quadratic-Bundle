# Imports Complex Math Module -- Quadratic Formula
import cmath
# Imports Math Module -- GCF, SQRT
import math

cases = int(input("How many times would you like to execute the program?: "))

for i in range(1, cases+1):

  # Default to Factorable = True
  factorable = True

  # Asks for Input
  quadratic = input("\nEnter a quadratic expression with the form ax^2+bx+c: ")

  # Cleans Up Input
  refinedQuadratic = quadratic.replace("^2", " ")
  refinedQuadratic = refinedQuadratic.replace("+", " ")
  refinedQuadratic = refinedQuadratic.replace("x", " ")
  refinedQuadratic = refinedQuadratic.replace("X", " ")

  # Splits Input
  refinedQuadratic = refinedQuadratic.split()

  # Gets Coefficients
  a = int(refinedQuadratic[0])
  b = int(refinedQuadratic[1])
  c = int(refinedQuadratic[2])

  # Makes Math More User Friendly
  discriminant = (b**2)-(4*a*c)

  # Finds Solutions
  solution1 = ((-1*b)+cmath.sqrt(discriminant))/(2*a)
  solution2 = ((-1*b)-cmath.sqrt(discriminant))/(2*a)

  # Converts to String
  solution1 = str(solution1)
  solution2 = str(solution2)

  # Cleans up Solutions
  if "-0j" in solution1:
    solution1 = solution1.replace("-0j","")
  if "-0j" in solution2:
    solution2 = solution2.replace("-0j","")

  if "+0j" in solution1:
    solution1 = solution1.replace("+0j","")
  if "+0j" in solution2:
    solution2 = solution2.replace("+0j","")

  if "0j" in solution1:
    solution1 = solution1.replace("0j","0")
  if "0j" in solution2:
    solution2 = solution2.replace("0j","0")

  solution1 = solution1.replace("(","")
  solution1 = solution1.replace(")","")
  solution2 = solution2.replace("(","")
  solution2 = solution2.replace(")","")

  # Outputs Solutions
  print("\nThe solutions are: %s and %s"%(solution1,solution2))

  # If Complex, Cannot be Factored
  if "j" in solution1 or "j" in solution2:
    factorable = False
    print("\nThis quadratic function cannot be factored.")
    exit()

  # Factors out GCF
  initialGCF = math.gcd(a,b)
  finalGCF = math.gcd(initialGCF,c)
  a //= finalGCF
  b //= finalGCF
  c //= finalGCF

  # Makes GCF Negative if a is negative
  if a < 0:
    finalGCF *= -1
    

  # If the Discriminant is not a Perfect Square, The Quadratic cannot be factored
  sqrtDiscriminant = math.sqrt(discriminant)

  if float(sqrtDiscriminant).is_integer():
    pass

  else:
    factorable = False
    print("\nThis quadratic function cannot be factored.")
    exit()

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

      # Find Factors
      factor1 = -1*solution1
      factor2 = -1*solution2

      # Make factors negative if a is negative
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
      
    
    if a != 1:

      if coefficient1 == "" and coefficient2 != "":
        print("The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, coefficient1, factor1, int(coefficient2), factor2))
      elif coefficient2 == "" and coefficient1 != "":
        print("The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, int(coefficient1), factor1, coefficient2, factor2))
      elif coefficient1 != "" and coefficient2 != "":
        print("The factors are: %s(%sx%s)(%sx%s)"%(finalGCF, int(coefficient1), factor1, int(coefficient2), factor2))
      

    else:
      
      print("The factors are: %s(x%s)(x%s)"%(finalGCF, factor1, factor2))
    
    # More Cleanup
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
      
    # Final Output
    print("The quadratic that was factored: (%sx^2%sx%s)"%(a, b, c))
