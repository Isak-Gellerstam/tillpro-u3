import csv
import subprocess
import locale


def clear_screen():
   subprocess.run('cls',shell=True)

def format_currency(value):
   return locale.currency(value,grouping=True)


def list_products(products):

   for idx, product in enumerate(products,start=1):
      
      name = product['name']
      price = format_currency(product['price'])
      quantity = product['quantity']

      print(f"{idx}) {name} \t {price} \t {quantity:<5}")


def view_product(idx, products):
   subprocess.run('cls', shell=True)
   
   product = products[idx]

   print(f"id: {product["id"]}")
   print(f"name: {product['name']}")
   print(f"description: {product['desc']}")
   print(f"price: {format_currency(product['price'])}")
   print(f"quantity: {product['quantity']}")


   
def load_data(filename): 
   products = []           #lista
   
   with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
      reader = csv.DictReader(file)
      for row in reader:
         id = int(row['id'])
         name = row['name']
         desc = row['desc']
         price = float(row['price'])
         quantity = int(row['quantity'])
         
         products.append(
               {                   
                  "id": id,       
                  "name": name,
                  "desc": desc,
                  "price": price,
                  "quantity": quantity
               }
         )
         
   return products

def add_product():

   print("Ny Produkt:")

   found_max = max(products, key=lambda id: id['id'])
   max_id = found_max['id']
   id = max_id + 1

   name = (input("name: "))
   desc = (input("desc: "))
   price = int(input("price: "))
   quantity = int(input("quantity: "))

   
   products.append(
   {                      
     "id": id,       
      "name": name,
      "desc": desc,
      "price": price,
      "quantity": quantity
   }
   )

def remove_product():



   idx = int(input("Vilken produkt: "))


   if 0 < idx <= len(products):
      products.pop(idx-1)
      print(f"Tog bort produkt id: {idx}")
      input()

   else:
      print("produkten fins inte")

#TODO: gör så man kan se en numrerad lista som börjar på 1.    done
#TODO: skriv klart funktionen som returnerar en specifik produkt med hjälp av id & products     done
#TODO: skriv en funkion som skapar en ny produkt - den behöver inte spara till fil! done
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id done

   # found_max = max(products, key=lambda id: id['id'])
   # max_id = found_max['id']
   # new_id = max_id + 1
   
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

subprocess.run('cls',shell=True)

products = load_data('db_products.csv')


while True:
   list_products(products)
   
   print("-" * 100)

   option = input("Vad vill du göra? [# = visa produkt | L = lägg till | T = ta bort | E = ändra | Q = avsluta] ")
   
   
   if option.isdigit():
      idx = int(option)
      
      if 0 < idx <= len(products):   
         view_product(idx -1, products)
         input() #bara vänta till tangentbordsklick   

   else: 
      if option.upper() == "Q":
         exit()

      elif option.upper() == "T":
         clear_screen()
         list_products(products)

         print("-" * 100)

         remove_product()

      elif option == "E":
         pass

      elif option.upper() == "L":
         clear_screen()
         list_products(products)
         
         print("-" * 100)

         add_product()