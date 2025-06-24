
class Prectice_questions:

    @staticmethod
    def first_non_repating_char(string):
        for j in range(len(string)):
            string2 = string
            string2 = string2[:j] + string2[j+1:]
            if string[j] not in string2 :
                return string2[j]
    
        return None

    @staticmethod
    def find_samllest_second_non_existing_int(data_list:list):
        missing_numbers = []
        smallest_positive_int = 1
        for i in data_list :
            pass
                        
    
        
print("Start")
print(Prectice_questions.first_non_repating_char("abababab"))

    



