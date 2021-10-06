# Comparing Ribosomal RNA sequences between humans and bacteria

def count_base_pairs(input):
    input = open(input+".fasta").read().replace("\n","")
    
    # Creating dictionary with base pairs
    counter = {}
    for n in ['A','T','C','G']:
        for m in ['A','T','C','G']:
            counter[n+m] = 0

    # Counting
    for i in range(len(input)-1):
        counter[input[i]+input[i+1]] += 1
    return counter

def printing_bases(name, color, output):
    counter = count_base_pairs(name)

    j = 1
    
    output.write("<div style='float:left; margin:50px;'>")
    output.write("<h3 style='text-align: center'>" + name + "</h3>")
    
    for k in counter:
        
        transparency = counter[k]/max(counter.values())

        
        output.write("<div "+
                "style='width:100px;" +
                "border:1px solid #111;" +
                "color:#fff; height:100px;" + 
                "float:left;" +
                "background-color:rgba(" + color + ", "+str(transparency)+"')>" + 
                "<ul style='list-style-type:none'><li>" + k + "</li>" + str(counter[k]) + "</li></ul>" + 
                "</div>")

        if j%4 == 0:
            output.write("<div style='clear:both '></div>")
        j+=1
    output.write("</div>")

# Generating html page with Comparison

output = open("Comparison.html","w")

output.write("<h1> Comparing Ribosomal RNA sequences between humans and bacteria </h1>")
printing_bases("16s_bacteria","20, 75, 93",output)
printing_bases("18s_human","20, 75, 3",output)
print("HTML file with comparison was generated!")