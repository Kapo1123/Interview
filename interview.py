# I created this class with 4 different functions to compute different output as needed
class Interview:
    def __init__(self, q1_input:str,q2_input1 :int,q2_input2 :int, q2_input3 :int,q3_input: int,q4_input: int):
        self.question1 :str = q1_input 
        self.question2_1 = q2_input1
        self.question2_2 = q2_input2
        self.question2_3 = q2_input3
        self.question3 = q3_input
        self.question4 = q4_input

    def reversing(self):
        return "".join(reversed(self.question1))
        
    def max_num(self):
        num = max(self.question2_1,self.question2_2,self.question2_3)
        return num
    def factorial_num(self):
        if self.question3 == 1:
            return 1
        else:
            return self.question3 * self.helping()
    def helping(self):
        self.question3 -= 1
        return self.factorial_num()

    def Fibonacci_sequence(self):
        dict_ = dict()
        dict_[1] = 1
        dict_[2] =1
        i=2
        while i < self.question4:
            dict_[i+1] = dict_[i]+dict_[i-1]
            i+=1
        return dict_[self.question4]
    
#test case
first_input = "Hello There"
second_input1 = 1
second_input2 = 2
second_input3 =3
factorial_num = 5
term = 14
New_try = Interview(first_input,second_input1,second_input2,second_input3,factorial_num,term)
print(f"Reverse of the string is \"{New_try.reversing()}\" ")
print(f"Max number among three numbers is {New_try.max_num()}")
print(f"Factorial of a given number is {New_try.factorial_num()}")
print(f"The {term}th term in fibonacci sequence is {New_try.Fibonacci_sequence()}")


            



    
    