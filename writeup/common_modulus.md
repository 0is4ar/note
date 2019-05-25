# common\_modulus

### description

have two cipher texts with the same n but different e 

According to **Bezout's Therorem**, integers a and b, which are not both 0, then there exists x and y such that: xa + yb = gcd\(a,b\)

![](../.gitbook/assets/image%20%283%29.png)

{% embed url="https://planetcalc.com/3298/" %}

above is a good website to calculate x and y 

```text
python3 common.py
Plain Text:  1135944599059320370371119265717159436532388789289025872261173832983916744880362317623719332482597904776644786558029038115743339799933
```

```text
a = "1135944599059320370371119265717159436532388789289025872261173832983916744880362317623719332482597904776644786558029038115743339799933"
binascii.unhexlify(hex(int(a))[2:])
```

flag{c0ngr@ts!\_youre\_d0n3\_with\_h0meworks!\_ffd3e643872e}





```python
import gmpy2


class RSAModuli:
   def __init__(self):
       self.a = 0
       self.b = 0
       self.m = 0
       self.i = 0
   def gcd(self, num1, num2):
       """
       This function os used to find the GCD of 2 numbers.
       :param num1:
       :param num2:
       :return:
       """
       if num1 < num2:
           num1, num2 = num2, num1
       while num2 != 0:
           num1, num2 = num2, num1 % num2
       return num1
   def extended_euclidean(self, e1, e2):
       """
       The value a is the modular multiplicative inverse of e1 and e2.
       b is calculated from the eqn: (e1*a) + (e2*b) = gcd(e1, e2)
       :param e1: exponent 1
       :param e2: exponent 2
       """
       self.a = gmpy2.invert(e1, e2)
       self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)
   def modular_inverse(self, c1, c2, N):
       """
       i is the modular multiplicative inverse of c2 and N.
       i^-b is equal to c2^b. So if the value of b is -ve, we
       have to find out i and then do i^-b.
       Final plain text is given by m = (c1^a) * (i^-b) %N
       :param c1: cipher text 1
       :param c2: cipher text 2
       :param N: Modulus
       """
       i = gmpy2.invert(c2, N)
       mx = pow(c1, self.a, N)
       my = pow(i, int(-self.b), N)
       self.m= mx * my % N
      def print_value(self):
       print("Plain Text: ", self.m)


def main():
   c = RSAModuli()
   N  =
   c1 =
   c2 =
   e1 =
   e2 =
   c.extended_euclidean(e1, e2)
   c.modular_inverse(c1, c2, N)
   c.print_value()

if __name__ == '__main__':
   main()
```

