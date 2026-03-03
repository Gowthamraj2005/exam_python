questions = [

{
"id": 1,
"question": """What is the output?

x = 5
def f():
    print(x)
    x = 10
f()
""",
"options": ["5", "10", "Error", "None"],
"answer": "Error"
},

{
"id": 2,
"question": """What is the output?

print(bool("False"))
""",
"options": ["False", "True", "Error", "None"],
"answer": "True"
},

{
"id": 3,
"question": """What is the output?

a = [1,2,3]
b = a
b += [4]
print(a)
""",
"options": ["[1,2,3]", "[1,2,3,4]", "Error", "None"],
"answer": "[1,2,3,4]"
},

{
"id": 4,
"question": """What is the output?

print(0.1 + 0.2 == 0.3)
""",
"options": ["True", "False", "Error", "0.3"],
"answer": "False"
},

{
"id": 5,
"question": """What is the output?

for i in range(3):
    if i == 1:
        continue
    print(i, end="")
""",
"options": ["012", "02", "01", "Error"],
"answer": "02"
},

{
"id": 6,
"question": """What is the output?

print("abc"*2 + "def")
""",
"options": ["abcabcdef", "abcdef", "Error", "abc2def"],
"answer": "abcabcdef"
},

{
"id": 7,
"question": """What is the type of t?

t = (1)
""",
"options": ["tuple", "int", "list", "Error"],
"answer": "int"
},

{
"id": 8,
"question": """What is the output?

print({1,2,3} & {2,3,4})
""",
"options": ["{2,3}", "{1,4}", "{1,2,3,4}", "Error"],
"answer": "{2,3}"
},

{
"id": 9,
"question": """What is the output?

d = {"a":1}
print(d.get("b",0))
""",
"options": ["Error", "None", "0", "1"],
"answer": "0"
},

{
"id": 10,
"question": """What is the output?

x = [i*i for i in range(3)]
print(x)
""",
"options": ["[1,4,9]", "[0,1,4]", "[0,1,4,9]", "Error"],
"answer": "[0,1,4]"
},

{
"id": 11,
"question": """What is the output?

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

B()
""",
"options": ["A B", "B A", "A", "Error"],
"answer": "A B"
},

{
"id": 12,
"question": """Which is immutable?""",
"options": ["list", "set", "dictionary", "tuple"],
"answer": "tuple"
},

{
"id": 13,
"question": """What is the output?

print([1,2] + [3,4])
""",
"options": ["[4,6]", "[1,2,3,4]", "Error", "10"],
"answer": "[1,2,3,4]"
},

{
"id": 14,
"question": """What is the output?

print("".join(reversed("abc")))
""",
"options": ["abc", "cba", "Error", "None"],
"answer": "cba"
},

{
"id": 15,
"question": """Dictionary lookup average complexity?""",
"options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"],
"answer": "O(1)"
},

{
"id": 16,
"question": """What is the output?

s = "Python"
print(s[-3:])
""",
"options": ["tho", "hon", "on", "ton"],
"answer": "hon"
},

{
"id": 17,
"question": """What is the output?

a = {1,2,3}
a.add(2)
print(len(a))
""",
"options": ["4", "3", "2", "Error"],
"answer": "3"
},

{
"id": 18,
"question": """What is the output?

print(list(map(lambda x: x*2, [1,2,3])))
""",
"options": ["[1,2,3]", "[2,4,6]", "Error", "None"],
"answer": "[2,4,6]"
},

{
"id": 19,
"question": """What does yield return?""",
"options": ["List", "Generator", "Tuple", "None"],
"answer": "Generator"
},

{
"id": 20,
"question": """What is GIL?""",
"options": ["Global Interpreter Lock", "General Import Library", "Global Index List", "None"],
"answer": "Global Interpreter Lock"
},

# NumPy

{
"id": 21,
"question": """What is the output?

import numpy as np
a = np.array([1,2,3])
print(a*2)
""",
"options": ["[1,2,3,1,2,3]", "[2,4,6]", "[1,4,9]", "Error"],
"answer": "[2,4,6]"
},

{
"id": 22,
"question": """np.zeros((2,2)) returns?""",
"options": ["2x2 ones", "2x2 zeros", "Error", "Empty list"],
"answer": "2x2 zeros"
},

# Pandas

{
"id": 23,
"question": """What does groupby() do in pandas?""",
"options": ["Sorting", "Filtering", "Aggregation", "Deleting"],
"answer": "Aggregation"
},

