from testing_package import *
if __name__ == '__main__':
    s1=students.student('sahil','23')#create object of student class    
    print("---------")
    s1.printParameter()#call class function of student class
    
    f =Fridge.Fridge({"eggs":6, "milk":4, "cheese":3}) # from Fridge.py file call Fridge class
    print("items before updating in Fridge:%s"%str(f.items))  #print items object of class
    print("grape has added ? %s"%f.add_one("grape")) # add item in items object
    f.add_many({"mushroom":5, "tomato":3})#add multiple items in items object
    print("cheese quantity is five ? %s"%f.has("cheese", 5))# check cheese quantity is 5
    print("items after updating in Fridge:%s"%str(f.items))  #print items object of class
