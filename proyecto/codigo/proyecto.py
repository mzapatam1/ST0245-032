# based on the video https://www.youtube.com/watch?v=LDRbO9a6XPU&t=350s
import os
import psutil
import csv
from time import time

def read_Dataset(filename):
    data = []
    with open(filename, encoding='utf-8') as datos:
        read = csv.reader(datos, delimiter=";")
        for line in read:
            data.append(line)
        return(data)
        
def convert(filename):
    data=read_Dataset(filename)
    n_rows=len(data)
    newdata=[None]*n_rows
    i=0
    for line in data:
        newdata[i]=line
        i=i+1
    datos=[None]*(n_rows-1)
    headers=newdata[0]  
    for j in range(n_rows-1):
        datos[j]=newdata[j+1]
    return headers,datos

train_=convert("C://Users//Alejandra//Downloads//2_train_balanced_75000.csv")
test_=convert("C://Users//Alejandra//Downloads//2_test_balanced_25000.csv")

headers,train=train_
headers,test=test_

def unique_vals(rows, col):
    #Find the unique values for a column in a dataset.
    return set([row[col] for row in rows])

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        # we just have to labels 1 and 0
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

class Question:
     def __init__(self, column, value):
        self.column = column
        self.value = value
        
     def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value
     
        
def partition(rows, question):
    """Partitions a dataset.
    For each row in the dataset, check if it matches the question. If
    so, add it to 'true rows', otherwise, add it to 'false rows'.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(rows):
    """Calculate the Gini Impurity for a list of rows.
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty):
    """Information Gain.
    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def find_best_split(rows):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    n_features = len(headers) - 1  # number of columns

    for col in range(n_features):  # for each feature

        values = unique_vals(rows, col)  # unique values in the column

        for val in values:  # for each value

            question = Question(col, val)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain > best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

class Leaf:
    """A Leaf node classifies data.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:
    """A Decision Node asks a question.
    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows,max_depth):


    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
    gain, question = find_best_split(rows)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0 or max_depth==0:
        return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
    true_rows, false_rows = partition(rows, question)

    # Recursively build the true branch.
    true_branch = build_tree(true_rows, max_depth-1)

    # Recursively build the false branch.
    false_branch = build_tree(false_rows,max_depth-1)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)

    

def classify(row, node):
    

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


def Predicted(test,tree):
    for row in test:
     print ("Actual: %s. Predicted: %s" %
        (row[-1], print_leaf(classify(row, tree))))
    

start=time()
my_tree = build_tree(train,5)
Predicted(test,my_tree)
final=time()-start
print(final)

     
process=psutil.Process(os.getpid())
print(process.memory_info().rss)
        

