n = 76.12786
print(f"2 dec places:     <{n:.2f}>")
print(f"8 spaces:         <{n:8.2f}>")
print(f"percentage:       <{n/100:8.3%}>")
print(f"left justify:     <{n:<12.2f}>")
print(f"right justify:    <{n:>12.2f}>")


n = 12345678901.2345
print(f"comma and period: <{n:,.2f}>")

num = 2343552.6516251625
print(f"{num:e}")
