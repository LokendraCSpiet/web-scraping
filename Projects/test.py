def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
        
 
n = 5
# print(factorial(n)

urls = ["https://www.dmart.in/category/grocery-aesc-grocerycore","https://www.dmart.in/category/baby---kids-aesc-babyandkidscore","https://www.dmart.in/category/clothing-accessories-aesc-clothingaccessories","https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore","https://www.dmart.in/category/personal-care-aesc-personalcarecore","https://www.dmart.in/category/specials-aesc-specialscore"]

num = 0
for url in urls:
    data = {
        "Product Name" : [],
    }
    UrlName = url.split("-")[-1]
    if num == 0:
        for i in range(5):
            data['Product Name'].append(1)
    if num == 1:
        for i in range(5):
            data['Product Name'].append(2)
            
    print(data)
    num += 1

    




""" 

lav
amn rila
scin puneet
isha jain
mahima sing
kanik
deep
ankit jio
sourav did
sachu
ankit mgh
mahinoor
akshit triv
th lucky
akriti
krish
mihir
vikran
miss.rishika
sachin meena
munvvar isl
akshay kumar
umesh megh
khyati
kalpesh megh
prakhar sir
anjali sahu
radha maheshw
vikas bhaiya bjnr
lokendra chunda


"""