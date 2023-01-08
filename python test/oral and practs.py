import random
from re import S

def oral():
    
    data_type = ["Numeric","String","list","Tuple","Dictionary","Set","array","dataframe"]
    data = random.choice(data_type)
    l = ["What is python describe history of python",f"Describe the {data} datatype.","Describe Python operators.","What is control flow ? Explain in brief.","What is function ? Describe its types.","Describe components of function.","What is OOPS concept ? Explain features,advantages and disadvantages.","Explain pillers of OOPS","What is Decorator ? explain its Types.","Explain file handling.","Expalain types of Methods","Explain type of objects","Explain Filter,Map,Reduce Function."]
    s=""
    j=0
    for i in range(5):
        q_1 = random.choice(l)
        j=j+1
        k=0
        if j==1 :
            print(q_1,"\n")
            s=s+q_1
            k=k+1
        elif j>=2 and j<4:
            if s==q_1:
                pass
            else:
                print(q_1,"\n")
                j=4


def ptractical():
    
    inheritance_1 = ["Single","Mul-Level","Multiple","heirarchical","Hybrid"]
    polymorphisom_1 = ["Method overloading","Operator overloading","Method overriding","Duck Typing"]
    data = random.choice(inheritance_1)
    data_1 = random.choice(polymorphisom_1)
    l = ["Lambda function greater than 3 numbers.","Recursion function","User Defined Decorators",f"Perform {data}  inheritance",f" Perform {data_1} of polymorphisom","Perform getter settor methids of encapsulation","Perform abstraction and create abstraction layer.","Peform serialization.","Perforn has a relation","Perform Filter,Map,Reduce Function."]

    s=""
    j=0
    for i in range(5):
        q_1 = random.choice(l)
        j=j+1
        k=0
        if j==1 :
            print(q_1,"\n")
            s=s+q_1
            k=k+1
        elif j>=2 and j<4:
            if s==q_1:
                pass
            else:
                print(q_1,"\n")
                j=4

print("*************** Question Paper ******************\n\n")
print("Q1.Theory Questions...\n")
oral()
print("\n\nQ2.Practical Question\n")
ptractical()





