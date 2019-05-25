public key : (n, e)
private key: (n, d)

1. pick primes p,q 
2. n = pq, phi = (p-1)(q-1) #phi actually is phi(n)
3. computer d so that $d*e mod phi = 1$

## why secure

if only know n, it's impossible to know p,q, so impossible to know phi, so cannot calculate d as easy as doing it with knowing phi.

## usage

cipher = messege^e (mod n)


plain = cipher^d (mod n) = message^ed (mod n)

according to lemma, message^ed (mod n) = message^(ed mod phi) = m^1
