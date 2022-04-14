import LangIdenApp.Project_code as Project_code
import math

yoruba_data = Project_code.normalstring("yoruba.txt")
igbo_data = Project_code.normalstring("igbo.txt")
hausa_data = Project_code.normalstring("hausa.txt")
Efik_data = Project_code.normalstring("Efik.txt")
isoko_data = Project_code.normalstring("isoko.txt")


Language_Lists = [yoruba_data, igbo_data, hausa_data, Efik_data,  isoko_data]


def compare(test_file):
    #test_data = Project_code.lang_model(test_file)
    #print("CURRENT_LOG",test_file)
    test_data = Project_code.normalstring(test_file)
    #for element in test_data:
        #print element
        
    result = [0,0,0,0,0]
    for index,language in enumerate(Language_Lists):
        for ngram,prob in language:
            for ng,pb in test_data:
                if ngram == ng:
                    sim = float((prob * float(math.log(pb))) + (pb * float(math.log(prob))))
                    result[index]+=sim                 
    
    if result[0] < result[1] and result[0] < result[2] and result[0] < result[3]  and result[0] < result[4]:
        print("Language is Yoruba", result)
        return "Language is Yoruba", result

    elif result[1] < result[0] and result[1] < result[2] and result[1] < result[3]  and result[1] < result[4]:
        print("Language is Igbo", result)
        return "Language is Igbo", result

    elif result[2] < result[0] and result[2] < result[1] and result[2] < result[3]  and result[2] < result[4]:
        print("Language is Hausa", result)
        return "Language is Hausa", result

    elif result[3] < result[0] and result[3] < result[1] and result[3] < result[2]  and result[3] < result[4]:
        print("Language is Efik", result)
        return "Language is Efik", result

    elif result[4] < result[0] and result[4] < result[1] and result[4] < result[2]  and result[4] < result[3]:
        print("Language is isoko", result)
        return "Language is isoko", result

        
    else:
        print("Not in database", result)
        return "Not in database", result

    
        
            

