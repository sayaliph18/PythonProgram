

#Python Program to Calculate Grade of a Student

sub1 = float(input('Enter a marks of first subject: '))
sub2 = float(input('Enter a marks of second subject: '))
sub3 = float(input('Enter a marks of third subject: '))
sub4 = float(input('Enter a marks of fourth subject: '))
sub5 = float(input('Enter a marks of fifth subject: '))

avg = ((sub1 + sub2 +sub3 + sub4 + sub5 )/5)
print('Average marks: ',avg)
if(avg >= 90):
    print('Grade: A')
elif(90 > avg >= 80):
    print('Grade: B')
elif(80 > avg >= 70):
    print('Grade: C')
elif(70 > avg >= 50):
    print('Grade: D')
else:
    print('Grade: E')
