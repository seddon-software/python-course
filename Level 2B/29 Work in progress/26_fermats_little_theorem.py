# Fermat's Little Theorem
#
# for any integer a, prime p:
#     aᵖ ≡ a (mod p)
#     (aᵖ - a) % p = 0 


a = 42
p = 7

aᵖ = a**p
print(aᵖ - a)
print((aᵖ - a) % p)


# If a is not divisible by p
# aᵖ⁻¹ − 1 is an integer multiple of p
# aᵖ⁻¹ = a**(p-1)
# print(aᵖ⁻¹ - 1)
# print((aᵖ⁻¹ - 1) % p)


