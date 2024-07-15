print(f"Digite quatro notas separados por 'enter'") 
p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
p6 = int(input())
p7 = int(input())
p8 = int(input())
p9 = int(input())
p10 = int(input())

total = int(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10)

print(f"O total é {total}. Com quanto vai pagar?")
pgto = int(input())

print(f"O troco é {pgto-total}")