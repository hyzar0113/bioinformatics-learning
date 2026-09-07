 protein = "MKTIIALSYIFCLVFADYKDDDDK"

# 计算长度
length = len(protein)

# 统计氨基酸
amino_acids = {}

for aa in protein:
    if aa in amino_acids:
        amino_acids[aa] += 1
    else:
        amino_acids[aa] = 1

# 输出数量
print("Amino acid count:")
print(amino_acids)


# 输出比例
print("\nAmino acid percentage:")

for aa, count in amino_acids.items():
    percentage = count / length * 100
    print(
        aa,
        round(percentage, 2),
        "%"
    )
