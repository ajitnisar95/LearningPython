# Modify this function to return a list of strings as defined above
def list_benefits():
    los = ["more organized code", "more readable code", "easier code reuse"]
    return los
    
def build_sentence(info):
    pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return("%s is a benefit of functions" % benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()