
import time

def find_fib_num_rec(num):
     if num == 1 or num == 2:
          return 1
    else :
        return find_fib_num_rec(num - 2) + find_fib_num_rec(num - 1)


def find_fib_num_loop(num):
    a,b = 0,1
   for elem in range(num) :
       a,b= b, a+b

       start = time.process_time()
       print(find_fib_num_rec(10))
       stop = time.process_time()
       print(f'Czas wykonywania funkcji "find_fib_num_rec" wynosi: {stop - start}')

       start1 = time.process_time()
       print(find_fib_num_loop(35))
       stop1 = time.process_time()
       print(f'Czas wykonania funkcji "find_fib_num_loop wynosi : {stop1 - start1}"')
           
       

def potenga (podstawa, wykladniki):
    if wykladnik == 0:
         return 1
    else:
        return podstawa * potenga(podstawa, wykladnik - 1)

print(potenga(3,3))


'''
 potenga(3,3) --->
 potenga(3,2) --->9
 potenga(3,1) --->3
 potenga(3,0) --->1


potenga(3,3) ---> 3*9 =27
potenga(3,2) ---> 3*3=9
potenga(3,1) ---> 3*1=3

'''


