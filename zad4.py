end = None

e = 0

top = 1
bottom = 1

i = 1

for _ in range(1000):
    top *= i
    top += 1
    bottom *= i
    i += 1
end

print(top//bottom, end='.')
top %= bottom
top *= 10
for i in range(1000):
    print(top//bottom, end='')
    top %= bottom
    top *= 10
end

print()
print("2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696770785449969967946864454905987931636889230098793127736178215424999229576351482208269895193668033182528869398496465105820939239829488793320362509443117301238197068416140397019837679320683282376464804295311802328782509819455815301756717361332069811250996181881593041690351598888519345807273866738589422879228499892086805825749279610484198444363463244968487560233624827041978623209002160990235304369941849146314093431738143640546253152096183690888707016768396424378140592714563549061303107208510383750510115747704171898610687396965521267154688957035035")

"""
1    1    1    1    1
1    1    2    6
0!   1!   2!   3!   4!

    2.
98641 : 36288


"""