x="This test worked"
print(x)

name = "My name is A"
print (name)

x=5
y=1.5
print(x*y)

month = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September","October","November","December"]
for i in range(len(month)):
    count=len(month[i])
    #count=len(month(i))
    print(month[i],count)


Dictionary = {"movies":["Incredibles", "Sponge Bob", "Spiderman"],"Seasons":
              ["Season-1","Season-2","Season-3"]}
print(Dictionary["movies"], Dictionary["Seasons"])

# Exercise 3

movies = {'Movie1': 'Season1', 'Movie2' :'Season2', 'Movie3':'Season3', 'Movie4':'Season4'}
for a, b in movies.items():
    print( 'My favorite  ' + a + '  is ' + b )

def division(c,d):
    print(c/d)

print(division(x,y))

ken_fav={'movie':['Parent Trap','Bride Wars'],'food':['French fries','cheese','bacon']}
for item, favs in ken_fav.items():
    for x in favs:
        print("Kenisha's Favorite"+item+"is"+x)



# Python program to display all the non prime and prime numbers within an interval

# change the values of lower and upper for a different result
lower = 1
upper = 100

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper+1):
   # prime numbers are greater than 1
   if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                print(num, 'is NOT a prime')
                break
            else:
                print(num, 'is a prime number')
                break

         
    


