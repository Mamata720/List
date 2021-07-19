# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question]

# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# solution_list = [3, 4,1]
# answer_list=[
#     ["(1)four","(3)seven"],
#     ["(4)Delhi","(2)Bhopal"],
#     ["(4)agriculture","(1)software engineering"]
# ]
# print("Kaun Banega Codepati (KBC)")
# i=0
# s=0
# count=0
# while i<len(question_list):
#     print(question_list[i])
#     a=0
#     b=i
#     while a<len(options_list[i]):
#         k=options_list[b][a]
#         print(a+1,k)
#         a=a+1
#     num1=input("do you want 5050 lifeline")
#     if num1=="yes":
#         print("50 50 lifeline")
#         if count<1:
#             print(answer_list[b])
#             num2=int(input("enter your answer"))
#             if num2==solution_list[i]:
#                 s+=10000
#                 print("your answer is correct")
#                 print ("you win Rs/",s)
#             else:
#                 print("incorrect answer")
#                 print("you can't play again")
#                 print("you win Rs/",s)
#                 break
#             count+=1
#         else:
#             print("you already use lifeline:")
#             m=int(input("enter your answer:"))
#             if m==solution_list[i]:
#                 print("congrats your answer is right")
#                 s+=10000
#                 print("you win Rs/",s)
#             else:
#                 print("No chance")
#                 print("your answer is wrong")
#                 print("you win",s)
#                 break
#     else:  
#         pass
#         k=int(input("enter your answer"))
#         if k==solution_list[i]:
#             print("right answer")
#             s+=10000
#             print("you win Rs/",s)
#         else:
#             print("no chance")
#             print("your answer is wrong")
#             print("you win Rs/",s)
#             break
#     i=i+1
# print("___congrulation you are a part of__KON BANAYGA CODEPATI__")
# print("you win Rs/",s)
# print("THANKYOU BEING PART OF KBC")
                     



question_list = [
"Q.1)How many continents are there ?",#pehla question.
"Q.2)What is the capital of India?",#doosra question.
"Q.3)NG mei kaun se course padhaya jaata hai?"# Teesra question.
]
option_list = [
["Four" , "Nine","Seven","Eight"],#pehle question ke liye options
["Chandigarh", "Bhopal","Chennai","Delhi"],#second question ke liye options.
["Software Engineering" ,"Counseling" ,"Tourism","Agriculture"]#third question ke liye options.
]

solution_list = [3 , 4,1 ]# har ek question ke liye, uski solution key (yeh index nahi hai)
length = len(question_list)#in length varible i assign length of question list.
life_line = 0#i assign life_line variable because i want to use this variable in 5050 in that we only use one time this option.
ans = [[4,3],[3,4],[1,3]]# ans list for life_line option **Hint ** for user .
index = 0# for started our loop .
while index < length:#i difine loop starting point and ending point.
    print(question_list[index]) # i print index of question list in that zero index our first question will print .
    print(option_list[index])#  i print option list index means zero index first option_list will print.
    user = int(input("enter your answer / if you want to use life_line enter 5050 :-"))#i am taking user int user input from user if user want user will chose 5050 lifeline option also.
    if user == solution_list[index]:#then we will check user is equal eual solution_list[index] or not .if this contion is trure inside print condition will be excutive or inside print condition will print.
        print("Congrats! Aapka aswer sahi hai")
    elif user == 5050:#if user will give output 5050
        if life_line == 0:# then it will chen life_line == 0 or not .if yes then it will going inside.
            life_line = 1#i assign variable life_life value 1 becaue we want to give only one chance to user.
            print(ans[index])# then i will print life_line ans list index
            answer = int(input("enter your answer :-"))# after that i will take one more user input from user in answer varible .
            if answer == solution_list[index]:#then i will check  answer is equeal to equal to solution_[index] anser. if this condition is true then 
                print("Congrats! Aap ka answer sahi hai")# it will print this line if this condition is false than it will print
            else:
                print("Aapka javab galat hai")#elese line.
                break#then i will do break becase i want if user answer is wrong then than i will tell user to  out of game.
        else:
            print("only one time you can use life line.")#if second time user will write 5050 then this line will print .
            answer1 = int(input("enter your answer1 :-"))#then i will ask to user again give me input in int varibale.
            if answer1 == solution_list[index]:# i will check user answer or soultion_list[index] menans answer is same or not. if yes then it will print 
                print("Congrats! Aapka aswer sahi hai")# this line if this conditon is false then 
            else:
                print("Aapka javab galat hai")# it will excute else condition aftter that 
                break#break condition will excute .
    else:
            print("Aapka javab galat hai")
            break
    index = index + 1# index for  increment .







    
    
 