{
"id": 24,
"question": """loc in pandas is used for?""",
"options": ["Position indexing", "Label indexing", "Sorting", "Merging"],
"answer": "Label indexing"
},

# Matplotlib

{
"id": 25,
"question": """Default matplotlib plot type?""",
"options": ["Pie", "Line", "Bar", "Scatter"],
"answer": "Line"
},

# Django

{
"id": 26,
"question": """Django follows which architecture?""",
"options": ["MVC", "MVT", "MVVM", "REST"],
"answer": "MVT"
},

{
"id": 27,
"question": """Django ORM stands for?""",
"options": ["Object Relation Mapping", "Object Relational Mapping", "Online Relational Model", "None"],
"answer": "Object Relational Mapping"
},

# More Advanced Logic

{
"id": 28,
"question": """What is output?

print(type(lambda x: x))
""",
"options": ["function", "lambda", "object", "Error"],
"answer": "function"
},

{
"id": 29,
"question": """What is output?

print({}.get("a"))
""",
"options": ["None", "0", "Error", "False"],
"answer": "None"
},

{
"id": 30,
"question": """What is output?

print(5//2)
""",
"options": ["2", "2.5", "3", "Error"],
"answer": "2"
},

# Remaining conceptual hard ones

{
"id": 31,
"question": "What is polymorphism?",
"options": ["Same interface different behavior", "Inheritance only", "Overloading only", "None"],
"answer": "Same interface different behavior"
},

{
"id": 32,
"question": "What is encapsulation?",
"options": ["Data hiding", "Looping", "Sorting", "Inheritance"],
"answer": "Data hiding"
},

{
"id": 33,
"question": "What is abstraction?",
"options": ["Hiding implementation", "Hiding variables", "Looping", "None"],
"answer": "Hiding implementation"
},

{
"id": 34,
"question": "What is recursion?",
"options": ["Loop", "Function calling itself", "Inheritance", "None"],
"answer": "Function calling itself"
},

{
"id": 35,
"question": "Which keyword handles exception?",
"options": ["try", "catch", "handle", "throw"],
"answer": "try"
},

{
"id": 36,
"question": "What is __init__?",
"options": ["Destructor", "Constructor", "Operator", "Loop"],
"answer": "Constructor"
},

{
"id": 37,
"question": "What is Django migration?",
"options": ["Data delete", "Schema change", "Server restart", "None"],
"answer": "Schema change"
},

{
"id": 38,
"question": "What is queryset?",
"options": ["Database result set", "List", "Tuple", "None"],
"answer": "Database result set"
},

{
"id": 39,
"question": "What is virtual environment?",
"options": ["Separate Python setup", "Loop", "Function", "None"],
"answer": "Separate Python setup"
},

{
"id": 40,
"question": "What is middleware in Django?",
"options": ["Template", "Request/Response processor", "Model", "None"],
"answer": "Request/Response processor"
},

{
"id": 41,
"question": "Which is mutable?",
"options": ["tuple", "list", "int", "str"],
"answer": "list"
},

{
"id": 42,
"question": "Set allows duplicate?",
"options": ["Yes", "No", "Sometimes", "Error"],
"answer": "No"
},

{
"id": 43,
"question": "Lambda is?",
"options": ["Anonymous function", "Loop", "Class", "Module"],
"answer": "Anonymous function"
},

{
"id": 44,
"question": "Break does?",
"options": ["Exit loop", "Skip iteration", "Nothing", "Error"],
"answer": "Exit loop"
},

{
"id": 45,
"question": "Continue does?",
"options": ["Exit loop", "Skip iteration", "Stop program", "None"],
"answer": "Skip iteration"
},

{
"id": 46,
"question": "Pass does?",
"options": ["Skip block", "Exit loop", "Error", "None"],
"answer": "Skip block"
},

{
"id": 47,
"question": "What is list comprehension?",
"options": ["Compact loop", "Function", "Module", "Class"],
"answer": "Compact loop"
},

{
"id": 48,
"question": "NumPy array supports?",
"options": ["Vectorization", "Only loops", "Only recursion", "None"],
"answer": "Vectorization"
},

{
"id": 49,
"question": "Pandas DataFrame is?",
"options": ["2D structure", "1D structure", "3D structure", "None"],
"answer": "2D structure"
},

{
"id": 50,
"question": "Matplotlib is used for?",
"options": ["Web dev", "Visualization", "Database", "Compiler"],
"answer": "Visualization"
}

]
