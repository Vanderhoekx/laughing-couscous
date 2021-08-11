#Doubly Linked List
#Written by Kelly Schmidt

import pyinputplus as pyip

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class AddData():
    def __init__(self):
        self.head = None

    def add_data_end(self, newdata):
        if self.head is None:
            data_adder = Node(newdata)
            data_adder.prev = None
            self.head = data_adder
        else:
            data_adder = Node(newdata)
            current = self.head
            
            while current.next:
                current = current.next
            
            current.next = data_adder
            data_adder.prev = current
            data_adder.next = None 

class AddDataRef(AddData):    
    def add_data_start(self, newdata):
        if self.head is None:
            data_adder = Node(newdata)
            self.head = data_adder
        else:
            data_adder = Node(newdata)
            data_adder.next = self.head
            self.head.prev = data_adder
            self.head = data_adder

    def add_at_position(self, newdata, index):
        counter = 0
        current = self.head
        if self.head is None:
            print('Index out of range')
        else:
            current = self.head
            while counter < index:
                counter += 1
                current = current.next
                
            current = current.prev
            data_adder = Node(newdata)
            data_adder.prev = current
            data_adder.next = current.next
            current.next = data_adder
    
    def add_after_position(self, newdata, index):
        counter = 0
        current = self.head
        if self.head is None:
            print('Index out of range')
        else:
            current = self.head
            while counter < index:
                counter += 1
                current = current.next
                
            data_adder = Node(newdata)
            data_adder.prev = current
            data_adder.next = current.next
            current.next = data_adder
    
    def add_before_reference(self, newdata, reference):
        counter = 0
        if self.head is None:
            self.empty_data()
        else:
            current = self.head
            while current:
                if current.data == reference:
                    print('{} found at node {}'.format(reference, counter))
                    counter += 1
                else:
                    counter += 1
                current = current.next
            print('Enter the index of the reference you would like to insert data at: ')
            self.add_at_position(newdata, pyip.inputInt())

    def add_after_reference(self, newdata, reference):
        counter = 0
        if self.head is None:
            self.empty_data()
        else:
            current = self.head
            while current:
                if current.data == reference:
                    print('{} found at node {}'.format(reference, counter))
                    counter += 1
                else:
                    counter += 1
                current = current.next
            print('Enter the index of the reference you would like to insert data at: ')
            self.add_after_position(newdata, pyip.inputInt())

class DeleteNode(AddDataRef):
    def del_first_item(self):
        if self.head is None:
            self.empty_data()
        else:
            current_node = self.head
            current_node = current_node.next
            current_node.prev = None
            self.head = current_node

    def del_last_item(self):
        if self.head is None:
            self.empty_data()
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node = current_node.prev
            current_node.next = None
    
    def del_by_reference(self, reference):
        counter = 0
        if self.head is None:
            self.empty_data()
        else:
            current_node = self.head
            while current_node:
                if current_node.data == reference:
                    print('{} found at node {}'.format(reference, counter))
                    counter += 1
                else:
                    counter += 1
                current_node = current_node.next
            
            print('Which index position of the reference would you like to delete.')
            self.del_by_position(pyip.inputInt())

    def del_by_position(self, index):
        counter = 0
        if self.head is None:
            self.empty_data()
        else:
            current = self.head
            while counter < index:
                current = current.next
                counter += 1
            
            del_node = current.next
            current = current.prev
            current.next = None
            current.next = del_node

class PrintNode(DeleteNode):
    def print_data(self):
        current_node = self.head
        counter = 0
        while current_node:
            if counter == 0:
                print('Head Node(0):', current_node.data)
            else:
                print('Node #{}'.format(counter), current_node.data)
            current_node = current_node.next    
            counter += 1
    
    def print_range(self, start_idx, stop_idx):
        current = self.head
        counter = 0
        while counter < start_idx:
            current = current.next
            counter += 1
        
        while counter <= stop_idx - 1:
            print(current.data)
            current = current.next
            counter += 1

    def print_backwards(self):
        current_node = self.head
        counter = 0
        
        while current_node.next:
            current_node = current_node.next
            counter += 1
        
        while current_node:
            if counter == 0:
                print('Head Node(0):', current_node.data)
            else:
                print('Node #{}'.format(counter), current_node.data)
            current_node = current_node.prev
            counter -= 1

class DoubleLL(PrintNode):
    def find_length(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next

        print('The amount of nodes in the data structure is {}'.format(counter))
    
    def empty_data(self):
        print('Data structure is empty.')    

