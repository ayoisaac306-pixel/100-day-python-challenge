def remove_duplicates(list):
     unique_list = []
     for i in list:
          if i not in unique_list:
                unique_list.append(i)
     return unique_list
          


numbers = [2, 6, 6, 9, 0, 0, 1, 2, 3, 3]

unique_num = remove_duplicates(numbers)
print(unique_num)

name = ["Alice", "Bob", "Alice", "Eve", "Bob", "Charlie"]
unique_name = remove_duplicates(name)   
print(unique_name)


     
         
        
        


          
          
     
