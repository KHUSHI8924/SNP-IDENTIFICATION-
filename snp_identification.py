import matplotlib.pyplot as plt 
s1 = input("Enter the DNA sequence 1:").upper()
s2 = input("Enter the DNA sequence 2:").upper()

if len(s1) != len(s2):
    raise ValueError("SEQUENCE MUST BE OF EQUAL LENGTH")

snp_locations = []

for i, (a,b) in enumerate(zip(s1,s2), start=1):
    if a != b:
        snp_locations.append((i, a, b))
        
print("Identified SNPs:")
for pos, base1, base2 in snp_locations:
    print(f"Positions {pos}:{base1} --- {base2}")
    
print(f"Total SNP count: {len(snp_locations)}")

if not snp_locations:
    print("No SNPs found between these two sequences.")
else:
    snp_locations=[pos for pos, base1, base2 in snp_locations]
    
    #PLOTTING
    plt.figure(figsize=(8,2))
    plt.hlines(1, 1, len(s1), color='blue')
    plt.plot(snp_locations, [1]*len(snp_locations), 'ro', label='SNPs')
    plt.xlabel("Sequence position")
    plt.yticks([])
    plt.title(f"SNPs between sequence: total {len(snp_locations)}")
    plt.tight_layout()
    plt.show()
    